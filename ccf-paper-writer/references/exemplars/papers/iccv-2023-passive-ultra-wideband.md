# Passive Ultra-Wideband Single-Photon Imaging


> **Venue:** ICCV2023

> **Source:** <https://openaccess.thecvf.com/content/ICCV2023/html/Wei_Passive_Ultra-Wideband_Single-Photon_Imaging_ICCV_2023_paper.html>


--- Mian Wei1* Sotiris Nousias1* Rahul Gulve2 David B. Lindell1 Kiriakos N. Kutulakos1 1Dept. of Computer Science, University of Toronto 2Dept. of Electrical and Computer Engineering, University of Toronto


## Abstract


We consider the problem of imaging a dynamic scene over an extreme range of timescales simultaneouslyseconds to picosecondsand doing so passively, without much light, and without any timing signals from the light source(s) emitting it. Because existing ﬂux estimation techniques for single-photon cameras break down in this regime, we develop a ﬂux probing theory that draws insights from stochas-

tic calculus to enable reconstruction of a pixels timevarying ﬂux from a stream of monotonically-increasing

photon detection timestamps.

We use this theory to (1) show that passive free-running SPAD cameras have an attainable frequency bandwidth that spans the entire DC-to-

31 GHz range in low-ﬂux conditions, (2) derive a novel Fourier-domain ﬂux reconstruction algorithm that scans this range for frequencies with statistically-signiﬁcant support in the timestamp data, and (3) ensure the algorithms noise model remains valid even for very low photon counts or non-negligible dead times. We show the potential of this asynchronous imaging regime by experimentally demonstrating several never-seen-before abilities: (1) imaging a

scene illuminated simultaneously by sources operating at vastly different speeds without synchronization (bulbs, projectors, multiple pulsed lasers), (2) passive non-line-of-

sight video acquisition, and (3) recording ultra-wideband video, which can be played back later at 30 Hz to show everyday motionsbut can also be played a billion times slower to show the propagation of light itself.

1. Introduction A basic rule of thumb in high-speed imaging is that speed needs light: the faster a scene changes, the more light we need to image it accurately without excessive noise or motion blur. Over the decades, high-speed light sources [1],

fast cameras [24], and depth sensors [5, 6] have made it possible to image dynamic phenomena occurring in eversmaller time intervals with the help of actively-controlled

light sources and synchronization: to collect enough light, * Joint ﬁrst authors: {mianwei,sotiris}@cs.toronto.edu Project website: https://compimaging.dgp.toronto.edu/ultra-wideband the same picosecond- or nanosecond-scale event may be imaged millions of times by operating a camera and a source

in lockstep, at MHz repetition rates or more.

Acquiring videos of ultrafast phenomena this wayfrom imaging light in ﬂight [7] to fast biological processes [8] is now quite common.

Unfortunately, while these techniques do capture ultrafast events, they cannot simultane-

ously capture slower ones too: time wraps at the sync period, blurring out anything occurring over longer timespans.


But how do we image highly dynamic scenesboth slow and ultrafastpassively, without any light sources under our control, no synchronization, and not much light? Very little is known about this problem because existing models for passive low-light imaging [913] break down at

timescales much shorter than the timespan between photon arrivals. As a result, ultrafast imaging in low light has remained beyond the reach of passive methods.


In this work we seek to bridge these two regimes, active and passive, by revisiting the need for synchronization when imaging ultrafast scenes in low light. Working from ﬁrst principles, we develop a novel theory of passive singlephoton imaging that is speciﬁcally designed to eliminate

synchronization between a camera and the light sources in a scene. The only requirements are that (1) the cameras pixels can detect and time-stamp individual photons and (2) their dead-time period does not impair detection of photons from one source signiﬁcantly more than any other. In this imaging regime, each camera pixel time-stamps the photons it detects using an internal clock that follows the arrow of time, obviating the need for any external timing signals.

Our work is based on the observation that passive (syncfree) imaging is fundamentally more powerful than active

imaging in such settings.

Speciﬁcally, without the periodic timing signal from a light source, time never wraps

at a sync period; ultrafast scenes can be imaged for arbitrarily long timespans; and ﬂux variations that occur concur-

rently across 12 orders of magnitude in time (picoseconds to seconds)and that involve many unknown sourcescan be recorded with just one camera.

Because photon timestamps due to all light sources and all This ICCV paper is the Open Access version, provided by the Computer Vision Foundation.

Except for this watermark, it is identical to the accepted version; the final published version of the proceedings is available on IEEE Xplore.


flux (Mpps) flux (k photons per sec) flux (kpps) flux (Mpps) photons per second (pps) raster scan lightbulb
Figure 1: Passive ultra-wideband imaging with a single free-running SPAD pixel. Left bottom & Center: In a real, captured experiment, an unsynchronized single-photon avalanche diode (SPAD) passively records indirect light coming from multiple sources operating


asynchronously from each other (unsynchronized picosecond lasers, projectors, etc.). See Figure 5 (row 2, middle) for actual scene. The incident ﬂux exhibits simultaneous intensity variations with a bandwidth that spans roughly 9 orders of magnitude in frequency. Bottom right: Multiple concurrently-occurring phenomena in the ﬂux function can be identiﬁed after acquisition: video ﬂicker (58 Hz), the pulsewidth modulation of an LED light bulb (900 Hz), a movie projected onto a nearby wall by a raster-scanning laser projector (up to 5 MHz),

and two unsynchronized picosecond lasers (40 MHz10 GHz). Top right: By reconstructing the time-varying ﬂux function of the laser projector, video frames are reconstructed at 1280x720 resolution using roughly 450-4500 photons collected during each 1/58 s frame.

timescales are recorded concurrently, the choice of which timescale to show and which light source(s) to use for visual processing can be done after acquisition (Figure 1).


Thus, just like light ﬁeld cameras [14] enable post-capture refocusing in space, this new imaging regime enables postcapture refocusing in timefrom transient to everyday

timescales. We demonstrate this one-of-a-kind capability experimentally in Figure 5, where we use photon timestamp data captured by a free-running SPAD camera to play back video of a rapidly-spinning fan at both 1,000 and 250 billion frames per second. We call this novel regime passive

ultra-wideband imaging.

The key challenge in this regime is how to reconstruct ﬂux functions with a ultra-wide spectrum (DC to over 10 GHz) from a stream of photon timestamps that increase monotonically. To tackle it, we develop a ﬂux probing theory

that draws on results from stochastic calculus [15, 16] to relate the Fourier series decomposition of a time-varying ﬂux function to the timestamp realizations of an underlying stochastic process [17, 18]. The mathematical under-

pinnings of our approach are grounded in statistics [19 21] and time series analysis [2227], and similar methods have explored ﬂux function estimation in optical communications [2830].


Our work ties together several lines of prior research on extreme imaging, both passive and active. In passive settings,

several techniques have recently been proposed for estimating ﬂux from photon data [13, 3133]. These rely on a va-

