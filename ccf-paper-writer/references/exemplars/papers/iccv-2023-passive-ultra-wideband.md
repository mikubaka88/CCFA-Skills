# Passive Ultra-Wideband Single-Photon Imaging

> **Venue:** ICCV2023
> **Source:** <https://openaccess.thecvf.com/content/ICCV2023/html/Wei_Passive_Ultra-Wideband_Single-Photon_Imaging_ICCV_2023_paper.html>

---

Mian Wei1*
Sotiris Nousias1*
Rahul Gulve2
David B. Lindell1
Kiriakos N. Kutulakos1
1Dept. of Computer Science, University of Toronto
2Dept. of Electrical and Computer Engineering, University of Toronto

## Abstract

We consider the problem of imaging a dynamic scene over
an extreme range of timescales simultaneously—seconds to
picoseconds—and doing so passively, without much light,
and without any timing signals from the light source(s)
emitting it. Because existing ﬂux estimation techniques for
single-photon cameras break down in this regime, we de-
velop a ﬂux probing theory that draws insights from stochas-
tic calculus to enable reconstruction of a pixel’s time-
varying ﬂux from a stream of monotonically-increasing
photon detection timestamps.
We use this theory to (1)
show that passive free-running SPAD cameras have an at-
tainable frequency bandwidth that spans the entire DC-to-
31 GHz range in low-ﬂux conditions, (2) derive a novel
Fourier-domain ﬂux reconstruction algorithm that scans this
range for frequencies with statistically-signiﬁcant support
in the timestamp data, and (3) ensure the algorithm’s noise
model remains valid even for very low photon counts or
non-negligible dead times. We show the potential of this
asynchronous imaging regime by experimentally demon-
strating several never-seen-before abilities: (1) imaging a
scene illuminated simultaneously by sources operating at
vastly different speeds without synchronization (bulbs, pro-
jectors, multiple pulsed lasers), (2) passive non-line-of-
sight video acquisition, and (3) recording ultra-wideband
video, which can be played back later at 30 Hz to show
everyday motions—but can also be played a billion times
slower to show the propagation of light itself.
1. Introduction
A basic rule of thumb in high-speed imaging is that speed
needs light: the faster a scene changes, the more light we
need to image it accurately without excessive noise or mo-
tion blur. Over the decades, high-speed light sources [1],
fast cameras [2–4], and depth sensors [5, 6] have made it
possible to image dynamic phenomena occurring in ever-
smaller time intervals with the help of actively-controlled
light sources and synchronization: to collect enough light,
* Joint ﬁrst authors: {mianwei,sotiris}@cs.toronto.edu
Project website: https://compimaging.dgp.toronto.edu/ultra-wideband
the same picosecond- or nanosecond-scale event may be im-
aged millions of times by operating a camera and a source
in lockstep, at MHz repetition rates or more.
Acquiring videos of ultrafast phenomena this way—from
imaging light in ﬂight [7] to fast biological processes [8]—
is now quite common.
Unfortunately, while these tech-
niques do capture ultrafast events, they cannot simultane-
ously capture slower ones too: time wraps at the sync pe-
riod, blurring out anything occurring over longer timespans.
But how do we image highly dynamic scenes—both slow
and ultrafast—passively, without any light sources under
our control, no synchronization, and not much light? Very
little is known about this problem because existing mod-
els for passive low-light imaging [9–13] break down at
timescales much shorter than the timespan between photon
arrivals. As a result, ultrafast imaging in low light has re-
mained beyond the reach of passive methods.
In this work we seek to bridge these two regimes, active and
passive, by revisiting the need for synchronization when
imaging ultrafast scenes in low light. Working from ﬁrst
principles, we develop a novel theory of passive single-
photon imaging that is speciﬁcally designed to eliminate
synchronization between a camera and the light sources in
a scene. The only requirements are that (1) the camera’s
pixels can detect and time-stamp individual photons and (2)
their dead-time period does not impair detection of photons
from one source signiﬁcantly more than any other. In this
imaging regime, each camera pixel time-stamps the photons
it detects using an internal clock that follows the arrow of
time, obviating the need for any external timing signals.
Our work is based on the observation that passive (sync-
free) imaging is fundamentally more powerful than active
imaging in such settings.
Speciﬁcally, without the peri-
odic timing signal from a light source, time never wraps
at a sync period; ultrafast scenes can be imaged for arbitrar-
ily long timespans; and ﬂux variations that occur concur-
rently across 12 orders of magnitude in time (picoseconds
to seconds)—and that involve many unknown sources—can
be recorded with just one camera.
Because photon timestamps due to all light sources and all
This ICCV paper is the Open Access version, provided by the Computer Vision Foundation.
Except for this watermark, it is identical to the accepted version;
the final published version of the proceedings is available on IEEE Xplore.
8135

flux (Mpps)
  25
flux (k photons per sec)
160
flux (kpps)
350
flux (Mpps)
3.5
photons per second (pps)
raster scan
lightbulb
Figure 1: Passive ultra-wideband imaging with a single free-running SPAD pixel. Left bottom & Center: In a real, captured experi-
ment, an unsynchronized single-photon avalanche diode (SPAD) passively records indirect light coming from multiple sources operating
asynchronously from each other (unsynchronized picosecond lasers, projectors, etc.). See Figure 5 (row 2, middle) for actual scene. The
incident ﬂux exhibits simultaneous intensity variations with a bandwidth that spans roughly 9 orders of magnitude in frequency. Bottom
right: Multiple concurrently-occurring phenomena in the ﬂux function can be identiﬁed after acquisition: video ﬂicker (58 Hz), the pulse-
width modulation of an LED light bulb (900 Hz), a movie projected onto a nearby wall by a raster-scanning laser projector (up to 5 MHz),
and two unsynchronized picosecond lasers (40 MHz–10 GHz). Top right: By reconstructing the time-varying ﬂux function of the laser
projector, video frames are reconstructed at 1280x720 resolution using roughly 450-4500 photons collected during each 1/58 s frame.
timescales are recorded concurrently, the choice of which
timescale to show and which light source(s) to use for vi-
sual processing can be done after acquisition (Figure 1).
Thus, just like light ﬁeld cameras [14] enable post-capture
refocusing in space, this new imaging regime enables post-
capture refocusing in time—from transient to everyday
timescales. We demonstrate this one-of-a-kind capability
experimentally in Figure 5, where we use photon timestamp
data captured by a free-running SPAD camera to play back
video of a rapidly-spinning fan at both 1,000 and 250 bil-
lion frames per second. We call this novel regime passive
ultra-wideband imaging.
The key challenge in this regime is how to reconstruct ﬂux
functions with a ultra-wide spectrum (DC to over 10 GHz)
from a stream of photon timestamps that increase mono-
tonically. To tackle it, we develop a ﬂux probing theory
that draws on results from stochastic calculus [15, 16] to
relate the Fourier series decomposition of a time-varying
ﬂux function to the timestamp realizations of an underly-
ing stochastic process [17, 18]. The mathematical under-
pinnings of our approach are grounded in statistics [19–
21] and time series analysis [22–27], and similar methods
have explored ﬂux function estimation in optical communi-
cations [28–30].
Our work ties together several lines of prior research on “ex-
treme” imaging, both passive and active. In passive settings,
several techniques have recently been proposed for estimat-
ing ﬂux from photon data [13, 31–33]. These rely on a va-
riety of ﬂux constancy assumptions and, as a result, are not
applicable to the ultra-wideband regime we consider. In ac-
tive settings, single-photon imaging techniques have relied
exclusively on sync-relative timestamps [34–38], where in-
formation about sub-MHz ﬂux variations has already been
lost.
Aside from single-photon imaging, active ultrafast
imaging techniques have also used heterodyning to measure
ﬂux at one speciﬁc modulation frequency [39–43]. These
techniques have neither the light efﬁciency nor the ultra-
wide bandwidth we demonstrate in this paper.
2. Passive Ultra-Wideband Imaging
Passive, sync-less imaging.
We assume that the imag-
ing system exerts no control over a scene’s appearance: the
scene’s light source(s) can be natural, artiﬁcial, or both, and
their number, operating principle, and time-varying prop-
erties are unknown and unconstrained (Figure 1). Impor-
tantly, we assume that no electronic timing signals, such as
triggers or sync pulses, are received from any of them.
The time-varying ﬂux function.
Following standard ra-
diometric conventions [44], we express incident light at a
pixel as an unknown time-varying function ϕ(t) that repre-
sents the pixel’s instantaneous ﬂux at time t ≥0. Our goal is
to acquire a continuous representation of the ﬂux function
over a possibly unbounded acquisition interval [0,t] (mil-
liseconds, seconds or much longer). In the following we
assume that ϕ(t) is expressed in units of photons per sec-
ond, is continuous, and has ﬁnite spectral support bounded
by frequencies fmin and fmax.
Ultra-wideband ﬂux.
We seek to reconstruct ﬂux func-
tions that have ultra-wide bandwidth, i.e., whose fre-
8136

