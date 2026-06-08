# From Speaker to Dubber

> **Venue:** ACM MM2024
> **Source:** <https://openreview.net/pdf/c1a849c12d7b851fa543b7af787bbc8fc9a945b7.pdf>

---
From Speaker to Dubber: Movie Dubbing with Prosody and
Duration Consistency Learning
Anonymous Authors


## Abstract

Movie Dubbing aims to convert scripts into speeches that align with
the given movie clip in both temporal and emotional aspects while
preserving the vocal timbre of one brief reference audio. The wide
variations in emotion, pace, and environment that dubbed speech
must exhibit to achieve real alignment make dubbing a complex task.
Considering the limited scale of the movie dubbing datasets (due
to copyright) and the interference from background noise, directly
learning from movie dubbing datasets limits the pronunciation qual-
ity of learned models. To address this problem, we propose a two-
stage dubbing method that allows the model to first learn pronunci-
ation knowledge before practicing it in movie dubbing. In the first
stage, we introduce a multi-task approach to pre-train a phoneme
encoder on a large-scale text-speech corpus for learning clear and
natural phoneme pronunciations. For the second stage, we devise a
prosody consistency learning module to bridge the emotional ex-
pression with the phoneme-level dubbing prosody attributes (pitch
and energy). Finally, we design a duration consistency reasoning
module to align the dubbing duration with the lip movement. Exten-
sive experiments demonstrate that our method outperforms several
state-of-the-art methods on two primary benchmarks. The source
code and model checkpoints will be released to the public. The
demos are available at https://speaker2dubber.github.io/.
CCS CONCEPTS
Computing methodologies Phonology / morphology;
Computer vision.
KEYWORDS
Movie dubbing, visual voice cloning, two-stage framework
ACM Reference Format:
Anonymous Authors. 2024. From Speaker to Dubber: Movie Dubbing with
Prosody and Duration Consistency Learning. In Proceedings of the 32nd
ACM International Conference on Multimedia (MM24), October 28-November
1, 2024, Melbourne, Australia. ACM, New York, NY, USA, 10 pages. https:
//doi.org/10.1145/nnnnnnn.nnnnnnn


## Introduction

Movie Dubbing, also known as Visual Voice Cloning (V2C) [4], aims
to convert scripts into speeches utilizing a specified voice guided
by a short reference audio while maintaining lip synchronization
Unpublished working draft. Not for distribution.
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than the
author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
republish, to post on servers or to redistribute to lists, requires prior specific permission
and/or a fee. Request permissions from permissions@acm.org.
ACM MM, 2024, Melbourne, Australia
© 2024 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 978-x-xxxx-xxxx-x/YY/MM
https://doi.org/10.1145/nnnnnnn.nnnnnnn
Stage Ⅰ
Speaker
Previous Works
Ours
Silent Movie Clip
Scripts
Reference Audio
You know how I feel
about the mumbling.
Blah-blah-blah-blah.
Dubbing
(a) Visual Voice Cloning (V2C) task
(b) Illustration of our proposed method
Dubber
Text-Speech Corpus
Dubbing Dataset
Baby
Stage Ⅱ
Pre-training
Practicing
Figure 1: (a) Illustration of the V2C task. (b) To overcome the
limitations of movie dubbing datasets in scale and enable the
model to generate dubbing with accurate and clear pronunci-
ation, we propose a novel two-stage dubbing method. Unlike
previous single-stage methods, it involves the pre-training
stage for pronunciation knowledge and the practicing stage
for dubbing abilities.
and reflecting the characters emotions in the given movie clip (as
shown in Figure 1 (a)). It requires the ability to bridge the visual,
natural language, and speech modalities, which brings significant
challenges.
Unlike traditional voice cloning (VC) [1, 3] or text-to-speech
(TTS) [19, 25, 28, 33] tasks solely depending on the input text for
modeling [38], movie dubbing requires maintaining consistency
between its variation information (e.g., prosody attributes, duration
of each phoneme) and the performances of movie characters. This
transforms the modeling of duration and prosody in movie dub-
bing from a one-to-many to a one-to-one mapping problem while
retaining the requirement for accurate pronunciation.
Firstly, regarding duration consistency, movie dubbing needs to
match the total duration of the video and further synchronize the
lip movements. To this end, previous works incorporate lip motion
into the prediction of the duration for each phoneme [4] or uti-
lize an attention-based upsampling module mapping the phoneme
sequence to the video frame length to ensure overall duration con-
sistency [5, 12]. However, the former standalone duration prediction
for each phoneme overlooks constraints imposed by the total length
of the video, while the latter breaks the completeness of a speech
unit, leading to unclear pronunciation.
Secondly, in terms of prosody modeling, to reflect the emotions
expressed by characters in the video, previous works [4, 12, 23]
model the prosody attributes (e.g., pitch and energy) through the
emotional expressions of movie characters at the mel-spectrogram
frame-level. The excessively fine prosody modeling scale degrades