riety of ﬂux constancy assumptions and, as a result, are not applicable to the ultra-wideband regime we consider. In active settings, single-photon imaging techniques have relied

exclusively on sync-relative timestamps [3438], where information about sub-MHz ﬂux variations has already been

lost.

Aside from single-photon imaging, active ultrafast imaging techniques have also used heterodyning to measure ﬂux at one speciﬁc modulation frequency [3943]. These techniques have neither the light efﬁciency nor the ultrawide bandwidth we demonstrate in this paper.


2. Passive Ultra-Wideband Imaging Passive, sync-less imaging.

We assume that the imaging system exerts no control over a scenes appearance: the

scenes light source(s) can be natural, artiﬁcial, or both, and their number, operating principle, and time-varying properties are unknown and unconstrained (Figure 1). Impor-

tantly, we assume that no electronic timing signals, such as triggers or sync pulses, are received from any of them.

The time-varying ﬂux function.

Following standard radiometric conventions [44], we express incident light at a

pixel as an unknown time-varying function ϕ(t) that represents the pixels instantaneous ﬂux at time t 0. Our goal is

to acquire a continuous representation of the ﬂux function over a possibly unbounded acquisition interval [0,t] (milliseconds, seconds or much longer). In the following we

assume that ϕ(t) is expressed in units of photons per second, is continuous, and has ﬁnite spectral support bounded

by frequencies fmin and fmax.

Ultra-wideband ﬂux.

We seek to reconstruct ﬂux functions that have ultra-wide bandwidth, i.e., whose fre-


quency content spans the entire range from constant ﬂux (fmin = 0 Hz) to extreme time-of-ﬂight timescales (fmax 10 GHz) [43, 45]. Moreover, we assume that no prior information is available about the spectrum of ϕ(t).


Photon arrival model.

Our work applies to the singlephoton imaging regime, where the timespan between con-

secutive photon arrivals is not negligible. In this setting, ϕ(t) is the rate function of an inhomogeneous Poisson process governing photon arrivals [29, 46]. The mean value

of ϕ(t) represents the average ﬂux received over the observation interval [0,t] in units of photons per second and its

inverse, denoted by Tavg, is the average timespan between consecutive photon arrivals [33].

Low-ﬂux photon detection model.

Modern SPADs can detect and time-stamp the arrival of individual photons with extremely high temporal precision (typically tens of picoseconds [3, 47]). SPADs are not perfect detectors, how-

ever, as they exhibit four main non-idealities: quantum efﬁciency, dead time, timestamp quantization and jitter. Quan-

tum efﬁciency refers to the pixels probability of actually detecting a photon when it is in its active state. This probability can be well below 1 depending on wavelength; since

it can be thought of as scaling the ﬂux function, we assume it is absorbed in ϕ(t). After a photon detection, SPADs are blind to subsequent photon arrivals for an interval known as the dead time. Dead time can skew photon detection statistics quite signiﬁcantly when photons arrive closely enough

in time to fall within a SPADs dead-time window with high probability [32, 48, 49]. For simplicity, we focus on lowﬂux imaging in the main paper, where consecutive arrivals

are spaced much farther apart than the SPADs dead time.1 In this case, detections are governed by the same stochastic process that describes photon arrivals [50], with rate function ϕ(t) and average timespan Tavg between detections.


Non-negligible dead time. When dead-time intervals become comparable to Tavg (or longer), photon detections are

not Poisson because the detection of a photon may impact the detection of subsequent ones. We show in supplementary Section C that our stochastic calculus framework cov-

ers this case as well, enabling acquisition of ϕ(t) by slightly amending the equations and algorithm in the main paper.

Timestamp model.

Photon timestamps are subject to quantization from the time-to-digital conversion process and jitter, i.e., instabilities in timing electronics. Both can be as low as a few picoseconds for SPADs in the visible range [51]. To simplify our analysis, we assume without loss of generality that timestamp resolution and timestamp accuracy are identical, so that the timestamps bin size Q accounts for jitter as well.2 1For example, Tavg was nearly six times our SPADs dead time in the


## Experiments


2When timestamp accuracy is worse than timestamp resolution, the The stream of absolute detection timestamps.

Since no external timing signal is available to serve as a reference, we assume that photon detection timestamps follow the arrow of time, increasing monotonically according to the SPADs internal clock.

This results in a stream of timestamps T = (τ1,...,τN(t)), where τi is the elapsed time from the beginning of acquisition until the i-th photon detection, and N(t) counts the total photons detected up to time t. We refer to timestamps τi as absolute timestamps.

Absolute timestamps can be acquired by operating SPAD pixels in their passive free-running mode [32].

Paper roadmap. The remainder of the main paper is aimed at readers with no background in stochastic calculus, as implementation of our ﬂux acquisition algorithms is straight-

forward and can be done without it. Readers may skip the formal deﬁnition of a martingale (supplement Section A) and focus on the comparisons in Section 2.1, the high-level description of our theoretical results in Section 3, and the algorithms in Section 4 (for low-ﬂux settings) and Section C.1

(for non-negligible dead time). For readers familiar with statistical estimation, Section D includes simpler proofs of Section 3s results, graciously provided by anonymous reviewer R1, which do not invoke stochastic calculus but ap-

ply only to low-ﬂux settings where dead time is negligible.

2.1. Imaging with Photon Timestamps The particular imaging regime outlined above generalizes two broad classes of single-photon imaging research, both of which use photon timestamps as their main input. We distinguish between the two by considering the relation between (a) the rate of photon detections and (b) the maximum reconstructible frequency in each case (Table 1).

Passive inter-photon imaging.

Recent work in passive single-photon imaging has proposed treating the timespan between consecutive detections as a noisy sample of the scenes ﬂux [32, 33]. This implicitly assumes that ﬂux does not vary in that timespan, which makes the rate of photon detections a (loose) upper bound on fmax. As a result, passive low-ﬂux imaging with SPADs has so far been restricted

to slow speeds, with fmax on the order of tens of kHz [13].

Active histogram-based imaging.

Approaches that employ synchronized light sources [50, 56] occupy the other extreme of the frequency range. Their basic principle is to time-stamp detections relative to a sync signal of a known frequency fsync, so that all timestamps wrap to the same brief interval [0,1/ fsync] regardless of the actual timespan between them. This forces photons to accumulate in a relatively small number of time binstypically a few timestamps effective number of bits is reduced [52]. Our systems timestamps, for example, are quantized to 4 picoseconds but the standard de-

viation of jitter is 16 picoseconds, so we conservatively use Q = 16 for performance modeling purposes. Explicit treatment of jitter is beyond this papers scope (e.g., jitter can actually improve timing resolution [5355]).


