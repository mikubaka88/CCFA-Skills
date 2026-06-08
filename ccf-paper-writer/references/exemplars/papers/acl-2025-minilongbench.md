# MiniLongBench

> **Venue:** ACL2025
> **Award:** Outstanding Paper
> **Source:** <https://aclanthology.org/2025.acl-long.560/>

---
Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 1144211460
July 27 - August 1, 2025 ©2025 Association for Computational Linguistics
MiniLongBench: The Low-cost Long Context Understanding
Benchmark for Large Language Models
Zhongzhan Huang1, Guoming Ling1, Shanshan Zhong1, Hefeng Wu1, Liang Lin1,2,3
1Sun Yat-sen University 2Peng Cheng Laboratory
3Guangdong Key Laboratory of Big Data Analysis and Processing


## Abstract

Long Context Understanding (LCU) is a crit-
ical area for exploration in current large lan-
guage models (LLMs). However, due to the
inherently lengthy nature of long-text data, ex-
isting LCU benchmarks for LLMs often re-
sult in prohibitively high evaluation costs, like
testing time and inference expenses. Through
extensive experimentation, we discover that
existing LCU benchmarks exhibit significant
redundancy, which means the inefficiency in


## Evaluation

cise data compression method tailored for long-
text data with sparse information characteris-
tics. By pruning the well-known LCU bench-
mark LongBench, we create MiniLongBench.
This benchmark includes only 237 test sam-
ples across six major task categories and 21
distinct tasks. Through empirical analysis of
over 60 LLMs, MiniLongBench achieves an
average evaluation cost reduced to only 4.5%
of the original while maintaining an average
rank correlation coefficient of 0.97 with Long-
Bench results. Therefore, our MiniLongBench,
as a low-cost benchmark, holds great potential
to substantially drive future research into the
LCU capabilities of LLMs. See Github for our
code, data and tutorial.


## Introduction

The ability for long context understanding, a.k.a
LCU, (Press et al., 2022; Sun et al., 2022; Chen
et al., 2023; Zeng et al., 2023; Li et al., 2023a;
Beltagy et al., 2020; Roy et al., 2021) is one of
the most important areas of exploration for cur-
rent large language models (LLMs). Tasks with
broad applications, such as summarization and
question answering based on books, papers, and
documents, as well as repository-level code gener-
ation, require the capability to handle long context
sequences spanning thousands or even tens of thou-
sands of tokens. Currently, the LCU capabilities
of LLMs are still in their early stages, and their
Test Time (hours)
OPT-30B Wizard-Vicuna Llama-30B LwQ-Instruct
30B-Epsilon
1.36h
1.04h
1.02h
0.83h
0.78h
LongBench
MiniLongBench (ours)
Figure 1: The computational cost of LongBench and
MiniLongBench. The proposed MiniLongBench effec-
tively reduces the computational cost of the LongBench,
thereby achieving a low-cost LCU benchmark.
rapid development relies on recent proposals of
LCU benchmarks (Shaham et al., 2022, 2023; An
et al., 2023; Bai et al., 2024d). However, unlike nor-
mal LLM benchmarks (Li et al., 2024; Guo et al.,
2023; Zhong et al., 2024b, 2023a), LCU bench-
marks inherently involve a large number of tokens
due to the nature of long context data. Combined
with the high number of test samples, the primary
challenge these benchmarks face is their high evalu-
ation cost. As shown in Fig. 1, some popular LLMs
on 8RTX3090 GPUs require approximately up
to 15 ∼30 hours to complete an evaluation on
LongBench with one batch size. Moreover, due
to the large number of tokens in each long-text
data, which significantly increases GPU memory
consumption, it is challenging to accelerate test-
ing through multi-batch processing. Therefore, the
computational cost illustrated in Fig. 1 cannot be
overlooked. Furthermore, when researchers de-
velop new LLM models and need to conduct mul-
tiple analyses of LCU capabilities, the time and
computational costs become even more prohibitive.
Given these challenges, we ask a critical question:
Do LCU benchmarks really need such a large
number of test samples?
To answer this question, in this paper, we explore
the compression of the well-known LCU bench-

Spearman Correlation
SQA MQA SUM FSL CODE SYN
SQA MQA SUM FSL CODE SYN
SQA MQA SUM FSL CODE SYN
Reduce 99%
Reduce 98%
Reduce 95%
Strong corr.
Moderate corr.
Strong corr.
Moderate corr.
Strong corr.
Moderate corr.
Figure 2: The redundancy of LongBench. "Reduce 95%" means randomly removing 95% of the dataset with
equal probability. A Spearman correlation (Sp) 0.8 indicates a strong correlation and Sp 0.6 means moderate
correlation between the results of randomly sampled subset and LongBench. The abscissa labels from "SQA" to
"SYN" represent the abbreviations of the six main tasks in LongBench, with details provided in Section 2.
mark, LongBench (Bai et al., 2024a). In Section 2,
we first validate the significant redundancy in the
LongBench through a series of random sampling
experiments. Furthermore, in Section 3, we pro-
pose a simple-yet-effective compression method
for long-text data with sparse information, resulting
in a compact LCU benchmark, MiniLongBench.
Finally, we explore the evaluation results of Mini-
LongBench across a range of existing LLMs. Our
findings indicate that the proposed MiniLongBench
substantially lowers the evaluation cost of LCU ca-
pabilities, reducing it to merely 4.5% of the origi-
nal, while maintaining the assessment outcomes of
LLM on LongBench. We show the related works
in Appendix D, and summarize the contributions
of this paper as follows:
In this paper, we analyze the redundancy of
current LCU benchmark for LLMs and propose
an effective method to reduce the number of
test samples for low-cost testing.
Analyzing on over 60 LLMs, our MiniLong-
Bench achieves an average ranking correlation
of about 0.97 with LongBench while reducing
computational cost to only 4.5% of the original.
The Redundancy of LCU Benchmark
In this section, we consider the well-known LCU
benchmark, LongBench (Bai et al., 2024a), as an
example to demonstrate that current LCU bench-
marks suffer from significant redundancy. Long-
Bench includes nearly 5000 test samples and covers
six main task categories, such as single-document
question answering (SQA), multi-document ques-
tion answering (MQA), summarization (SUM),
few-shot learning (FSL), code completion (CODE),
and synthetic tasks (SYN), which represent key
long-text application scenarios. For specific details
of LongBench, please refer to the Appendix A.
First, we randomly sample the long-text data
from different categories of LongBench n=10,000
times to obtain n subsets of test samples with com-
pression ratio p, where p represents the proportion
of remaining samples after sampling. We then test
these subsets using dozens of LLMs (see the Ap-
pendix B for details), and compute the Spearman
correlation (Sp) coefficient (Spearman, 1961) to
measure the ranking correlation between the evalu-
ation results of each subset and those of the original
LongBench SL. The closer "Sp" is to 1.0, the more
the evaluation of the sampled subset aligns with the


## Evaluation

and select the top 7500 results based on Sp for
statistical analysis. The experimental results are
shown in Fig 2. We find that even though Long-
Bench data is randomly reduced by a large amount,
some subsets of LongBench still exhibit strong
ranking correlations with the original benchmark,
e.g., with Sp greater than 0.8 and even 0.9. This in-
dicates that LongBench contains significant redun-
dancy and does not require so many test samples.
Therefore, in this paper, we will design an efficient


## Method

Compression for LCU Benchmark
In this section, we explore how to filter long-text
data to reduce the size of LCU benchmark, en-
abling our MiniLongBench for low-cost estimation
of LCU capabilities. Although Fig. 2 shows that
random sampling can also yield subsets with large
Sp, due to its high variance, we need to develop
a more stable compression method. A straight-
forward intuition is that, given a set of m LLMs
{ℓi}m
i=1, we can leverage their performance on all
test samples from LongBench SL = {sj}|SL|
j=1. Us-
ing their performance record, we aim to construct
a regression model to map these sparsely infor-