quency content spans the entire range from constant ﬂux
(fmin = 0 Hz) to extreme time-of-ﬂight timescales (fmax ≥
10 GHz) [43, 45]. Moreover, we assume that no prior infor-
mation is available about the spectrum of ϕ(t).
Photon arrival model.
Our work applies to the single-
photon imaging regime, where the timespan between con-
secutive photon arrivals is not negligible. In this setting,
ϕ(t) is the rate function of an inhomogeneous Poisson pro-
cess governing photon arrivals [29, 46]. The mean value
of ϕ(t) represents the average ﬂux received over the obser-
vation interval [0,t] in units of photons per second and its
inverse, denoted by Tavg, is the average timespan between
consecutive photon arrivals [33].
Low-ﬂux photon detection model.
Modern SPADs can
detect and time-stamp the arrival of individual photons with
extremely high temporal precision (typically tens of pi-
coseconds [3, 47]). SPADs are not perfect detectors, how-
ever, as they exhibit four main non-idealities: quantum efﬁ-
ciency, dead time, timestamp quantization and jitter. Quan-
tum efﬁciency refers to the pixel’s probability of actually
detecting a photon when it is in its active state. This proba-
bility can be well below 1 depending on wavelength; since
it can be thought of as scaling the ﬂux function, we assume
it is absorbed in ϕ(t). After a photon detection, SPADs are
blind to subsequent photon arrivals for an interval known as
the dead time. Dead time can skew photon detection statis-
tics quite signiﬁcantly when photons arrive closely enough
in time to fall within a SPAD’s dead-time window with high
probability [32, 48, 49]. For simplicity, we focus on low-
ﬂux imaging in the main paper, where consecutive arrivals
are spaced much farther apart than the SPAD’s dead time.1
In this case, detections are governed by the same stochastic
process that describes photon arrivals [50], with rate func-
tion ϕ(t) and average timespan Tavg between detections.
Non-negligible dead time. When dead-time intervals be-
come comparable to Tavg (or longer), photon detections are
not Poisson because the detection of a photon may impact
the detection of subsequent ones. We show in supplemen-
tary Section C that our stochastic calculus framework cov-
ers this case as well, enabling acquisition of ϕ(t) by slightly
amending the equations and algorithm in the main paper.
Timestamp model.
Photon timestamps are subject to
quantization from the time-to-digital conversion process
and jitter, i.e., instabilities in timing electronics. Both can
be as low as a few picoseconds for SPADs in the visible
range [51]. To simplify our analysis, we assume without
loss of generality that timestamp resolution and timestamp
accuracy are identical, so that the timestamps’ bin size Q
accounts for jitter as well.2
1For example, Tavg was nearly six times our SPAD’s dead time in the

## Experiments

2When timestamp accuracy is worse than timestamp resolution, the
The stream of absolute detection timestamps.
Since no
external timing signal is available to serve as a reference,
we assume that photon detection timestamps follow the
arrow of time, increasing monotonically according to
the SPAD’s internal clock.
This results in a stream of
timestamps T = (τ1,...,τN(t)), where τi is the elapsed
time from the beginning of acquisition until the i-th photon
detection, and N(t) counts the total photons detected up to
time t. We refer to timestamps τi as absolute timestamps.
Absolute timestamps can be acquired by operating SPAD
pixels in their “passive free-running” mode [32].
Paper roadmap. The remainder of the main paper is aimed
at readers with no background in stochastic calculus, as im-
plementation of our ﬂux acquisition algorithms is straight-
forward and can be done without it. Readers may skip the
formal deﬁnition of a martingale (supplement Section A)
and focus on the comparisons in Section 2.1, the high-level
description of our theoretical results in Section 3, and the al-
gorithms in Section 4 (for low-ﬂux settings) and Section C.1
(for non-negligible dead time). For readers familiar with
statistical estimation, Section D includes simpler proofs of
Section 3’s results, graciously provided by anonymous re-
viewer R1, which do not invoke stochastic calculus but ap-
ply only to low-ﬂux settings where dead time is negligible.
2.1. Imaging with Photon Timestamps
The particular imaging regime outlined above generalizes
two broad classes of single-photon imaging research, both
of which use photon timestamps as their main input. We
distinguish between the two by considering the relation
between (a) the rate of photon detections and (b) the
maximum reconstructible frequency in each case (Table 1).
Passive inter-photon imaging.
Recent work in passive
single-photon imaging has proposed treating the timespan
between consecutive detections as a noisy sample of the
scene’s ﬂux [32, 33]. This implicitly assumes that ﬂux does
not vary in that timespan, which makes the rate of photon
detections a (loose) upper bound on fmax. As a result, pas-
sive low-ﬂux imaging with SPADs has so far been restricted
to slow speeds, with fmax on the order of tens of kHz [13].
Active histogram-based imaging.
Approaches that
employ synchronized light sources [50, 56] occupy the
other extreme of the frequency range. Their basic principle
is to time-stamp detections relative to a sync signal of
a known frequency fsync, so that all timestamps wrap to
the same brief interval [0,1/ fsync] regardless of the actual
timespan between them. This forces photons to accumulate
in a relatively small number of time bins—typically a few
timestamps’ effective number of bits is reduced [52]. Our system’s times-
tamps, for example, are quantized to 4 picoseconds but the standard de-
viation of jitter is 16 picoseconds, so we conservatively use Q = 16 for
performance modeling purposes. Explicit treatment of jitter is beyond this
paper’s scope (e.g., jitter can actually improve timing resolution [53–55]).
8137