ACM MM, 2024, Melbourne, Australia
Anonymous Authors
the models generalization capability [28], resulting in unstable
prosody fluctuations. Furthermore, previous approaches that di-
rectly fuse timbre features with phoneme sequences also fail to
achieve satisfactory voice cloning effects [4, 5, 12, 23].
Besides, the required audiovisual consistency in movie dubbing
emphasizes the comprehensive application of accurate and clear
pronunciation. However, movie dubbing datasets are limited in
scale (due to copyright issues) and usually involve complicated
pronunciation and prosody. The presence of background sounds
and ambient noise inherent in movies further increases the difficulty
of modeling accurate and clear pronunciation. Existing works [4,
5, 12, 23] try to simultaneously learn pronunciation from scratch
and achieve the alignment between dubbing and movie clip solely
relying on movie dubbing datasets (as shown in Figure 1 (b) blue
arrows), leads to poor pronunciation quality. This demonstrates
that the model attempting to leap directly from "baby" to dubber
solely depends on movie dubbing datasets is quite difficult and
inefficient.
To address the above-mentioned problems, we propose a novel
two-stage dubbing method (as shown in Figure 1 (b) green arrows)
that better aligns with the practicing process from speaker to dub-
ber. The two-stage framework allows the model to first learn the
pronunciation knowledge via multi-task speaker pre-training and
then practice synchronizing with movie content to achieve prosody
and duration consistency. Specifically, in the first stage, we intro-
duce the multi-task pre-training to learn universal pronunciation
representation from a large-scale text-to-speech corpus. It over-
comes the limitation of movie dubbing datasets and enhances the
pronunciation clarity of dubbing. In the second stage, we design
a prosody consistency learning module to bridge the visual emo-
tion features with phoneme-level prosody attributes. Furthermore,
timbre-adaptive layer normalization (TALN) is introduced to main-
tain the timbre consistency with reference audio. Last, we propose
a duration consistency reasoning module to predict the optimal
monotonic alignment between phoneme-level acoustic features
and video frame-level lip motion. This module aims to synchro-
nize dubbing with the movie clip in terms of lip movement and
overall duration. Finally, the mel-decoder [34] is used to predict
the mel-spectrogram of dubbing, and the vocoder [22] converts the
mel-spectrogram into a waveform in the time domain.
The main contributions are summarized as follows:
We propose a two-stage framework for movie dubbing that
enables the model to learn pronunciation from large-scale
text-to-speech corpus before practicing in movie dubbing,
therefore improving the quality of dubbing pronunciation.
To better achieve prosody consistency, we propose a prosody
consistency learning module to bridge the characters emo-
tion with the phoneme-level prosody attributes and utilize
TALN to preserve the vocal timbre of reference audio.
To achieve duration consistency, we propose a duration con-
sistency reasoning module to predict the optimal alignment
between the phoneme-level acoustics features and lip move-
ment in the video.
Extensive experiments demonstrate that our proposed method
outperforms the current state-of-the-art, validating the ef-
fectiveness of each module.
RELATED WORKS
Speech Synthesis
Speech synthesis, or text-to-speech, plays a crucial role in various
applications, including virtual assistants, navigation systems, acces-
sibility tools, and entertainment media. In recent years, numerous
advancements have been made in speech synthesis. WaveNet [40]
and Tacotron [35] architectures demonstrate remarkable perfor-
mance in generating high-quality and expressive speech in an
autoregressive way. Then, the Fastspeech series [33, 34] achieve
high-quality and rapid speech synthesis by expanding phoneme
sequences to the same length as mel-spectrogram using Montreal
forced alignment (MFA) [26] and length regulator. Recently, a prolif-
eration of models based on diffusion [14, 31] or generative flow [9,
20], aiming to generate natural and human-level speech [8, 13, 16,
19, 42]. To further improve the naturalness of synthesized speech,
the NaturalSpeech series [17, 36, 38] employ elaborate designed
neural speech codecs for speech attribute factorization and a factor-
ized diffusion model to build fine-grained speech attributes. Despite
the impressive progress, these methods cannot be directly applied
to the V2C task as they lack the required prosody and duration
consistency modeling with input move clip.
Pre-training in Text-to-Speech
Pre-trained language models (e.g., BERT [7]) achieve state-of-the-
art performance in solving natural language processing tasks. Since
training a TTS model is like learning a language from scratch [24],
recently many works [11, 15, 24, 29, 45] employ additional BERT
encoders to enhance the pronunciation quality and expressiveness
of the generated speech. In order to enable the BERT to operate at
the phoneme level sequence avoiding the inconsistency between
phoneme and character information, MP-BERT [45] merges the
phoneme and sup-phoneme sequences into a new sequence, PL-
BERT [24] combines whole-word masked phoneme and grapheme
prediction as pre-train strategy, both achieve promising results. Pre-
training of masked language models provides abundant phoneme-
level contextual information which can enhance the naturalness of
speech. Therefore, we incorporate this pre-train strategy into the
movie dubbing task to enhance the naturalness of dubbing.
Visual Voice Cloning
The V2C task [4] introduces video information as one of the condi-
tions for speech synthesis, requiring the generated dubbing to align
with the video content in terms of lip movements, emotions, and
duration. This eliminates the one-to-many problem in traditional
speech synthesis tasks and significantly increases the complexity
of the task. Building on this, a hierarchical prosody learning model
is proposed [5], which adapts the prosody of dubbing by learn-
ing at three levels: lip movements, character facial information,
and global scene information, at the level of video frames. Recent
works [12, 23] try to solve the dubbing task using human-face as
the timbre identity features using the non-autoregressive model or
diffusion model. Although previous works make progress in improv-
ing the consistency between dubbing audio and movie clips, the
complexity and limited scale of movie dubbing datasets constrain
the pronunciation accuracy of learned models.

From Speaker to Dubber: Movie Dubbing with Prosody and
Duration Consistency Learning
ACM MM, 2024, Melbourne, Australia
� you know how I feel .
Dubbing Script
Mel Decoder
Vocoder
Duration Consistency Reasoning
Phoneme-level Acoustics Feature
Reference Audio
Lip Motion Encoder
Emotion Encoder
Lip Extraction
[Y UW1 N … F IY1 L]
Phoneme Sequence
G2P
Pretrained
Phoneme Encoder
Pitch Predictor
Energy Predictor
K,V
Prosody Consistency Learning
Large Text-to-Speech Corpus
Variance Adaptor
Mel Decoder
Vocoder
LMLM
LTTS
Multi-task Speaker Pre-training
Mel-Timbre Encoder
Timbre-Adaptive Layer Norm
Timbre Feature
Length Regulator
Timbre Feature
TALN
Output Dubbing
Video Frame-level Lip Motion Feature
Phoneme & Position
Phoneme Target
AA1
AH0
EH1
Grapheme2Phoneme
(G2P)
MLM Predict
Phoneme Encoder
Multi-head
Attention
Output Speech

Speaker
Add & TALN
Conv1D
Mel-spectrogram
[M]
Add & TALN
AA1
AH0
[M]
[M]
Silent Movie
Face Extraction
Dubber
Figure 2: The main architecture of the proposed two-stage dubbing method. In the first stage, we introduce a multi-task
speaker pre-training (Section 3.2) to improve the quality of dubbing pronunciation. In the second stage, we propose the Prosody
Consistency Learning (Section 3.3) and Duration Consistency Reasoning (Section 3.4) to improve audiovisual consistency.
METHODS
Overview
The target of the overall movie dubbing task is:
(1)
where the ˜𝐴𝐷𝑢𝑏is the generated dubbing and 𝐴𝑅𝑒𝑓,𝑇𝑠,𝑉𝑅𝑒𝑓are
the reference audio, scripts, and reference video, i.e., movie clip
respectively.
The main architecture of the proposed method is shown in Fig-
ure 2. Our method involves two training stages: multi-task speaker
pre-training (MTSP) (top) and dubbing training with prosody and
duration consistency learning (bottom). In the first stage, we con-
duct a multi-task speaker pre-training for the phoneme encoder.
Since conventional speech and movie dubbing differ significantly in
tone and prosody but share common pronunciation semantics, pre-
training the phoneme encoder is the optimal choice. Compared to
movie dubbing datasets, the recording environment of text-speech
corpus is often a noise-free recording studio. The prosody and pro-
nunciation in the corpus are smooth and clear. Therefore it can
offer rich pronunciation knowledge for movie dubbing.
In the second stage, we freeze the pre-trained phoneme encoder
and train the model using the movie dubbing datasets. We propose
the Prosody Consistency Learning (PCL) module and the Duration
Consistency Reasoning (DCR) module. These modules enable the
model to better practice pronunciation skills thus achieving prosody
and duration consistency with the movie clip. They respectively
align the emotion and lip movement of the character with the
phoneme-level prosody and duration of the dubbing. Additionally,
in the PCL module, we employ a mel-timbre encoder and timbre-
adaptive layer normalization (TALN) to extract and integrate the
timbre feature of the reference audio, thereby ensuring timbre
consistency. We detail each module below.
Multi-task Speaker Pre-training
The pre-training consists of two tasks: the TTS task and the MLM
prediction task. The former enables the model learns to extract ac-
curate pronunciation representations from high-quality text-speech
corpus and the latter facilitates the model to learn contextual rela-
tionships between phonemes and better handle unseen text.
TTS task. We adopt an architecture similar to the FastSpeech2 [33]
in this stage, where the model primarily consists of three main com-
ponents for generating the mel-spectrogram of speech, namely the
phoneme encoder, variance adaptor, and mel-decoder. Specifically,
after the text is converted into phoneme sequence by an open-
source grapheme-to-phoneme tool1 (G2P), it serves as the input to
the model. Subsequently, a phoneme encoder composed of stacked
Feed-Forward-Transformer (FFT) blocks [34] is utilized to extract
phoneme embeddings, and the variance adaptor is employed to
model the prosody attributes of speech, namely pitch, energy, and
1https://github.com/Kyubyong/g2p