imaging regime passive inter-photon imaging active histogram-based imaging passive ultra-wideband imaging (interdetection-limited) (sync- and quantization-limited) (quantization-limited only) fmax < 1/Tavg fmin fsync, fmax 1/(2Q) fmax 1/(2Q) light source(s) one or more sources, no sync one source only, periodic with period 1/ fsync, sync required one or more sources, no sync typical freq. range low Hz to tens of kHz (plus DC) low MHz to well above 10 GHz (plus DC) DC to well above 10 GHz valid frequencies all frequencies in range all frequencies in ϕ(t) must be integer multiples of fsync all frequencies in range corrupting ﬂux any ﬂux with frequencies > 1/Tavg any ﬂux with frequencies that are not integer multiples of fsync frequencies > 31 GHz input data stream of absolute timestamps stream of sync-relative timestamps stream of absolute timestamps
# distinct time bins

not applicable thousands (typical) billions to trillions (increases with t)
# photons per bin

not applicable a non-negative integer; Poisson-distributed, mean proportional to ⌊t fsync⌋ 0 or 1, vast majority of bins have 0 ϕ1(t) = 5+5sin(2πt) ϕ2(t) = 5+5sin(762πt) ϕ3(t) = 5+5sin(582πt) ϕ4(t) = ϕ1(t)+ϕ2(t)+ϕ3(t) illustration of ﬂux, detections & sync in each regime elapsed time t (sec) detections due to ϕ1 no sync (0 Hz) elapsed time t (sec) detections due to ϕ2 sync (7 Hz) elapsed time t (sec) detections due to ϕ3 sync (5 Hz) elapsed time t (sec) detections due to ϕ4 no sync (0 Hz) measurement model of each regime estimated ﬂux inter-photon ﬂux elapsed time t (sec) ﬂux photon-count histograms 7 Hz 5 Hz corruptions ϕ1,ϕ3 ϕ2 photons photon-count histograms 7 Hz 5 Hz corruptions ϕ1,ϕ2 ϕ3 photons 0 Hz 1 Hz 40 Hz 42 Hz detection threshold frequency (Hz) amplitude frequency spectrum
Table 1: Low-ﬂux imaging with photon timestamps. Left column: Passive imaging has so far assumed that photons can be detected at a

rate (much) greater than the highest ﬂux frequency. Middle column: Active techniques are designed to handle the opposite case, where photon detections occur at a rate (much) lower than the ﬂux functions frequencies. If a light sources frequency is not a multiple of fsync (e.g., 5 Hz for ϕ2 photons and 7 Hz for ϕ3 photons in third row above), its photons will land in the wrong time bin. This contributes to noise instead of signal, i.e., the histogram will be ﬂattened (compare the two red and two green histograms, respectively, in third row).

Moreover, even when fsync is well-matched to one light source, other sources emitting at non-multiples of fsync will corrupt the histogram (third row, gray histograms). Please refer to the supplementary video for another illustration of these effects. Right column: Our approach inherits the most important features of both regimes, without their limitations.

thousandand yields a photon-count histogram [57] that is a noisy sampling of the scaled and time-wrapped ﬂux function, ⌊t fsync⌋ϕ(t −⌊t fsync⌋/ fsync).

The maximum reconstructible frequency in this case is governed by the Nyquist theorem, not the photon interdetection time: a bin size of 16 picoseconds, for example, theoretically enables ﬂux acquisition with fmax equal to 31.25 GHz.3 Although this general approach achieves extremely high imaging speeds [12], its reliance on relative timestamps comes with a major constraint: the incident ﬂux must also be a periodic function with a period equal to 1/ fsync, to ensure that ϕ(t) and its time-wrapped counterpart are identi-

cal. This can be trivially satisﬁed when the only light in the scene comes from a precisely-synchronized source (a pulsed laser, light-emitting diode, etc.), but ﬂux variations due to other causes cannot be reconstructed. This includes variations caused by scene motion; light sources that emit at frequencies lower than fsync; and sources that emit at higher frequencies that are not integer multiples of fsync. Photons from such sources result in histogram artifacts in the form 3As a reference, 31.25 GHz is the −3 dB cut-off frequency of a Gaussian pulse with a full-width-at-half-max of 36 picoseconds.


of additional photon noise [58], beat signals [45], or both.

Role of the sync frequency fsync.

Sync frequencies are typically in the low-MHz range in single-photon imaging applications that involve pulsed sources [35, 50, 59,

60]. This choice balances improved signal-to-noise ratio (a faster sync means more laser pulses, more photons detected in each histogram bin, and fewer time bins for them to accumulate in) against the likelihood of photons being missed

due to dead time [48, 49, 58], or photons arriving too late because time has wrapped already [12, 61]. At such MHz sync frequencies, the memory and compute cost of reconstructing histograms from timestamps can be signiﬁcant,

prompting several recent schemes for just-in-time processing of (sync-relative) photon timestamps [37, 38, 62].


The passive ultra-wideband imaging regime. Intuitively, the regime we tackle in this paper can be understood as the limit case of photon histogramming, where the sync frequency is reduced all the way to zero. Speciﬁcally, as fsync decreases, the interval [0,1/ fsync] increases; more histogram bins are needed to span it; fewer photons land into

each bin; the time-wrapped ﬂux function is able to represent variations that take place over longer timespans; and the space of reconstructible frequencies (i.e., the integer mul-

martingale M(t) elapsed time t elapsed time t ﬂux ϕ(t) = 4+4sin(80πt) Nyquist rate 1/2 fmax average interdetection time photon stream T counting process N(t) ﬂux integral R t 0 ϕ(u)du photons / sec total photons detected
Figure 2:

Relation between the stream of absolute timestamps, the counting process, the ﬂux function and its integral. Timestamps are from a computational simulation of the inhomogeneous

Poisson process with the ﬂux function ϕ(t) indicated above.

tiples of fsync) expands. In the limit when fsync is exactly zero, there is no sync at all, timestamps become absolute and every photon lands into its own unique time bin. Crucially, all frequencies from DC up to the Nyquist limitand

from any light sourcebecome potentially reconstructible.

Mathematical modeling of this limit case, however, is nontrivial because the concept of a histogram breaks down:

photons never accumulate, and the contents0 or 1of any given bin provide almost no information about the ﬂux function.4 On the computational side, the entire acquisition interval [0,t] is effectively partitioned into time bins at the SPADs timing resolution, so acquisitions of a second or more can potentially involve trillions of time bins (most of which are empty). Fortunately, as we show in the next section, both these challenges can be overcome by formulating

ﬂux reconstruction in terms of the photon counting process, which is not degenerate even when fsync = 0.

3. Probing Flux Functions Our approach establishes a direct mathematical link between (1) the stream of absolute timestamps detected at a

pixelhowever few or far apart they may beand (2) the ﬂux function that produced them. This link allows us to probe the Fourier spectrum of an unknown ﬂux function across the entire DC-to-GHz range for frequencies that have statistically-signiﬁcant support in the timestamp data. We introduce our ﬂux probing theory below and address ﬂux reconstruction in Section 4. For the sake of generality, we consider timestamps to be continuous-valued random variables and model quantization as part of our theory.