imaging regime
passive inter-photon imaging
active histogram-based imaging
passive ultra-wideband imaging
(interdetection-limited)
(sync- and quantization-limited)
(quantization-limited only)
fmax < 1/Tavg
fmin ≥fsync, fmax ≤1/(2Q)
fmax ≤1/(2Q)
light source(s)
one or more sources, no sync
one source only, periodic with period 1/ fsync, sync required
one or more sources, no sync
typical freq. range
low Hz to tens of kHz (plus DC)
low MHz to well above 10 GHz (plus DC)
DC to well above 10 GHz
valid frequencies
all frequencies in range
all frequencies in ϕ(t) must be integer multiples of fsync
all frequencies in range
corrupting ﬂux
any ﬂux with frequencies > 1/Tavg
any ﬂux with frequencies that are not integer multiples of fsync
frequencies > 31 GHz
input data
stream of absolute timestamps
stream of sync-relative timestamps
stream of absolute timestamps
# distinct time bins
not applicable
thousands (typical)
billions to trillions (increases with t)
# photons per bin
not applicable
a non-negative integer; Poisson-distributed, mean proportional to ⌊t fsync⌋
0 or 1, vast majority of bins have 0
ϕ1(t) = 5+5sin(2πt)
ϕ2(t) = 5+5sin(7×6×2πt)
ϕ3(t) = 5+5sin(5×8×2πt)
ϕ4(t) = ϕ1(t)+ϕ2(t)+ϕ3(t)
illustration of
ﬂux, detections
& sync in each
regime
elapsed time t (sec)
detections due to ϕ1
no sync (0 Hz)
0
1
elapsed time t (sec)
detections due to ϕ2
sync (7 Hz)
0
1
elapsed time t (sec)
detections due to ϕ3
sync (5 Hz)
0
1
elapsed time t (sec)
detections due to ϕ4
no sync (0 Hz)
0
1
measurement
model of each
regime
102
101
0
1
estimated ﬂux
inter-photon ﬂux
elapsed time t (sec)
ﬂux
photon-count histograms
7 Hz
5 Hz
corruptions
ϕ1,ϕ3
ϕ2 photons
photon-count histograms
7 Hz
5 Hz
corruptions
ϕ1,ϕ2
ϕ3 photons
0 Hz
1 Hz
40 Hz 42 Hz
detection threshold
50
frequency (Hz)
amplitude
15
0
frequency spectrum
Table 1: Low-ﬂux imaging with photon timestamps. Left column: Passive imaging has so far assumed that photons can be detected at a
rate (much) greater than the highest ﬂux frequency. Middle column: Active techniques are designed to handle the opposite case, where
photon detections occur at a rate (much) lower than the ﬂux function’s frequencies. If a light source’s frequency is not a multiple of fsync
(e.g., 5 Hz for ϕ2 photons and 7 Hz for ϕ3 photons in third row above), its photons will land in the wrong time bin. This contributes to
noise instead of signal, i.e., the histogram will be “ﬂattened”’ (compare the two red and two green histograms, respectively, in third row).
Moreover, even when fsync is well-matched to one light source, other sources emitting at non-multiples of fsync will corrupt the histogram
(third row, gray histograms). Please refer to the supplementary video for another illustration of these effects. Right column: Our approach
inherits the most important features of both regimes, without their limitations.
thousand—and yields a photon-count histogram [57] that
is a noisy sampling of the scaled and time-wrapped ﬂux
function, ⌊t fsync⌋ϕ(t −⌊t fsync⌋/ fsync).
The maximum
reconstructible frequency in this case is governed by the
Nyquist theorem, not the photon interdetection time: a bin
size of 16 picoseconds, for example, theoretically enables
ﬂux acquisition with fmax equal to 31.25 GHz.3
Although this general approach achieves extremely high
imaging speeds [12], its reliance on relative timestamps
comes with a major constraint: the incident ﬂux must also
be a periodic function with a period equal to 1/ fsync, to en-
sure that ϕ(t) and its time-wrapped counterpart are identi-
cal. This can be trivially satisﬁed when the only light in
the scene comes from a precisely-synchronized source (a
pulsed laser, light-emitting diode, etc.), but ﬂux variations
due to other causes cannot be reconstructed. This includes
variations caused by scene motion; light sources that emit at
frequencies lower than fsync; and sources that emit at higher
frequencies that are not integer multiples of fsync. Photons
from such sources result in histogram artifacts in the form
3As a reference, 31.25 GHz is the −3 dB cut-off frequency of a Gaus-
sian pulse with a full-width-at-half-max of 36 picoseconds.
of additional photon noise [58], beat signals [45], or both.
Role of the sync frequency fsync.
Sync frequencies are
typically in the low-MHz range in single-photon imag-
ing applications that involve pulsed sources [35, 50, 59,
60]. This choice balances improved signal-to-noise ratio (a
faster sync means more laser pulses, more photons detected
in each histogram bin, and fewer time bins for them to ac-
cumulate in) against the likelihood of photons being missed
due to dead time [48, 49, 58], or photons arriving “too late”
because time has wrapped already [12, 61]. At such MHz
sync frequencies, the memory and compute cost of recon-
structing histograms from timestamps can be signiﬁcant,
prompting several recent schemes for just-in-time process-
ing of (sync-relative) photon timestamps [37, 38, 62].
The passive ultra-wideband imaging regime. Intuitively,
the regime we tackle in this paper can be understood as
the limit case of photon histogramming, where the sync
frequency is reduced all the way to zero. Speciﬁcally, as
fsync decreases, the interval [0,1/ fsync] increases; more his-
togram bins are needed to span it; fewer photons land into
each bin; the time-wrapped ﬂux function is able to represent
variations that take place over longer timespans; and the
space of reconstructible frequencies (i.e., the integer mul-
8138

0
0
martingale M(t)

t
elapsed time t
elapsed time t
ﬂux ϕ(t) = 4+4sin(80πt)
Nyquist rate 1/2 fmax
average interdetection time
photon stream T
counting process N(t)
ﬂux integral
R t
0 ϕ(u)du
photons / sec
total photons detected
1
2
3
4
5
Figure 2:
Relation between the stream of absolute timestamps,
the counting process, the ﬂux function and its integral. Times-
tamps are from a computational simulation of the inhomogeneous
Poisson process with the ﬂux function ϕ(t) indicated above.
tiples of fsync) expands. In the limit when fsync is exactly
zero, there is no sync at all, timestamps become absolute
and every photon lands into its own unique time bin. Cru-
cially, all frequencies from DC up to the Nyquist limit—and
from any light source—become potentially reconstructible.
Mathematical modeling of this limit case, however, is non-
trivial because the concept of a histogram breaks down:
photons never accumulate, and the contents—0 or 1—of
any given bin provide almost no information about the ﬂux
function.4 On the computational side, the entire acquisition
interval [0,t] is effectively partitioned into time bins at the
SPAD’s timing resolution, so acquisitions of a second or
more can potentially involve trillions of time bins (most of
which are empty). Fortunately, as we show in the next sec-
tion, both these challenges can be overcome by formulating
ﬂux reconstruction in terms of the photon counting process,
which is not degenerate even when fsync = 0.
3. Probing Flux Functions
Our approach establishes a direct mathematical link be-
tween (1) the stream of absolute timestamps detected at a
pixel—however few or far apart they may be—and (2) the
ﬂux function that produced them. This link allows us to
“probe” the Fourier spectrum of an unknown ﬂux function
across the entire DC-to-GHz range for frequencies that have
statistically-signiﬁcant support in the timestamp data. We
introduce our ﬂux probing theory below and address ﬂux
reconstruction in Section 4. For the sake of generality, we
consider timestamps to be continuous-valued random vari-
ables and model quantization as part of our theory.
4More formally, the Poisson-distributed random variable associated
with any given time bin has a mean that goes to zero as t →∞[63].
The photon counting process. Even though a single abso-
lute timestamp provides (almost) no information about the
underlying ﬂux function, the stream of absolute timestamps
as a whole contains considerable information about it. The
speciﬁc relation between the two comes from stochastic cal-
culus [15].
Speciﬁcally, in the continuous-time domain,
a stream T of real-valued absolute timestamps provides a
noisy “reconstruction” of the integral of ϕ(t) (Figure 2):
N(t)
| {z }
counting process
=
Z t
0 ϕ(u)du
|
{z
}
ﬂux integral up to time t
+
M(t)
| {z }
martingale noise
.
(1)
The function N(t) in Eq. (1) counts the photons received up
to time t and is completely determined by T ; formally, it is
a counting process [15, 19]. Viewed from the perspective
of histogram-based single-photon imaging (Table 1, mid-
dle), N(t) is the continuous-time analog of the cumulative
photon-counthistogram over the interval [0,t], for fsync = 0.
The function M(t) in Eq. (1) is a continuous-time random
process called a martingale [64] that can be thought of as a
form of additive zero-mean noise.5
As can be seen from the example of Figure 2, a single ran-
dom realization of the counting process (cyan curve) is a
highly discontinuous function that, on ﬁrst inspection, bears
no resemblance to the ﬂux integral it is supposed to approxi-
mate in Eq. (1). These discontinuities introduce dense, spu-
rious frequencies in the Fourier-domain representation of
N(t) that do not exist in the actual ﬂux integral.
3.1. Theory of Flux Probing
Our theoretical results use tools from stochastic calculus
to address two basic questions. First, what is the highest
possible frequency fmax that can be recovered by a passive
single-photon imaging system that outputs quantized abso-
lute timestamps? Second, for frequencies within the attain-
able bandwidth, how can we derive a noise model that al-
lows spurious frequencies to be efﬁciently detected and dis-
carded, and the accuracy of real frequencies to be quantiﬁed
as a function of the acquired timestamp stream? We sum-
marize these results below and defer proofs to Section B.
The probing operation.
Proposition 1 tells us that we
can always probe the ﬂux function to recover a (noisy)
measurement of its inner product with practically any
other function. Moreover, probing is efﬁcient to compute
from the timestamp stream and can be thought of as a
continuous-time and sync-free generalization of compres-
sive acquisition schemes for conventional photon-counting
histograms [37, 38, 62]. In particular, let T be the stream of
real-valued absolute timestamps up to time t and let p(t) be
5One example of a martingale is an unbiased random walk. Like N(t)
in Eq. (1), many other increasing stochastic processes can be expressed as
the sum of a deterministic increasing function and a martingale [15]. See
supplement Section A for the formal deﬁnition of a martingale.
8139