ACM MM, 2024, Melbourne, Australia
Anonymous Authors
the duration of each phoneme. Then transform them into acoustic
features with the desired length as the mel-spectrogram as follows:
𝑇𝑒= PhonemeEncoder(𝑇𝑝) ∈R𝐿𝑝𝑑𝑚,
(2)
where 𝑇𝑜, 𝑇𝑝, and 𝑇𝑒are the original text, phoneme sequence, and
phoneme embedding, respectively. 𝐿𝑝and 𝐿𝑚𝑒𝑙denote the length of
the phoneme sequence and desired mel-spectrogram, respectively.
𝑑𝑚denotes the hidden size of the model. 𝐷𝑝, 𝑃𝑝, and 𝐸𝑝denote the
duration and prosody attributes of each phoneme, namely pitch
and energy. 𝑇𝑚𝑒𝑙denotes the expended phoneme-level acoustic
sequence with prosody attributes.
It is worth noting that in the original TTS task, the duration,
pitch, and energy of each phoneme are predicted by the variance
adaptor directly from the phoneme sequence. However, in the movie
dubbing task, the duration and the prosody attributes of dubbing
need to be bridged with visual information, such as the lip move-
ments and emotional expressions of characters. Since no matching
visual information is available in the text-speech corpus, we directly
use the ground truth duration, pitch, and energy information in
the TTS pre-training task. Furthermore, to enable the model to bet-
ter adapt to a multi-speaker environment during the pre-training
phase, we also employ the mel-timbre encoder and TALN at this
stage. We provide a detailed explanation of these components in
Section 3.3. The omission here does not affect the description of
the pre-training process.
Then, we predict the mel-spectrogram of target speech and cal-
culate the loss of this task:
𝑀= MelDecoder(𝑇𝑚𝑒𝑙),
𝑡=0

(3)
where the mel-decoder is composed of stacked FFT blocks [34]
similar to the phoneme encoder, 𝑀and ˜𝑀denote the ground truth
mel-spectrogram and the predicted one, respectively. Subscript 𝑡
denotes the 𝑡-th frame.
MLM prediction task. The MLM prediction task enables the model
to enhance the naturalness of dubbing audio by learning phoneme
contextual relationships in a self-supervised manner.
Specifically, we convert the text in the corpus into phoneme
sequences and then randomly mask the sequences with a pre-
determined masking ratio. After inputting the phoneme sequences
into the phoneme encoder, we predict the masked input phoneme
tokens from the hidden states of the last layer using a linear pro-
jection along with a softmax function. The loss function is the
cross-entropy loss commonly used for multi-class prediction. The
training target of the MLM prediction task is:
L𝑀𝐿𝑀= 𝐶𝐸(PhonemeEncoder(𝑇𝑚𝑎𝑠𝑘),𝑇𝑝),
(4)
where the 𝑇𝑚𝑎𝑠𝑘is the masked phoneme sequence and 𝐶𝐸(·) de-
notes the cross-entropy loss.
Loss function of the first stage. During the multi-task speaker
pre-training, the TTS task and MLM prediction task are conducted
separately. The masking in the MLM prediction task does not affect
the encoding of phonemes in the TTS task. The total loss for the
first stage is as follows:
(5)
where the 𝛼1 and 𝛼2 are pre-defined hyper parameters.
Prosody Consistency Learning
The Prosody Consistency Learning (PCL) module consists of two
parts: 1) Bridging the emotional states of characters in movie clips
with the phoneme-level prosody attributes of dubbing and 2) accu-
rately replicating the timbre of the reference audio.
Bridging emotion with dubbing. In movie dubbing, the consis-
tency between the dubbings prosody and the characters emotions
is crucial. A professional dubber always observes the characters fa-
cial expressions in the movie to adjust their pronunciation prosody.
To enable the model to achieve this, we model the phoneme-level
prosody attributes pitch and energy based on the facial information
of the characters in the video.
Following [5], we exact the face region of each frame of movie
clip 𝑉𝑓𝑎𝑐𝑒via S3FD face detection [46], then utilize an emotion
face-alignment network (EmoFAN) [39] to encode the face region
to emotion features 𝑉𝑒𝑚𝑜:
(6)
where the 𝐿𝑣denotes the frame number of the reference video.
To model the pitch and energy of each phoneme based on the
emotion from video frames, we utilize multi-head cross-modal at-
tention to bridge the characters emotion features with prosody
attributes of each phoneme:
(7)
where𝑘denotes𝑘-th heads output,𝑊
𝑗are learnable parameter ma-
trix, 𝜉𝑝ℎ𝑜,𝑝𝑖𝑡𝑐ℎand 𝜉𝑝ℎ𝑜,𝑒𝑛𝑒𝑟𝑔𝑦are phoneme-level prosody feature
for pitch and energy, respectively. After bridging the prosody of
dubbing with the characters emotion, we predict the pitch energy
of each phoneme using the pitch and energy predictor and transfer
them to pitch and energy embedding then add to the phoneme
sequence:
𝑇𝑎= 𝑇𝑒+ PitchEmb(e𝑃𝑝ℎ𝑜) + EnergyEmb(e𝐸𝑝ℎ𝑜),
(8)
where e𝑃𝑝ℎ𝑜and e𝐸𝑝ℎ𝑜are the predicted pitch and energy and 𝑇𝑎∈
R𝐿𝑝𝑑𝑚are the phoneme-length acoustics feature with prosody
attributes.
Timbre consistency. To keep the timbre consistency within the
same character and ensure a coherent and consistent understanding
of the characters by the audience, we propose a mel-timbre encoder
to extract the timbre feature from reference audio.