4More formally, the Poisson-distributed random variable associated with any given time bin has a mean that goes to zero as t [63].

The photon counting process. Even though a single absolute timestamp provides (almost) no information about the

underlying ﬂux function, the stream of absolute timestamps as a whole contains considerable information about it. The speciﬁc relation between the two comes from stochastic calculus [15].


Speciﬁcally, in the continuous-time domain, a stream T of real-valued absolute timestamps provides a noisy reconstruction of the integral of ϕ(t) (Figure 2): N(t) | {z } counting process Z t 0 ϕ(u)du ﬂux integral up to time t M(t) | {z } martingale noise (1) The function N(t) in Eq. (1) counts the photons received up to time t and is completely determined by T ; formally, it is a counting process [15, 19]. Viewed from the perspective of histogram-based single-photon imaging (Table 1, middle), N(t) is the continuous-time analog of the cumulative

photon-counthistogram over the interval [0,t], for fsync = 0.

The function M(t) in Eq. (1) is a continuous-time random process called a martingale [64] that can be thought of as a form of additive zero-mean noise.5 As can be seen from the example of Figure 2, a single random realization of the counting process (cyan curve) is a

highly discontinuous function that, on ﬁrst inspection, bears no resemblance to the ﬂux integral it is supposed to approximate in Eq. (1). These discontinuities introduce dense, spu-

rious frequencies in the Fourier-domain representation of N(t) that do not exist in the actual ﬂux integral.

3.1. Theory of Flux Probing Our theoretical results use tools from stochastic calculus to address two basic questions. First, what is the highest possible frequency fmax that can be recovered by a passive single-photon imaging system that outputs quantized absolute timestamps? Second, for frequencies within the attain-

able bandwidth, how can we derive a noise model that allows spurious frequencies to be efﬁciently detected and dis-

carded, and the accuracy of real frequencies to be quantiﬁed as a function of the acquired timestamp stream? We summarize these results below and defer proofs to Section B.


The probing operation.

Proposition 1 tells us that we can always probe the ﬂux function to recover a (noisy) measurement of its inner product with practically any other function. Moreover, probing is efﬁcient to compute from the timestamp stream and can be thought of as a continuous-time and sync-free generalization of compressive acquisition schemes for conventional photon-counting

histograms [37, 38, 62]. In particular, let T be the stream of real-valued absolute timestamps up to time t and let p(t) be 5One example of a martingale is an unbiased random walk. Like N(t) in Eq. (1), many other increasing stochastic processes can be expressed as the sum of a deterministic increasing function and a martingale [15]. See supplement Section A for the formal deﬁnition of a martingale.


an arbitrary known and square-integrable function: Proposition 1 (Flux Probing Equation). The inner product of the probing function p(t) and the unknown ﬂux function ϕ(t) over the time interval [0,t] satisﬁes the relation p(T ) = ⟨p,ϕ⟩+ Mp(t) (2) where p(T ) are probing measurements which sum the values of the probing function at the absolute timestamps p(T ) def = ∑ p(τ) , (3) Mp(t) is a martingale, and the inner product is deﬁned as R t 0 p(u)ϕ(u)du.

Fundamental limit on bandwidth. In the special case of probing with the Fourier basis functions p f (t) = e−j2π ft, we prove in supplement Section B that probing with f > 1/2Q yields aliased measurements that wrap around the frequency spectrum and are identical toand indistinguish-

able fromlower-frequency measurements: Proposition 2. Given timing resolution Q, the maximum recoverable frequency is fmax = 2Q.

Intuitively, Proposition 2 says that ﬂux frequencies above 1/2Q are unrecoverable regardless of whether we detect a few photons or a million.

Noise model. Our model accounts for the inhomogeneous Poisson nature of photon detections and treats the general case of real-valued timestamps. The model is valid for arbitrary ﬂux levels within the low-ﬂux regime and, as we show

in supplement Section G.4, it remains valid for low-count acquisitions (e.g., as few as ten photons). More speciﬁcally, Proposition 3 tells us that the noise in probing mea-

surements has a distribution that can be estimated from the timestamp stream through another probing operation. Thus, probing gives the means both to observe a ﬂux function and to quantify the uncertainty of that observation: Proposition 3 (Distribution of Probing Measurements).

The probing measurements p(T ) are approximately normally distributed with mean ⟨p,ϕ⟩and variance ⟨p2,ϕ⟩.


Fourier probing noise. Finally, Corollaries 1 and 2 allow us to quantify the accuracy by which speciﬁc ﬂux frequencies can be estimated from a given timestamp stream:

Corollary 1 (Distribution of Fourier Probing). The Fourier probing measurements p f (T ) approximately follow a complex normal distribution with mean and covariance matrix

µ = ⟨cos(2π ft), ϕ(t) ⟩ ⟨−sin(2π ft), ϕ(t) ⟩ (4) Σ = ⟨cos2(2π ft),ϕ(t)⟩ ⟨sin2(2π ft),ϕ(t)⟩ (5) Corollary 2 (Distribution of Fourier Probing Energy). The normalized energy of the Fourier basis probing measurements

f (T ) def  p f (T ) pΣ1,1 + Im  p f (T ) pΣ2,2 (6) follows a non-central χ2 distribution with 2 degrees of freedom and non-centrality parameter µ2

1/Σ1,1 + µ2 2/Σ2,2.

In supplement Section B we show that unbiased estimators of the parameters of the above distributions can be obtained via probing.

Frequency detection. Given the estimated distribution of the Fourier Probing Energy, we derive the constant false alarm rate (CFAR) detector [65] (see supplement Section B) to identify and remove noisy frequencies based on a desired probability of false alarm . False alarms occur when we keep f and E[|p f (T )|] = 0; we remove f if pE f (T ) is lower than CDF−1 χ2 (1−), derived from Corollary 2. Speciﬁcally, we detect frequencies for which |p f (T )|2 CDF−1 χ2 (1 −)N(t) (7) Note that (1) for a ﬁxed , the probability of detecting a frequency is proportional to the total number of photons detected, and (2) for ﬂux functions dominated by a particular

frequency such that |p fi(T )|2 is large, N(t) also tends to become proportionally larger, reducing the probability of detecting other frequencies.

Implications for passive single-photon imaging. Proposition 2 implies that rather than being a hindrance, sync-

less imaging with absolute timestamps confers an extreme bandwidth advantage to SPAD cameras: systems with 16picosecond resolution, such as our own, can simultane-

ously acquire ﬂux variations that span the entire DC-to- 31 GHz range of frequencies, and that are due to any number of unknown light sources operating independently. This

bandwidth is orders of magnitude broader than intensity camerasSPADs or otherwisewere thought capable of acquiring directly [4143, 45], i.e., without resorting to homodyne [43] or heterodyne [41, 42, 45] detection schemes.


While Proposition 2 describes reconstructability (i.e., frequencies above the limit are unreconstructible), Proposi-