an arbitrary known and square-integrable function:
Proposition 1 (Flux Probing Equation). The inner product
of the probing function p(t) and the unknown ﬂux function
ϕ(t) over the time interval [0,t] satisﬁes the relation
p(T ) = ⟨p,ϕ⟩+ Mp(t)
(2)
where p(T ) are “probing measurements” which sum the
values of the probing function at the absolute timestamps
p(T ) def
= ∑
τ∈T
p(τ) ,
(3)
Mp(t) is a martingale, and the inner product is deﬁned as
R t
0 p(u)ϕ(u)du.
Fundamental limit on bandwidth. In the special case of
probing with the Fourier basis functions p f (t) = e−j2π ft, we
prove in supplement Section B that probing with f > 1/2Q
yields aliased measurements that “wrap around” the fre-
quency spectrum and are identical to—and indistinguish-
able from—lower-frequency measurements:
Proposition 2. Given timing resolution Q, the maximum
recoverable frequency is fmax =
1
2Q.
Intuitively, Proposition 2 says that ﬂux frequencies above
1/2Q are unrecoverable regardless of whether we detect a
few photons or a million.
Noise model. Our model accounts for the inhomogeneous
Poisson nature of photon detections and treats the general
case of real-valued timestamps. The model is valid for arbi-
trary ﬂux levels within the low-ﬂux regime and, as we show
in supplement Section G.4, it remains valid for low-count
acquisitions (e.g., as few as ten photons). More speciﬁ-
cally, Proposition 3 tells us that the noise in probing mea-
surements has a distribution that can be estimated from the
timestamp stream through another probing operation. Thus,
probing gives the means both to observe a ﬂux function and
to quantify the uncertainty of that observation:
Proposition 3 (Distribution of Probing Measurements).
The probing measurements p(T ) are approximately nor-
mally distributed with mean ⟨p,ϕ⟩and variance ⟨p2,ϕ⟩.
Fourier probing noise. Finally, Corollaries 1 and 2 allow
us to quantify the accuracy by which speciﬁc ﬂux frequen-
cies can be estimated from a given timestamp stream:
Corollary 1 (Distribution of Fourier Probing). The Fourier
probing measurements p f (T ) approximately follow a com-
plex normal distribution with mean and covariance matrix
µ =

⟨cos(2π ft), ϕ(t) ⟩
⟨−sin(2π ft), ϕ(t) ⟩

(4)
Σ =

⟨cos2(2π ft),ϕ(t)⟩
0
0
⟨sin2(2π ft),ϕ(t)⟩

.
(5)
Corollary 2 (Distribution of Fourier Probing Energy). The
normalized energy of the Fourier basis probing measure-
ments
pE
f (T )
def
=
Re
 p f (T )
pΣ1,1
2
+ Im
 p f (T )
pΣ2,2
2
(6)
follows a non-central χ2 distribution with 2 degrees of free-
dom and non-centrality parameter µ2
1/Σ1,1 + µ2
2/Σ2,2.
In supplement Section B we show that unbiased estimators
of the parameters of the above distributions can be obtained
via probing.
Frequency detection. Given the estimated distribution of
the Fourier Probing Energy, we derive the constant false
alarm rate (CFAR) detector [65] (see supplement Section B)
to identify and remove noisy frequencies based on a desired
probability of false alarm α. False alarms occur when we
keep f and E[|p f (T )|] = 0; we remove f if pE
f (T ) is lower
than CDF−1
χ2 (1−α), derived from Corollary 2. Speciﬁcally,
we detect frequencies for which
|p f (T )|2 ≥CDF−1
χ2 (1 −α)N(t)
2t2
.
(7)
Note that (1) for a ﬁxed α, the probability of detecting a
frequency is proportional to the total number of photons de-
tected, and (2) for ﬂux functions dominated by a particular
frequency such that |p fi(T )|2 is large, N(t) also tends to
become proportionally larger, reducing the probability of
detecting other frequencies.
Implications for passive single-photon imaging. Propo-
sition 2 implies that rather than being a hindrance, sync-
less imaging with absolute timestamps confers an extreme
bandwidth advantage to SPAD cameras: systems with 16-
picosecond resolution, such as our own, can simultane-
ously acquire ﬂux variations that span the entire DC-to-
31 GHz range of frequencies, and that are due to any num-
ber of unknown light sources operating independently. This
bandwidth is orders of magnitude broader than intensity
cameras—SPADs or otherwise—were thought capable of
acquiring directly [41–43, 45], i.e., without resorting to ho-
modyne [43] or heterodyne [41, 42, 45] detection schemes.
While Proposition 2 describes reconstructability (i.e., fre-
quencies above the limit are unreconstructible), Proposi-
tion 3 and Eq. (7) provide insights about the accuracy
and detectability of ﬂux variations at different frequencies.
Lastly, although we have not veriﬁed the theorized DC-
to-31 GHz bandwidth experimentally due to unavailability
of lasers that are fast enough, we show several real-world
demonstrations of simultaneous DC-to-16.9 GHz imaging
under very challenging low-ﬂux conditions (see Figure 1,
Section 5, and Section E). These validate our noise models
in Eqs. (4)-(6) and (partially) conﬁrm our theoretical bound.
8140