From Speaker to Dubber: Movie Dubbing with Prosody and
Duration Consistency Learning
ACM MM, 2024, Melbourne, Australia
The mel-timbre encoder comprises three parts: (1) a fully con-
nected layer to transform each frame of the mel-spectrogram into
the hidden sequence of acoustics features, (2) a temporal processing
module to capture contextual information using a stacked 1-D con-
volutional neural network, and (3) a multi-head attention module
to aggregate global information of vocal timbre. Due to the issue of
poor generalization of learnable timbre encoder in movie dubbing
datasets, we pre-train the mel-timbre encoder on the multi-speaker
text-speech corpus [44] using GE2E loss [41] and froze its weights
during both stages of training unlike [28].
Inspired by the style transfer in the image and speech generation
domain [18, 28], we utilize a Timbre-Adaptive Layer Norm to fuse
the timbre feature into phoneme encoding and mel-spectrogram
generation by predicting the gain and bias of the input vector
sequence giving the timbre feature:
(9)
where 𝑥and 𝐸𝑡𝑖𝑚𝑏𝑟𝑒are the input sequence and timbre feature,
𝜇, 𝜎are the mean and variance of 𝑥, 𝑔𝑎𝑖𝑛(·) and 𝑏𝑖𝑎𝑠(·) are the
prediction function of gain and bias, respectively. The proposed
TALN is applied in every FFT block of both the phoneme encoder
and mel-decoder to integrate the vocal timbre feature.
Duration Consistency Reasoning
The proposed Duration Consistency Reasoning module (DCR) con-
tains two steps: (1) reasoning the phoneme-lip alignment and (2)
expanding to the length of desired mel-spectrogram.
Reasoning the phoneme-lip alignment. To exact lip motion fea-
tures from the reference video, we first extract the lip region 𝑉𝐿𝑖𝑝∈
R𝐿𝑣𝐻𝐿𝑖𝑝𝑊𝐿𝑖𝑝𝐶from the video, then exploit a lip motion encoder
to obtain the lip movement representation 𝐸𝐿𝑖𝑝∈R𝐿𝑣𝑑𝑚𝑜𝑑𝑒𝑙.
After obtaining the lip motion features from the movie clip,
we can calculate the upper triangular similarity matrix between
phoneme-level acoustic features and lip-motion features:
...
...
...
...
(10)
where the 𝑠𝑖,𝑗is the cosine similarity between 𝑖-th phoneme-level
acoustic feature and 𝑗-th frames lip motion feature.
The alignment between lip phoneme and lip motion should sat-
isfy surjectivity, which means the alignment path must begin at 𝑠11
and end at 𝑠𝐿𝑝𝐿𝑣. Additionally, this alignment also needs to satisfy
monotonicity, each step of the alignment path can only move to
the right or diagonally down to the right, thus we can use dynamic
programming algorithms to find the optimal alignment:
otherwise
(11)
𝐴= argmax
(12)
where 𝐴is the alignment matrix and 𝐴is the optimal alignment
between phoneme-level acoustic and lip-motion features which
simultaneously satisfy monotonicity and surjectivity.
Expanding to the mel-length. The duration of the video cor-
responds strictly to the duration of the audio, hence, the number
of video frames corresponds one-to-one with the length of the
corresponding mel-spectrogram, maintaining a fixed ratio relation-
ship [5, 12]:
(13)
where the𝑠𝑟andℎ𝑠are the sampling rate and hop size when process-
ing the audio and 𝐹𝑃𝑆denotes the Frames Per Second of the video.
With this fixed coefficient 𝑛, we can extend the obtained phoneme-
lip alignment to phoneme-mel-spectrogram alignment, acquiring
the duration of each phoneme. Then we expand the acoustics fea-
ture sequence of phoneme length to the required mel-spectrogram
length using length regulator [34] for mel-spectrogram generation
and audio generation:
˜𝐴𝐷𝑢𝑏= Vocoder(MelDecoder(LR(𝑇𝑎,𝐴 𝑛), 𝐸𝑡𝑖𝑚𝑏𝑟𝑒)),
(14)
where the LR(·) denotes the length regulator.
Loss Function of Second Stage
The total loss function of this training stage is:
(15)
where 𝜆are pre-defined hyper-parameters, L𝑚𝑒𝑙, L𝑝𝑖𝑡𝑐ℎ, and
L𝑒𝑛𝑒𝑟𝑔𝑦are the L1 Loss to the mel-spectrogram and the predic-
tion of the pitch and energy of each phoneme respectively. For the
alignment in duration consistency reasoning, since the dynamic
programming algorithm does not have any learnable parameters,
we optimize the lip motion encoder using ground truth alignment,
gradually making the similarity matrix approach the ideal align-
ment. For detailed information refer to Appendix.
EXPERIMENTS
We primarily evaluate our method on two dubbing datasets: V2C-
Animation [4] and GRID [6]. Here, we present our experimental


## Results

mentation details, evaluation metrics, qualitative and quantitative
analysis, as well as ablation studies.
Datasets
V2C-Animation dataset [4] is currently the only publicly avail-
able movie dubbing dataset. Specifically, it consists of 10,217 video-
audio-text triplets cropped from 26 Disney animated movies, to-
taling 153 different speakers, with complete speaker and emotion
annotations. The dataset extracts the middle audio track from movie
clips as dubbing data but still exists some environmental sounds
and noise that cannot be eliminated. Due to the authenticity of
this dataset which is from publicly available movies, its the most
challenging dataset for the V2C task currently. Therefore, our main
experimental results are validated on this dataset.
GRID dataset [6] is a basic benchmark for multi-speaker dubbing.
The whole dataset has 33 speakers, each with 1,000 short English
samples. All participants are recorded in a noise-free studio with
a unified screen background. The V2C-Animation dataset and the

ACM MM, 2024, Melbourne, Australia
Anonymous Authors
Table 1: Results on V2C-Animation benchmark. The method with * refers to a variant taking video embedding as an additional
input following [4]. For the Dub 1.0 setting, we use the ground truth audio as reference audio, for the Dub 2.0 setting, we use the
non-ground truth audio from the same speaker within the dataset as the reference audio which is more aligned with practical
usage in dubbing. The same setup is applied to the GRID benchmark.
Setting
Dub 1.0
Dub 2.0
Methods
Visual
SECS (%)
WER (%)
EMO-ACC (%)
MCD-DTW
MCD-DTW-SL
SECS (%)
WER (%)
EMO-ACC (%)
MCD-DTW
MCD-DTW-SL
GT Mel + Vocoder
Fastspeech2 [33]
StyleSpeech [28]
Zero-shot TTS [47]
Matcha-TTS [27]
Fastspeech2* [33]
StyleSpeech* [28]
Zero-shot TTS* [47]
V2C-Net [4]
HPMDubbing [5]
Face-TTS [23]
Ours
GRID dataset correspond respectively to dubbing for animated films
and live-action recording, covering a wide range of application
scenarios.
LibriTTS dataset [44] is a multi-speaker English corpus derived
from LibriSpeech [30]. LibriTTS comprises 110 hours of audio from
1,141 speakers along with their corresponding text transcripts. It
filters out mismatched or significantly noisy samples found in Lib-
riSpeech and is widely used in speech synthesis or automatic speech
recognition (ASR) tasks. Due to its advantages in speech quality
and scale as well as the similar multi-speaker settings, we employ
LibriTTS as our speaker pre-training dataset in the first stage.
Implementation Details
The video frames are sampled at 25 FPS and all audios are resampled
to 22.05kHz. For all audio data, we convert the raw waveform into
mel-spectrograms following [4, 5, 28, 33, 34] with FFT size of 1024,
hop size of 256, window size of 1024, and frequency bins of 80.
The ground truth of phoneme duration is extracted by Montreal
Forced Aligner [26]. We use continuous wavelet transform (CWT)
to decompose the continuous pitch series into pitch spectrograms
to get the phoneme-level pitch [10, 37]. For energy extraction, we
compute the mean L2-norm of the amplitude of each short-time
Fourier transform (STFT) frame within a phoneme duration [33].
For the MLM prediction task of the multi-task speaker pre-
training in the first stage, we use a 15% random masking rate and
train with a batch size of 16 for 100 epochs together with the TTS
task on the LibriTTS-Clean-100 dataset. The weight in Equation 5
are set to 𝛼1 = 1, 𝛼2 = 0.1. In the second stage of training, we
freeze the pre-trained phoneme encoder and train the rest part of
the model on the dubbing datasets. We use a pre-trained universal
speaker version of HiFi-GAN [22] as vocoder to convert the mel-
spectrogram to time-domain waveforms. The weight in Equation 15
are set to 𝜆1 = 1, 𝜆2 = 0.1, 𝜆3 = 0.1, 𝜆4 = 0.2. An Adam [21] with
𝛽1 = 0.9, 𝛽2 = 0.98, 𝜖= 10−9 is used as the optimizer in both the
training stages. The learning rate is set to 0.00625. Both training and
inference are implemented with PyTorch on a GeForce RTX 4090
GPU. For a fair comparison, all comparison models are re-trained on
the same dataset. For more details of training and implementation
please refer to Appendix.


## Evaluation