tion 3 and Eq. (7) provide insights about the accuracy and detectability of ﬂux variations at different frequencies.

Lastly, although we have not veriﬁed the theorized DCto-31 GHz bandwidth experimentally due to unavailability

of lasers that are fast enough, we show several real-world demonstrations of simultaneous DC-to-16.9 GHz imaging under very challenging low-ﬂux conditions (see Figure 1, Section 5, and Section E). These validate our noise models in Eqs. (4)-(6) and (partially) conﬁrm our theoretical bound.


procedure FLUXREC(T , t, fmax, ) // Frequency scanning.

∆f = 0.6/t (see supp. Section B) F = freqs from 0 to fmax with step ∆f loop f ∈F pf (T ) = (1/t)∑τ∈T e−j2π fτ // Frequency detection.

Fused = /0 loop f ∈F Af = |pf (T )|, φf = ∠pf (T ) reject f using CFAR (Eq.(7)) Fused = Fused ∪{f} if not rejected // Flux reconstruction.

ˆϕ(t) = ∑f∈Fused Af cos(2π ft +φf ) measured ground truth std. dev.

Timestamps estimated ground truth detected frequencies Frequency Scanning Flux Function & Timestamps Flux Reconstruction Frequency Detection Flux function & Timestamps Frequency Scanning Frequency Detection Flux Reconstruction probability of false alarm CFAR threshold measured threshold ϕ(t) = ∑f ∈F A f cos(2π ft +φf ) pf (T ) = (1/t)∑τ∈T e−j2π f τ ˆϕ(t) = ∑f ∈Fused A f cos(2π ft +φf )
Figure 3: Overview of imaging by ﬂux probing. Left: Flux reconstruction algorithm used in our experiments. Right: Visual illustration

of the algorithm. Flux function: A ﬂux function of ﬁnite spectral support can be expressed as a sum of sinusoids and produces a stream of absolute timestamps. Frequency scanning: We probe the ﬂux function using a Fourier basis and measure the response at each frequency.

Frequency detection: For each of the probed frequencies, we detect whether it contributes to the ﬂux function if its corresponding amplitude is greater than a threshold (top) which is selected to achieve the desired probability of false alarm. (bottom). Flux reconstruction: Finally, we reconstruct a continuous-time ﬂux function from the amplitudes and phases of detected frequencies.

4. Imaging by Flux Probing Our probing theory leads directly to an algorithm that reconstructs the Fourier transform of the ﬂux function by

frequency-scanning the entire DC-to-GHz bandwidth (Figure 3).


This algorithm is similar to the Fourier-domain histogramming technique used in conventional active settings [62], but also differs in two key respects: (1) it pro-

vides a principled way to estimate frequency uncertainty in an acquired timestamp stream, and (2) it enables tractable operation in a regime involving potentially billions of candidate frequenciese.g., a 1 Hz-resolution scan of DC-to-

20 GHzby rejecting spurious frequencies and reducing storage requirements. The frequency detection step uses the CFAR detector of Section 3, where we set so that the expected number of false alarms is less than 1. Figure 3 includes a visual depiction of the ﬂux reconstruction algorithm, along with a complete description in pseudocode.


5. Experiments We validate our theory experimentally with (1) passive ultra-wideband sensing of both 1D intensity signals and 2D video signals ranging from DC to 16.9 GHz, (2) passive non-line-of-sight (NLOS) video via MHz-rate ﬂux function reconstruction, (3) generalization to 2D SPAD arrays

for high speed video, and (4) simulation-based quantitative


## Evaluation


mental video and to supplement Sections E, F, and G for more experiments and implementation details.

Passive ultra-wideband sensing. We demonstrate recovering signals with frequencies spanning roughly 9 orders

of magnitude from DC to 10 GHz (Figure 1). We place a single-pixel SPAD in the scene to capture ﬂux variations from (1) pulse-width modulation of a light bulb (900 Hz), (2) backscattered light from a raster-scanning laser projector (60 Hz10 MHz), and (3) two unsynchronized picosec-

ond lasers (40 MHz10 GHz). Remarkably, the ﬂux function is reconstructed from only 77,000 photon timestamps.6

We recover time-varying ﬂux across billions of frequencies from this minuscule set of photons. Moreover, by employing a brighter and faster laser, we achieve passive DC-to-

16.9 GHz sensing over room-size distances (Section E.2.2).

We also demonstrate ultra-wideband video (Figure 5, top) by raster scanning a scene in which a pulsed laser, with 20 MHz repetition and 80 ps FWHM, is diffused to illuminate a fan spinning at 54 Hz.


We detect frequencies from DC to 10 GHz and render ﬂux functions at 1 kfps and 250 Gfps, showing both the fan blades rotating and the propagation of the laser pulse.

In contrast, conventional approaches reconstruct the scene at only one of the

aforementioned frame rates, temporally blurring either slow or fast events.

Furthermore, our method can render the ﬂux at whatever timescale, essentially freezing time at all timescales. Note that because we only had access to a single pixel SPAD, the timestamps were collected by scanning

across the ﬁeld of view of the SPAD. To temporally align the ﬂux functions between pixels, we use synchronization signals from both the laser and the fan. We emphasize that no synchronization signals were used to reconstruct the ﬂux functions themselveswe are demonstrating a new capability of reconstructing the appearance of the scene as it ap-

peared during each laser pulsethis is distinct from the use of synchronization and histogramming to estimate the average appearance of the ﬂux function over time [7, 12, 66].


We also emphasize that the images are rendered by integrating the ﬂux function over the exposure of each frame. As

6Conventional camera pixels collect a few thousand photons to return a single estimate of light intensity.


Figure 4: Simulation-based comparisons. Left to right: Laser pulse reconstructed by three methods from 2000 timestamps produced by

a 20 MHz pulse train. Reconstruction from a 20 MHz train of much shorter pulses, using just 50 timestamps. Pulse reconstruction error as a function of the number of timestamps given as input. Reconstructed pulses from 100 realizations of a ﬁfty-photon timestamp stream.

such, these images exhibit not only high dynamic range but their intensities are also expressed in physical units of photons, thereby ensuring radiometric calibration by nature.


We show another video example in Figure 5 (row 2), where the same picosecond laser illuminates a Coca-Cola bottle ﬁlled with water and a small amount of milk to scatter the light. Within the same scene, a compact ﬂuorescent lightbulb (CFL) ﬂickers at 120 Hz. We render videos at 10 kfps

and 200 Gfps to visualize the CFL ﬂicker and light pulses propagating through the bottle (Figure 5, rows 34). For the same reasons outlined in the previous paragraph, we use synchronization signals from the laser and the bulb.

Recovering passive NLOS videos. We demonstrate passive NLOS video reconstruction using light measured indi-

rectly from a raster-scanning laser projector (see illustration in Figure 1 and photo in Figure 5, row 2). The SPAD observes a single point on a diffuse box during the projector