procedure FLUXREC(T , t, fmax, α)
// Frequency scanning.
∆f = 0.6/t (see supp. Section B)
F = freqs from 0 to fmax with step ∆f
loop f ∈F
pf (T ) = (1/t)∑τ∈T e−j2π fτ
// Frequency detection.
Fused = /0
loop f ∈F
Af = |pf (T )|, φf = ∠pf (T )
reject f using CFAR (Eq.(7))
Fused = Fused ∪{f} if not rejected
// Flux reconstruction.
ˆϕ(t) = ∑f∈Fused Af cos(2π ft +φf )
20
0
0
50
100
measured
ground truth
std. dev.
0
1
0
400
Timestamps
0
1
0
200
400
estimated
ground truth
detected frequencies
Frequency Scanning
Flux Function & Timestamps
Flux Reconstruction
Frequency Detection
j
Flux function & Timestamps
Frequency Scanning
Frequency Detection
Flux Reconstruction
probability of
false alarm
CFAR threshold
0.0
0.5
1.0
  0
400
200
600
measured
threshold
20
0
101
102
103
104
ϕ(t) = ∑f ∈F A f cos(2π ft +φf ) pf (T ) = (1/t)∑τ∈T e−j2π f τ
ˆϕ(t) = ∑f ∈Fused A f cos(2π ft +φf )
Figure 3: Overview of imaging by ﬂux probing. Left: Flux reconstruction algorithm used in our experiments. Right: Visual illustration
of the algorithm. Flux function: A ﬂux function of ﬁnite spectral support can be expressed as a sum of sinusoids and produces a stream of
absolute timestamps. Frequency scanning: We probe the ﬂux function using a Fourier basis and measure the response at each frequency.
Frequency detection: For each of the probed frequencies, we detect whether it contributes to the ﬂux function if its corresponding amplitude
is greater than a threshold (top) which is selected to achieve the desired probability of false alarm. (bottom). Flux reconstruction: Finally,
we reconstruct a continuous-time ﬂux function from the amplitudes and phases of detected frequencies.
4. Imaging by Flux Probing
Our probing theory leads directly to an algorithm that re-
constructs the Fourier transform of the ﬂux function by
frequency-scanning the entire DC-to-GHz bandwidth (Fig-
ure 3).
This algorithm is similar to the Fourier-domain
histogramming technique used in conventional active set-
tings [62], but also differs in two key respects: (1) it pro-
vides a principled way to estimate frequency uncertainty in
an acquired timestamp stream, and (2) it enables tractable
operation in a regime involving potentially billions of can-
didate frequencies—e.g., a 1 Hz-resolution scan of DC-to-
20 GHz—by rejecting spurious frequencies and reducing
storage requirements. The frequency detection step uses
the CFAR detector of Section 3, where we set α so that
the expected number of false alarms is less than 1. Figure 3
includes a visual depiction of the ﬂux reconstruction algo-
rithm, along with a complete description in pseudocode.
5. Experiments
We validate our theory experimentally with (1) passive
ultra-wideband sensing of both 1D intensity signals and 2D
video signals ranging from DC to 16.9 GHz, (2) passive
non-line-of-sight (NLOS) video via MHz-rate ﬂux func-
tion reconstruction, (3) generalization to 2D SPAD arrays
for high speed video, and (4) simulation-based quantitative

## Evaluation

mental video and to supplement Sections E, F, and G for
more experiments and implementation details.
Passive ultra-wideband sensing. We demonstrate recov-
ering signals with frequencies spanning roughly 9 orders
of magnitude from DC to 10 GHz (Figure 1). We place
a single-pixel SPAD in the scene to capture ﬂux variations
from (1) pulse-width modulation of a light bulb (900 Hz),
(2) backscattered light from a raster-scanning laser projec-
tor (60 Hz–10 MHz), and (3) two unsynchronized picosec-
ond lasers (40 MHz–10 GHz). Remarkably, the ﬂux func-
tion is reconstructed from only 77,000 photon timestamps.6
We recover time-varying ﬂux across billions of frequencies
from this minuscule set of photons. Moreover, by employ-
ing a brighter and faster laser, we achieve passive DC-to-
16.9 GHz sensing over room-size distances (Section E.2.2).
We also demonstrate ultra-wideband video (Figure 5, top)
by raster scanning a scene in which a pulsed laser, with
20 MHz repetition and 80 ps FWHM, is diffused to illu-
minate a fan spinning at 54 Hz.
We detect frequencies
from DC to 10 GHz and render ﬂux functions at 1 kfps
and 250 Gfps, showing both the fan blades rotating and
the propagation of the laser pulse.
In contrast, conven-
tional approaches reconstruct the scene at only one of the
aforementioned frame rates, temporally blurring either slow
or fast events.
Furthermore, our method can render the
ﬂux at whatever timescale, essentially freezing time at all
timescales. Note that because we only had access to a sin-
gle pixel SPAD, the timestamps were collected by scanning
across the ﬁeld of view of the SPAD. To temporally align
the ﬂux functions between pixels, we use synchronization
signals from both the laser and the fan. We emphasize that
no synchronization signals were used to reconstruct the ﬂux
functions themselves—we are demonstrating a new capa-
bility of reconstructing the appearance of the scene as it ap-
peared during each laser pulse—this is distinct from the use
of synchronization and histogramming to estimate the aver-
age appearance of the ﬂux function over time [7, 12, 66].
We also emphasize that the images are rendered by integrat-
ing the ﬂux function over the exposure of each frame. As
6Conventional camera pixels collect a few thousand photons to return
a single estimate of light intensity.
8141