Objective metrics. To measure the difference between the gen-
erated dubbing and the ground truth, we adopt the Mel Cepstral
Distortion Dynamic Time Warping (MCD-DTW) metric follow-
ing [4]. To further assess the duration consistency between the
generated dubbing and the video, we utilize the MCD-DTW-SL
metric which adjusts the weights based on duration consistency [4].
Furthermore, to evaluate the timbre consistency between the gen-
erated dubbing and the reference audio, we employ the speaker
encoder cosine similarity (SECS) following [2, 3] to compute the
similarity of speaker identity. To assess the pronunciation quality
of the generated dubbing, we utilize the state-of-the-art automatic
speech recognition (ASR) model whisper2 [32] from OpenAI for
dubbing recognition and computing the word error rate (WER) 3
against the script to evaluate the accuracy of the generated dubbing.
In addition, we utilize a speech emotion recognition model [43]
to evaluate the emotion accuracy (EMO-ACC) of the generated
dubbing (For the V2C-Animation benchmark only because there is
no emotion label in GRID dataset).
Subjective metrics. For subjective evaluation, we conduct human
evaluations of mean opinion score (MOS) in aspects of naturalness
(NMOS) and similarity (SMOS). Both metrics are rated on a 1-to-5
scale and reported with the 95% confidence intervals (CI). Following
the settings in [4, 5], all participants are asked to assess the dubbing
quality of 30 randomly selected audio samples from each test set.
In addition to SMOS and NMOS, we also utilize Comparative MOS
(CMOS) with 7 points (from -3 to 3) to compare different models.
Comparison with SOTA


## Results

our model achieves the best performance across almost all met-
rics, except for the EMO-ACC metric in the dub 2.0 setting, where
it slightly lagged behind the current SOTA dubbing model HPM-
Dubbing [5]. In both dub settings, our method achieves the best
performance on SECS. It indicates that our method performs better
in extracting and cloning vocal timbre. Since the V2C-Animation
2https://huggingface.co/openai/whisper-large
3https://github.com/jitsi/jiwer

From Speaker to Dubber: Movie Dubbing with Prosody and
Duration Consistency Learning
ACM MM, 2024, Melbourne, Australia
Table 2: Results on GRID benchmark with the same dub setting as the V2C-Animation benchmark.
Setting
Dub 1.0
Dub 2.0
Methods
Visual
SECS (%)
WER (%)
MCD-DTW
MCD-DTW-SL
SECS (%)
WER (%)
MCD-DTW
MCD-DTW-SL
GT Mel + Vocoder
Fastspeech2 [33]
StyleSpeech [28]
Zero-shot TTS [47]
Fastspeech2* [33]
StyleSpeech* [28]
Zero-shot TTS* [47]
V2C-Net [4]
HPMDubbing [5]
Face-TTS [23]
Ours
Table 3: Subjective evaluation on V2C-Animation and GRID
benchmarks.
Dataset
V2C-Animation
GRID
Methods
NMOS
SMOS
CMOS
NMOS
SMOS
CMOS
+0.23
+0.14
GT Mel + Vocoder
+0.21
+0.16
Fastspeech2 [33]
-0.29
-0.26
StyleSpeech [28]
-0.22
-0.25
Zero-shot TTS [47]
-0.26
-0.23
Fastspeech2* [33]
-0.27
-0.26
StyleSpeech* [28]
-0.20
-0.24
Zero-shot TTS* [47]
-0.24
-0.21
V2C-Net [4]
-0.21
-0.19
HPMDubbing [5]
-0.18
-0.14
Face-TTS [23]
-0.37
-0.32
Ours
Table 4: Results on zero-shot test.


## Method

Visual
SECS
WER
NMOS
SMOS
CMOS
FastSpeech2 [33]
-0.25
StyleSpeech [28]
-0.19
Zero-shot TTS [47]
-0.18
FastSpeech2* [33]
-0.24
StyleSpeech* [28]
-0.21
Zero-shot TTS* [47]
-0.16
V2C-Net [4]
-0.14
HPMDubbing [5]
-0.11
FaceTTS [23]
-0.29
Ours
dataset is derived from real movie dubbing clips, its samples involve
complex pronunciation and prosody variations, which increases
the difficulty for the model to learn accurate pronunciation from
them. Previous methods fail to perform accurate pronunciation, as
reflected in the high WER values. However, our model achieves
pronunciation accuracy significantly better than other models with
an absolute margin from 16.52% to 183.62%. While ensuring pronun-
ciation accuracy, our model also achieves the lowest MCD-DTW
and MCD-DTW-SL, indicating smaller discrepancies compare to
ground truth dubbing and better duration consistency.
In the subjective evaluation, we randomly select 15 samples from
the generated dubbing of each dub setting for human study. Table 3
shows the results. All objective evaluations of our model in the
V2C benchmark achieve the highest scores. It demonstrates that
our model can generate dubbing closer to realistic dubbing in both
naturalness and similarity. In addition, our model outperforms the
current state-of-the-art dubbing model [5] in CMOS evaluation
with a margin of +0.18.


## Results

achieves the best performance across all metrics on the GRID bench-
mark. Unlike V2C-Animation, samples in GRID are recorded in a
studio environment which does not involve exaggerated prosody
variation and background noise. Therefore, the pronunciation ac-
curacy of all comparison methods is generally better on the GRID
benchmark compared to the V2C-Animation benchmark. Never-
theless, our model still achieves the best pronunciation clarity (see
WER) and the best SECS in both dub settings. The lowest MCD-
DTW and MCD-DTW-SL demonstrate the ability of our model
to generate dubbing closer to ground truth. Moreover, our model
also achieves the highest scores in naturalness and similarity in
subjective evaluations and surpasses other models in comparative
evaluations with a margin of +0.14.
Results of Zero-shot test. In addition to the evaluation on two
benchmarks, we also conduct a zero-shot experiment to verify
the robustness of our method. In the zero-shot experiment, we
utilize scripts and movie clips from the V2C-Animation dataset
and reference audio from the GRID dataset (i.e., out of domain) to
simulate the application of generating customized dubbed videos in
real-world scenarios. Due to the absence of corresponding ground
truth in this test, we only calculate WER and SECS for objective


## Evaluation

As shown in Table 4, our model achieves the best pronunciation
clarity and timbre consistency in the zero-shot test. It demonstrates
that our method can maintain stable dubbing synthesis when fac-
ing reference audio from out-of-domain sources. The subjective
evaluation results also demonstrate the superiority of our approach
over other models. Our model surpasses the state-of-the-art model
in naturalness, similarity, and comparison tests.
Qualitative Analysis
We visualize the mel-spectrograms of ground-truth and synthesized
audios by our model and the other two state-of-the-art methods
in Figure 3. The red and white bounding boxes represent regions
where different models exhibit significant differences in duration
consistency and pronunciation details compared to the ground truth.
Through the observation of the red bounding box, it is evident that
our model outperforms others in maintaining duration consistency.