Data Preprocessing
Test sample
(sparse)
Test sample
(dense)
Embedding
Reduce dim
Representation Learning
Clustering
Sample Emb.
LLM Emb.
Per.
Regression
-means with
Data Pruning
Figure 3: The compression process of the LCU benchmark. "Emb." and "Per." respectively denote embedding and
the performance of LLM ℓi on sample sj under the given metric metr(·, ·).
Algorithm 1 The construction of MiniLongBench.
Input: The long-text data SL = (s1, s2, ..., s|SL|), reduced
dimension d and ratio p. The performance record metr(ℓi, sj)
from LLM ℓi and sample sj. Text embedding κtest.
Output: Compact LCU benchmark.
▷Data preprocessing
Intra-sample dimension reduction s′
j κtext(sj);
Inter-sample dimension reduction by
{ej}|SL|
j=1 PCAd[s′
1, s′
2, ..., s′
|SL|];
▷Representation learning for test samples
Initialize LLM ℓis representation by θi ∼N(0, Id);
Initialized j 0;
Update learnable (ej, j) and θi by Eq. (2);
▷Clustering
Determine the number of cluster centers K (1−p)|SL|;
Obtain K centers (c1, c2, .., cK) by clustering and (ej, j);
Smini (c1, c2, .., cK);
return Compact LCU benchmark Smini
mative long-text samples into a denser text space
first, and gradually project them into a performance
space. After that, we can learn the representation
of the test samples. Moreover, we then cluster
these samples and retain only a certain number
of cluster centers as representative test samples,
forming Smini, thereby compressing the benchmark.
Fig. 3 and Alg. 1 show the compression process of
the LCU benchmark and construction of proposed
MiniLongBench. Specifically,
(1) Data Preprocessing. Unlike data from conven-
tional LLM benchmarks, the effective information
in long-text data is highly sparse. Without proper
compression of this information, it can significantly
impact subsequent representation learning and clus-
tering processes. Therefore, for the sparse infor-
mation in these long-text data, we initially den-
sify them using a text encoder κtext OpenAIEmbed-
ding (Xian et al., 2024) and a principal component
analysis, a.k.a PCA, (Abdi and Williams, 2010) to
obtain part of dense d−dimentional initialization
of test samples, i.e.,
{ej}|SL|
j=1 = PCAd[{κtext(sj)}|SL|
j=1],
(1)
For a detailed discussion on how data preprocess-
ing influences the construction of MiniLongBench,
please refer to Section 5.
(2) Representation Learning. Moreover, similar
to (Polo et al., 2024), which utilizes the Item Re-
sponse Theory in psychology and education (Cai
et al., 2016), we can perform representation learn-
ing for test samples.
Suppose we have LLMs
{ℓi}m
i=1 and test samples sj ∈SL with perfor-
mance measured by the metric metr(·, ·). We then
assume that the probability of LLM ℓi correctly
answering sample sj is given by:
P(metr(ℓi, sj) = 1|θi, ej, j)
= [1 + exp(−ej⊤θi + j)]−1,
(2)
where the learnable parameter θi ∈Rd represents
the d-dimensional embedding of LLM ℓi, initial-
ized using a d-dimensional standard normal dis-
tribution. Eq. (2) is classical logistic regression
model (Kleinbaum et al., 2002). The parameters
(ej, j) are the learnable representations of the test
sample sj, where j is initialized to zero vector
and ej initialized by Eq. (1). In this paper, we set
d = 10. See further analysis on these representa-
tions, initialization and d in Section 5.
It is worth noting that in Eq. (2), we use a bi-
nary classification example for the metric, where
metr(ℓi, sj) = 1 if ℓi performs correctly on sj, and
metr(ℓi, sj) = 0 otherwise. If metr(·, ·) is con-
tinuous metrics, it can also be transformed into a
binary classification scenario. Specifically, the met-
ric metr(·, ·) is generally bounded. For example,
in LongBench, metrics such as F1 score, edit dis-
tance, etc., are used. We can normalize them to
the interval [0, 1] , and then consider the following
optimization problem.
min
i=1
X|SL|
j=1 metr(ℓi, sj)
i=1
X|SL|
j=1 1[metr(ℓi,sj)c]∥,
(3)
Note that the existence of a solution to Eq. (3) is
evident. It can be obtained by simply searching

Dataset
Index
Metric
Language
Long. Avg len
MiniLong. Avg len
Long. #data
MiniLong. #data
Single-Document QA
NarrativeQA
English
6 (97%)
Qasper
English
9 (96%)
MultiFieldQA-en
English
7 (95%)
MultiFieldQA-zh
Chinese
15 (93%)
Multi-Document QA
HotpotQA
English
13 (94%)
2WikiMultihopQA
English
13 (94%)
MuSiQue
English
7 (97%)
DuReader
Rouge-L
Chinese
6 (97%)
Summarization
GovReport
Rouge-L
English
12 (94%)
QMSum
Rouge-L
English
6 (97%)
MultiNews
Rouge-L
English
11 (95%)
VCSUM
Rouge-L
Chinese
6 (97%)
Few-shot Learning
TREC
Acc. (CLS)
English
8 (96%)
TriviaQA
English
12 (94%)
SAMSum
Rouge-L
English
15 (93%)
LSHT
Acc. (CLS)
Chinese
8 (96%)
Synthetic Task
PassageCount
Acc. (EM)
English
4 (98%)
PassageRetrieval-en
Acc. (EM)
English
15 (93%)
PassageRetrieval-zh
Acc. (EM)
Chinese
15 (93%)
Code Completion
LCC
Edit Sim
Python/C#/Java
26 (95%)
RepoBench-P
Edit Sim
Python/Jave
23 (95%)
Table 1: The dataset statistics in LongBench and MiniLongBench. "Long." and "MiniLong." denote LongBench
and MiniLongBench. "Avg len" (average length) is computed using the number of words for the English (code)
datasets and the number of characters for the Chinese datasets. "Acc. (CLS)" refers to classification accuracy, while
"Acc. (EM)" refers to exact match accuracy. "#data" means the number of data.
Count
Chinese
English
Length
Length
LongBench
LongBench
Figure 4: The Length distribution for English and Chi-
nese data in LongBench and MiniLongBench, measured
by the number of words and characters.
the interval [0, 1] to get an approximate solution
for c. Once c is obtained, we replace the origi-
nal metr(ℓi, sj) with metr(ℓi, sj)′ = 1[metr(ℓi,sj)c]
which can transform the continuous metric into a
discrete binary scenario similar to Eq. (2).
(3) Clustering. Next, we update θi, ej, and j
simultaneously using the training approach of lo-
gistic regression. Once these learnable parameters
converge, we concatenate (ej, j) as the final rep-
resentation of the test sample sj, and perform clus-
tering analysis on them using K-Means (Hamerly
and Elkan, 2003) under Euclidean distance, where
K = (1−p)|SL|. Finally, the all cluster centers are
integrated as the test samples of MiniLongBench
Smini. In Section 4, we will further validate the
effectiveness of MiniLongBench from an experi-
mental perspective.
Compact LCU Benchmark:
In this section, we present our compact MiniLong-
Bench and demonstrate through comprehensive
experiments that it significantly reduces computa-
tional costs while preserving original LongBenchs


## Evaluation

for analysis, with m = 20 of them participating in
the training described in Section 3, and the rest serv-
ing as candidates for validating the effectiveness
of MiniLongBench. See Appendix B for details of
LLMs considered.
The Details of MiniLongBench
Chosing compression ratio p = 0.95, we use the
compression method shown in Section 3 for Long-
Bench to obtain compact LCU benchmark Mini-
LongBench. This benchmark includes only 237
test samples across six task categories, with an av-
erage length of 6193 words (English) and 10344

Model
SQA
MQA
SUM
FSL
SYN
CODE
DeepSeek-V3-128k
GPT-4o-mini-128k
GPT-3.5-Turbo-16k
Internlm3-8B-32k
ChatGLM3-6B-8k
ChatGLM4-9B-128k
Qwen-7B-8k
Qwen2-7B-128k
Qwen2.5-7B-128k
Qwen2.5-14B-128k
Qwen2.5-32B-128k
Llama-7B-2k
Llama2-7B-4k
Llama3-8B-8k
Llama-30B-2k
OPT-30B-2k
Wizard-Vicuna-2k
LwQ-Instruct-2k
30B-Epsilon-2k
Table 2: Specific evaluation results on MiniLongBench.
See Appendix C and Appendix G for the more analysis
and detail results on various advanced LLMs.
characters (Chinese). Consistent with LongBench,
MiniLongBench has six major task categories and
21 distinct tasks, covering key long-text application
scenarios. Through the long-text dataset compres-
sion method proposed in Alg. 1, these different
tasks have been compressed by about 95%, greatly
reducing the computational consumption of the
LCU benchmark in the testing process. The spe-
cific statistics is shown in Table 1.
As shown in Table 1, the average length of Mini-
LongBench is smaller compared to that of Long-
Bench due to data pruning, but it generally main-
tains a similar magnitude. This indicates that Long-
Bench retains a good diversity of long-text data
even after compression. Moreover, we further illus-
trate the length distribution of data across different
languages, including English and Chinese, in Fig. 4.
We observe that for different languages, our pro-
posed MiniLongBench significantly reduces the to-
tal length of data input to the LLM, thereby greatly
decreasing the number of tokens in the model in-
put and reducing computational costs. The further
discussions with other compression ratio p and m
trained LLMs are shown in Section 5.
The Evaluation Method
In this section, we explore how to evaluate the
LCU capabilities of LLMs using MiniLongBench.
A straightforward approach is to directly assess
them on MiniLongBench, yielding reliable results
with a Sp of 0.95 compared to LongBench (see
Appendix G for details). However, its important
to note that MiniLongBench, having significantly
Longbench Scores
MiniLongbench Scores
Train (Sp=0.98)
Test (Sp=0.96)
ALL (Sp=0.97)
Figure 5: The analysis of rank correlation (Sp) between
LongBench and MiniLongBench.
fewer test samples than LongBench, may introduce
some evaluation bias. To mitigate this, we can use
MiniLongBench samples to estimate the perfor-
mance (Polo et al., 2024; Pacchiardi et al., 2024)
of the LLMs on LongBench, thereby reducing bias
and achieving an improved Sp of up to 0.97.
Specifically, For a new LLM ℓ0 to be tested,
we first evaluate it on all test samples cj from
MiniLongBench Smini and obtain its performance
metr(ℓ0, cj). Subsequently, we apply consistent
normalization and discretization for metr(ℓ0, cj) as
outlined in Section 3, and initialize a d-dimensional
feature vector ¯θ for the LLM ℓ0 using a standard
normal distribution.
Next, we fine-tune ¯θ on the test samples of Smini
using Eq. (2) to adapt it to the representation space
of the test samples. After completing the fine-
tuning, we can construct the following MiniLong-
Bench score through Eq. (2) to estimate the perfor-
mance of ℓ0 across the entire SL:
X|SL|
j=1[1 + exp(−ej⊤¯θ + j)]−1/|SL|,
(4)
The time required for fine-tuning in the aforemen-
tioned evaluation process and the storage cost for
the features of SL are both minimal, requiring only
about 10 MB of disk space and as little as 0.03 sec-
onds of GPU time, even on a laptop. For specific
statistics, please refer to Appendix H.
The Evaluation Results
Moreover, Fig. 5 shows the rank correlation be-
tween LongBench and the proposed MiniLong-
Bench are 0.96∼0.98, whether on the LLMs that
participated in the training or on other unseen
LLMs. Moreover, in conjunction with the results
presented in Fig.1, this indicates that the proposed
MiniLongBench can effectively replicate the evalu-
ation outcomes of LongBench while maintaining
very low computational costs.
Additionally, we present in Table 2 the specific
performance of various advanced LLMs across dif-