beams raster scan, collecting light that bounced twice (i.e., diffuserdiffuse boxSPAD). This conﬁguration is analogous to dual photography [67]. By reconstructing the 1D

ﬂux function over a one-second span, we recover the video being played. We show results for the multi-illumination setting of Figure 1 and for a projector-only setting. In the latter case, we recover ﬁne details of each video frame (Figure 5, rows 56) even though only 3000 photons were col-

lected on average during a frames 1/58 s raster scan.

Probing with SPAD arrays.

Our method can be applied off the shelf to data from 2D SPAD sensors. To demonstrate this, we compare to Seets et al. [13] who recover high-

speed video with a 3232 SPAD array. They assume ﬂux is piecewise constant and identify contiguous sets of timestamps with the same ﬂux. Photon inter-arrivals are then av-

eraged to obtain a single ﬂux estimate per set (Figure 5, bottom right). In contrast, we recover a time-varying ﬂux function by probing (Figure 5, bottom left). Because the sensor outputs just one timestamp per 20 microseconds for each pixela dead time too long to ignore even at relatively low ﬂux levelswe probe using the generalized algorithm of Section C.1. This yields a periodic ﬂux function truer to the rotating fans motion, whereas periodicity and highfrequency variations are lost by the method in [13].


Simulations.

Lastly, we consider reconstruction of a ﬂux function corresponding to 20 MHz pulse trains from an ultrafast laser with frequency support of 12.5 GHz and 125 GHz, respectively, i.e., up to the theoretically-attainable limit of a jitter-less SPAD with 4 ps timestamp quantization (Proposition 2). Figure 4 compares the result of three methods: (1) conventional photon-count histogramming which

requires synchronization, (2) our sync-less reconstruction algorithm in Figure 3, and (3) oracle-based ﬂux probing, which probes the ground-truth set of frequencies instead of relying on frequency scanning. As can be seen, probing can recover pulses up to the theoretical limit from just 50 timestamps and, despite being passive, outperforms histogram-

ming considerably as photon counts increase. Please see Section G for a more detailed quantitative evaluation.

6. Concluding Remarks The sheer amount of data involved in probing timestamp streams cannot be ignored: even a single pixel can output tens of thousands of timestamps per second in low light, and our ultrawide-bandwidth results require probing billions of frequencies. Sketching [38] and Non-Uniform FFT [68] may offer ways forward but major challenges remain. That said, we believe that passive acquisition and processing of timestamp streams from free-running SPADs opens new directions in dynamic imaging: completely unsynchronized,

single-shot observations of ultrafast phenomena with multiple light sources across different timescales; passive depth

imaging using uncooperative, environmental light sources; compressive ultrafast video recording from sparse timestamps; temporal microscopes that allow monitoring in-

tensity ﬂuctuations across timescales spanning the nine-plus orders of magnitude (i.e., DC to 31 GHz) theoretically captured by SPADs; and more. We are thus looking forward to

more advances on these remarkable sensors.

Acknowledgements We thank the anonymous reviewers, and R1 in particular, for their invaluable comments and suggestions. We also thank Louis Zhang for creating an inter-

active tool for visualizing and sampling ﬂux integrals efﬁciently using OpenCL, and John Hancock for conﬁguring

the servers used in our experiments. Lastly, KNK and DBL gratefully acknowledge the support of NSERC under the RGPIN and RTI programs.


flux rendered at 1 kfps AC-powered fluorescent bulb (120 Hz flicker rate) picosecond laser pointing at bottle (20 MHz pulse rate) raster-scanning path of projectors laser beam passive ultra-wideband video acquisition (DC to 10 GHz) reconstructed per-pixel flux (rendered at two timescales) 10,000 fps video 200 billion fps video passive ultrafast single-pixel imaging & NLOS video bulb too dim at this timescale, pulse propagation visible bulb blinking, light on bottle appears constant reconstructed flux function (4 pixels & 2 timescales shown) 100 milliseconds 5000 picoseconds t = 3915 ps after reaching C, pulses bounce back to D t = 4610 ps t = 0.9 ms 2699 photons t = 2.800 s 3175 photons t = 3.477 s t = 0.374 s t = 1.562 s projected (ground truth) reconstructed passive NLOS video acquisition comparison to related work on SPAD arrays change point flux for pixel X this work Seets et al. 2021 7 milliseconds reconstructed flux function for pixel 7 milliseconds flux rendered at 250 Gfps conventional transient video flux rendered at 250 Gfps t = 3.33 ms + 4.408 ns = 4 ps = 1 ms t = 3.33 ms = 4 ps t = 3.33 ms + 4.472 ns = 4 ps t = 3.33 ms + 4.472 ns lasers laser video projector diffuser diffusers SPAD line of sight ceiling bulb reflection 2995 photons 3567 photons
Figure 5: Passive ultra-wideband imaging experiments. Row 1: Simultaneous recovery of spinning fan and light propagation (see text

for experiment setup). Rendering the ﬂux function at 1 kfps reveals motion of the fan (yellow arrow), but light propagation is invisible; at 250 Gfps light propagation is visible, and the fan freezes. Conventional histogramming (right) synced to the laser fails to recover the (unsynced) fan rotation. Row 2: Experimental setup for ultra-wideband video acquisition (left) and NLOS video imaging in a scene with multiple light sources (right). Rows 34: Flux function images at two timescales (left, bottom right) and for different points in the scene illuminated by a pulsed laser and ﬂickering light bulb (top right). The three peaks at B, C, and D correspond to a light pulse entering the bottle (B) propagating to the cap (C), and reﬂecting back (D). Rows 56: Passive NLOS acquisition using a raster-scanning laser projector with ground truth and reconstructed frames. Rows 78: We use SPAD array data from Seets et al. [13] to reconstruct per-pixel ﬂux (left).

The common assumption of piecewise constant ﬂux (right) does not hold even for this simple scene of a rotating fan.


References [1] C. Rullière, Femtosecond Laser Pulses. Springer New York, 2005.

[2] D. J. Bradley, B. Liddy, and W. E. Sleat, Direct linear measurement of ultrashort light pulses with a pi-

cosecond streak camera, Opt. Commun., vol. 2, no. 8, pp. 391395, 1971.

[3] F. Zappa, S. Tisa, A. Tosi, and S. Cova, Principles and features of single-photon avalanche diode arrays, Sens. Actuators A: Phys., vol. 140, no. 1, pp. 103112, [4] L. Gao, J. Liang, C. Li, and L. V. Wang, Single-shot compressed ultrafast photography at one hundred billion frames per second, Nature, vol. 516, no. 7529,

pp. 7477, 2014.

[5] C. Niclass, A. Rochas, P.-A. Besse, and E. Charbon, Design and characterization of a CMOS 3-D image sensor based on single photon avalanche diodes,

IEEE J. Solid-State Circuits, vol. 40, no. 9, pp. 1847 [6] R. Schwarte, Z. Xu, H.-G. Heinol, J. Olk, R. Klein, B. Buxbaum, H. Fischer, and J. Schulte, New electrooptical mixing and correlating sensor: Facilities and