ACM MM, 2024, Melbourne, Australia
Anonymous Authors
Ours
HPMDubbing
V2C-Net
Reference: Bossbaby@BossBaby
Reference: Zootopia@Nick
Reference: Frozen@Anna
Reference From GRID: GRID@S2
Reference From GRID: GRID@S3
Input
Character
Character
Character
Character
Character
Figure 3: The visualization of the mel-spectrograms from ground truth and synthesized audios by different models. The red
and white bounding boxes highlight regions where different models exhibit significant differences in duration pausing and
pronunciation details.
The phoneme and pause durations are notably closer to the ground
truth dubbing. This phenomenon is more pronounced in the V2C-
Animation benchmark due to its complex speaking speed variation.
Additionally, from the clearer spectrum lines in the white bounding
box, it can be observed that the dubbing generated by our model
exhibits clearer and more natural pronunciation details.
Ablation Studies
To further investigate the specific effects of each module in our pro-
posed method, we conduct ablation studies on the Dub 1.0 setting
on the V2C-Animation benchmark.
Effectiveness of PCL. The results are presented in Row A-C of
Table 5. We find that the incorporation of TALN enables the model
to better clone the timbre of the reference audio. Furthermore, since
TALN does not directly affect phoneme features as [4], the pronun-
ciation accuracy of the model is also improved. The PCL module
utilizes emotional information of characters to model the phoneme-
level prosody attributes of dubbing, enhancing the models ability to
capture character emotions. Compared to mel-spectrogram frame-
level prosody modeling (Row A-B), the phoneme-level modeling
used in PCL improves the EMO-ACC. It demonstrates a better align-
ment between dubbing prosody and the emotion of the character.
Besides, the integration of PCL also reduces the distance between
the generated mel-spectrogram and the ground truth, demonstrat-
ing its effectiveness in improving dubbing quality.
Effectiveness of MTSP. The results are presented in Row D-F
of Table 5. The results indicate that the TTS pre-training task can
significantly enhance the pronunciation quality, and improve the
WER by an absolute margin of 35.02%. The integration of the TTS
pre-training task enables our model to generate dubbing with pro-
nunciation accuracy even reaching the level of ground truth. (We
do not fine-tune the ASR model on the movie dubbing datasets, so
it may even outperform the ground truth.) Additionally, although
the MLM pre-training task does not contribute to pronunciation
quality improvement as noticeably as the TTS pre-training task,
Table 5: Results of ablation study


## Method

SECS
WER
EMO-ACC
MCD-DTW
MCD-DTW-SL
GT Mel+ Vocoder
Baseline [4]
A+TALN
A+PCL
C+MLM Pretrain
C+TTS Pretrain
C+MTSP
DCR v.s. Duration Prediction
Full Model
their combination can lead to better performance improvements for
the model. The improvement in pronunciation quality also reduces
the deviation between synthesized and ground truth dubbing.
Duration Consistency Reasoning v.s. Duration Prediction.
We compare the performance of our model using duration predic-
tion (Row G) and the proposed DCR (Row H) respectively. The
proposed duration consistency reasoning method considers the
relationships between dubbing-lip motion and video-audio syn-
chronization. Unlike the duration prediction method, it does not
predict the duration of each phoneme separately, thus avoiding
inconsistencies in the overall duration compared to the video. The
drops on MCD-DTW-SL demonstrate the effectiveness of DCR.
CONCLUSIONS
In this work, we propose a two-stage dubbing method to improve
the pronunciation quality of dubbing and achieve better audiovisual
consistency. In the first stage, we conduct multi-task pre-training
on a large-scale text-speech corpus to enable the model to learn uni-
versal pronunciation knowledge. In the second stage, the proposed
prosody and duration consistency learning module bridges the
phoneme-level duration and prosody of dubbing with the movie
clip, towards consistency in both aspects. Experimental results
demonstrate our method outperforms the current state-of-the-art
(SOTA) on two primary benchmarks across multiple settings, vali-
dating the effectiveness of our method.