Spearman Corr.
Compression dimension
Train (r = -0.77)
Test (r = -0.96)
Figure 6: The impact of compression dimension d on
the construction of MiniLongBench. "r" is Pearson
correlation coefficient.
ferent tasks on the proposed MiniLongBench. For
more detailed results, please refer to Appendix C.
Analysis
In this Section, We conduct a more comprehensive
analysis of the proposed MiniLongBench.
(1) How does the reduced dimension d affect
the compression of the LCU benchmark?
In Eq. (1) of Session 3, we perform initial compres-
sion of the long-text data in LongBench using text
embedding OpenAIEmbedding (Xian et al., 2024)
and a PCA (Abdi and Williams, 2010), allowing
the long-text information to be initialized as some
vectors with dimension d.
In this section, we further explore the specific
impact of the compressed dimension d on construct-
ing a compact MiniLongBench. Specifically, fol-
lowing the experiment setting in Section 4, we con-
sider d ∈{5, 10, 15, 20, 25, 30, 50, 70, 100} and
present the Sp of the evaluation results for Long-
Bench and MiniLongBench under different values
of d in Fig. 6. We observe that a negative corre-
lation between Sp and d. This indicates that for
long-texts data with sparse information, using ex-
cessively high-dimensional representations is not
advisable, as it can still lead to sparse representa-
tions even after representation learning. Further
information compression is crucial. In this paper,
we set d = 10 by default.
(2) Is PCA necessary for MiniLongBench?
In data preprocessing, PCA is employed to fur-
ther reduce the dimensionality of features after text
embedding. If we remove the PCA operation in
Eq. (1), on one hand, the high dimension of κtext,
which reaches 1024, would result in significant ad-
ditional computational overhead during training.
(a)Various compression ratio
(b) text embedding
(c) For bias
Ratio
Longf.
w/o
rand
randn
zero
Open.
BERT
Figure 7: Further analysis for MiniLongBench. The


## Results

text embedding κtext. (c) The influence of various j.
The bars with darker color represent the settings adopted
by our settings. "rand" and "randn" denote the standard
uniform and normal distribution. "Longf." and "Open."
are Longformer and OpenAIEmbedding.
Moreover, due to the large dimensionality, we ob-
serve that the average Sp of MiniLongBench and
LongBench drops from 0.95 to 0.67, which aligns
with the phenomenon observed in Fig. 6. There-
fore, the dimension reducing method, like PCA, is
essential for the construction of MiniLongBench.
(3) How to select the text embedding κtext.
In the data preprocessing phase, we utilize Ope-
nAIEmbedding (Xian et al., 2024) for text em-
bedding. In Fig. 7 (b), we present the results of
employing alternative text embeddings, including
Longformer (Zhu et al., 2021) and BERT (Liu et al.,
2019). We observe that BERT, which only supports
token inputs with a maximum length of 512, sig-
nificantly underperforms compared to OpenAIEm-
bedding and Longformer, which support lengths of
8192 and 4096, respectively. This is primarily due
to BERTs weaker capability in information densi-
fication and the inevitable information loss when
handling test samples exceeding the token length
limit, as they can only be processed through chun-
ked densification. Therefore, this paper defaults to
using the more capable OpenAIEmbedding.
(4) How about other compression ratios p?
In this paper, we set the compression ratio p = 0.95
as the default. Subsequently, we further explore the
selection of p in Fig. 7 (a). We observe that as p ap-

Density
Density
Spearman Correlation
Spearman Correlation
Spearman Correlation
Single-Document QA
Multi-Document QA
Summarization
Few-shot Learning
Code Completion
Synthetic Task
Spearman Correlation
Spearman Correlation
Spearman Correlation
Ours (Sp = 0.93)
Avg. (Sp = 0.84)
Ours (Sp = 0.93)
Avg. (Sp = 0.89)
Ours (Sp = 0.83)
Avg. (Sp = 0.77)
Ours (Sp = 0.90)
Avg. (Sp = 0.87)
Ours (Sp = 0.96)
Avg. (Sp = 0.88)
Ours (Sp = 0.84)
Avg. (Sp = 0.80)
Figure 8: The impact of the selection of LLMs on the construction of MiniLongBench .
proaches 1, meaning more test samples are reduced,
the Sp between MiniLongBench and LongBench
decreases, which aligns with the observations in
Fig. 2. This is because, although the LCU bench-
mark has significant redundancy in test samples,
an extremely low compression ratio can easily dis-
rupt the data distribution or diversity of the bench-
mark, leading to substantial bias in the evaluation
of LLMs. Based on the experimental results in
Fig. 7 (a), p = 0.95 is a favorable choice, as it
balances both the testing cost and the evaluation
capability of the benchmark.
(5) Is the learnable bias j important?
In Eq. (2), we introduce a learnable bias j for the
logistic regression model. In Fig. 7 (c), we explore
its impact on the construction of MiniLongBench
by testing different initializations and removing it
entirely. We observe that, on one hand, the inclu-
sion of j aids in the representation learning of
test samples, as removing it results in a noticeable
decline in Sp. On the other hand, different ini-
tializations yield varying performance levels, with
zero initialization achieving the best results. In con-
clusion, the setting of learnable j is important, and
we employ a learnable bias with zero initialization.
(6) About the selection of m LLMs.
In this section, we further analyze the impact of the
LLMs involved in training on the construction of
MiniLongBench from the selection of LLMs.
We fix the number of LLMs, m, and then inde-
pendently sample 1000 times from all the LLMs
considered in this paper. Using the method men-
tioned in Section 3, we obtain various compact
new "MiniLongBench" and compute its Sp distri-
bution against LongBench evaluation results. The
results are shown in Fig. 8. We find that the choice
of LLMs involved in training significantly affects
the construction of MiniLongBench, which is in-
tuitive. This is because the representation of test
samples depends on the performance records of
the LLMs on LongBench, and when the selected
LLMs perform poorly, their representations strug-
gle to correctly project the test samples into the
performance space. In this paper, we manually se-
lect a few LLMs with generally good performance
across various aspects to participate in the construc-
tion of MiniLongBench. A list of the chosen LLMs
can be found in Appendix B. In the future, the
automated LLMs selection is needed.
(7) What is the appropriate number of
LLMs m to involve in training?
Moreover, we further explore the impact of the
number of LLMs involved in training. For a spe-
cific number of LLMs, m, we repeat the indepen-
dent sampling 5 times and compute the average Sp
of the constructed MiniLongBench and LongBench


## Evaluation

shown in Fig. 9. We observe that as m increases,
Sp gradually increases and approaches 1.0. This
indicates that involving enough LLMs is benefi-
cial for the representation learning of test samples.
And we also note that when m = 20, the Sp in
different tasks seems acceptable, suggesting that

Single-Document QA
Multi-Document QA
Summarization
Few-shot Learning
Code Completion
Synthetic Task
# Trained LLMs
# Trained LLMs
# Trained LLMs
# Trained LLMs
# Trained LLMs
# Trained LLMs
Spearman Corr.
Spearman Corr.
Figure 9: The impact of the number of LLMs m on the construction of MiniLongBench .
although the number of LLMs aids in representa-
tion learning, there is still considerable redundancy.
Considering the computational cost, we take the
acceptable m = 20 as default.
(8) Is the average Sp 0.97 enough?
In Section 4, we show that the proposed MiniLong-
Bench achieves an average Sp of 0.97 compared to
LongBench. And, we also find that the p-value is
less than 0.001, indicating the ranking correlation
is not only very strong but also highly statistically
significant. Next, It is noted that since Sp cannot
completely reach 1.0, therefore, the errors are in-
evitably present.
To demonstrate the usability of MiniLongBench
with Sp = 0.97, in addition to the experiment in
Fig. 5, we consider directly visualizing the ranking


## Results

in Fig. 10, for some random test samples, we also
randomly selected 8 different LLMs to compare
their ranking results on MiniLongBench and Long-
Bench. We can observe that the ranking results
are quite similar, despite some minor discrepancies.
For more results, please refer to Appendix F. In
the future, we should further refine the compres-
sion methods to bring Sp as close as possible to 1.0
across all subtasks.
(9) Why not just random sampling?
In Fig. 2, we show that through random sampling,
we identify a significant amount of redundancy in
LongBench. However, relying solely on random
LongBench
Rank
Example 1
Example 2
LLM Index
LLM Index
LongBench
Figure 10: The visualization of ranking. See more
ranking examples in Appendix F.
sampling to compress LongBench is insufficient.
The primary reason is that while random sampling
can probabilistically yield high Sp results, as shown
in Fig. 2, the variance is substantial, making it easy
to achieve suboptimal compression.
The compression method we propose in Sec-
tion 3 for the LCU benchmark effectively mitigates
these issues, consistently achieving high Sp across
various subtasks.


## Conclusion

In this paper, we propose a concise data compres-
sion method for long-text data with sparse informa-
tion. By pruning the well-known LCU benchmark
LongBench, we created MiniLongBench. Through
empirical analysis of over 60 LLMs with varying
performance levels, MiniLongBench achieved an
average evaluation cost reduction to 4.5% of the
original, while maintaining strong consistency with
LongBench results. This phenomenon indicates
that the proposed MiniLongBench has great poten-
tial to greatly promote the exploration of LLMs
LCU capabilities in the future.