applications of the photonic mixer device (PMD), in Proc. SPIE, vol. 3100, pp. 245253, 1997.

[7] G. Gariepy, N. Krstaji´c, R. Henderson, C. Li, R. R. Thomson, G. S. Buller, B. Heshmat, R. Raskar, J. Leach, and D. Faccio, Single-photon sensitive light-in-ﬁght imaging, Nat. Commun., vol. 6,

no. 6021, 2015.

[8] W. Becker, Fluorescence lifetime imaging techniques and applications, J. Microsc., vol. 247, no. 2, pp. 119136, 2012.

[9] E. R. Fossum, J. Ma, S. Masoodian, L. Anzagira, and R. Zizza, The quanta image sensor: Every photon counts, Sensors, vol. 16, no. 8, 2016.

[10] K. Morimoto, A. Ardelean, M.-L. Wu, A. C. Ulku, I. M. Antolovic, C. Bruschini, and E. Charbon, Megapixel time-gated SPAD image sensor for 2D and 3D imaging applications, Optica, vol. 7, no. 4, pp. 346354, 2020.

[11] Y. Chi, A. Gnanasambandam, V. Koltun, and S. H. Chan, Dynamic low-light imaging with quanta image sensors, in Proc. Eur. Conf. on Computer Vision

(ECCV), pp. 122138, Springer, 2020.

[12] M. OToole, F. Heide, D. B. Lindell, K. Zang, S. Diamond, and G. Wetzstein, Reconstructing transient images from single-photon sensors, in Proc.


IEEE/CVF Conf. on Computer Vision and Pattern Recognition (CVPR), pp. 15391547, 2017.

[13] T. Seets, A. Ingle, M. Laurenzis, and A. Velten, Motion adaptive deblurring with single-photon cameras,

in Proc. IEEE/CVF Winter Conf. on Applications of Computer Vision (WACV), pp. 19441953, 2021.

[14] R. Ng, M. Levoy, M. Brédif, G. Duval, M. Horowitz, and P. Hanrahan, Light ﬁeld photography with a hand-held plenoptic camera, Technical Report, 2005.

[15] J. L. Doob, Stochastic Processes. Wiley New York, [16] S. N. Cohen and R. J. Elliott, Stochastic Calculus and Applications, vol. 2. Birkhäuser New York, 2015.

[17] N. Chen, D. K. K. Lee, and S. N. Negahban, Superresolution estimation of cyclic arrival rates, Ann.

Stat., vol. 47, no. 3, pp. 17541775, 2019.

[18] K.-S. Lii and M. Rosenblatt, Estimation for almost periodic processes, Ann. Stat., vol. 34, no. 3,

pp. 11151139, 2006.

[19] M. S. Bartlett, The spectral analysis of point processes, J. R. Stat. Soc., B: Stat. Methodol., vol. 25,

no. 2, pp. 264296, 1963.

[20] D. Vere-Jones, On the estimation of frequency in point-process data, J. Appl. Probab., vol. 19, pp. 383 [21] Á. Gajardo and H.-G. Müller, Cox point process regression, IEEE Trans. Inf. Theory, vol. 68, no. 2,

pp. 11331156, 2022.

[22] M. S. Bartlett, Periodogram analysis and continuous spectra, Biometrika, vol. 37, no. 1/2, pp. 116, 1950.

[23] G. U. Yule, On a method of investigating periodicities in disturbed series, with special reference to

Wolfers sunspot numbers, Philos. Trans. R. Soc.

Lond., A, vol. 226, pp. 267298, 1927.

[24] M. G. Kendall, On the analysis of oscillatory timeseries, J. R. Stat. Soc., vol. 108, no. 1/2, pp. 93141,

[25] N. R. Lomb, Least-squares frequency analysis of unequally spaced data, Astrophys. Space Sci., vol. 39,

no. 2, pp. 447462, 1976.

[26] S. M. Ransom, S. S. Eikenberry, and J. Middleditch, Fourier techniques for very long astrophysical timeseries analysis, Astron. J., vol. 124, no. 3, pp. 1788

[27] J. T. VanderPlas, Understanding the LombScargle periodogram, Astrophys. J. Suppl. Ser., vol. 236, no. 1, pp. 128, 2018.


[28] O. Macchi and B. Picinbono, Estimation and detection of weak optical signals, IEEE Trans. Inf. Theory,

vol. 18, no. 5, pp. 562573, 1972.

[29] J. E. Mazo and J. Salz, On optical data communication via direct detection of light pulses, Bell Syst.

Tech. J., vol. 55, no. 3, pp. 347369, 1976.

[30] A. Komaee, Maximum likelihood and minimum mean squared error estimations for measurement of light intensity, in Proc. Conf. on Information Sciences and Systems (CISS), pp. 16, 2010.

[31] S. Ma, S. Gupta, A. C. Ulku, C. Bruschini, E. Charbon, and M. Gupta, Quanta burst photography, ACM

Trans. Graph. (SIGGRAPH), vol. 39, no. 4, pp. 116, [32] A. Ingle, A. Velten, and M. Gupta, High ﬂux passive imaging with single-photon sensors, in Proc.

IEEE/CVF Conf. on Computer Vision and Pattern Recognition (CVPR), pp. 67536762, 2019.

[33] A. Ingle, T. Seets, M. Buttafava, S. Gupta, A. Tosi, M. Gupta, and A. Velten, Passive inter-photon imaging, in Proc. IEEE/CVF Conf. on Computer Vi-

sion and Pattern Recognition (CVPR), pp. 85858595, [34] D. B. Lindell, M. OToole, and G. Wetzstein, Towards transient imaging at interactive rates with

single-photon detectors, in Proc. IEEE Int. Conf. on Computational Photography (ICCP), pp. 18, 2018.

[35] D. Shin, F. Xu, D. Venkatraman, R. Lussana, F. Villa, F. Zappa, V. K. Goyal, F. N. Wong, and J. H. Shapiro, Photon-efﬁcient imaging with a single-photon camera, Nat. Commun., vol. 7, no. 12046, 2016.


[36] Q. Sun, X. Dun, Y. Peng, and W. Heidrich, Depth and transient imaging with compressive SPAD array cameras, in Proc. IEEE/CVF Conf. on Computer Vision

and Pattern Recognition (CVPR), pp. 273282, 2018.

[37] F. Gutierrez-Barragan, A. Ingle, T. Seets, M. Gupta, and A. Velten, Compressive single-photon 3D cameras, in Proc. IEEE/CVF Conf. on Computer Vision

and Pattern Recognition (CVPR), pp. 1785417864, [38] M. P. Sheehan, J. Tachella, and M. E. Davies, A sketching framework for reduced data transfer in photon counting lidar, IEEE Trans. Comput. Imaging,

vol. 7, pp. 9891004, 2021.