Figure 4: Simulation-based comparisons. Left to right: Laser pulse reconstructed by three methods from 2000 timestamps produced by
a 20 MHz pulse train. Reconstruction from a 20 MHz train of much shorter pulses, using just 50 timestamps. Pulse reconstruction error as
a function of the number of timestamps given as input. Reconstructed pulses from 100 realizations of a ﬁfty-photon timestamp stream.
such, these images exhibit not only high dynamic range but
their intensities are also expressed in physical units of pho-
tons, thereby ensuring radiometric calibration by nature.
We show another video example in Figure 5 (row 2), where
the same picosecond laser illuminates a Coca-Cola bottle
ﬁlled with water and a small amount of milk to scatter the
light. Within the same scene, a compact ﬂuorescent light-
bulb (CFL) ﬂickers at 120 Hz. We render videos at 10 kfps
and 200 Gfps to visualize the CFL ﬂicker and light pulses
propagating through the bottle (Figure 5, rows 3–4). For
the same reasons outlined in the previous paragraph, we use
synchronization signals from the laser and the bulb.
Recovering passive NLOS videos. We demonstrate pas-
sive NLOS video reconstruction using light measured indi-
rectly from a raster-scanning laser projector (see illustration
in Figure 1 and photo in Figure 5, row 2). The SPAD ob-
serves a single point on a diffuse box during the projector
beam’s raster scan, collecting light that bounced twice (i.e.,
diffuser→diffuse box→SPAD). This conﬁguration is anal-
ogous to dual photography [67]. By reconstructing the 1D
ﬂux function over a one-second span, we recover the video
being played. We show results for the multi-illumination
setting of Figure 1 and for a projector-only setting. In the
latter case, we recover ﬁne details of each video frame (Fig-
ure 5, rows 5–6) even though only 3000 photons were col-
lected on average during a frame’s 1/58 s raster scan.
Probing with SPAD arrays.
Our method can be applied
off the shelf to data from 2D SPAD sensors. To demon-
strate this, we compare to Seets et al. [13] who recover high-
speed video with a 32×32 SPAD array. They assume ﬂux
is piecewise constant and identify contiguous sets of times-
tamps with the same ﬂux. Photon inter-arrivals are then av-
eraged to obtain a single ﬂux estimate per set (Figure 5,
bottom right). In contrast, we recover a time-varying ﬂux
function by probing (Figure 5, bottom left). Because the
sensor outputs just one timestamp per 20 microseconds for
each pixel—a dead time too long to ignore even at relatively
low ﬂux levels—we probe using the generalized algorithm
of Section C.1. This yields a periodic ﬂux function truer
to the rotating fan’s motion, whereas periodicity and high-
frequency variations are lost by the method in [13].
Simulations.
Lastly, we consider reconstruction of a
ﬂux function corresponding to 20 MHz pulse trains from
an ultrafast laser with frequency support of 12.5 GHz and
125 GHz, respectively, i.e., up to the theoretically-attainable
limit of a jitter-less SPAD with 4 ps timestamp quantization
(Proposition 2). Figure 4 compares the result of three meth-
ods: (1) conventional photon-count histogramming which
requires synchronization, (2) our sync-less reconstruction
algorithm in Figure 3, and (3) “oracle-based” ﬂux probing,
which probes the ground-truth set of frequencies instead of
relying on frequency scanning. As can be seen, probing can
recover pulses up to the theoretical limit from just 50 times-
tamps and, despite being passive, outperforms histogram-
ming considerably as photon counts increase. Please see
Section G for a more detailed quantitative evaluation.
6. Concluding Remarks
The sheer amount of data involved in probing timestamp
streams cannot be ignored: even a single pixel can output
tens of thousands of timestamps per second in low light, and
our ultrawide-bandwidth results require probing billions of
frequencies. Sketching [38] and Non-Uniform FFT [68]
may offer ways forward but major challenges remain. That
said, we believe that passive acquisition and processing of
timestamp streams from free-running SPADs opens new di-
rections in dynamic imaging: completely unsynchronized,
single-shot observations of ultrafast phenomena with multi-
ple light sources across different timescales; passive depth
imaging using uncooperative, environmental light sources;
compressive ultrafast video recording from sparse times-
tamps; temporal “microscopes” that allow monitoring in-
tensity ﬂuctuations across timescales spanning the nine-plus
orders of magnitude (i.e., DC to 31 GHz) theoretically cap-
tured by SPADs; and more. We are thus looking forward to
more advances on these remarkable sensors.
Acknowledgements We thank the anonymous reviewers,
and R1 in particular, for their invaluable comments and sug-
gestions. We also thank Louis Zhang for creating an inter-
active tool for visualizing and sampling ﬂux integrals efﬁ-
ciently using OpenCL, and John Hancock for conﬁguring
the servers used in our experiments. Lastly, KNK and DBL
gratefully acknowledge the support of NSERC under the
RGPIN and RTI programs.
8142

flux rendered at 1 kfps
AC-powered fluorescent bulb (120 Hz flicker rate)
picosecond laser pointing at bottle (20 MHz pulse rate)
raster-scanning path of
projectors laser beam
passive ultra-wideband video acquisition (DC to 10 GHz)
reconstructed per-pixel flux (rendered at two timescales)
10,000 fps video
 200 billion fps video
passive ultrafast single-pixel imaging & NLOS video
C
B
D
A
bulb too dim at this timescale, pulse propagation visible
bulb blinking, light on bottle appears constant
reconstructed flux function (4 pixels & 2 timescales shown)
A
100 milliseconds
C
B
D
5000 picoseconds
t =  3915 ps
after reaching C, pulses bounce back to D
t =  4610 ps
t =  0.9 ms
2699 photons
t = 2.800 s
 3175 photons
t = 3.477 s
t = 0.374 s
t = 1.562 s
projected (ground truth)
reconstructed
passive  NLOS video acquisition
comparison to related work on SPAD arrays
change point flux for pixel X
this work
Seets et al. 2021
X
7 milliseconds
reconstructed flux function for pixel
X
X
7 milliseconds
flux rendered at 250 Gfps
conventional transient video
flux rendered at 250 Gfps
t = 3.33 ms + 4.408 ns
       = 4 ps
      = 1 ms
t = 3.33 ms
       = 4 ps
t = 3.33 ms + 4.472 ns
      = 4 ps
t = 3.33 ms + 4.472 ns
C
B
D
A
C
B
D
A
lasers
laser video
projector
diffuser
diffusers
SPAD line of sight
ceiling bulb
reflection
2995 photons
3567 photons
Figure 5: Passive ultra-wideband imaging experiments. Row 1: Simultaneous recovery of spinning fan and light propagation (see text
for experiment setup). Rendering the ﬂux function at 1 kfps reveals motion of the fan (yellow arrow), but light propagation is invisible;
at 250 Gfps light propagation is visible, and the fan freezes. Conventional histogramming (right) synced to the laser fails to recover the
(unsynced) fan rotation. Row 2: Experimental setup for ultra-wideband video acquisition (left) and NLOS video imaging in a scene with
multiple light sources (right). Rows 3–4: Flux function images at two timescales (left, bottom right) and for different points in the scene
illuminated by a pulsed laser and ﬂickering light bulb (top right). The three peaks at B, C, and D correspond to a light pulse entering the
bottle (B) propagating to the cap (C), and reﬂecting back (D). Rows 5–6: Passive NLOS acquisition using a raster-scanning laser projector
with ground truth and reconstructed frames. Rows 7–8: We use SPAD array data from Seets et al. [13] to reconstruct per-pixel ﬂux (left).
The common assumption of piecewise constant ﬂux (right) does not hold even for this simple scene of a rotating fan.
8143