Limitations
The LCU benchmark compression method shown
in this paper requires performance records from
various LLMs as training data. However, most of
this data is not open-source in practice. Conse-
quently, we need to incur significant API costs and
GPU computational resources to obtain this data.
On the other hand, although we have achieved ef-
fective compression for LongBench, since Sp can-
not be 1.0, we cannot expect MiniLongBench to
have exactly the same evaluation capabilities as
LongBench, only nearly identical. Additionally,
there is still considerable room for performance
improvement in the summarization and synthetic
tasks, which are worthwhile directions for future
enhancements.
Acknowledgments
This work was supported by National Science and
Technology Major Project (No.2021ZD0111601),
National Natural Science Foundation of China
under Grants No.
62325605, Guangdong Basic and Applied Ba-
sic Research Foundation (No.2023A1515011374,
2023A1515012845), and Guangzhou Science and
Technology Program (No.2024A04J6365).
References
Herve Abdi and Lynne J Williams. 2010. Principal
component analysis. Wiley interdisciplinary reviews:
computational statistics, 2(4):433459.
Rishabh Agarwal, Avi Singh, Lei M Zhang, Bernd
Bohnet, Luis Rosias, Stephanie Chan, Biao Zhang,
Ankesh Anand, Zaheer Abbas, Azade Nova, et al.
2024. Many-shot in-context learning. arXiv preprint
arXiv:2404.11018.
Joshua Ainslie, Tao Lei, Michiel de Jong, Santiago
Ontañón, Siddhartha Brahma, Yury Zemlyanskiy,
David Uthus, Mandy Guo, James Lee-Thorp, Yi Tay,
et al. 2023.
Colt5: Faster long-range transform-
ers with conditional computation. arXiv preprint
arXiv:2303.09752.
Chenxin An, Shansan Gong, Ming Zhong, Mukai
Li, Jun Zhang, Lingpeng Kong, and Xipeng Qiu.
2023. L-eval: Instituting standardized evaluation
for long context language models. arXiv preprint
arXiv:2307.11088.
Chenxin An, Shansan Gong, Ming Zhong, Xingjian
Zhao, Mukai Li, Jun Zhang, Lingpeng Kong, and
Xipeng Qiu. 2024. L-eval: Instituting standardized


## Evaluation

ceedings of the 62nd Annual Meeting of the Associa-
tion for Computational Linguistics (Volume 1: Long
Papers), pages 1438814411, Bangkok, Thailand.
Association for Computational Linguistics.
Anthropic. 2024. Anthropic: Introducing claude 3.5
sonnet.
Yushi Bai, Xin Lv, and et al. 2024a. Longbench: A bilin-
gual, multitask benchmark for long context under-
standing. In Proceedings of the 62nd Annual Meet-
ing of the Association for Computational Linguistics,
pages 31193137. Association for Computational
Linguistics.
Yushi Bai, Xin Lv, Jiajie Zhang, Yuze He, Ji Qi, Lei
Hou, Jie Tang, Yuxiao Dong, and Juanzi Li. 2024b.
LongAlign: A recipe for long context alignment of
large language models. In Findings of the Associa-
tion for Computational Linguistics: EMNLP 2024,
pages 13761395, Miami, Florida, USA. Association
for Computational Linguistics.
Yushi Bai, Xin Lv, Jiajie Zhang, Hongchang Lyu,
Jiankai Tang, Zhidian Huang, Zhengxiao Du, Xiao
Liu, Aohan Zeng, Lei Hou, Yuxiao Dong, Jie Tang,
and Juanzi Li. 2024c. LongBench: A bilingual, mul-
titask benchmark for long context understanding. In
Proceedings of the 62nd Annual Meeting of the As-
sociation for Computational Linguistics (Volume 1:
Long Papers), pages 31193137, Bangkok, Thailand.
Association for Computational Linguistics.
Yushi Bai, Shangqing Tu, Jiajie Zhang, Hao Peng,
Xiaozhi Wang, Xin Lv, Shulin Cao, Jiazheng Xu,
Lei Hou, Yuxiao Dong, et al. 2024d. Longbench
v2: Towards deeper understanding and reasoning
on realistic long-context multitasks. arXiv preprint
arXiv:2412.15204.
Yushi Bai, Jiajie Zhang, Xin Lv, Linzhi Zheng, Siqi
Zhu, Lei Hou, Yuxiao Dong, Jie Tang, and Juanzi
Li. 2024e. Longwriter: Unleashing 10,000+ word
generation from long context llms. arXiv preprint
arXiv:2408.07055.
Iz Beltagy, Matthew E Peters, and Arman Cohan. 2020.
Longformer: The long-document transformer. arXiv
preprint arXiv:2004.05150.
Egor Bogomolov, Aleksandra Eliseeva, Timur Gal-
imzyanov, Evgeniy Glukhov, Anton Shapkin, Maria
Tigina, Yaroslav Golubev, Alexander Kovrigin, Arie
van Deursen, Maliheh Izadi, et al. 2024. Long code
arena: a set of benchmarks for long-context code
models. arXiv preprint arXiv:2406.11612.
Aydar Bulatov, Yury Kuratov, and Mikhail Burtsev.
2022. Recurrent memory transformer. Advances
in Neural Information Processing Systems, 35:11079
Li Cai, Kilchan Choi, Mark Hansen, and Lauren Har-
rell. 2016. Item response theory. Annual Review of
Statistics and Its Application, 3(1):297321.

Shouyuan Chen, Sherman Wong, Liangjian Chen, and
Yuandong Tian. 2023. Extending context window of
large language models via positional interpolation.
arXiv preprint arXiv:2306.15595.
Rewon Child,
Scott Gray,
Alec Radford,
and
Ilya
Sutskever.
Generating
long
se-
quences with sparse transformers. arXiv preprint
arXiv:1904.10509.
Zihang Dai, Zhilin Yang, Yiming Yang, Jaime G Car-
bonell, Quoc Le, and Ruslan Salakhutdinov. 2019.
Transformer-xl: Attentive language models beyond
a fixed-length context. In Proceedings of the 57th
Annual Meeting of the Association for Computational
Linguistics, pages 29782988.
Pradeep Dasigi, Kyle Lo, Iz Beltagy, Arman Cohan,
Noah A Smith, and Matt Gardner. 2021. A dataset
of information-seeking questions and answers an-
chored in research papers. In Proceedings of the
2021 Conference of the North American Chapter of
the Association for Computational Linguistics: Hu-
man Language Technologies, pages 45994610.
Jiayu Ding, Shuming Ma, Li Dong, Xingxing Zhang,
Shaohan Huang, Wenhui Wang, and Furu Wei. 2023.
Longnet: Scaling transformers to 1,000,000,000 to-
kens. arXiv preprint arXiv:2307.02486.
Zican Dong, Tianyi Tang, Junyi Li, Wayne Xin Zhao,
and Ji-Rong Wen. 2024. Bamboo: A comprehensive
benchmark for evaluating long text modeling capac-
ities of large language models. In Proceedings of
the 2024 Joint International Conference on Compu-
tational Linguistics, Language Resources and Evalu-
ation (LREC-COLING 2024), pages 20862099.
Dheeru Dua, Yizhong Wang, Pradeep Dasigi, Gabriel
Stanovsky, Sameer Singh, and Matt Gardner. 2019.
Drop: A reading comprehension benchmark requir-
ing discrete reasoning over paragraphs. In Proceed-
ings of the 2019 Conference of the North American
Chapter of the Association for Computational Lin-
guistics: Human Language Technologies, Volume 1
(Long and Short Papers), pages 23682378.
Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey,
Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman,
Akhil Mathur, Alan Schelten, Amy Yang, Angela
Fan, et al. 2024. The llama 3 herd of models. arXiv
preprint arXiv:2407.21783.
Alexander Richard Fabbri, Irene Li, Tianwei She, Suyi
Li, and Dragomir Radev. 2019. Multi-news: A large-
scale multi-document summarization dataset and ab-
stractive hierarchical model. In Proceedings of the
57th Annual Meeting of the Association for Compu-
tational Linguistics, pages 10741084.
William Fedus, Barret Zoph, and Noam Shazeer. 2022.
Switch transformers: Scaling to trillion parame-
ter models with simple and efficient sparsity. The
Journal of Machine Learning Research, 23(1):5232
Yao Fu, Rameswar Panda, Xinyao Niu, Xiang Yue, Han-
naneh Hajishirzi, Yoon Kim, and Hao Peng. 2024.
Data engineering for scaling language models to
128K context. In Proceedings of the 41st Interna-
tional Conference on Machine Learning, volume 235
of Proceedings of Machine Learning Research, pages
1412514134. PMLR.
Samir Yitzhak Gadre, Gabriel Ilharco, Alex Fang,
Jonathan Hayase, Georgios Smyrnis, Thao Nguyen,
Ryan Marten, Mitchell Wortsman, Dhruba Ghosh,
Jieyu Zhang, et al. 2024. Datacomp: In search of the
next generation of multimodal datasets. Advances in
Neural Information Processing Systems, 36.
Tianyu Gao, Alexander Wettig, Howard Yen, and
Danqi Chen. 2024.
How to train long-context
language models (effectively).
arXiv preprint
arXiv:2410.02660.
Team GLM, Aohan Zeng, Bin Xu, and et al. 2024.
Chatglm:
A family of large language models
from glm-130b to glm-4 all tools. arXiv preprint
arXiv:2406.12793.
Taicheng Guo, Bozhao Nan, Zhenwen Liang, Zhichun
Guo, Nitesh Chawla, Olaf Wiest, Xiangliang Zhang,
et al. 2023. What can large language models do in
chemistry? a comprehensive benchmark on eight
tasks. Advances in Neural Information Processing
Systems, 36:5966259688.
Greg Hamerly and Charles Elkan. 2003. Learning the k
in k-means. Advances in neural information process-
ing systems, 16.
Wei He, Zhongzhan Huang, Mingfu Liang, Senwei
Liang, and Haizhao Yang. 2021. Blending pruning
criteria for convolutional neural networks. In Artifi-
cial Neural Networks and Machine LearningICANN
2021: 30th International Conference on Artificial
Neural Networks, Bratislava, Slovakia, September
1417, 2021, Proceedings, Part IV 30, pages 315.
Springer.
Xanh Ho, Anh-Khoa Duong Nguyen, Saku Sugawara,
and Akiko Aizawa. 2020. Constructing a multi-hop
qa dataset for comprehensive evaluation of reasoning
steps. In Proceedings of the 28th International Con-
ference on Computational Linguistics, pages 6609
Cheng-Ping Hsieh, Simeng Sun, Samuel Kriman, Shan-
tanu Acharya, Dima Rekesh, Fei Jia, Yang Zhang,
and Boris Ginsburg. 2024. Ruler: Whats the real
context size of your long-context language models?
arXiv preprint arXiv:2404.06654.
Luyang Huang, Shuyang Cao, Nikolaus Parulian, Heng
Ji, and Lu Wang. 2021a. Efficient attentions for long
document summarization. In Proceedings of the 2021
Conference of the North American Chapter of the
Association for Computational Linguistics: Human
Language Technologies, pages 14191436.