From Speaker to Dubber: Movie Dubbing with Prosody and
Duration Consistency Learning
ACM MM, 2024, Melbourne, Australia
REFERENCES
[1] Sercan Ömer Arik, Jitong Chen, Kainan Peng, Wei Ping, and Yanqi Zhou. 2018.
Neural Voice Cloning with a Few Samples. In Advances in Neural Information
Processing Systems 31: Annual Conference on Neural Information Processing Systems
2018, NeurIPS 2018, December 3-8, 2018, Montréal, Canada. 1004010050.
[2] Edresson Casanova, Christopher Shulby, Eren Gölge, Nicolas Michael Müller,
Frederico Santos de Oliveira, Arnaldo Candido Jr., Anderson da Silva Soares,
Sandra Maria Aluísio, and Moacir Antonelli Ponti. [n. d.]. SC-GlowTTS: An
Efficient Zero-Shot Multi-Speaker Text-To-Speech Model. In Interspeech 2021,
22nd Annual Conference of the International Speech Communication Association,
Brno, Czechia, 30 August - 3 September 2021. 36453649.
[3] Edresson Casanova, Julian Weber, Christopher Dane Shulby, Arnaldo Cândido
Júnior, Eren Gölge, and Moacir A. Ponti. 2022. YourTTS: Towards Zero-Shot
Multi-Speaker TTS and Zero-Shot Voice Conversion for Everyone. In International
Conference on Machine Learning, ICML 2022, 17-23 July 2022, Baltimore, Maryland,
USA, Vol. 162. 27092720.
[4] Qi Chen, Mingkui Tan, Yuankai Qi, Jiaqiu Zhou, Yuanqing Li, and Qi Wu. 2022.
V2C: Visual Voice Cloning. In IEEE/CVF Conference on Computer Vision and Pattern
Recognition, CVPR 2022, New Orleans, LA, USA, June 18-24, 2022. 2121021219.
[5] Gaoxiang Cong, Liang Li, Yuankai Qi, Zheng-Jun Zha, Qi Wu, Wenyu Wang, Bin
Jiang, Ming-Hsuan Yang, and Qingming Huang. 2023. Learning to Dub Movies
via Hierarchical Prosody Models. In IEEE/CVF Conference on Computer Vision
and Pattern Recognition, CVPR 2023, Vancouver, BC, Canada, June 17-24, 2023.
[6] Martin Cooke, Jon Barker, Stuart Cunningham, and Xu Shao. 2006. An audio-
visual corpus for speech perception and automatic speech recognition. The
Journal of the Acoustical Society of America 120, 5 (2006), 24212424.
[7] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2018. BERT:
Pre-training of Deep Bidirectional Transformers for Language Understanding.
CoRR abs/1810.04805 (2018).
[8] Wenhao Guan, Yishuang Li, Tao Li, Hukai Huang, Feng Wang, Jiayan Lin, Lingyan
Huang, Lin Li, and Qingyang Hong. 2024. MM-TTS: Multi-Modal Prompt Based
Style Transfer for Expressive Text-to-Speech Synthesis. In Thirty-Eighth AAAI
Conference on Artificial Intelligence, AAAI 2024, Thirty-Sixth Conference on Inno-
vative Applications of Artificial Intelligence, IAAI 2024, Fourteenth Symposium on
Educational Advances in Artificial Intelligence, EAAI 2014, February 20-27, 2024,
Vancouver, Canada. 1811718125.
[9] Yiwei Guo, Chenpeng Du, Ziyang Ma, Xie Chen, and Kai Yu. 2024. VoiceFlow:
Efficient Text-to-Speech with Rectified Flow Matching. In ICASSP 2024-2024
IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP).
[10] Keikichi Hirose and Jianhua Tao. 2015. Speech Prosody in Speech Synthesis:
Modeling and generation of prosody for high quality and flexible speech synthesis.
Springer.
[11] Wei-Ning Hsu, Benjamin Bolte, Yao-Hung Hubert Tsai, Kushal Lakhotia, Ruslan
Salakhutdinov, and Abdelrahman Mohamed. 2021. HuBERT: Self-Supervised
Speech Representation Learning by Masked Prediction of Hidden Units. IEEE
ACM Trans. Audio Speech Lang. Process. 29 (2021), 34513460. https://doi.org/10.
[12] Chenxu Hu, Qiao Tian, Tingle Li, Yuping Wang, Yuxuan Wang, and Hang Zhao.
2021. Neural Dubber: Dubbing for Videos According to Scripts. In Advances
in Neural Information Processing Systems 34: Annual Conference on Neural In-
formation Processing Systems 2021, NeurIPS 2021, December 6-14, 2021, virtual.
[13] Rongjie Huang, Mingze Li, Dongchao Yang, Jiatong Shi, Xuankai Chang, Zhenhui
Ye, Yuning Wu, Zhiqing Hong, Jiawei Huang, Jinglin Liu, Yi Ren, Yuexian Zou,
Zhou Zhao, and Shinji Watanabe. 2024. AudioGPT: Understanding and Generat-
ing Speech, Music, Sound, and Talking Head. In Thirty-Eighth AAAI Conference
on Artificial Intelligence, AAAI , 2024, Vancouver, Canada. 2380223804.
[14] Rongjie Huang, Zhou Zhao, Huadai Liu, Jinglin Liu, Chenye Cui, and Yi Ren. 2022.
ProDiff: Progressive Fast Diffusion Model for High-Quality Text-to-Speech. In
MM 22: The 30th ACM International Conference on Multimedia, Lisboa, Portugal,
October 10 - 14, 2022. 25952605.
[15] Ye Jia, Heiga Zen, Jonathan Shen, Yu Zhang, and Yonghui Wu. 2021. PnG BERT:
Augmented BERT on Phonemes and Graphemes for Neural TTS. In Interspeech
2021, 22nd Annual Conference of the International Speech Communication Associa-
tion, Brno, Czechia, 30 August - 3 September 2021. 151155.
[16] Ziyue Jiang, Jinglin Liu, Yi Ren, Jinzheng He, Chen Zhang, Zhenhui Ye, Pengfei
Wei, Chunfeng Wang, Xiang Yin, Zejun Ma, and Zhou Zhao. 2023. Mega-TTS
2: Zero-Shot Text-to-Speech with Arbitrary Length Speech Prompts. CoRR
abs/2307.07218 (2023). https://doi.org/10.48550/arXiv.2307.07218
[17] Zeqian Ju, Yuancheng Wang, Kai Shen, Xu Tan, Detai Xin, Dongchao Yang,
Yanqing Liu, Yichong Leng, Kaitao Song, Siliang Tang, et al. 2024. NaturalSpeech
3: Zero-Shot Speech Synthesis with Factorized Codec and Diffusion Models. arXiv
preprint arXiv:2403.03100 (2024).
[18] Tero Karras, Samuli Laine, and Timo Aila. 2019. A Style-Based Generator Archi-
tecture for Generative Adversarial Networks. In IEEE Conference on Computer
Vision and Pattern Recognition, CVPR 2019, Long Beach, CA, USA, June 16-20, 2019.
[19] Eugene Kharitonov, Damien Vincent, Zalán Borsos, Raphaël Marinier, Sertan
Girgin, Olivier Pietquin, Matt Sharifi, Marco Tagliasacchi, and Neil Zeghidour.
2023. Speak, read and prompt: High-fidelity text-to-speech with minimal super-
vision. Transactions of the Association for Computational Linguistics 11 (2023),
[20] Jaehyeon Kim, Sungwon Kim, Jungil Kong, and Sungroh Yoon. 2020. Glow-
TTS: A Generative Flow for Text-to-Speech via Monotonic Alignment Search.
In Advances in Neural Information Processing Systems 33: Annual Confer-
ence on Neural Information Processing Systems 2020, NeurIPS 2020, Decem-
ber 6-12, 2020, virtual.
https://proceedings.neurips.cc/paper/2020/hash/
5c3b99e8f92532e5ad1556e53ceea00c-Abstract.html
[21] Diederik P. Kingma and Jimmy Ba. 2015. Adam: A Method for Stochastic Opti-
mization. In 3rd International Conference on Learning Representations, ICLR 2015,
San Diego, CA, USA, May 7-9, 2015, Conference Track Proceedings.
[22] Jungil Kong, Jaehyeon Kim, and Jaekyoung Bae. 2020.
HiFi-GAN: Gener-
ative Adversarial Networks for Efficient and High Fidelity Speech Synthe-
sis. In Advances in Neural Information Processing Systems 33: Annual Con-
ference on Neural Information Processing Systems 2020, NeurIPS 2020, De-
cember 6-12, 2020, virtual.
https://proceedings.neurips.cc/paper/2020/hash/
c5d736809766d46260d816d8dbc9eb44-Abstract.html
[23] Jiyoung Lee, Joon Son Chung, and Soo-Whan Chung. 2023. Imaginary Voice:
Face-Styled Diffusion Model for Text-to-Speech. In IEEE International Conference
on Acoustics, Speech and Signal Processing ICASSP 2023, Rhodes Island, Greece,
June 4-10, 2023. 15.
[24] Yinghao Aaron Li, Cong Han, Xilin Jiang, and Nima Mesgarani. 2023. Phoneme-
Level Bert for Enhanced Prosody of Text-To-Speech with Grapheme Predictions.
In IEEE International Conference on Acoustics, Speech and Signal Processing ICASSP
2023, Rhodes Island, Greece, June 4-10, 2023. IEEE, 15.
[25] Yinghao Aaron Li, Cong Han, Vinay S. Raghavan, Gavin Mischler, and Nima
Mesgarani. 2023. StyleTTS 2: Towards Human-Level Text-to-Speech through
Style Diffusion and Adversarial Training with Large Speech Language Models.
In Advances in Neural Information Processing Systems 36: Annual Conference
on Neural Information Processing Systems 2023, NeurIPS 2023, New Orleans, LA,
USA, December 10 - 16, 2023. http://papers.nips.cc/paper_files/paper/2023/hash/
3eaad2a0b62b5ed7a2e66c2188bb1449-Abstract-Conference.html
[26] Michael McAuliffe, Michaela Socolof, Sarah Mihuc, Michael Wagner, and Morgan
Sonderegger. 2017. Montreal Forced Aligner: Trainable Text-Speech Alignment
Using Kaldi. In Interspeech 2017, 18th Annual Conference of the International Speech
Communication Association, Stockholm, Sweden, August 20-24, 2017. 498502.
[27] Shivam Mehta, Ruibo Tu, Jonas Beskow, Éva Székely, and Gustav Eje Henter.
2024. Matcha-TTS: A fast TTS architecture with conditional flow matching. In
ICASSP 2024-2024 IEEE International Conference on Acoustics, Speech and Signal
Processing (ICASSP). IEEE, 1134111345.
[28] Dongchan Min, Dong Bok Lee, Eunho Yang, and Sung Ju Hwang. 2021. Meta-
StyleSpeech : Multi-Speaker Adaptive Text-to-Speech Generation. In Proceedings
of the 38th International Conference on Machine Learning, ICML 2021, 18-24 July
2021, Virtual Event, Vol. 139. 77487759.
[29] Linh The Nguyen, Thinh Pham, and Dat Quoc Nguyen. 2023. XPhoneBERT: A
Pre-trained Multilingual Model for Phoneme Representations for Text-to-Speech.
CoRR abs/2305.19709 (2023). https://doi.org/10.48550/arXiv.2305.19709
[30] Vassil Panayotov, Guoguo Chen, Daniel Povey, and Sanjeev Khudanpur. 2015.
Librispeech: An ASR corpus based on public domain audio books. In 2015 IEEE
International Conference on Acoustics, Speech and Signal Processing, ICASSP 2015,
South Brisbane, Queensland, Australia, April 19-24, 2015. 52065210.
[31] Vadim Popov, Ivan Vovk, Vladimir Gogoryan, Tasnima Sadekova, and Mikhail A.
Kudinov. 2021. Grad-TTS: A Diffusion Probabilistic Model for Text-to-Speech. In
Proceedings of the 38th International Conference on Machine Learning, ICML 2021,
18-24 July 2021, Virtual Event, Vol. 139. 85998608.
[32] Alec Radford, Jong Wook Kim, Tao Xu, Greg Brockman, Christine McLeavey,
and Ilya Sutskever. 2023. Robust Speech Recognition via Large-Scale Weak
Supervision. In International Conference on Machine Learning, ICML 2023, 23-29
July 2023, Honolulu, Hawaii, USA. 2849228518.
[33] Yi Ren, Chenxu Hu, Xu Tan, Tao Qin, Sheng Zhao, Zhou Zhao, and Tie-Yan Liu.
2021. FastSpeech 2: Fast and High-Quality End-to-End Text to Speech. In 9th
International Conference on Learning Representations, ICLR 2021, Virtual Event,
Austria, May 3-7, 2021. https://openreview.net/forum?id=piLPYqxtWuA
[34] Yi Ren, Yangjun Ruan, Xu Tan, Tao Qin, Sheng Zhao, Zhou Zhao, and Tie-
Yan Liu. 2019. FastSpeech: Fast, Robust and Controllable Text to Speech. In
Advances in Neural Information Processing Systems 32: Annual Conference on
Neural Information Processing Systems 2019, NeurIPS 2019, December 8-14, 2019,
Vancouver, BC, Canada. 31653174.
[35] Jonathan Shen, Ruoming Pang, Ron J. Weiss, Mike Schuster, Navdeep Jaitly,
Zongheng Yang, Zhifeng Chen, Yu Zhang, Yuxuan Wang, RJ-Skerrv Ryan, Rif A.
Saurous, Yannis Agiomyrgiannakis, and Yonghui Wu. 2018. Natural TTS Syn-
thesis by Conditioning Wavenet on MEL Spectrogram Predictions. In 2018 IEEE