References
[1] C. Rullière, Femtosecond Laser Pulses. Springer New
York, 2005.
[2] D. J. Bradley, B. Liddy, and W. E. Sleat, “Direct lin-
ear measurement of ultrashort light pulses with a pi-
cosecond streak camera,” Opt. Commun., vol. 2, no. 8,
pp. 391–395, 1971.
[3] F. Zappa, S. Tisa, A. Tosi, and S. Cova, “Principles
and features of single-photon avalanche diode arrays,”
Sens. Actuators A: Phys., vol. 140, no. 1, pp. 103–112,
2007.
[4] L. Gao, J. Liang, C. Li, and L. V. Wang, “Single-shot
compressed ultrafast photography at one hundred bil-
lion frames per second,” Nature, vol. 516, no. 7529,
pp. 74–77, 2014.
[5] C. Niclass, A. Rochas, P.-A. Besse, and E. Charbon,
“Design and characterization of a CMOS 3-D im-
age sensor based on single photon avalanche diodes,”
IEEE J. Solid-State Circuits, vol. 40, no. 9, pp. 1847–
1854, 2005.
[6] R. Schwarte, Z. Xu, H.-G. Heinol, J. Olk, R. Klein,
B. Buxbaum, H. Fischer, and J. Schulte, “New electro-
optical mixing and correlating sensor: Facilities and
applications of the photonic mixer device (PMD),” in
Proc. SPIE, vol. 3100, pp. 245–253, 1997.
[7] G. Gariepy, N. Krstaji´c, R. Henderson, C. Li, R. R.
Thomson, G. S. Buller, B. Heshmat, R. Raskar,
J. Leach, and D. Faccio,
“Single-photon sensi-
tive light-in-ﬁght imaging,” Nat. Commun., vol. 6,
no. 6021, 2015.
[8] W.
Becker,
“Fluorescence
lifetime
imaging–
techniques and applications,” J. Microsc., vol. 247,
no. 2, pp. 119–136, 2012.
[9] E. R. Fossum, J. Ma, S. Masoodian, L. Anzagira, and
R. Zizza, “The quanta image sensor: Every photon
counts,” Sensors, vol. 16, no. 8, 2016.
[10] K. Morimoto, A. Ardelean, M.-L. Wu, A. C. Ulku,
I. M. Antolovic, C. Bruschini, and E. Charbon,
“Megapixel time-gated SPAD image sensor for 2D
and 3D imaging applications,” Optica, vol. 7, no. 4,
pp. 346–354, 2020.
[11] Y. Chi, A. Gnanasambandam, V. Koltun, and S. H.
Chan, “Dynamic low-light imaging with quanta im-
age sensors,” in Proc. Eur. Conf. on Computer Vision
(ECCV), pp. 122–138, Springer, 2020.
[12] M. O’Toole, F. Heide, D. B. Lindell, K. Zang,
S. Diamond, and G. Wetzstein, “Reconstructing tran-
sient images from single-photon sensors,” in Proc.
IEEE/CVF Conf. on Computer Vision and Pattern
Recognition (CVPR), pp. 1539–1547, 2017.
[13] T. Seets, A. Ingle, M. Laurenzis, and A. Velten, “Mo-
tion adaptive deblurring with single-photon cameras,”
in Proc. IEEE/CVF Winter Conf. on Applications of
Computer Vision (WACV), pp. 1944–1953, 2021.
[14] R. Ng, M. Levoy, M. Brédif, G. Duval, M. Horowitz,
and P. Hanrahan, “Light ﬁeld photography with a
hand-held plenoptic camera,” Technical Report, 2005.
[15] J. L. Doob, Stochastic Processes. Wiley New York,
1953.
[16] S. N. Cohen and R. J. Elliott, Stochastic Calculus and
Applications, vol. 2. Birkhäuser New York, 2015.
[17] N. Chen, D. K. K. Lee, and S. N. Negahban, “Super-
resolution estimation of cyclic arrival rates,” Ann.
Stat., vol. 47, no. 3, pp. 1754–1775, 2019.
[18] K.-S. Lii and M. Rosenblatt, “Estimation for al-
most periodic processes,” Ann. Stat., vol. 34, no. 3,
pp. 1115–1139, 2006.
[19] M. S. Bartlett, “The spectral analysis of point pro-
cesses,” J. R. Stat. Soc., B: Stat. Methodol., vol. 25,
no. 2, pp. 264–296, 1963.
[20] D. Vere-Jones, “On the estimation of frequency in
point-process data,” J. Appl. Probab., vol. 19, pp. 383–
394, 1982.
[21] Á. Gajardo and H.-G. Müller, “Cox point process re-
gression,” IEEE Trans. Inf. Theory, vol. 68, no. 2,
pp. 1133–1156, 2022.
[22] M. S. Bartlett, “Periodogram analysis and continuous
spectra,” Biometrika, vol. 37, no. 1/2, pp. 1–16, 1950.
[23] G. U. Yule, “On a method of investigating period-
icities in disturbed series, with special reference to
Wolfer’s sunspot numbers,” Philos. Trans. R. Soc.
Lond., A, vol. 226, pp. 267–298, 1927.
[24] M. G. Kendall, “On the analysis of oscillatory time-
series,” J. R. Stat. Soc., vol. 108, no. 1/2, pp. 93–141,
1945.
[25] N. R. Lomb, “Least-squares frequency analysis of un-
equally spaced data,” Astrophys. Space Sci., vol. 39,
no. 2, pp. 447–462, 1976.
[26] S. M. Ransom, S. S. Eikenberry, and J. Middleditch,
“Fourier techniques for very long astrophysical time-
series analysis,” Astron. J., vol. 124, no. 3, pp. 1788–
1809, 2002.
[27] J. T. VanderPlas, “Understanding the Lomb–Scargle
periodogram,” Astrophys. J. Suppl. Ser., vol. 236,
no. 1, pp. 1–28, 2018.
8144