Zhongzhan Huang, Senwei Liang, Mingfu Liang, Wei
He, Haizhao Yang, and Liang Lin. 2022. The lottery
ticket hypothesis for self-attention in convolutional
neural network. arXiv preprint arXiv:2207.07858.
Zhongzhan Huang, Wenqi Shao, Xinjiang Wang, Liang
Lin, and Ping Luo. 2021b. Rethinking the pruning
criteria for convolutional neural network. Advances
in Neural Information Processing Systems, 34:16305
Greg Kamradt. 2023. Needle in a haystack - pressure
testing llms.
https://github.com/gkamradt/
LLMTest_NeedleInAHaystack.
Bo-Kyeong Kim, Geonmin Kim, Tae-Ho Kim, Thibault
Castells, Shinkook Choi, Junho Shin, and Hyoung-
Kyu Song. 2024. Shortened llama: A simple depth
pruning for large language models. arXiv preprint
arXiv:2402.02834, 11.
Alex Kipnis, Konstantinos Voudouris, Luca M Schulze
Buschoff, and Eric Schulz. 2024.
metabencha
sparse benchmark to measure general ability in large
language models. arXiv preprint arXiv:2407.12844.
Nikita Kitaev, Lukasz Kaiser, and Anselm Levskaya.
2020. Reformer: The efficient transformer. In Inter-
national Conference on Learning Representations.
David G Kleinbaum, K Dietz, M Gail, Mitchel Klein,
and Mitchell Klein. 2002.
Logistic regression.
Springer.
Satyapriya Krishna, Kalpesh Krishna, Anhad Mo-
hananey, Steven Schwarcz, Adam Stambler, Shyam
Upadhyay, and Manaal Faruqui. 2024.
Fact,
fetch,
and reason:
A unified evaluation of
retrieval-augmented generation.
arXiv preprint
arXiv:2409.12941.
Yuri Kuratov, Aydar Bulatov, Petr Anokhin, Ivan Rod-
kin, Dmitry Sorokin, Artyom Sorokin, and Mikhail
Burtsev. 2024. Babilong: Testing the limits of llms
with long context reasoning-in-a-haystack. arXiv
preprint arXiv:2406.10149.
Philippe Laban, Alexander Richard Fabbri, Caiming
Xiong, and Chien-Sheng Wu. 2024. Summary of a
haystack: A challenge to long-context llms and rag
systems. In Proceedings of the 2024 Conference on
Empirical Methods in Natural Language Processing,
pages 98859903.
Shiye Lei and Dacheng Tao. 2023. A comprehensive
survey of dataset distillation. IEEE Transactions on
Pattern Analysis and Machine Intelligence.
Bohao Li, Yuying Ge, Yixiao Ge, Guangzhi Wang, Rui
Wang, Ruimao Zhang, and Ying Shan. 2024. Seed-
bench: Benchmarking multimodal large language
models. In Proceedings of the IEEE/CVF Conference
on Computer Vision and Pattern Recognition, pages
Dacheng Li, Rulin Shao, Anze Xie, Ying Sheng, Lian-
min Zheng, Joseph E. Gonzalez, Ion Stoica, Xuezhe
Ma, and Hao Zhang. 2023a. How long can open-
source llms truly promise on context length?
Jiaqi Li, Mengmeng Wang, Zilong Zheng, and Muhan
Zhang. 2023b. Loogle: Can long-context language
models understand long contexts?
arXiv preprint
arXiv:2311.04939.
Xin Li and Dan Roth. 2002. Learning question clas-
sifiers. In COLING 2002: The 19th International
Conference on Computational Linguistics.
Senwei Liang, Zhongzhan Huang, Mingfu Liang, and
Haizhao Yang. 2020. Instance enhancement batch
normalization: An adaptive regulator of batch noise.
In Proceedings of the AAAI conference on artificial
intelligence, volume 34, pages 48194827.
Xinnian Liang, Bing Wang, Hui Huang, Shuangzhi Wu,
Peihao Wu, Lu Lu, Zejun Ma, and Zhoujun Li. 2023.
Unleashing infinite-length input capacity for large-
scale language models with self-controlled memory
system. arXiv preprint arXiv:2304.13343.
Haokun Lin, Haoli Bai, Zhili Liu, Lu Hou, Muyi Sun,
Linqi Song, Ying Wei, and Zhenan Sun. 2024. Mope-
clip: Structured pruning for efficient vision-language
models with module-wise pruning error metric. In
Proceedings of the IEEE/CVF Conference on Com-
puter Vision and Pattern Recognition, pages 27370
Tianyang Liu, Canwen Xu, and Julian McAuley.
2023. Repobench: Benchmarking repository-level
code auto-completion systems.
arXiv preprint
arXiv:2306.03091.
Xiang Liu, Peijie Dong, Xuming Hu, and Xiaowen
Chu. 2024.
Longgenbench: Long-context gener-
ation benchmark. In Findings of the Association
for Computational Linguistics: EMNLP 2024, pages
Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Man-
dar Joshi, Danqi Chen, Omer Levy, Mike Lewis,
Luke Zettlemoyer, and Veselin Stoyanov. 2019.
Roberta: A robustly optimized bert pretraining ap-
proach. ArXiv.
Pedro Henrique Martins, Zita Marinho, and André FT
Martins. 2022. -former: Infinite memory trans-
former. In Proceedings of the 60th Annual Meeting
of the Association for Computational Linguistics (Vol-
ume 1: Long Papers), pages 54685485.
Saurav Muralidharan, Sharath Turuvekere Sreenivas,
Raviraj Bhuminand Joshi, Marcin Chochowski,
Mostofa Patwary, Mohammad Shoeybi, Bryan Catan-
zaro, Jan Kautz, and Pavlo Molchanov. 2024. Com-
pact language models via pruning and knowledge
distillation. In The Thirty-eighth Annual Conference
on Neural Information Processing Systems.
OpenAI. 2024. Openai: Hello gpt-4o.

Antonio Orvieto, Samuel L Smith, Albert Gu, Anushan
Fernando, Caglar Gulcehre, Razvan Pascanu, and
Soham De. 2023.
Resurrecting recurrent neu-
ral networks for long sequences.
arXiv preprint
arXiv:2303.06349.
Lorenzo Pacchiardi,
Lucy G Cheke,
and José
Hernández-Orallo. 2024. 100 instances is all you
need: predicting the success of a new llm on unseen
data by testing on a few instances. arXiv preprint
arXiv:2409.03563.
Richard Yuanzhe Pang, Alicia Parrish, Nitish Joshi,
Nikita Nangia, Jason Phang, Angelica Chen, Vishakh
Padmakumar, Johnny Ma, Jana Thompson, He He,
et al. 2022. Quality: Question answering with long
input texts, yes! In Proceedings of the 2022 Con-
ference of the North American Chapter of the Asso-
ciation for Computational Linguistics: Human Lan-
guage Technologies.
Felipe Maia Polo, Lucas Weber, Leshem Choshen,
Yuekai Sun, Gongjun Xu, and Mikhail Yurochkin.
2024. tinybenchmarks: evaluating llms with fewer
examples. In Forty-first International Conference on
Machine Learning.
Ofir Press, Noah Smith, and Mike Lewis. 2022. Train
short, test long: Attention with linear biases enables
input length extrapolation. In International Confer-
ence on Learning Representations.
Haoran Que, Feiyu Duan, Liqun He, Yutao Mou,
Wangchunshu Zhou, Jiaheng Liu, Wenge Rong,
Zekun Moore Wang, Jian Yang, Ge Zhang, et al.
2024. Hellobench: Evaluating long text generation
capabilities of large language models. arXiv preprint
arXiv:2409.16191.
Jack W Rae, Anna Potapenko, Siddhant M Jayakumar,
Chloe Hillier, and Timothy P Lillicrap. 2020. Com-
pressive transformers for long-range sequence mod-
elling. In International Conference on Learning Rep-
resentations.
Machel Reid, Nikolay Savinov, Denis Teplyashin,
Dmitry Lepikhin, Timothy Lillicrap, Jean-baptiste
Alayrac, Radu Soricut, Angeliki Lazaridou, Orhan Fi-
rat, Julian Schrittwieser, et al. 2024. Gemini 1.5: Un-
locking multimodal understanding across millions of
tokens of context. arXiv preprint arXiv:2403.05530.
Aurko Roy, Mohammad Saffar, Ashish Vaswani, and
David Grangier. 2021. Efficient content-based sparse
attention with routing transformers. Transactions of
the Association for Computational Linguistics, 9:53
Noveen Sachdeva and Julian McAuley. 2023. Data dis-
tillation: A survey. arXiv preprint arXiv:2301.04272.
Uri Shaham, Maor Ivgi, Avia Efrat, Jonathan Be-
rant, and Omer Levy. 2023. Zeroscrolls: A zero-
shot benchmark for long text understanding. arXiv
preprint arXiv:2305.14196.
Uri Shaham, Elad Segal, Maor Ivgi, Avia Efrat, Ori
Yoran, Adi Haviv, Ankit Gupta, Wenhan Xiong, Mor
Geva, Jonathan Berant, et al. 2022. Scrolls: Stan-
dardized comparison over long language sequences.
In Proceedings of the 2022 Conference on Empiri-
cal Methods in Natural Language Processing, pages
Mingyang Song, Mao Zheng, and Xuan Luo. 2024.
Counting-stars: A simple, efficient, and reasonable
strategy for evaluating long-context large language
models. arXiv preprint arXiv:2403.11802.
Charles Spearman. 1961. The proof and measurement
of association between two things.
Yutao Sun, Li Dong, Barun Patra, Shuming Ma, Shao-
han Huang, Alon Benhaim, Vishrav Chaudhary, Xia
Song, and Furu Wei. 2022. A length-extrapolatable
transformer. arXiv preprint arXiv:2212.10554.
Yi Tay, Mostafa Dehghani, Dara Bahri, and Donald Met-
zler. 2022. Efficient transformers: A survey. ACM
Comput. Surv., 55(6).
Hugo Touvron, Matthieu Cord, Matthijs Douze, Fran-
cisco Massa, Alexandre Sablayrolles, and Hervé Jé-
gou. 2021. Training data-efficient image transform-
ers and distillation through attention. In International
conference on machine learning, pages 1034710357.
PMLR.
Harsh Trivedi, Niranjan Balasubramanian, Tushar Khot,
and Ashish Sabharwal. 2022.
Musique: Multi-
hop questions via single-hop question composition.
Transactions of the Association for Computational
Linguistics, 10:539554.
Laurens Van der Maaten and Geoffrey Hinton. 2008.
Visualizing data using t-sne. Journal of machine
learning research, 9(11).
Kiran Vodrahalli, Santiago Ontanon, Nilesh Tripuraneni,
Kelvin Xu, Sanil Jain, Rakesh Shivanna, Jeffrey Hui,
Nishanth Dikkala, Mehran Kazemi, Bahare Fatemi,
et al. 2024. Michelangelo: Long context evaluations
beyond haystacks via latent structure queries. arXiv
preprint arXiv:2409.12640.
Alex Wang, Richard Yuanzhe Pang, Angelica Chen,
Jason Phang, and Samuel Bowman. 2022. Squality:
Building a long-document summarization dataset the
hard way. In Proceedings of the 2022 Conference on
Empirical Methods in Natural Language Processing,
pages 11391156.
Minzheng Wang, Longze Chen, Fu Cheng, Shengyi
Liao, Xinghua Zhang, Bingli Wu, Haiyang Yu, Nan
Xu, Lei Zhang, Run Luo, et al. 2024. Leave no
document behind: Benchmarking long-context llms
with extended multi-doc qa. In Proceedings of the
2024 Conference on Empirical Methods in Natural
Language Processing, pages 56275646.
Sinong Wang, Belinda Z Li, Madian Khabsa, Han Fang,
and Hao Ma. 2020. Linformer: Self-attention with
linear complexity. arXiv preprint arXiv:2006.04768.