[39] F. Heide, M. B. Hullin, J. Gregson, and W. Heidrich, Low-budget transient imaging using photonic mixer devices, ACM Trans. Graph. (SIGGRAPH), vol. 32, no. 4, pp. 110, 2013.

[40] F. Li, F. Willomitzer, M. M. Balaji, P. Rangarajan, and O. Cossairt, Exploiting wavelength diversity for high resolution time-of-ﬂight 3D imaging, IEEE Trans.

Pattern Anal. Machine Intell., vol. 43, no. 7, pp. 2193 [41] F. Li, F. Willomitzer, P. Rangarajan, M. Gupta, A. Velten, and O. Cossairt, SH-ToF: Micro resolution time-

of-ﬂight imaging with superheterodyne interferometry, in Proc. IEEE Int. Conf. on Computational Pho-

tography (ICCP), pp. 110, 2018.

[42] S.-H. Baek, N. Walsh, I. Chugunov, Z. Shi, and F. Heide, Centimeter-wave free-space neural timeof-ﬂight imaging, ACM Trans. Graph. (SIGGRAPH),

vol. 42, no. 1, pp. 118, 2022.

[43] M. Gupta, S. K. Nayar, M. B. Hullin, and J. Martin, Phasor imaging: A generalization of correlation-

based time-of-ﬂight imaging, ACM Trans. Graph.

(SIGGRAPH), vol. 34, no. 5, pp. 118, 2015.

[44] R. W. Boyd, Radiometry and the Detection of Optical Radiation. Wiley, 1983.

[45] A. Kadambi and R. Raskar, Rethinking machine vision time of ﬂight with GHz heterodyning, IEEE Ac-

cess, vol. 5, pp. 2621126223, 2017.

[46] S. M. Ross, Stochastic Processes. Wiley, 1983. [47] M. Itzler, Ben-Michael, C.-F.

Hsu, K. Slomkowski, A. Tosi, S. Cova, F. Zappa, and Ispasoiu, Single photon avalanche diodes (SPADs) for 1.5 µm photon counting applications, J.

Mod. Opt., vol. 54, no. 2-3, pp. 283304, 2007.

[48] A. Pediredla, Sankaranarayanan, M. Buttafava, A. Tosi, and A. Veeraraghavan, Signal processing based pile-up compensation for gated single-photon avalanche diodes, arXiv preprint arXiv:1806.07437, 2018.

[49] J. Rapp, Y. Ma, R. M. A. Dawson, and V. K. Goyal, Dead time compensation for high-ﬂux ranging, IEEE Trans. Signal Process., vol. 67, no. 13,

pp. 34713486, 2019.

[50] G. A. Kirmani, Computational Time-resolved Imaging. PhD thesis, Massachusetts Institute of Technol-

ogy, 2015.

[51] S. Riccardo, E. Conca, V. Sesta, A. Velten, and A. Tosi, Fast-gated 16 16 SPAD array with 16 on-chip 6 ps time-to-digital converters for non-lineof-sight imaging, IEEE Sens. J., vol. 22, no. 17,

[52] T. C. Carusone, D. Johns, and K. Martin, Analog Integrated Circuit Design. Wiley, 2011.


[53] J. Rapp, R. M. A. Dawson, and V. K. Goyal, Dithered depth imaging, Opt. Express, vol. 28, no. 23, pp. 3514335157, 2020.

[54] J. Rapp, R. M. A. Dawson, and V. K. Goyal, Estimation from quantized Gaussian measurements: When

and how to use dither, IEEE Trans. Signal Process., vol. 67, no. 13, pp. 34243438, 2019.

[55] A. Raghuram, A. Pediredla, S. G. Narasimhan, I. Gkioulekas, and A. Veeraraghavan, STORM: Super-resolving transients by oversampled measurements, in Proc. IEEE Int. Conf. on Computational

Photography (ICCP), pp. 111, 2019.

[56] X. Liu, I. Guillén, M. L. Manna, J. H. Nam, S. A. Reza, T. H. Le, A. Jarabo, D. Gutierrez, and A. Velten, Non-line-of-sight imaging using phasor-ﬁeld virtual wave optics, Nature, vol. 572, no. 7771, pp. 620 [57] Y. Chen, J. D. Müller, P. T. C. So, and E. Gratton, The photon counting histogram in ﬂuorescence ﬂuctuation spectroscopy, Biophys. J., vol. 77, no. 1, pp. 553567, [58] A. Gupta, A. Ingle, and M. Gupta, Asynchronous single-photon 3D imaging, in Proc. IEEE/CVF Int.

Conf. on Computer Vision (ICCV), pp. 79097918, [59] F. Heide, S. Diamond, D. B. Lindell, and G. Wetzstein, Sub-picosecond photon-efﬁcient 3D imaging using single-photon sensors, Sci. Rep., vol. 8, no. 17726, [60] V. Zickus, M.-L. Wu, K. Morimoto, V. Kapitany, A. Fatima, A. Turpin, R. Insall, J. Whitelaw, L. Machesky, C. Bruschini, D. Faccio, and E. Charbon, Flu-

orescence lifetime imaging with a megapixel SPAD camera and neural network lifetime estimation, Sci.

Rep., vol. 10, no. 20986, 2020.

[61] A. M. Pawlikowska, A. Halimi, R. A. Lamb, and G. S. Buller, Single-photon three-dimensional imaging at up to 10 kilometers range, Opt. Express, vol. 25, no. 10, pp. 1191911931, 2017.

[62] X. Liu, S. Bauer, and A. Velten, Phasor ﬁeld diffraction based reconstruction for fast non-line-of-sight

imaging systems, Nat. Commun., vol. 11, no. 1645, [63] D. L. Snyder and M. I. Miller, Random Point Processes in Time and Space. Springer New York, 2012.

[64] J. Ville, Etude critique de la notion de collectif, Bull. Am. Math. Soc., vol. 45, no. 11, p. 824, 1939.

[65] L. L. Scharf and C. Demeure, Statistical Signal Processing: Detection, Estimation, and Time Series Anal-

ysis. Prentice Hall, 1991.

[66] A. Velten, D. Wu, A. Jarabo, B. Masia, C. Barsi, C. Joshi, E. Lawson, M. Bawendi, D. Gutierrez, and R. Raskar, Femto-photography: Capturing and visualizing the propagation of light, ACM Trans. Graph.


(SIGGRAPH), vol. 32, no. 4, pp. 18, 2013.

[67] P. Sen, B. Chen, G. Garg, S. R. Marschner, M. Horowitz, M. Levoy, and H. P. A. Lensch, Dual photography, ACM Trans. Graph. (SIGGRAPH), vol. 24, no. 3, p. 745755, 2005.

[68] A. H. Barnett, J. Magland, and L. A. Klinteberg, A parallel nonuniform fast Fourier transform library based on an "exponential of semicircle" kernel, SIAM J. Sci. Comput., vol. 41, no. 5, pp. C479C504, 2019.