ACM MM, 2024, Melbourne, Australia
Anonymous Authors
International Conference on Acoustics, Speech and Signal Processing, ICASSP 2018,
Calgary, AB, Canada, April 15-20, 2018. 47794783.
[36] Kai Shen, Zeqian Ju, Xu Tan, Yanqing Liu, Yichong Leng, Lei He, Tao Qin, Sheng
Zhao, and Jiang Bian. 2023. NaturalSpeech 2: Latent Diffusion Models are Natural
and Zero-Shot Speech and Singing Synthesizers. CoRR abs/2304.09116 (2023).
https://doi.org/10.48550/ARXIV.2304.09116
[37] Antti Suni, Daniel Aalto, Tuomo Raitio, Paavo Alku, and Martti Vainio. 2013.
Wavelets for intonation modeling in HMM speech synthesis. In The Eighth ISCA
Tutorial and Research Workshop on Speech Synthesis, Barcelona, Spain, August
31-September 2, 2013. 285290.
[38] Xu Tan, Jiawei Chen, Haohe Liu, Jian Cong, Chen Zhang, Yanqing Liu, Xi Wang,
Yichong Leng, Yuanhao Yi, Lei He, et al. 2024. Naturalspeech: End-to-end text-to-
speech synthesis with human-level quality. IEEE Transactions on Pattern Analysis
and Machine Intelligence (2024).
[39] Antoine Toisoul, Jean Kossaifi, Adrian Bulat, Georgios Tzimiropoulos, and Maja
Pantic. 2021. Estimation of continuous valence and arousal levels from faces in
naturalistic conditions. Nat. Mach. Intell. 3, 1 (2021), 4250.
[40] Aäron van den Oord, Sander Dieleman, Heiga Zen, Karen Simonyan, Oriol
Vinyals, Alex Graves, Nal Kalchbrenner, Andrew W. Senior, and Koray
Kavukcuoglu. 2016. WaveNet: A Generative Model for Raw Audio. In The 9th
ISCA Speech Synthesis Workshop, Sunnyvale, CA, USA, 13-15 September 2016. 125.
[41] Li Wan, Quan Wang, Alan Papir, and Ignacio López-Moreno. 2018. Generalized
End-to-End Loss for Speaker Verification. In 2018 IEEE International Conference
on Acoustics, Speech and Signal Processing, ICASSP 2018, Calgary, AB, Canada,
April 15-20, 2018. 48794883.
[42] Chengyi Wang, Sanyuan Chen, Yu Wu, Ziqiang Zhang, Long Zhou, Shujie Liu,
Zhuo Chen, Yanqing Liu, Huaming Wang, Jinyu Li, Lei He, Sheng Zhao, and
Furu Wei. 2023. Neural Codec Language Models are Zero-Shot Text to Speech
Synthesizers. CoRR abs/2301.02111 (2023). https://doi.org/10.48550/arXiv.2301.
[43] Jiaxin Ye, Xin-Cheng Wen, Yujie Wei, Yong Xu, Kunhong Liu, and Hongming
Shan. 2023. Temporal Modeling Matters: A Novel Temporal Emotional Modeling


## Approach

Acoustics, Speech and Signal Processing ICASSP 2023, Rhodes Island, Greece, June
4-10, 2023. IEEE, 15.
[44] Heiga Zen, Viet Dang, Rob Clark, Yu Zhang, Ron J. Weiss, Ye Jia, Zhifeng Chen,
and Yonghui Wu. 2019. LibriTTS: A Corpus Derived from LibriSpeech for Text-
to-Speech. In Interspeech 2019, 20th Annual Conference of the International Speech
Communication Association, Graz, Austria, 15-19 September 2019. 15261530.
[45] Guangyan Zhang, Kaitao Song, Xu Tan, Daxin Tan, Yuzi Yan, Yanqing Liu, Gang
Wang, Wei Zhou, Tao Qin, Tan Lee, and Sheng Zhao. 2022. Mixed-Phoneme
BERT: Improving BERT with Mixed Phoneme and Sup-Phoneme Representations
for Text to Speech. In Interspeech 2022, 23rd Annual Conference of the International
Speech Communication Association, Incheon, Korea, 18-22 September 2022. 456
[46] Shifeng Zhang, Xiangyu Zhu, Zhen Lei, Hailin Shi, Xiaobo Wang, and Stan Z Li.
2017. S3fd: Single shot scale-invariant face detector. In Proceedings of the IEEE
international conference on computer vision. 192201.
[47] Yixuan Zhou, Changhe Song, Xiang Li, Luwen Zhang, Zhiyong Wu, Yanyao
Bian, Dan Su, and Helen Meng. 2022. Content-Dependent Fine-Grained Speaker
Embedding for Zero-Shot Speaker Adaptation in Text-to-Speech Synthesis. In In-
terspeech 2022, 23rd Annual Conference of the International Speech Communication
Association, Incheon, Korea, 18-22 September 2022. 25732577.