Yuhao Wu, Ming Shan Hee, Zhiqing Hu, and Roy Ka-
Wei Lee. 2024. Longgenbench: Benchmarking long-
form generation in long context llms. arXiv preprint
arXiv:2409.02076.
Yuhuai Wu, Markus Norman Rabe, DeLesley Hutchins,
and Christian Szegedy. 2022. Memorizing transform-
ers. In International Conference on Learning Repre-
sentations.
Jasper Xian, Tommaso Teofili, Ronak Pradeep, and
Jimmy Lin. 2024. Vector search with openai em-
beddings: Lucene is all you need. In Proceedings
of the 17th ACM International Conference on Web
Search and Data Mining, pages 10901093.
Wenhan Xiong, Jingyu Liu, Igor Molybog, Hejia Zhang,
Prajjwal Bhargava, Rui Hou, Louis Martin, Rashi
Rungta, Karthik Abinav Sankararaman, Barlas Oguz,
et al. 2024. Effective long-context scaling of founda-
tion models. In Proceedings of the 2024 Conference
of the North American Chapter of the Association for
Computational Linguistics: Human Language Tech-
nologies (Volume 1: Long Papers), pages 46434663.
Yifei Yang, Zouying Cao, and Hai Zhao. 2024. Laco:
Large language model pruning via layer collapse.
arXiv preprint arXiv:2402.11187.
Zhilin Yang, Peng Qi, Saizheng Zhang, Yoshua Bengio,
William Cohen, Ruslan Salakhutdinov, and Christo-
pher D Manning. 2018. Hotpotqa: A dataset for
diverse, explainable multi-hop question answering.
In Proceedings of the 2018 Conference on Empiri-
cal Methods in Natural Language Processing, pages
Howard Yen, Tianyu Gao, Minmin Hou, Ke Ding,
Daniel Fleischer, Peter Izsak, Moshe Wasserblat, and
Danqi Chen. 2024. Helmet: How to evaluate long-
context language models effectively and thoroughly.
arXiv preprint arXiv:2410.02694.
Ruonan Yu, Songhua Liu, and Xinchao Wang. 2023.
Dataset distillation: A comprehensive review. IEEE
Transactions on Pattern Analysis and Machine Intel-
ligence.
Manzil Zaheer, Guru Guruganesh, Kumar Avinava
Dubey, Joshua Ainslie, Chris Alberti, Santiago On-
tanon, Philip Pham, Anirudh Ravula, Qifan Wang,
Li Yang, et al. 2020. Big bird: Transformers for
longer sequences. Advances in neural information
processing systems, 33:1728317297.
Aohan Zeng, Xiao Liu, Zhengxiao Du, Zihan Wang,
Hanyu Lai, Ming Ding, Zhuoyi Yang, Yifan Xu,
Wendi Zheng, Xiao Xia, et al. 2023. Glm-130b: An
open bilingual pre-trained model. In The Eleventh In-
ternational Conference on Learning Representations.
Jiajie Zhang, Yushi Bai, Xin Lv, Wanjun Gu, Danqing
Liu, Minhao Zou, Shulin Cao, Lei Hou, Yuxiao Dong,
Ling Feng, et al. 2024a. Longcite: Enabling llms
to generate fine-grained citations in long-context qa.
arXiv preprint arXiv:2409.02897.
Xinrong Zhang, Yingfa Chen, Shengding Hu, Zihang
Xu, Junhao Chen, Moo Hao, Xu Han, Zhen Thai,
Shuo Wang, Zhiyuan Liu, and Maosong Sun. 2024b.
Bench: Extending long context evaluation beyond
100K tokens. In Proceedings of the 62nd Annual
Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), pages 15262
15277, Bangkok, Thailand. Association for Compu-
tational Linguistics.
Ming Zhong, Da Yin, Tao Yu, Ahmad Zaidi, Mutethia
Mutuma, Rahul Jha, Ahmed Hassan, Asli Celikyil-
maz, Yang Liu, Xipeng Qiu, et al. 2021. Qmsum: A
new benchmark for query-based multi-domain meet-
ing summarization. In Proceedings of the 2021 Con-
ference of the North American Chapter of the Asso-
ciation for Computational Linguistics: Human Lan-
guage Technologies, pages 59055921.
Shanshan Zhong, Shanghua Gao, Zhongzhan Huang,
Wushao Wen, Marinka Žitnik, and Pan Zhou. 2024a.
Moextend: Tuning new experts for modality and task
extension. In Proceedings of the 62nd Annual Meet-
ing of the Association for Computational Linguistics,
pages 8091.
Shanshan Zhong, Zhongzhan Huang, Shanghua Gao,
Wushao Wen, Liang Lin, Marinka Zitnik, and Pan
Zhou. 2024b. Lets think outside the box: Explor-
ing leap-of-thought in large language models with
creative humor generation. In Proceedings of the
IEEE/CVF Conference on Computer Vision and Pat-
tern Recognition, pages 1324613257.
Shanshan Zhong, Zhongzhan Huang, Weushao Wen,
Jinghui Qin, and Liang Lin. 2023a. Sur-adapter: En-
hancing text-to-image pre-trained diffusion models
with large language models. In Proceedings of the
31st ACM International Conference on Multimedia,
pages 567578.
Shanshan Zhong, Jinghui Qin, Zhongzhan Huang, and
Daifeng Li. 2022. Cem: Machine-human chatting
handoff via causal-enhance module. In Proceedings
of the 2022 Conference on Empirical Methods in
Natural Language Processing, pages 32423253.
Shanshan Zhong, Wushao Wen, Jinghui Qin, Qiangpu
Chen, and Zhongzhan Huang. 2023b.
Lsas:
Lightweight sub-attention strategy for alleviating at-
tention bias problem. In 2023 IEEE International
Conference on Multimedia and Expo (ICME), pages
20512056. IEEE.
Wangchunshu Zhou, Yuchen Eleanor Jiang, Peng Cui,
Tiannan Wang, Zhenxin Xiao, Yifan Hou, Ryan Cot-
terell, and Mrinmaya Sachan. 2023. Recurrentgpt:
Interactive generation of (arbitrarily) long text. arXiv
preprint arXiv:2305.13304.
Chen Zhu, Wei Ping, Chaowei Xiao, Mohammad
Shoeybi, Tom Goldstein, Anima Anandkumar, and
Bryan Catanzaro. 2021. Long-short transformer: Ef-
ficient transformers for language and vision. Ad-
vances in neural information processing systems,