[28] O. Macchi and B. Picinbono, “Estimation and detec-
tion of weak optical signals,” IEEE Trans. Inf. Theory,
vol. 18, no. 5, pp. 562–573, 1972.
[29] J. E. Mazo and J. Salz, “On optical data communi-
cation via direct detection of light pulses,” Bell Syst.
Tech. J., vol. 55, no. 3, pp. 347–369, 1976.
[30] A. Komaee, “Maximum likelihood and minimum
mean squared error estimations for measurement of
light intensity,” in Proc. Conf. on Information Sciences
and Systems (CISS), pp. 1–6, 2010.
[31] S. Ma, S. Gupta, A. C. Ulku, C. Bruschini, E. Char-
bon, and M. Gupta, “Quanta burst photography,” ACM
Trans. Graph. (SIGGRAPH), vol. 39, no. 4, pp. 1–16,
2020.
[32] A. Ingle, A. Velten, and M. Gupta, “High ﬂux pas-
sive imaging with single-photon sensors,” in Proc.
IEEE/CVF Conf. on Computer Vision and Pattern
Recognition (CVPR), pp. 6753–6762, 2019.
[33] A. Ingle, T. Seets, M. Buttafava, S. Gupta, A. Tosi,
M. Gupta, and A. Velten, “Passive inter-photon imag-
ing,” in Proc. IEEE/CVF Conf. on Computer Vi-
sion and Pattern Recognition (CVPR), pp. 8585–8595,
2021.
[34] D. B. Lindell, M. O’Toole, and G. Wetzstein, “To-
wards transient imaging at interactive rates with
single-photon detectors,” in Proc. IEEE Int. Conf. on
Computational Photography (ICCP), pp. 1–8, 2018.
[35] D. Shin, F. Xu, D. Venkatraman, R. Lussana, F. Villa,
F. Zappa, V. K. Goyal, F. N. Wong, and J. H. Shapiro,
“Photon-efﬁcient imaging with a single-photon cam-
era,” Nat. Commun., vol. 7, no. 12046, 2016.
[36] Q. Sun, X. Dun, Y. Peng, and W. Heidrich, “Depth and
transient imaging with compressive SPAD array cam-
eras,” in Proc. IEEE/CVF Conf. on Computer Vision
and Pattern Recognition (CVPR), pp. 273–282, 2018.
[37] F. Gutierrez-Barragan, A. Ingle, T. Seets, M. Gupta,
and A. Velten, “Compressive single-photon 3D cam-
eras,” in Proc. IEEE/CVF Conf. on Computer Vision
and Pattern Recognition (CVPR), pp. 17854–17864,
2022.
[38] M. P. Sheehan, J. Tachella, and M. E. Davies, “A
sketching framework for reduced data transfer in pho-
ton counting lidar,” IEEE Trans. Comput. Imaging,
vol. 7, pp. 989–1004, 2021.
[39] F. Heide, M. B. Hullin, J. Gregson, and W. Heidrich,
“Low-budget transient imaging using photonic mixer
devices,” ACM Trans. Graph. (SIGGRAPH), vol. 32,
no. 4, pp. 1–10, 2013.
[40] F. Li, F. Willomitzer, M. M. Balaji, P. Rangarajan, and
O. Cossairt, “Exploiting wavelength diversity for high
resolution time-of-ﬂight 3D imaging,” IEEE Trans.
Pattern Anal. Machine Intell., vol. 43, no. 7, pp. 2193–
2205, 2021.
[41] F. Li, F. Willomitzer, P. Rangarajan, M. Gupta, A. Vel-
ten, and O. Cossairt, “SH-ToF: Micro resolution time-
of-ﬂight imaging with superheterodyne interferome-
try,” in Proc. IEEE Int. Conf. on Computational Pho-
tography (ICCP), pp. 1–10, 2018.
[42] S.-H. Baek, N. Walsh, I. Chugunov, Z. Shi, and
F. Heide, “Centimeter-wave free-space neural time-
of-ﬂight imaging,” ACM Trans. Graph. (SIGGRAPH),
vol. 42, no. 1, pp. 1–18, 2022.
[43] M. Gupta, S. K. Nayar, M. B. Hullin, and J. Mar-
tin, “Phasor imaging: A generalization of correlation-
based time-of-ﬂight imaging,” ACM Trans. Graph.
(SIGGRAPH), vol. 34, no. 5, pp. 1–18, 2015.
[44] R. W. Boyd, Radiometry and the Detection of Optical
Radiation. Wiley, 1983.
[45] A. Kadambi and R. Raskar, “Rethinking machine vi-
sion time of ﬂight with GHz heterodyning,” IEEE Ac-
cess, vol. 5, pp. 26211–26223, 2017.
[46] S. M. Ross, Stochastic Processes. Wiley, 1983.
[47] M.
A.
Itzler,
R.
Ben-Michael,
C.-F.
Hsu,
K. Slomkowski, A. Tosi, S. Cova, F. Zappa, and
R.
Ispasoiu,
“Single
photon
avalanche
diodes
(SPADs) for 1.5 µm photon counting applications,” J.
Mod. Opt., vol. 54, no. 2-3, pp. 283–304, 2007.
[48] A.
K.
Pediredla,
A.
C.
Sankaranarayanan,
M. Buttafava,
A. Tosi,
and A. Veeraraghavan,
“Signal processing based pile-up compensation for
gated single-photon avalanche diodes,” arXiv preprint
arXiv:1806.07437, 2018.
[49] J. Rapp, Y. Ma, R. M. A. Dawson, and V. K.
Goyal, “Dead time compensation for high-ﬂux rang-
ing,” IEEE Trans. Signal Process., vol. 67, no. 13,
pp. 3471–3486, 2019.
[50] G. A. Kirmani, Computational Time-resolved Imag-
ing. PhD thesis, Massachusetts Institute of Technol-
ogy, 2015.
[51] S. Riccardo, E. Conca, V. Sesta, A. Velten, and
A. Tosi, “Fast-gated 16 × 16 SPAD array with 16
on-chip 6 ps time-to-digital converters for non-line-
of-sight imaging,” IEEE Sens. J., vol. 22, no. 17,
pp. 16874–16885, 2022.
[52] T. C. Carusone, D. Johns, and K. Martin, Analog Inte-
grated Circuit Design. Wiley, 2011.
8145

[53] J. Rapp, R. M. A. Dawson, and V. K. Goyal,
“Dithered depth imaging,” Opt. Express, vol. 28,
no. 23, pp. 35143–35157, 2020.
[54] J. Rapp, R. M. A. Dawson, and V. K. Goyal, “Estima-
tion from quantized Gaussian measurements: When
and how to use dither,” IEEE Trans. Signal Process.,
vol. 67, no. 13, pp. 3424–3438, 2019.
[55] A. Raghuram, A. Pediredla, S. G. Narasimhan,
I. Gkioulekas, and A. Veeraraghavan, “STORM:
Super-resolving transients by oversampled measure-
ments,” in Proc. IEEE Int. Conf. on Computational
Photography (ICCP), pp. 1–11, 2019.
[56] X. Liu, I. Guillén, M. L. Manna, J. H. Nam, S. A.
Reza, T. H. Le, A. Jarabo, D. Gutierrez, and A. Velten,
“Non-line-of-sight imaging using phasor-ﬁeld virtual
wave optics,” Nature, vol. 572, no. 7771, pp. 620 –
623, 2019.
[57] Y. Chen, J. D. Müller, P. T. C. So, and E. Gratton, “The
photon counting histogram in ﬂuorescence ﬂuctuation
spectroscopy,” Biophys. J., vol. 77, no. 1, pp. 553–567,
1999.
[58] A. Gupta, A. Ingle, and M. Gupta, “Asynchronous
single-photon 3D imaging,” in Proc. IEEE/CVF Int.
Conf. on Computer Vision (ICCV), pp. 7909–7918,
2019.
[59] F. Heide, S. Diamond, D. B. Lindell, and G. Wetzstein,
“Sub-picosecond photon-efﬁcient 3D imaging using
single-photon sensors,” Sci. Rep., vol. 8, no. 17726,
2018.
[60] V. Zickus, M.-L. Wu, K. Morimoto, V. Kapitany,
A. Fatima, A. Turpin, R. Insall, J. Whitelaw, L. Mach-
esky, C. Bruschini, D. Faccio, and E. Charbon, “Flu-
orescence lifetime imaging with a megapixel SPAD
camera and neural network lifetime estimation,” Sci.
Rep., vol. 10, no. 20986, 2020.
[61] A. M. Pawlikowska, A. Halimi, R. A. Lamb, and G. S.
Buller, “Single-photon three-dimensional imaging at
up to 10 kilometers range,” Opt. Express, vol. 25,
no. 10, pp. 11919–11931, 2017.
[62] X. Liu, S. Bauer, and A. Velten, “Phasor ﬁeld diffrac-
tion based reconstruction for fast non-line-of-sight
imaging systems,” Nat. Commun., vol. 11, no. 1645,
2020.
[63] D. L. Snyder and M. I. Miller, Random Point Pro-
cesses in Time and Space. Springer New York, 2012.
[64] J. Ville, “Etude critique de la notion de collectif,” Bull.
Am. Math. Soc., vol. 45, no. 11, p. 824, 1939.
[65] L. L. Scharf and C. Demeure, Statistical Signal Pro-
cessing: Detection, Estimation, and Time Series Anal-
ysis. Prentice Hall, 1991.
[66] A. Velten, D. Wu, A. Jarabo, B. Masia, C. Barsi,
C. Joshi, E. Lawson, M. Bawendi, D. Gutierrez, and
R. Raskar, “Femto-photography: Capturing and visu-
alizing the propagation of light,” ACM Trans. Graph.
(SIGGRAPH), vol. 32, no. 4, pp. 1–8, 2013.
[67] P. Sen,
B. Chen,
G. Garg,
S. R. Marschner,
M. Horowitz, M. Levoy, and H. P. A. Lensch, “Dual
photography,” ACM Trans. Graph. (SIGGRAPH),
vol. 24, no. 3, p. 745–755, 2005.
[68] A. H. Barnett, J. Magland, and L. A. Klinteberg,
“A parallel nonuniform fast Fourier transform library
based on an "exponential of semicircle" kernel,” SIAM
J. Sci. Comput., vol. 41, no. 5, pp. C479–C504, 2019.
8146