The Details of LongBench
LongBench (Bai et al., 2024a) represents the first
bilingual, multi-task benchmark specifically devel-
oped for assessing long-context comprehension.
The benchmark encompasses six primary task cate-
gories and 21 distinct tasks, spanning crucial long-
text application domains (Dasigi et al., 2021; Yang
et al., 2018; Ho et al., 2020; Trivedi et al., 2022;
Huang et al., 2021a; Zhong et al., 2021; Fabbri
et al., 2019; Ainslie et al., 2023; Li and Roth, 2002)
including multi-document QA, single-document
QA, summarization, few-shot learning, code com-
pletion, and synthetic tasks, as detailed in Table 1.
To thoroughly evaluate large models bilingual
proficiency in long-context processing, LongBench
incorporates tasks in both Chinese and English.
The dataset comprises 4,750 test instances, with
average lengths of 6,711 words and 13,386 charac-
ters for English and Chinese respectively, ensuring
extensive coverage of diverse scenarios. The chal-
lenge of long-context understanding (Press et al.,
2022; Sun et al., 2022; Chen et al., 2023; Zhong
et al., 2024a, 2022) can be formally defined as
follows: given an input sequence I and a context
sequence C, the model is tasked with generating an
output A. For example, in a QA task, I represents
the question, C corresponds to the document, and
A is the answer. Across LongBench, I and A are
typically short, whereas C can span thousands of
tokens. Specific instantiations of (I, C, A) for each
task are provided in Table 7 of (Bai et al., 2024a).
The LLMs Considered in
In this section, we list all LLMs we considered
in Table 3. Among them, 20 LLMs were utilized
for training to aid in obtaining effective represen-
tations of test samples in the LCU benchmark. In
this study, we have carefully curated a selection of
LLMs that demonstrate consistently strong perfor-
mance across multiple dimensions to contribute to
the development of MiniLongBench. These mod-
els were chosen based on their proven capabili-
ties in various tasks and benchmarks. However, to
enhance the scalability and objectivity of our ap-
proach, future work should focus on implementing
an automated LLM selection mechanism. This ad-
vancement would not only streamline the selection
process but also ensure a more systematic and un-
biased evaluation of potential models for inclusion
in MiniLongBench.
Model
Type
Model
Type
ALMA-7B-Ja-V2
Amd-llama-135m
GOAT-7B-Community
Amd-llama-135m-code
Koss-7B-chat
Distilled-HermesChat-7B
Kunoichi-7B
Loyal-Macaroni-Maid-7B
Llama-2-7b-ft-instruct-es
Llama-3-8b-hf
Llama-2-7b-hf
Llama-7b-SFT_ds_wiki65k
Llama-7b-hf
Llama-shishya-7b-ep3-v1
Mistral-7B-Instruct-v0.2
Llama-30b
OLMo-1B
OLMo-1B-SFT
Airoboros-7b
StopCarbon-10.7B-v6
Gemma2-9b-hf
Synatra-RP-Orca-2-7b-v0.1
Giraffe-7b
TowerInstruct-7B-v0.1
Mistral-7b-v0.1-hf
Gemma2-2b-hf
Perry-7b
Manatee-7b
Qwen-7b-hf
Mistral-7b-v0.3-hf
Qwen1.5-0.5b-hf
Qwen1.5-1.8b-hf
Qwen2-0.5b-hf
Qwen2.5-0.5b-instruct-hf
Qwen2.5-0.5b-base
Qwen2.5-3b-base
Qwen2.5-1.5b-base
Qwen2.5-3b-instruct-hf
Tulu-7B-fp16
Recycled-wizardlm-7b-v2.0
OPT-30B
Wizaed-Vicuna
Llama-30B
LwQ-Instruct
30B-Epsilon
DeepSeek V3
GPT o1 mini
GPT-3.5-turbo
ChatGLM-6B
ChatGLM3-6B
ChatGLM3-9B
Qwen-7B
Qwen2-7B
Qwen2.5-7B
Qwen2.5-14B
Qwen2.5-32B
Gemma2-9B
Llama-7B-2k
Llama2-7B-4k
Llama3-8B
Table 3: The LLMs considered in MiniLongBench. "T"
and "A" denote "for tranining" and "for analysis".
The Details Results of Advanced LLMs
In Section 4.3, we present the direct performance


## Results

tasks of MiniLongBench. Note that MiniLong-
Bench includes not only the six main tasks but also
21 subtasks. Therefore, in this section, we will dis-
play the detailed results. The results are shown in
Table 4 and Table 5, where the indices in the table
correspond to those in Table 2 in the main text.
In addition to the performance estimation of the
target LLM on the entire LongBench using Mini-
LongBenchs test samples, as demonstrated in Sec-
tion 4.3, we further propose a more straightforward
but slightly less effective method for evaluating
LCU capabilities in Appendix G. Specifically, the
target LLM is directly tested on MiniLongBenchs
test samples without requiring any additional steps.
Related Works
D.1
Long Context Understanding (LCU)
Existing research on LCU in LLMs primarily ad-
dresses two critical challenges in long-text model-
ing: the substantial runtime overhead associated
with extended contexts and the issue of catastrophic
forgetting during long sequence processing.
A significant body of work has concentrated on

Model
Single-Doc QA
Multi-Doc QA
Summarization
Avg
Avg
Avg
DeepSeek-V3-128k
GPT-4o-mini-128k
GPT-3.5-Turbo-16k
Internlm3-8B-32k
ChatGLM3-6B-8k
ChatGLM4-9B-128k
Qwen-7B-8k
Qwen2-7B-128k
Qwen2.5-7B-128k
Qwen2.5-14B-128k
Qwen2.5-32B-128k
Llama-7B-2k
Llama2-7B-4k
Llama3-8B-8k
Llama-30B-2k
OPT-30B-2k
Wizard-Vicuna-2k
LwQ-Instruct-2k
30B-Epsilon-2k
Table 4: Results on single-doc QA, multi-doc QA and summarization tasks. The indexes, like "1-1" or "4-1", are
following Table 1. "avg" represents the average performance of subtasks under different main tasks.
Figure 11: The visualization of learned representation (ej, j) of test sample.
enhancing the efficiency and memory retention of
Transformers (Tay et al., 2022). This includes inno-
vations in sparse and efficient computation (Child
et al., 2019; Kitaev et al., 2020; Beltagy et al., 2020;
Zaheer et al., 2020; Wang et al., 2020; Fedus et al.,
2022; Ding et al., 2023), as well as the integration
of recurrent and memory modules (Dai et al., 2019;
Rae et al., 2020; Wu et al., 2022; Martins et al.,
2022; Bulatov et al., 2022; Orvieto et al., 2023;
Liang et al., 2023; Zhou et al., 2023).
More recently, several advanced methods (Press
et al., 2022; Sun et al., 2022; Chen et al., 2023)
have been developed to facilitate length extrapola-
tion in Transformers. These techniques have been
incorporated into the training frameworks of long-
context LLMs such as ChatGLM2-32k (Zeng et al.,
2023) and LongChat-32k (Li et al., 2023a), among
others. These models have successfully extended
their context lengths to 128k tokens or more (An-
thropic, 2024; OpenAI, 2024; Reid et al., 2024;
GLM et al., 2024; Dubey et al., 2024; Xiong et al.,
2024; Fu et al., 2024; Bai et al., 2024b; Gao et al.,
2024), marking a significant advancement in the
field.
D.2
The LCU Benchmarks for LLMs
Given the critical importance of LCU capabilities
for LLMs, an increasing number of benchmarks
have been proposed to evaluate these capabilities,
playing a pivotal role in exploring and advanc-
ing LLMs LCU proficiency. A significant por-
tion of these benchmarks of LLMs focuses on
comprehensive LCU assessment, encompassing
tasks such as Question Answering, information
retrieval, and summarization. Notable examples
include L-Eval (An et al., 2024), LongBench (Bai
et al., 2024c), ZeroSCROLLS (Shaham et al.,
2023), BAMBOO (Dong et al., 2024), LooGLE (Li

Model
Few-show Learning
Synthetic
Code
Overall
Avg
Avg
Avg
All
DeepSeek-V3-128k
GPT-4o-mini-128k
GPT-3.5-Turbo-16k
Internlm3-8B-32k
ChatGLM3-6B-8k
ChatGLM4-9B-128k
Qwen-7B-8k
Qwen2-7B-128k
Qwen2.5-7B-128k
Qwen2.5-14B-128k
Qwen2.5-32B-128k
Llama-7B-2k
Llama2-7B-4k
Llama3-8B-8k
Llama-30B-2k
OPT-30B-2k
Wizard-Vicuna-2k
LwQ-Instruct-2k
30B-Epsilon-2k
Table 5: Results on few-shot learning, synthetic, and code tasks. Overall is computed by the macro-average (the
mean of Avg) over major task categories. This is computed on English (EN) tasks, Chinese (ZH) tasks, and all
(All) tasks, code tasks are included in both languages. The indexes, like "1-1" or "4-1", are following Table 1. "avg"
represents the average performance of subtasks under different main tasks.
et al., 2023b), -bench (Zhang et al., 2024b),
Ruler (Hsieh et al., 2024), and HELMET (Yen et al.,
2024). Another category of benchmarks is specifi-
cally designed to explore particular aspects of LCU
capabilities. These include retrieval and attribution
tasks (Kamradt, 2023; Kuratov et al., 2024; Song
et al., 2024; Laban et al., 2024; Zhang et al., 2024a;
Vodrahalli et al., 2024; Krishna et al., 2024), doc-
ument QA (Dua et al., 2019; Dasigi et al., 2021;
Pang et al., 2022; Wang et al., 2024), summariza-
tion (Zhong et al., 2021; Huang et al., 2021a; Wang
et al., 2022), coding (Liu et al., 2023; Bogomolov
et al., 2024), many-shot learning (Agarwal et al.,
2024), and long-text generation (Bai et al., 2024e;
Wu et al., 2024; Liu et al., 2024; Que et al., 2024).
These specialized benchmarks provide targeted
insights into the diverse and complex facets of
LCU, contributing to a more nuanced understand-
ing and development of LLMs long-context pro-
cessing abilities.
D.3
Low-cost Deep Learning
Recently, there has been a surge of efforts aimed
at achieving low-cost deep learning, encompass-
ing strategies such as the compression of model
parameters or the design of lightweight archi-
tectures (Yang et al., 2024; Muralidharan et al.,
2024; Lin et al., 2024; Kim et al., 2024; Zhong
et al., 2023b; He et al., 2021; Huang et al., 2022,
2021b; Liang et al., 2020). Concurrently, some
research has explored compressing the training
dataset (Gadre et al., 2024; Sachdeva and McAuley,
2023; Yu et al., 2023; Lei and Tao, 2023; Tou-
vron et al., 2021) to reduce computational costs
while maintaining performance.
Beyond these
approaches, in the era of large language models,
works including this paper consider compressing
test data (Polo et al., 2024; Pacchiardi et al., 2024;
Kipnis et al., 2024) as an effective means to aid in
model architecture design, parameter tuning, and
other training-related processes, thereby accelerat-
ing the iteration speed of robust models.
The Visualization of Learned
Representation of Test Samples
In Section 3, we use the performance record of m
LLMs on various test samples in LongBench, and
use a logistic regression model for representation
learning, obtaining their representations (ej, j).
In Fig. 11, we visualize test samples from certain
sub-tasks listed in Table 1 using t-SNE (Van der
Maaten and Hinton, 2008). It can be observed that
many test samples form clusters, and the repre-
sentations of samples within the same cluster are
highly similar. This further demonstrates that Long-
Bench contains a significant amount of redundancy
in its data, and the representation learning method
proposed in Section 3 is effective for identifying

(a)
LongBench
Rank
Rank
Rank
Rank
LLM Index
LLM Index
LLM Index
LLM Index
LLM Index
LLM Index
LLM Index
LLM Index
LLM Index
LLM Index
LLM Index
LLM Index
LLM Index
LLM Index
LLM Index
LLM Index
(b)
(c)
(d)
(e)
(f)
(g)
(h)
(i)
(j)
(k)
(l)
(m)
(n)
(o)
(p)
Figure 12: The more examples of visualization of ranking by MiniLongBench and LongBench..
redundant data in LongBench through clustering.
More Visualizations of Ranking
In the Fig. 10, we provided some examples of rank-
ings by MiniLongBench and LongBench. In this
section, we will present more random examples
to illustrate the usability and reliability of Mini-
LongBench. The results are shown in Fig. 12. As
illustrated in Fig. 12, similar to the observations
in the main texts Fig. 10, the results from 16 ran-
dom sampling trials consistently demonstrate that
the ranking outcomes of various LLMs on Mini-
LongBench closely align with those on LongBench.
Although minor discrepancies exist, they are within
an acceptable range, particularly considering that
the Spearman correlation coefficient (Sp) does not
reach a perfect 1.0. These visualizations further
validate that MiniLongBench achieves evaluation
results comparable to LongBench while signifi-
cantly reducing computational costs. This high-
lights MiniLongBenchs effectiveness as a low-cost
alternative for assessing LLM performance.
Evaluating Directly by MiniLongBench
In Section 4.2 of the main text, we primarily intro-
duce a method that utilizes test samples from Mini-
LongBench to assist in evaluating the performance
of a target LLM on LongBench.
This method
Model
SQA
MQA
SUM
FSL
SYN
CODE
DeepSeek-V3-128k
GPT-4o-mini-128k
GPT-3.5-Turbo-16k
Internlm3-8B-32k
ChatGLM3-6B-8k
ChatGLM4-9B-128k
Qwen-7B-8k
Qwen2-7B-128k
Qwen2.5-7B-128k
Qwen2.5-14B-128k
Qwen2.5-32B-128k
Llama-7B-2k
Llama2-7B-4k
Llama3-8B-8k
Llama-30B-2k
OPT-30B-2k
Wizard-Vicuna-2k
LwQ-Instruct-2k
30B-Epsilon-2k
Table 6: Specific evaluation results on evaluating di-
rectly by MiniLongBench. Due to differences in evalu-
ation methods, the score values presented in this table
vary somewhat from those in Table 2, but they yield a
similar ranking of LLMs in terms of LCU capability.
achieves a performance of up to 0.97 in Sp. In prac-
tice, we can also directly test the target LLM on
MiniLongBenchs test samples to obtain an assess-
ment of its LCU capability. The results in Fig. 13
confirm that this evaluation method achieves good
Sp across various tasks in MiniLongBench, with an
average Sp of 0.95, slightly lower than the evalua-
tion method presented in Section 4.2. Furthermore,
in Table 6, we present the results of this evaluation

Single-Document QA
Multi-Document QA
Summarization
Few-shot Learning
Code Completion
Synthetic Task
MiniLongbench Scores
Longbench Scores
Train (Sp=0.9188)
Test (Sp=0.9805)
Train (Sp=0.9504)
Test (Sp=0.9474)
Train (Sp=0.8812)
Test (Sp=0.9515)
Train (Sp=0.8992)
Test (Sp=0.9549)
Train (Sp=0.9293)
Test (Sp=0.9549)
Train (Sp=0.8673)
Test (Sp=0.8469)
MiniLongbench Scores
MiniLongbench Scores
Longbench Scores
MiniLongbench Scores
MiniLongbench Scores
MiniLongbench Scores
ALL (Sp=0.9563)
ALL (Sp=0.9674)
ALL (Sp=0.9347)
ALL (Sp=0.9360)
ALL (Sp=0.9565)
ALL (Sp=0.8730)
Figure 13: The analysis of rank correlation (Sp) between LongBench and MiniLongBench where the result of
MiniLongBench is evaluating directly.


## Method

provide more detailed results for each subtask in
Table 7 and Table 8.
It is noteworthy that, in practice, whether directly
evaluating on LongBench or MiniLongBench, or
using the predictive method in Section 4.2, there
may be some discrepancies in the score values.
However, these discrepancies do not affect the
ranking of LLMs LCU capabilities. For instance,
Fig. 13 and the main texts Fig. 5 demonstrate that
the results from different evaluation methods are
highly consistent, despite minor deviations in score
values. This phenomenon primarily arises from
several factors: first, MiniLongBench involves sig-
nificant pruning of test samples compared to Long-
Bench, leading to unavoidable errors; second, dur-
ing the logistic regression in Section 3s Eq. (2),
normalization and discretization introduce certain
errors, particularly in scaling. Fortunately, the pri-
mary goal of the LCU benchmark is to rank LLMs
based on their LCU capabilities, so the absolute
score values do not impact the final outcomes.
The Cost by Fine-tuning ¯θ
In Section 4.2, additional fine-tuning of ¯θ is re-
quired, which primarily involves two costs: the
training cost for fine-tuning and the storage cost
for the representation vectors of LongBenchs test
samples. In practice, these costs are minimal and
entirely acceptable. Specifically, storing the test
samples of MiniLongBench and the representation
vectors of LongBenchs test samples requires only
9.01MB and 1.13MB of disk space, respectively.
This is significantly lower and entirely acceptable
compared to the original storage cost of nearly
200MB for LongBenchs test samples. This re-
duction is largely due to the two-step dimension-
ality compression method described in Section 3,
which uses text embedding and PCA to compress
each feature vector to a dimension of just d = 10,
thereby greatly reducing storage costs.
On the other hand, the cost of fine-tuning ¯θ is
also very low and can even be performed on a
standard laptop without the need for server-grade
GPUs. This is because MiniLongBench contains
only about 200 test samples, and the dimensions
of all representation vectors are all d = 10, so
the logistic regression training does not require
significant computational power. Through 100 re-
peated experiments, the average time required for
fine-tuning ¯θ was calculated. on a server (CPU:
AMD EPYC 7K62, GPU: RTX 3090 24GB) and
a laptop (CPU: AMD Ryzen 6 5600H, GPU: RTX
3050 4GB), fine-tuning takes approximately 0.02
seconds and 0.03 seconds, respectively. Compared
to the original testing time of LongBench shown in
Fig. 1, this is almost negligible.

Model
Single-Doc QA
Multi-Doc QA
Summarization
Avg
Avg
Avg
DeepSeek-V3-128k
GPT-4o-mini-128k
GPT-3.5-Turbo-16k
Internlm3-8B-32k
ChatGLM3-6B-8k
ChatGLM4-9B-128k
Qwen-7B-8k
Qwen2-7B-128k
Qwen2.5-7B-128k
Qwen2.5-14B-128k
Qwen2.5-32B-128k
Llama-7B-2k
Llama2-7B-4k
Llama3-8B-8k
Llama-30B-2k
OPT-30B-2k
Wizard-Vicuna-2k
LwQ-Instruct-2k
30B-Epsilon-2k
Table 7: Results on single-doc QA, multi-doc QA and summarization tasks based on evaluating directly by
MiniLongBench. The indexes, like "1-1" or "4-1", are following Table 1. "avg" represents the average performance
of subtasks under different main tasks.
Model
Few-show Learning
Synthetic
Code
Overall
Avg
Avg
Avg
All
DeepSeek-V3-128k
GPT-4o-mini-128k
GPT-3.5-Turbo-16k
Internlm3-8B-32k
ChatGLM3-6B-8k
ChatGLM4-9B-128k
Qwen-7B-8k
Qwen2-7B-128k
Qwen2.5-7B-128k
Qwen2.5-14B-128k
Qwen2.5-32B-128k
Llama-7B-2k
Llama2-7B-4k
Llama3-8B-8k
Llama-30B-2k
OPT-30B-2k
Wizard-Vicuna-2k
LwQ-Instruct-2k
30B-Epsilon-2k
Table 8: Results on few-shot learning, synthetic, and code tasks based on evaluating directly by MiniLongBench.
Overall is computed by the macro-average (the mean of Avg) over major task categories. This is computed on
English (EN) tasks, Chinese (ZH) tasks, and all (All) tasks, code tasks are included in both languages. The indexes,
like "1-1" or "4-1", are following Table 1. "avg" represents the average performance of subtasks under different
main tasks.

