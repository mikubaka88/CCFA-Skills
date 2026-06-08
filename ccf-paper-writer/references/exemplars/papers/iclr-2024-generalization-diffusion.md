# Generalization in Diffusion Models

> **Venue:** ICLR2024
> **Award:** Outstanding Paper
> **Source:** <https://openreview.net/forum?id=ANvmVS2Yr0>

---

Published as a conference paper at ICLR 2024
GENERALIZATION IN DIFFUSION MODELS ARISES FROM
GEOMETRY-ADAPTIVE HARMONIC REPRESENTATIONS
Zahra Kadkhodaie
Ctr. for Data Science, New York University
zk388@nyu.edu
Florentin Guth
Ctr. for Data Science, New York University
Flatiron Institute, Simons Foundation
florentin.guth@nyu.edu
Eero P. Simoncelli
New York University
Flatiron Institute, Simons Foundation
eero.simoncelli@nyu.edu
Stéphane Mallat
Collège de France
Flatiron Institute, Simons Foundation
stephane.mallat@ens.fr

## Abstract

Deep neural networks (DNNs) trained for image denoising are able to generate high-
quality samples with score-based reverse diffusion algorithms. These impressive
capabilities seem to imply an escape from the curse of dimensionality, but recent
reports of memorization of the training set raise the question of whether these
networks are learning the “true” continuous density of the data. Here, we show
that two DNNs trained on non-overlapping subsets of a dataset learn nearly the
same score function, and thus the same density, when the number of training
images is large enough. In this regime of strong generalization, diffusion-generated
images are distinct from the training set, and are of high visual quality, suggesting
that the inductive biases of the DNNs are well-aligned with the data density.
We analyze the learned denoising functions and show that the inductive biases
give rise to a shrinkage operation in a basis adapted to the underlying image.
Examination of these bases reveals oscillating harmonic structures along contours
and in homogeneous regions. We demonstrate that trained denoisers are inductively
biased towards these geometry-adaptive harmonic bases since they arise not only
when the network is trained on photographic images, but also when it is trained
on image classes supported on low-dimensional manifolds for which the harmonic
basis is suboptimal. Finally, we show that when trained on regular image classes
for which the optimal basis is known to be geometry-adaptive and harmonic, the
denoising performance of the networks is near-optimal.
1

## Introduction

Deep neural networks (DNNs) have demonstrated ever-more impressive capabilities for sampling
from high-dimensional image densities, most recently through the development of diffusion methods.
These methods operate by training a denoiser, which provides an estimate of the score (the gradient
of the log of the noisy image distribution). The score is then used to sample from the corresponding
estimated density, using an iterative reverse diffusion procedure (Sohl-Dickstein et al., 2015; Song
& Ermon, 2019; Ho et al., 2020; Kadkhodaie & Simoncelli, 2020). However, approximating a
continuous density in a high-dimensional space is notoriously difficult: do these networks actually
achieve this feat, learning from a relatively small training set to generate high-quality samples, in
apparent defiance of the curse of dimensionality? If so, this must be due to their inductive biases, that
is, the restrictions that the architecture and optimization place on the learned denoising function. But
the approximation class associated with these models is not well understood. Here, we take several
steps toward elucidating this mystery.
Several recently reported results show that, when the training set is small relative to the network
capacity, diffusion generative models do not approximate a continuous density, but rather memorize
samples of the training set, which are then reproduced (or recombined) when generating new samples
Source code: https://github.com/LabForComputationalVision/memorization_generalization_in_diffusion_models
1

Published as a conference paper at ICLR 2024
(Somepalli et al., 2023; Carlini et al., 2023). This is a form of overfitting (high model variance).
Here, we confirm this behavior for DNNs trained on small data sets, but demonstrate that these same
models do not memorize when trained on sufficiently large sets. Specifically, we show that two
denoisers trained on sufficiently large non-overlapping sets converge to essentially the same denoising
function. That is, the learned model becomes independent of the training set (i.e., model variance
falls to zero). As a result, when used for image generation, these networks produce nearly identical
samples. These results provide stronger and more direct evidence of generalization than standard
comparisons of average performance on train and test sets. This generalization can be achieved with
large but realizable training sets (for our examples, roughly 105 images suffices), reflecting powerful
inductive biases of these networks. Moreover, sampling from these models produces images of high
visual quality, implying that these inductive biases are well-matched to the underlying distribution of
photographic images (Wilson & Izmailov, 2020; Goyal & Bengio, 2022; Griffiths et al., 2023).
To study these inductive biases, we develop and exploit the relationship between denoising and
density estimation. We find that DNN denoisers trained on photographic images perform a shrinkage
operation in an orthonormal basis consisting of harmonic functions that are adapted to the geometry
of features in the underlying image. We refer to these as geometry-adaptive harmonic bases (GAHBs).
This observation, taken together with the generalization performance of DNN denoisers, suggests that
optimal bases for denoising photographic images are GAHBs and, moreover, that inductive biases of
DNN denoisers encourage such bases. To test this more directly, we examine a particular class of
images whose intensity variations are regular over regions separated by regular contours. A particular
type of GAHB, known as “bandlets” (Peyré & Mallat, 2008), have been shown to be near-optimal for
denoising these images (Dossal et al., 2011). We observe that the DNN denoiser operates within a
GAHB similar to a bandlet basis, also achieving near-optimal performance. Thus the inductive bias
enables the network to appropriately estimate the score in these cases.
If DNN denoisers induce biases towards the GAHB approximation class, then they should perform
sub-optimally for distributions whose optimal bases are not GAHBs. To investigate this, we train
DNN denoisers on image classes supported on low-dimensional manifolds, for which the optimal
denoising basis is only partially constrained. Specifically, an optimal denoiser (for small noise) should
project a noisy image on the tangent space of the manifold. We observe that the DNN denoiser closely
approximates this projection, but also partially retains content lying within a subspace spanned by a
set of additional GAHB vectors. These suboptimal components reflect the GAHB inductive bias.
2
DIFFUSION MODEL VARIANCE AND DENOISING GENERALIZATION
Consider an unknown image probability density, p(x). Rather than approximating this density
directly, diffusion models learn the scores of the distributions of noise-corrupted images. Here, we
show that the denoising error provides a bound on the density modeling error, and use this to analyze
the convergence of the density model.
2.1
DIFFUSION MODELS AND DENOISING
Let y = x + z where z ∼N(0, σ2Id). The density pσ(y) of noisy images is then related to p(x)
through marginalization over x:
pσ(y) =
Z
p(y|x) p(x) dx =
Z
gσ(y −x) p(x) dx,
(1)
where gσ(z) is the density of z. Hence, pσ(y) is obtained by convolving p(x) with a Gaussian with
standard deviation σ. The family of densities {pσ(y); σ ≥0} forms a scale-space representation of
p(x), analogous to the temporal evolution of a diffusion process.
Diffusion models learn an approximation sθ(y) (dropping the σ dependence for simplicity) of the
scores ∇log pσ(y) of the blurred densities pσ(y) at all noise levels σ. The collection of these score
models implicitly defines a model pθ(x) of the density of clean images p(x) through a reverse
diffusion process. The error of the generative model, as measured by the KL divergence between p(x)
and pθ(x), is then controlled by the integrated score error across all noise levels (Song et al., 2021):
DKL(p(x) ∥pθ(x)) ≤
Z ∞
0
E
y
h
∥∇log pσ(y) −sθ(y)∥2i
σ dσ.
(2)
2

Published as a conference paper at ICLR 2024
The key to learning the scores is an equation due to Robbins (1956) and Miyasawa (1961) (proved in
Appendix D.1 for completeness) that relates them to the mean of the corresponding posteriors:
∇log pσ(y) = (E
x[x | y] −y)/σ2.
(3)
The score is learned by training a denoiser fθ(y) to minimize the mean squared error (MSE) (Raphan
& Simoncelli, 2011; Vincent, 2011):
MSE(fθ, σ2) = E
x,y
h
∥x −fθ(y)∥2i
,
(4)
so that fθ(y) ≈Ex[x | y]. This estimated conditional mean is used to recover the estimated score
using eq. (3): sθ(y) = (fθ(y) −y)/σ2. As we show in Appendix D.2, the error in estimating the
density p(x) is bounded by the integrated optimality gap of the denoiser across noise levels:
DKL(p(x) ∥pθ(x)) ≤
Z ∞
0

MSE(fθ, σ2) −MSE(f ⋆, σ2)

σ−3 dσ,
(5)
where f ⋆(y) = Ex[x | y] is the optimal denoiser. Thus, learning the true density model is equivalent
to performing optimal denoising at all noise levels. Conversely, a suboptimal denoiser introduces a
score approximation error, which in turn can result in an error in the modeled density.
Generally, the optimal denoising function f ⋆(as well as the “true” distribution, p(x)) is unknown
for photographic images, which makes numerical evaluation of sub-optimality challenging. We can
however separate deviations from optimality arising from model bias and model variance. Model
variance measures the size of the approximation class, and hence the strength (or restrictiveness) of
the inductive biases. It can be evaluated without knowledge of f ⋆. Here, we define generalization as
near-zero model variance (i.e., an absence of overfitting), which is agnostic to model bias. This is
the subject of Section 2.2. Model bias measures the distance of the true score to the approximation
class, and thus the alignment between the inductive biases and the data distribution. In the context of
photographic images, visual quality of generated samples can be a qualitative indicator of the model
bias, although high visual quality does not necessarily guarantee low model bias. We evaluate model
bias in Section 3.2 by considering synthetic image classes for which f ⋆is approximately known.
2.2
TRANSITION FROM MEMORIZATION TO GENERALIZATION
DNNs are susceptible to overfitting, because the number of training examples is typically small
relative to the model capacity. Since density estimation, in particular, suffers from the curse of
dimensionality, overfitting is of more concern in the context of generative models. An overfitted
denoiser performs well on training images but fails to generalize to test images, resulting in low-
diversity generated images. Consistent with this, several papers have reported that diffusion models
can memorize their training data (Somepalli et al., 2023; Carlini et al., 2023; Dar et al., 2023; Zhang
et al., 2023). To directly assess this, we compared denoising performance on training and test data
for different training set sizes N. We trained denoisers on subsets of the (downsampled) CelebA
dataset (Liu et al., 2015) of size N = 100, 101, 102, 103, 104, 105. We used a UNet architecture
(Ronneberger et al., 2015), which is composed of 3 convolutional encoder and decoder blocks with
rectifying non-linearities. These denoisers are universal and blind: they operate on all noise levels
without having noise level as an input Mohan* et al. (2020). Networks are trained to minimize mean
squared error (4). See Appendix A for architecture and training details.

## Results

image, leading to a high test error. Increasing N substantially increases the performance on the test
set while worsening performance on the training set, as the network transitions from memorization to
generalization. At N = 105, empirical test and train error are matched for all noise levels.
To investigate this generalization further, we train denoisers on non-overlapping subsets of CelebA of
various size N. We then generate samples using the scores learned by each denoiser, through the
reverse diffusion algorithm of Kadkhodaie & Simoncelli (2020)—see Appendix A for details. Figure
2 shows samples generated by these denoisers, initialized from the same noise sample. For small
N, the networks memorize their respective training images. However, for large N, the networks
converge to the same score function (and thus sample from the same model density), generating nearly
identical samples. This surprising behavior provides a much stronger demonstration of convergence
than comparison of average train and test performance.
3

Published as a conference paper at ICLR 2024
42
39
36
33
30
27
24
21
18
15
12
9
6
3
0
Input PSNR
9
12
15
18
21
24
27
30
33
36
39
42
45
48
51
54
57
60
63
Output PSNR
Train
42
39
36
33
30
27
24
21
18
15
12
9
6
3
0
Input PSNR
Test
N: 1
N: 10
N: 100
N: 1000
N: 10000
N: 100000
identity
Figure 1: Transition from memorization to generalization, for a UNet denoiser trained on face images.
Each curve shows the denoising error (output PSNR, ten times log10 ratio of squared dynamic range
to MSE) as a function of noise level (input PSNR), for a training set of size N. As N increases,
performance on the training set generally worsens (left), while performance on the test set improves
(right). For N = 1 and N = 10, the train PSNR improves with unit slope, while test PSNR is poor,
independent of noise level, a sign of memorization. The increase in test performance on small noise
levels at N = 1000 is indicative of the transition phase from memorization to generalization. At
N = 105, test and train PSNR are essentially identical, and the model is no longer overfitting the
training data.
3
INDUCTIVE BIASES
The number of samples needed for estimation of an arbitrary probability density grows exponentially
with dimensionality (the “curse of dimensionality”). As a result, estimating high-dimensional
distributions is only feasible if one imposes strong constraints or priors over the hypothesis space.
In a diffusion model, these arise from the network architecture and the optimization algorithm, and
are referred to as the inductive biases of the network (Wilson & Izmailov, 2020; Goyal & Bengio,
2022; Griffiths et al., 2023). In Section 2.2, we demonstrated that DNN denoisers can learn scores
(and thus a density) from relatively small training sets. This generalization result, combined with the
high quality of sampled images, is evidence that the inductive biases are well-matched to the “true”
distribution of images, allowing the model to rapidly converge to a good solution through learning.
On the contrary, when inductive biases are not aligned with the true distribution, the model will arrive
at a poor solution with high model bias.
For diffusion methods, learning the right density model is equivalent to performing optimal denoising
at all noise levels (see Section 2.1). The inductive biases on the density model thus arise directly
from inductive biases in the denoiser. This connection offers a means of evaluating the accuracy of
the learned probability models, which is generally difficult in high-dimensions.
3.1
DENOISING AS SHRINKAGE IN AN ADAPTIVE BASIS
The inductive biases of the DNN denoiser can be studied through an eigendecomposition of its
Jacobian. We describe the general properties that are expected for an optimal denoiser, and examine
several specific cases for which the optimal solution is partially known.
Jacobian eigenvectors as an adaptive basis.
To analyze inductive biases, we perform a local
analysis of a denoising estimator ˆx(y) = f(y) by looking at its Jacobian ∇f(y). For simplicity,
we assume that the Jacobian is symmetric and non-negative (we show below that this holds for the
optimal denoiser, and it is approximately true of the network Jacobian (Mohan* et al., 2020)). We
can then diagonalize it to obtain eigenvalues (λk(y))1≤k≤d and eigenvectors (ek(y))1≤k≤d.
If f(y) is computed with a DNN denoiser with no additive “bias” parameters, its input-output mapping
is piecewise linear, as opposed to piecewise affine (Mohan* et al., 2020; Romano et al., 2017). It
4

Published as a conference paper at ICLR 2024
Closest image from S1:
N=1
N=10
N=100
N=1000
N=10000
N=100000
Generated by models trained on S1:
Generated by models trained on S2:
Closest image from S2:
0.0
0.25
0.5
0.75
1.0
N = 10
0.0
0.25
0.5
0.75
1.0
N = 1000
0.0
0.25
0.5
0.75
1.0
N = 10000
0.0
0.25
0.5
0.75
1.0
N = 100000
Samples from two denoisers
Sample and closest train image
Figure 2: Convergence of model variance. Diffusion models are trained on non-overlapping subsets
S1 and S2 of a face dataset (filtered for duplicates). The subset size N varies from 1 to 105. We then
generate a sample from each model with a reverse diffusion algorithm, initialized from the same noise
image. Top. For training sets of size N = 1 to N = 100, the networks memorize, producing samples
nearly identical to examples from the training set. For N = 1000, generated samples are similar to
a training example, but show distortions in some regions. This transitional regime corresponds to
a qualitative change in the shape of the PSNR curve (Figure 1). For N = 105, the two networks
generate nearly identical samples, which no longer resemble images in their corresponding training
sets. Bottom. The distribution of cosine similarity (normalized inner product) between pairs of
images generated by the two networks (blue) shifts from left to right with increasing N, showing
vanishing model variance. Conversely, the distribution of cosine similarity between generated samples
and the most similar image in their corresponding training set (orange) shifts from right to left. For
comparison, Appendix B shows the distribution of cosine similarities of closest pairs between the
two training subsets, and additional results on the LSUN bedroom dataset (Yu et al., 2015) and for
the BF-CNN architecture (Mohan* et al., 2020).
follows that the denoiser mapping can be rewritten in terms of the Jacobian eigendecomposition as
f(y) = ∇f(y) y =
X
k
λk(y) ⟨y, ek(y)⟩ek(y).
(6)
The denoiser can thus be interpreted as performing shrinkage with factors λk(y) along axes of a basis
specified by ek(y). Note that both the eigenvalues and eigenvectors depend on the noisy image y (i.e.,
both the basis and shrinkage factors are adaptive (Milanfar, 2012)).
Even if the denoiser is not bias-free, small eigenvalues λk(y) reveal local invariances of the denoising
function: small perturbations in the noisy input along the corresponding eigenvectors ek(y) do not
affect the denoised output. Intuitively, such invariances are a desirable property for a denoiser, and
they are naturally enforced by minimizing mean squared error (MSE) as expressed with Stein’s
unbiased risk estimate (SURE, proved in Appendix D.3 for completeness):
MSE(f, σ2) = E
y
h
2σ2 tr ∇f(y) + ∥y −f(y)∥2 −σ2d
i
.
(7)
To minimize MSE, the denoiser must trade off the approximate “rank” of the Jacobian (the trace is the
sum of the eigenvalues) against an estimate of the denoising error: ∥y −f(y)∥2 −σ2d. The denoiser
thus locally behaves as a (soft) projection on a subspace whose dimensionality corresponds to the
5

Published as a conference paper at ICLR 2024
rank of the Jacobian. As we now explain, this subspace approximates the support of the posterior
distribution p(x|y), and thus gives a local approximation of the support of p(x).
It is shown in Appendix D.1 that the optimal minimum MSE denoiser and its Jacobian are given by
f ⋆(y) = y + σ2∇log pσ(y) = E
x[x|y],
(8)
∇f ⋆(y) = Id + σ2∇2 log pσ(y) = σ−2Cov[x | y].
(9)
That is, the Jacobian of the optimal denoiser is proportional to the posterior covariance matrix, which
is symmetric and non-negative. This gives us another interpretation of the adaptive eigenvector basis
as providing an optimal approximation of the unknown clean image x given the noisy observation y.
Further, the optimal denoising error is then given by (see Appendix D.1 for the first equality)
MSE(f ⋆, σ2) = E
y[tr Cov[x | y]] = σ2 E
y

tr ∇f ⋆(y)

= σ2 E
y
"X
k
λ⋆
k(y)
#
.
(10)
A small denoising error thus implies an approximately low-rank Jacobian (with many small eigenval-
ues) and thus an efficient approximation of x given y.
In most cases, the optimal adaptive basis (e⋆
k(y))1≤k≤d is not known. Rather than aiming for exact
optimality, classical analyses (Donoho, 1995) thus focus on the asymptotic decay of the denoising
error as the noise level σ2 falls, up to multiplicative constants. This corresponds to finding a basis
(ek(y))1≤k≤d which captures the asymptotic slope of the PSNR plots in Figure 1 but not necessarily
the intercept. This weaker notion of optimality is obtained by showing matching upper and lower-
bounds on the asymptotic behavior of the denoising error. To provide intuition, we first consider a
fixed orthonormal basis ek(y) = ek, and then consider the more general case of best bases selected
from a fixed dictionary.
Denoising in a fixed basis.
Consider a denoising algorithm that is restricted to operate in a fixed
basis ek but can adapt its shrinkage factors λk(y). An unreachable lower-bound on the denoising
error—and thus an upper-bound on the PSNR slope—is obtained by evaluating the performance of an
“oracle” denoiser where the shrinkage factors λk depend on the unknown clean image x rather than
the noisy observation y (Mallat, 2008). Appendix D.4 shows that the denoising error of this oracle is
E
x
"X
k

(1 −λk(x))2⟨x, ek⟩2 + λk(x)2σ2#
,
(11)
which is minimized when λk(x) =
⟨x,ek⟩2
⟨x,ek⟩2+σ2 . The coefficient λk(x) thus acts as a soft threshold:
λk(x) ≈1 when the signal dominates the noise and λk(x) ≈0 when the signal is weaker than the
noise. Appendix D.4 then shows that the oracle denoising error is the expected value of
σ2X
k
λk(x) =
X
k
σ2⟨x, ek⟩2
⟨x, ek⟩2 + σ2 ∼
X
k
min(⟨x, ek⟩2, σ2) = Mσ2 + ∥x −xM∥2,
(12)
where xM = P
⟨x,ek⟩2>σ2⟨x, ek⟩ek is the M-term approximation of x with the M basis coefficients
⟨x, ek⟩above the noise level, and ∼means that the two terms are of the same order up to multiplicative
constants (here smaller than 2). The denoising error is small if x has a sparse representation in the
basis, so that both M and the approximation error ∥x −xM∥2 are small. For example, if the
coefficients decay as ⟨x, ek⟩2 ∼k−(α+1) (up to reordering), Appendix D.4 shows that
Mσ2 + ∥x −xM∥2 ∼σ2α/(α+1),
(13)
which is a lower bound on the MSE of any denoising algorithm in the basis ek. Reciprocally,
this oracle denoising error is nearly reached with a soft-thresholding estimator that computes the
shrinkage factors λk(y) by comparing ⟨y, ek⟩2 (rather than ⟨x, ek⟩2) with a threshold proportional
to σ2 (Donoho & Johnstone, 1994), and achieves the decay (13) up to a logarithmic factor. The
decay (13) of the MSE with decreasing σ corresponds to an asymptotic slope of α/(α + 1) in the
PSNR curve when the input PSNR increases. Thus, a larger sparsity/regularity exponent α, which
corresponds to a faster decay of the small coefficients of x in the basis (ek)1≤k≤d, leads to improved
denoising performance.
6

Published as a conference paper at ICLR 2024
Clean
Noisy
Denoised
0
1000
2000
3000
4000
5000
6000
k
0
2
4
6
8
10
12
14
x, ek
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
k(y)
5 = 1.244
17 = 1.115
29 = 1.046
41 = 1.008
53 = 0.973
65 = 0.93
77 = 0.896
89 = 0.857
101 = 0.822
113 = 0.792
125 = 0.758
137 = 0.718
149 = 0.689
161 = 0.663
173 = 0.637
185 = 0.612
197 = 0.59
209 = 0.569
221 = 0.551
233 = 0.53
245 = 0.51
Figure 3: Analysis of a denoiser trained on 105 face images, evaluated on a noisy test image. Top
left. Clean, noisy (σ = 0.15) and denoised images. Bottom left. Decay of shrinkage values λk(y)
(red), and corresponding coefficients ⟨x, ek(y)⟩(blue), evaluated for the noisy image y. The rapid
decay of the coefficients indicates that the image content is highly concentrated within the preserved
subspace. Right. The adaptive basis vectors ek(y) contain oscillating patterns, adapted to lie along
the contours and within smooth regions of the image, whose frequency increases as λk(y) decreases.
Best adaptive bases.
Adapting the basis (ek)1≤k≤d to the noisy image y allows obtaining sparser
representations of the unknown clean image x with a faster decay, and thus a larger PSNR slope. To
calculate the optimal adaptive basis, we need to find an oracle denoiser that has the same asymptotic
MSE as a non-oracle denoiser, yielding matching lower and upper bounds on the asymptotic MSE.
Consider an oracle denoiser which performs a thresholding in an oracle basis (ek(x)) that depends on
the unknown clean image x. The above analysis then still applies, and if the coefficients ⟨x, ek(x)⟩2
decay as k−(α+1), then the asymptotic PSNR slope is again α/(α + 1). The best oracle basis satisfies
e1(x) = x/∥x∥, but it yields a loose lower bound as it cannot be estimated from the noisy image
y alone. We thus restrict the oracle denoiser to choose the basis (ek(x)) within a fixed dictionary.
A larger dictionary increases adaptivity, but it then becomes harder to estimate the basis that best
represents x from y alone. If the dictionary of bases is constructed from a number of vectors ek
which is polynomial in the dimension d (the number of bases can however be exponential in d) then a
thresholding in the basis (ek(y)) that best approximates the noisy image y achieves the same slope as
the oracle denoiser (Barron et al., 1999; Dossal et al., 2011). This near-optimality despite the presence
of noise comes from the limited choice of possible basis vectors ek in the dictionary, which limits
the variance of the best-basis estimation, e.g. by preventing e1(y) = y/∥y∥. The main difficulty is
then to design a small-enough dictionary that gives optimal representations of images from the data
distribution in order to achieve the optimal PSNR slope.
We now evaluate the inductive biases of DNN denoisers through this lens. In Section 2, we showed
that the DNN denoisers overcome the curse of dimensionality: their variance decays to zero in the
generalization regime. In the next section, we explain this observation by demonstrating that they are
inductively biased towards adaptive bases ek(y) from a particular class.
3.2
GEOMETRY-ADAPTIVE HARMONIC BASES IN DNNS
Figure 3 shows the shrinkage factors (λk(y)), adaptive basis vectors (ek(y)), and signal coefficients
(⟨x, ek(y)⟩) of a DNN denoiser trained on 105 face images. The eigenvectors have oscillating patterns
both along the contours and in uniformly regular regions and thus adapt to the geometry of the
input image. We call this a geometry-adaptive harmonic basis (GAHB). The coefficients are sparse
in this basis, and the fast rate of decay of eigenvalues exploits this sparsity. The high quality of
generated images and the strong generalization results of Section 2 show that DNN denoisers rely on
inductive biases that are well-aligned to photographic image distributions. All of this suggests that
DNN denoisers might be inductively biased towards GAHBs. In the following, we provide evidence
supporting this conjecture by analyzing networks trained on synthetic datasets where the optimal
solution is (approximately) known.
Cα images and bandlet bases.
If DNNs are inductively biased towards GAHBs, we expect that
they generalize and converge to the optimal denoising performance when such bases are optimal. We
7

Published as a conference paper at ICLR 2024
34
31
29
27
25
22
20
17
15
12
10
7
5
2
0
Input PSNR
15
20
25
30
35
40
45
50
55
Output PSNR
= 1, slope= 0.46 (0.5)
= 2, slope= 0.61 (0.67)
= 3, slope= 0.75 (0.75)
= 5, slope= 0.83 (0.83)
identity
0 = 1.147
1 = 1.072
2 = 1.056
3 = 1.046
4 = 1.032
5 = 1.019
6 = 1.01
7 = 0.997
8 = 0.996
9 = 0.984
10 = 0.948
11 = 0.943
12 = 0.897
13 = 0.891
14 = 0.83
15 = 0.811
16 = 0.767
17 = 0.759
18 = 0.736
19 = 0.65
Figure 4: UNet denoisers trained on 105 Cα images achieve near-optimal performance. Left. PSNR
curves for various regularity levels α. The empirical slopes closely match the theoretical optimal
slopes (parenthesized values, dashed lines). Right. A Cα image (α = 4) of size 80 × 80 and its top
eigenvectors, which consist of harmonics on the two regions and harmonics along the boundary. The
frequency of the harmonics increases with k. More examples are given in Appendix C.1.
consider the so-called geometric Cα class of images (Korostelev & Tsybakov, 1993; Donoho, 1999;
Peyré & Mallat, 2008) which consist of regular contours on regular backgrounds, where the degree of
regularity is controlled by α. Examples of these images are shown in Figure 4 and Appendix C.1. A
mathematical definition and an algorithm for their synthesis are presented in Appendix E.
Optimal sparse representations of Cα images are obtained with “bandlet” bases (Peyré & Mallat,
2008). Bandlets are harmonic functions oscillating at different frequencies, whose geometry is adapted
to the directional regularity of images along contours. Geometric Cα images can be represented
with few bandlets having low-frequency oscillations in regular regions and along contours but sharp
variations across contours. The k-th coefficient in the best bandlet basis then decays as k−(α+1). It
follows that the optimal denoiser has a PSNR which asymptotically increases with a slope α/(α + 1)
as a function of input PSNR (Korostelev & Tsybakov, 1993; Dossal et al., 2011).
Figure 4 shows that DNN denoisers trained on Cα images also achieve this optimal rate and learns
GAHBs, similarly to bandlets but with a more flexible geometry. This generalization performance
confirms that inductive biases of DNNs favor GAHBs.
Low-dimensional manifolds.
If DNNs are inductively biased towards GAHBs, then we expect
these bases to emerge even in cases where they are suboptimal. To test this prediction, we consider a
dataset of disk images with varying positions, sizes, and foreground/background intensities. This
defines a five-dimensional curved manifold, with a tangent space evaluated at a disk image x that is
spanned by deformations of x along these five dimensions. When the noise level σ is much smaller
than the radius of curvature of the manifold, the posterior distribution p(x|y) is supported on an
approximately flat region of the manifold, and the optimal denoiser is approximately a projection
onto the tangent space. Thus, the optimal Jacobian should have only five non-negligible eigenvalues,
whose corresponding eigenvectors span the tangent space. The remaining eigenvectors should have
shrinkage factors of λ = 0, but are otherwise unconstrained. The optimal MSE is asymptotically
equal to 5σ2, corresponding to a PSNR slope of one.
Figure 5 shows an analysis of a denoiser trained on 105 disk images, of size 80 × 80. We observe
additional basis vectors with non-negligible eigenvalues that have a GAHB structure, with oscillations
on the background region and along the contour of the disk. We also find that the number of non-zero
eigenvalues increases as the noise level decreases, leading to a suboptimal PSNR slope that is less
than 1.0. These results reveal that the inductive biases of the DNN are not perfectly aligned with
low-dimensional manifolds, and that in the presence of the curvature, this suboptimality increases
as the noise level decreases. We obtain similar results on two additional examples of a distribution
supported on a low-dimensional manifold, given in Appendix C.2.
Shuffled faces.
We also consider in Appendix C.3 a dataset of shuffled faces, obtained by applying
a common permutation to the pixels of each face image. This permutation does not preserve locality
between neighboring pixels, and thus the optimal basis does not have harmonic structure. The
resulting mismatch between the DNN inductive biases and the data distribution result in substantially
worse performance than for the original (unscrambled) faces.
8

Published as a conference paper at ICLR 2024
Clean
Noisy
Denoised
0 = 1.177
1 = 1.067
2 = 1.004
3 = 0.999
4 = 0.945
5 = 0.674
6 = 0.552
7 = 0.39
8 = 0.304
9 = 0.278
0
1000
2000
3000
4000
5000
6000
k
0.0
2.5
5.0
7.5
10.0
12.5
15.0
17.5
x, ek
0.0
0.2
0.4
0.6
0.8
1.0
1.2
k(y)
34
31
29
27
25
22
20
17
15
12
10
7
5
2
0
input PSNR
10
22
35
48
60
output PSNR
empirical
optimal
identity
Figure 5: UNet denoiser trained on a dataset of translating and dilating disks, with variable fore-
ground/background intensity. Top center. Clean, noisy (σ = 0.04), and denoised images. Bottom
center. The decay of shrinkage factors λk(y) and coefficients ⟨x, ek(y)⟩indicates that the network
achieves and preserves a sparse representation of the true image. Top right. denoising performance
is sub-optimal, with PSNR slope below the optimal value of 1.0 for small noise. Top left. An optimal
basis (in the small-noise limit) spanning the 5-dimensional tangent space of the image manifold.
Bottom left. Top eigenvectors of the adaptive basis. The first five basis vectors closely match the
basis of the tangent space of the manifold evaluated at the clean image. In contrast, the next five are
GAHBs that lie along contours and within background regions of the clean image.
4

## Discussion

Diffusion generative models, which operate through iterative application of a trained DNN denoiser,
have recently surpassed all previous methods of learning probability models of images. Their training
objective (minimization of squared denoising error) is simple and robust, and they generate samples
of impressive quality. In this paper, we elucidate the approximation properties that underlie this
success, by analyzing the trained denoiser, which is directly related to the score function, and to the
density from which the samples are drawn.
We show empirically that diffusion models memorize samples when trained on small sets, but
transition to a strong form of generalization as the training set size increases, converging to a unique
density model that is independent of the specific training samples. The amount of data needed to
reach this phase transition is very small relative to the size of dataset needed for convergence without
any inductive biases, and depends on the image size and complexity relative to the neural network
capacity (Yoon et al., 2023). It is of interest to extend both the theory and the empirical studies to
account for the interplay of these factors. Appendix B.4 shows preliminary results in this direction.
We also examined the inductive biases that enable this strong generalization. Using a well-established
mathematical framework, we showed that DNN denoisers perform shrinkage of noisy coefficients in a
geometry-adaptive harmonic basis (GAHB) which is shaped by geometric features of the image. For
the Cα class of images, such geometric bases are known to be optimal, and DNN denoisers achieve
near-optimal performance on this class. Previous mathematical literature has shown that bandlet
bases, which are a specific type of GAHB, are near-optimal for this class, but the GAHBs learned
by the DNN denoiser are more general and more flexible. For images drawn from low-dimensional
manifolds, for which the optimal basis spans the tangent subspace of the manifold, we find that DNN
denoisers achieve good denoising within a basis aligned with this subspace, but also incorporate
GAHB vectors in the remaining unconstrained dimensions. The non-suppressed noise along these
additional GAHB components leads to suboptimal denoising performance. This observation, along
with similar ones shown in Appendix C.2, provide more supporting evidence for the hypothesis that
inductive biases of DNN denoisers promote GAHBs.
We do not provide a formal mathematical definition of the class of GAHBs arising from the inductive
biases of DNNs. Convolutions in DNN architectures, whose eigenvectors are sinusoids, presumably
engender GAHB harmonic structure, but the geometric adaptivity must arise from interactions with
rectification nonlinearities (ReLUs). A more precise elucidation of this GAHB function class, and its
role in shaping inductive biases of the DNNs used in a wide variety of other tasks and modalities, is
of fundamental interest.
9

Published as a conference paper at ICLR 2024
ACKNOWLEDGMENTS
We gratefully acknowledge the support and computing resources of the Flatiron Institute (a research
division of the Simons Foundation), and NSF Award 1922658 to the Center for Data Science at NYU.
REFERENCES
Andrew Barron, Lucien Birgé, and Pascal Massart. Risk bounds for model selection via penalization.
Probability theory and related fields, 113:301–413, 1999.
Giulio Biroli, Tony Bonnaire, Valentin de Bortoli, and Marc Mézard. Dynamical regimes of diffusion
models. arXiv preprint arXiv:2402.18491, 2024.
Nicolas Carlini, Jamie Hayes, Milad Nasr, Matthew Jagielski, Vikash Sehwag, Florian Tramer, Borja
Balle, Daphne Ippolito, and Eric Wallace. Extracting training data from diffusion models. In 32nd
USENIX Security Symposium (USENIX Security 23), pp. 5253–5270, 2023.
Salman Ul Hassan Dar, Arman Ghanaat, Jannik Kahmann, Isabelle Ayx, Theano Papavassiliou,
Stefan O Schoenberg, and Sandy Engelhardt. Investigating data memorization in 3d latent diffusion
models for medical image synthesis. arXiv preprint arXiv:2307.01148, 2023.
D Donoho. Denoising by soft-thresholding. IEEE Trans Information Theory, 43:613–627, 1995.
David L Donoho. Wedgelets: Nearly minimax estimation of edges. the Annals of Statistics, 27(3):
859–897, 1999.
David L Donoho and Iain M Johnstone. Ideal spatial adaptation by wavelet shrinkage. biometrika, 81
(3):425–455, 1994.
Ch. Dossal, E. Le Pennec, and S. Mallat. bandlet image estimation with model selection. Signal
Processing, 91:2743–2753, 2011.
Bradley Efron. Tweedie’s formula and selection bias. J American Statistical Association, 106(496):
1602–1614, Dec 2011.
Anirudh Goyal and Yoshua Bengio. Inductive biases for deep learning of higher-level cognition.
Proceedings of the Royal Society A, 478(2266):20210068, 2022.
Thomas L Griffiths, Jian-Qiao Zhu, Erin Grant, and R Thomas McCoy. Bayes in the age of intelligent
machines. arXiv preprint arXiv:2311.10206, 2023.
J Ho, A Jain, and P Abbeel. Denoising diffusion probabilistic models. Adv Neural Information
Processing Systems (NeurIPS), 33, 2020.
Z Kadkhodaie and E P Simoncelli. Solving linear inverse problems using the prior implicit in a
denoiser. arXiv preprint arXiv:2007.13640, Jul 2020.
Z Kadkhodaie and E P Simoncelli. Stochastic solutions for linear inverse problems using the prior
implicit in a denoiser. In Adv Neural Information Processing Systems (NeurIPS*21), volume 34,
Dec 2021.
Z Kadkhodaie, F Guth, S Mallat, and E P Simoncelli. Learning multi-scale local conditional
probability models of images. In Int’l Conf on Learning Representations (ICLR), Kigali, Rwanda,
May 2023.
T Karras, T Aila, S Laine, and J Lehtinen. Progressive growing of GANs for improved quality,
stability, and variation. arXiv preprint arXiv:1710.10196, 2018.
A. P. Korostelev and A. B. Tsybakov. Minimax theory of image reconstruction. Springer New York,
NY, 1993.
Z Liu, P Luo, X Wang, and X Tang. Deep learning face attributes in the wild. In Proc Int’l Conference
on Computer Vision (ICCV), Dec 2015.
10

Published as a conference paper at ICLR 2024
S Mallat. A wavelet tour of signal processing: The sparse way. Academic Press, 2008.
Peyman Milanfar. A tour of modern image filtering: New insights and methods, both practical and
theoretical. IEEE signal processing magazine, 30(1):106–128, 2012.
K Miyasawa. An empirical Bayes estimator of the mean of a normal population. Bull. Inst. Internat.
Statist., 38:181–188, 1961.
S Mohan*, Z Kadkhodaie*, E P Simoncelli, and C Fernandez-Granda. Robust and interpretable
blind image denoising via bias-free convolutional neural networks. In Int’l Conf on Learning
Representations (ICLR), Addis Ababa, Ethiopia, Apr 2020.
G. Peyré and S. Mallat. Orthogonal bandlet bases for geometric images approximation. Comm. on
Pure and Applied Math., 61(9):1173–1212, 2008.
M Raphan and E P Simoncelli. Least squares estimation without priors or supervision. Neural
Computation, 23(2):374–420, Feb 2011. doi: 10.1162/NECO_a_00076.
H Robbins. An empirical bayes approach to statistics. In Proc Third Berkeley Symposium on
Mathematical Statistics and Probability, volume I, pp. 157–163. University of CA Press, 1956.
Yaniv Romano, Michael Elad, and Peyman Milanfar. The little engine that could: Regularization by
denoising (red). SIAM Journal on Imaging Sciences, 10(4):1804–1844, 2017.
O Ronneberger, P Fischer, and T Brox. U-net: Convolutional networks for biomedical image
segmentation. In Int’l Conf Medical Image Computing and Computer-assisted Intervention, pp.
234–241. Springer, 2015.
J Sohl-Dickstein, E Weiss, N Maheswaranathan, and S Ganguli. Deep unsupervised learning using
nonequilibrium thermodynamics. In Francis Bach and David Blei (eds.), Proc 32nd Int’l Conf
on Machine Learning (ICML), volume 37 of Proceedings of Machine Learning Research, pp.
2256–2265, Lille, France, 07–09 Jul 2015. PMLR.
Gowthami Somepalli, Vasu Singla, Micah Goldblum, Jonas Geiping, and Tom Goldstein. Diffusion
art or digital forgery? investigating data replication in diffusion models. In Proceedings of the
IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 6048–6058, 2023.
Y Song and S Ermon. Generative modeling by estimating gradients of the data distribution. Adv
Neural Information Processing Systems (NeurIPS), 32, 2019.
Yang Song, Conor Durkan, Iain Murray, and Stefano Ermon. Maximum likelihood training of
score-based diffusion models. Advances in Neural Information Processing Systems, 34:1415–1428,
2021.
P Vincent. A connection between score matching and denoising autoencoders. Neural Computation,
23(7):1661–1674, 2011.
Andrew G Wilson and Pavel Izmailov. Bayesian deep learning and a probabilistic perspective of
generalization. Advances in neural information processing systems, 33:4697–4708, 2020.
TaeHo Yoon, Joo Young Choi, Sehyun Kwon, and Ernest K Ryu. Diffusion probabilistic models
generalize when they fail to memorize. In ICML 2023 Workshop on Structured Probabilistic
Inference & Generative Modeling, 2023.
Fisher Yu, Ari Seff, Yinda Zhang, Shuran Song, Thomas Funkhouser, and Jianxiong Xiao. LSUN:
Construction of a large-scale image dataset using deep learning with humans in the loop. arXiv
preprint arXiv:1506.03365, 2015.
Huijie Zhang, Jinfan Zhou, Yifu Lu, Minzhe Guo, Liyue Shen, and Qing Qu. The emergence of
reproducibility and consistency in diffusion models. arXiv preprint arXiv:2310.05264, 2023.
Kai Zhang, Wangmeng Zuo, Yunjin Chen, Deyu Meng, and Lei Zhang. Beyond a gaussian denoiser:
Residual learning of deep cnn for image denoising. IEEE Transactions on Image Processing, 26
(7):3142–3155, 2017. doi: 10.1109/TIP.2017.2662206.
11

Published as a conference paper at ICLR 2024
A
EXPERIMENTAL DETAILS
A.1
TRAINING AND ARCHITECTURE DETAILS
Architectures.
We performed empirical experiments using two different architectures: UNet, and
BF-CNN. All the denoisers are “bias-free”: we remove all additive constants from convolution
and batch-normalization operations (i.e., the batch normalization does not subtract the mean). This
facilitates unversality (denoisers can operate at all noise levels), and interpretability (network trans-
formations are homogeneous of order 1, and the Jacobian provides a local characterization) - see
Mohan* et al. (2020).
UNet networks contain 3 decoder blocks, one mid-level block, and 3 decoder blocks (Ronneberger
et al., 2015). Each block consists of 2 convolutional layers followed by a ReLU non-linearity and
bias-free batch-normalization. Each encoder block is followed by a 2 × 2 spacial down-sampling
and a 2 fold increase in the number of channels. Each decoder block is followed by a 2 × 2 spacial
upsampling and a 2 fold reduction of channels. The total number of parameters is 7.6m.
BF-CNN networks Mohan* et al. (2020) are bias-free versions of DNCNN networks (Zhang et al.,
2017), contain 21 convolutional layers with no subsampling, each consisting of 64 channels. Each
layer, except for the first and the last, is followed by a ReLU non-linearity and bias-free batch-
normalization. All convolutional kernels are of size 3 × 3, resulting in 700k parameters in total.
Training.
We follow the training procedure described in Mohan* et al. (2020), minimizing the
mean squared error in denoising images corrupted by i.i.d. Gaussian noise with standard deviations
drawn from the range [0, 1] (relative to image intensity range [0, 1]). Training is carried out on batches
of size 512, for 1000 epochs. Note that all denoisers are universal and blind: they are trained to
handle a range of noise, and the noise level is not provided as input to the denoiser. These properties
are exploited by the sampling algorithm, which can operate without manual specification of the
step size schedule (Kadkhodaie & Simoncelli, 2020). This method produces high-quality results
in generative sampling, as well as sampling conditioned on linear measurements (Kadkhodaie &
Simoncelli, 2021).
Datasets.
For experiments shown in Figures 1 to 3 and 7, we use the CelebA dataset (Liu et al.,
2015) downsampled to 80×80 resolution. For experiments shown in Figures 9 and 10, we use images
drawn from the LSUN bedroom dataset (Yu et al., 2015) downsampled to 80 × 80 resolution. This
dataset is downsampled to 32 × 32 resolution for experiments shown in Figure 13. For experiments
shown in Figure 11 we use CelebA HQ dataset (Karras et al., 2018) downsampled to 40 × 40
resolution.
A.2
SAMPLING ALGORITHM
Sampling from both the DNN denoisers is achieved using the algorithm presented in Kadkhodaie &
Simoncelli (2020), which is specified below in Algorithm 1. Aside from initial and final noise levels
(σ0, σ∞), this method uses two hyperparameters h ∈[0, 1] and β ∈(0, 1], which control the step
size and injected noise respectively. We chose h = 0.01, β = 0.1, σ0 = 1, and σ∞= 0.05.
12

Published as a conference paper at ICLR 2024
Algorithm 1 Sampling via ascent of the log-likelihood gradient from a denoiser residual
Require: denoiser f, step size h, stochasticity from injected noise β, initial noise level σ0, final
noise level σ∞, distribution mean m
1: t = 0
2: Draw x0 ∼N(m, σ2
0Id)
3: while σt ≥σ∞do
4:
t ←t + 1
5:
st ←f(xt−1) −xt−1
▷Compute the score from the denoiser residual
6:
σ2
t ←||st||2/d
▷Compute the current noise level for stopping criterion
7:
γ2
t =

(1 −βh)2 −(1 −h)2
σ2
t
8:
Draw zt ∼N(0, I)
9:
xt ←xt−1 + hdt + γtzt
▷Perform a partial denoiser step and add noise
10: end while
11: return xt
B
ADDITIONAL NUMERICAL RESULTS ON GENERALIZATION
B.1
SIMILARITY BETWEEN DATA SUBSETS
0.0
0.2
0.4
0.6
0.8
1.0
cosine similarity
0.0
0.2
0.4
0.6
0.8
1.0
cosine similarity
Figure 6: Histogram of cosine similarity between pairs of closest images in the non-overlapping
subsets S1 and S2 of CelebA (left) and LSUN bedroom (right). Images with similarity score higher
than 0.95 are removed from the datasets before training to eliminate replicated images. This should
be compared with the histograms in Figures 2 and 10.
B.2
GENERALIZATION OF UNET MODEL
In this section, we show that convergence of model variance is robust to the change of data distribution
and architecture. The minimum size of the training set, N, for which the model transitions from
memorization to generalization indeed depends on the architecture, image size and data distribution.
Nevertheless, with enough data, two models trained on non-overlapping subsets of data converge to
virtually the same function.
B.2.1
TRAINED ON CELEBA DATASET
Figure 7: More examples to illustrate convergence of model variance for models shown in Figure 2, at
N = 105. Samples generated by each denoiser are shown in separate rows, where each column shows
same initialization across the networks. The networks generate nearly identical samples, showing
convergence to the same function.
13

Published as a conference paper at ICLR 2024
Figure 8: Bifurcation of trajectories. Sampling trajectories for the two samples shown in the last
column of Figure 7. The two diffusion models arrive at different samples starting from the same
initial point. The bifurcation of gradients appears to emerge somewhere around the middle of the
trajectories, which illustrates instabilities predicted by recent dynamical models (Biroli et al., 2024).
All the intermediate samples in the trajectories have been denoised in a on-shot denoising manner
using the corresponding denoisers. This example shows that the convergence is not perfect, hence the
distribution of cosine similarities at N = 105 is not perfectly a delta function at 1.
B.2.2
TRAINED ON LSUN BEDROOM DATASET
42
39
36
33
30
27
24
21
18
15
12
9
6
3
0
Input PSNR
9
12
15
18
21
24
27
30
33
36
39
42
45
48
51
54
57
60
63
Output PSNR
Train
42
39
36
33
30
27
24
21
18
15
12
9
6
3
0
Input PSNR
Test
N: 1
N: 10
N: 100
N: 1000
N: 10000
N: 100000
identity
Figure 9: Transition from memorization to generalization, for a UNet denoiser trained on bedroom
LSUN images (Yu et al., 2015) downsampled to 80 × 80. Similarly to denoisers trained on face
images shown in Figure 1, the model transitions from memorizing the training set to generalizing
outside of the training set. At N = 105 the performance is almost identical on training and test sets,
and the model is no longer overfitting the training data.
14

Published as a conference paper at ICLR 2024
Closest image from S1:
N=1
N=10
N=100
N=1000
N=10000
N=100000
Generated by models trained on S1:
Generated by models trained on S2:
Closest image from S2:
0.0
0.25
0.5
0.75
1.0
N = 10
0.0
0.25
0.5
0.75
1.0
N = 1000
0.0
0.25
0.5
0.75
1.0
N = 10000
0.0
0.25
0.5
0.75
1.0
N = 100000
Samples from two denoisers
Sample and closest train image
Figure 10: Convergence of model variance. Diffusion models are trained on non-overlapping subsets
S1 and S2 of a bedroom LSUN dataset. The subset size N varies from 1 to 105. Notice the samples
generated by network trained on N = 100 images: they are combinations of patches of training
images. This type of memorization has been previously reported in (Somepalli et al., 2023). See
caption of Figure 2 for a complete description of the figure.
B.3
GENERALIZATION OF BF-CNN MODEL
B.3.1
TRAINED ON CELEBA DATASET
42
39
36
33
30
27
24
21
18
15
12
9
6
3
0
Input PSNR
9
12
15
18
21
24
27
30
33
36
39
42
45
48
51
54
57
60
63
Output PSNR
Train
42
39
36
33
30
27
24
21
18
15
12
9
6
3
0
Input PSNR
Test
N: 1
N: 10
N: 100
N: 1000
N: 10000
identity
Figure 11: Transition from memorization to generalization, for a BF-CNN denoiser trained on CelebA
HQ dataset (Karras et al., 2018) downsampled to 40 × 40 resolution. See caption of Figure 1.
15

Published as a conference paper at ICLR 2024
Closest image from S1:
N=1
N=10
N=100
N=1000
N=10000
Generated by models trained on S1:
Generated by models trained on S2:
Closest image from S2:
0.0
0.25
0.5
0.75
1.0
N = 10
0.0
0.25
0.5
0.75
1.0
N = 100
0.0
0.25
0.5
0.75
1.0
N = 1000
0.0
0.25
0.5
0.75
1.0
N = 10000
Samples from two denoisers
Sample and closest train image
Figure 12: Convergence of model variance. BF-CNN denoisers are trained on non-overlapping
subsets S1 and S2 of CelebA HQ dataset. The subset size N varies from 1 to 104. See caption of
Figure 2.
B.3.2
TRAINED ON LSUN BEDROOM DATASET
Figure 13: Convergence of model variance on LSUN bedroom dataset (Yu et al., 2015). A dataset
of bedroom images is partitioned into two non-overlapping datasets, S1 and S2, each containing
N = 20, 000 images down-sampled to size 32 × 32. We train two networks (BF-CNN architecture
described in Appendix A) on S1 and S2. Each network is then used in an iterative deterministic
reverse diffusion algorithm to generate a sample, with both networks initialized with the same noise
image. Samples generated by each denoiser are shown in separate rows, where each column shows
same initialization across the networks. The networks generate nearly identical samples, showing
convergence to the same function.
16

Published as a conference paper at ICLR 2024
0.0
0.2
0.4
0.6
0.8
1.0
N = 20000
Samples from two denoisers
Sample and closest train image
Figure 14: Blue histogram: cosine similarity between samples generated by two denoisers trained
on non-overlapping training sets of size N = 20, 000 from LSUN bedroom dataset downsampled to
32 × 32 resolution. Orange histograms: cosine similarity between generated samples and the closest
image from the corresponding training set. Images drawn from the two denoisers are very similar to
each other, compared to the closest image in their respective training sets.
B.4
CONVERGENCE AS A FUNCTION OF TRAINING SET SIZE N AND IMAGE RESOLUTION
1.0
10.0
100.0
1000.0
10000.0
100000.0
N
0.001
0.01
0.1
1.0
10.0
100.0
PSNR gap (Train - Test)
d = 20x20
d = 40x40
d = 80x80
d = 160x160
Figure 15: Generalization as a function of training set size, N. Generalization is measured as the
difference between train and test PSNRs averaged across noise levels σ ∈[0, 1]. Each curve shows
average PSNR gap for a specific image resolution d × d. The capacity of the UNet is adjusted to
the image resolution. See Table 1 for specific UNet architecture used for each image resolution. As
expected, to reach the threshold PSNR gap, denoisers trained on larger images require more training
data. However, the number of training images does not increase proportionally with the image size:
the increase in needed to hit the threshold ∆N from 80 × 80 to 160 × 160 images is much smaller
than the ∆N from 40 × 40 to 80 × 80. This observation is consistent with previous reports indicating
that conditioned on coarser content of the image, learning the finer details requires less data due to
the conditional Markov property of images (Kadkhodaie et al., 2023).
Image resolution
number of encoder
decoder blocks
Receptive field size
number of parameters
20 × 20
1
18 × 18
360k
40 × 40
2
44 × 44
1.8m
80 × 80
3
92 × 92
7.6m
160 × 160
4
188 × 188
31m
Table 1: UNet architectures used in experiments shown in Figure 15. With the four-fold increase of
the image size, the number of parameters increases approximately four times.
17

Published as a conference paper at ICLR 2024
C
ADDITIONAL NUMERICAL RESULTS ON INDUCTIVE BIASES
C.1
MORE Cα EXAMPLES
Figure 16: BF-CNN denoisers trained on Cα images of size 40×40 achieve near-optimal performance.
Top. PSNR curves of trained networks for various regularity levels α. The empirical slopes achieved
for different values of α closely match the optimal slopes (dashed lines). Bottom. Eigenvectors for
two Cα images (top row: α = 4, bottom row: α = 2), which consist of harmonics on the two regions
and harmonics along the boundary. The frequency of the harmonics increases with k. For less regular
images, the harmonics are more localized along the contours.
Figure 17: Geometric-adaptive harmonic basis shown for three test images from Cα class. Here the
regularity of the one-dimensional contours α1 is different from the regularity of the two-dimensional

## Background

right: α1 = 1.5, 2, 4. Background regularity is the same in all three examples, α2 = 8, and σ = 0.2.
Bottom. Top 10 basis vectors for each image are shown. With increasing α1, the contours become
more regular, and the harmonics along the boundaries become less localized. This allows for a faster
decay of coefficients and a lower denoising error.
18

Published as a conference paper at ICLR 2024
Figure 18: Top. An additional example of a Cα test image with α = 3. Bottom. Top eigenvectors of
the geometric harmonic adaptive basis.
C.2
ADDITIONAL LOW-DIMENSIONAL MANIFOLD EXAMPLES
Figure 19: BF-CNN denoiser trained on a single face image, with intensity rescaling. We consider
an image class consisting of a single image x ∈Rd and its positive rescalings s x for s > 0. The
resulting images lie on a ray emanating from the origin, and optimal denoising corresponds to
projecting the noisy image onto this ray. The optimal denoising basis should therefore include the
normalized vector x/∥x∥with associated shrinkage factor λ = 1, whereas the remaining basis vectors
should have shrinkage factors of λ = 0 but are otherwise unconstrained. This optimal denoiser
achieves an MSE of σ2, and thus a linear PSNR curve with unit slope and intercept 10 log10(d).
Top left. Denoising of the training image with σ = 0.04. Right. Decay of the coefficients ⟨x, ek⟩
and the shrinkage factors λk. The DNN denoiser exhibits a slower decay of shrinkage factors than
the optimal solution, which results in suboptimal performance. Bottom left. Top 5 basis vectors
ek(y). The first basis vector is nearly identical to the (normalized) train image. The next vectors,
which have non-zero shrinkage factors, exhibit 2D harmonics. These GAHB components underlie
the non-optimal behavior of the denoiser. Specifically, the N = 1 curve in the left panel of Figure 11
shows that performance as a function of noise level falls below the optimal solution (dotted line). The
DNN performance has a unit slope over most of the noise range but has a less-than-optimal intercept
(the flattening of the curve at small noise levels is a result of de-emphasis of small noise levels during
training).
19

Published as a conference paper at ICLR 2024
Figure 20: A BF-CNN denoiser is trained on a set of 2D sine wave images with unit frequency
and varying phases and intensities. The train images thus lie on a 2D cone manifold with low
curvature. For small σ, the manifold can be assumed to be locally flat, so that the optimal denoising
is achieved by projecting the noisy image on the two-dimensional subspace tangent to the manifold.
This subspace is spanned by two sine waves with unit frequency and a π/2 phase shift. Top left.
Clean, noisy (σ = 0.08), and denoised test image. Middle left. The unit vectors spanning the
tangent subspace. The optimal denoising results from projection onto this subspace. Bottom row.
Empirical basis obtained from the network Jacobian. The empirical solution has a slower decay than
optimal (i.e., ⟨x, ek(y)⟩> 0 for k ≥2, as seen in the right panel), with harmonic patterns. This
sub-optimality reveals the nature of the inductive bias.
C.3
SHUFFLED FACES
Shuffled
Clean
Noisy
Denoised
5 = 1.182
17 = 1.07
29 = 0.974
41 = 0.91
53 = 0.87
0
1000
2000
3000
4000
5000
6000
k
0
2
4
6
8
10
12
14
16
x, ek
0.0
0.5
1.0
1.5
2.0
2.5
k(y)
42
39
36
33
30
27
24
21
18
15
12
9
6
3
0
input PSNR
10
22
35
output PSNR
non-shuffled
identity
Figure 21: DNN denoiser trained on a dataset of shuffled faces obtained by permuting the pixels
of 105 face images in the CelebA dataset. The permutation was chosen randomly, and does not
preserve locality, as neighboring pixels are mapped to independent positions. By construction, the
optimal denoiser on shuffled faces has the same performance as the optimal denoiser on ordinary faces
(unshuffling the image pixels, optimally denoising the face image, and then shuffling the pixels back).
For visualization purposes, we “unshuffle” the pixels by applying the inverse of the permutation to
the images before display. Top left. Clean (shuffled then unshuffled), noisy (unshuffled, σ = 0.3),
and denoised (unshuffled) images. Middle. The shrinkage factors λk(y) decay more slowly than
when the denoiser is trained on non-shuffled faces (Figure 3), which is indicative of suboptimality..
Right. The denoiser performs significantly worse than the denoiser trained on unshuffled faces: the
MSE is much higher with a much lower PSNR slope. Bottom left. Basis vectors (top row: shuffled,
bottom row: unshuffled). After unshuffling, we observe GAHBs adapted to the geometry of the face,
although these are noisier and less precisely aligned with the image features than the non-shuffled
examples in Figure 3.
20

Published as a conference paper at ICLR 2024
D
MATHEMATICAL DERIVATIONS
D.1
MIYASAWA RELATIONSHIPS
The relationship of MMSE estimation of a signal corrupted by additive Gaussian noise to the score
was published in Miyasawa (1961), and generalized in Raphan & Simoncelli (2011); Efron (2011).
For completeness, and notational consistency, we provide a derivation here. We begin by expressing
the score ∇log p(y) (dropping the σ dependence to simplify notation) and its Jacobian ∇2 log p(y)
in terms of the measurement density p(y|x) (which is Gaussian) and the posterior density p(x|y).
Using Bayes’ rule and marginalization, the probability density of the noisy images is expressed as
p(y) =
Z
p(x) p(y|x) dx.
Taking the logarithm and differentiating with respect to y, and using the fact that for any function h,
∇h(y) = h(y) ∇log h(y), we find
∇log p(y) =
Z
p(x) p(y|x) ∇y log p(y|x) dx

p(y)
=
Z
p(x|y) ∇y log p(y|x) dx
= E

∇y log p(y|x)
 y

,
(14)
which can be thought of as an equivalent of the chain rule on the scores as opposed to the densities.
Differentiating again with respect to y, we have
∇2 log p(y) =
Z
p(x|y)

∇y log p(x|y)∇y log p(y|x)T + ∇2 log p(y|x)

dx.
(15)
The term ∇y log p(x|y) can be calculated by differentiating the logarithm of Bayes rule:
log p(x|y) = log p(y|x) −log p(y) + log p(x),
∇y log p(x|y) = ∇y log p(y|x) −∇log p(y),
(16)
so that when injected into eq. (15) we obtain
∇2 log p(y) =
Z
p(x|y)
 ∇y log p(y|x) −∇log p(y)

∇y log p(y|x)T + ∇2 log p(y)

dx
= E
h ∇y log p(y|x) −∇log p(y)

∇y log p(y|x)T  y
i
+ E
h
∇2 log p(y|x)
 y
i
= Cov

∇y log p(y|x)
 y

+ E
h
∇2 log p(y|x)
 y
i
,
(17)
where the last line used ∇log p(y) = E

∇y log p(y|x)
 y

.
We then use the fact that y is obtained from x by adding Gaussian white noise of variance σ2Id:
log p(y|x) = −1
2σ2 ∥y −x∥2 + cst,
(18)
∇y log p(y|x) = −1
σ2 (y −x),
(19)
∇2
y log p(y|x) = −1
σ2 Id,
(20)
so that eqs. (14) and (17) become
∇log p(y) = 1
σ2 (E[x | y] −y),
∇2 log p(y) = 1
σ4 Cov[x | y] −1
σ2 Id.
21

Published as a conference paper at ICLR 2024
Finally, the above identities can be rearranged to yield the first- and second-order Miyasawa relation-
ships:
E[x | y] = y + σ2∇log p(y),
(21)
Cov[x | y] = σ2
Id + σ2∇2 log p(y)

.
(22)
Note that the optimal denoising error satisfies
E
h
∥x −E[x | y]∥2i
= E
h
E
h
tr(x −E[x | y])(x −E[x | y])T  y
ii
= E[tr Cov[x | y]].
D.2
CONTROL ON KULLBACK-LEIBLER DIVERGENCE
Equation (2) results from Theorem 1 of Song et al. (2021), considering the so-called “variance-
exploding” SDE dxt = dwt where (wt)t≥0 is a Brownian motion (t = σ2 then corresponds to the
noise variance), and letting the stopping time T go to infinity.
To reformulate the score-matching error as a denoising objective, we insert the Miyasawa equation (3)
as well as the expression of the score model sθ(y) = (fθ(y) −y)/σ2 into the score-matching error:
E
h
∥∇log pσ(y) −sθ(y)∥2i
= 1
σ4 E
h
∥E[x | y] −fθ(y)∥2i
.
(23)
We recall the decomposition of the denoising error when conditioning on y:
E
h
∥x −fθ(y)∥2i
= E
h
∥x −E[x | y]∥2i
+ E
h
∥E[x | y] −fθ(y)∥2i
,
(24)
so that inserting eq. (24) into eq. (23) yields
E
h
∥∇log pσ(y) −sθ(y)∥2i
= 1
σ4

E
h
∥x −fθ(y)∥2i
−E
h
∥x −E[x | y]∥2i
= 1
σ4

MSE(fθ, σ2) −MSE(f ⋆, σ2)

.
Combined with eq. (2), this proves eq. (5).
D.3
SURE OBJECTIVE
We decompose the MSE as follows:
E
h
∥x −f(y)∥2i
= E
h
∥(y −f(y)) −(y −x)∥2i
= E
h
∥y −f(y)∥2i
−2E[⟨y −x, y −f(y)⟩] + E
h
∥y −x∥2i
.
(25)
The last term is the total variance of the noise and is thus equal to σ2d. The middle term can be
rewritten with an integration by parts, using the fact that y −x = −σ2∇y log p(y|x):
E[⟨y −x, y −f(y)⟩] = −σ2
ZZ
∇y log p(y|x), y −f(y)

p(x) p(y|x) dx dy,
= −σ2
ZZ
∇yp(y|x), y −f(y)

p(x) dx dy,
= σ2
ZZ
tr(Id −∇f(y)) p(x) p(y|x) dx dy,
= σ2E[d −tr ∇f(y)].
(26)
Inserting eq. (26) into eq. (25), we then obtain
E
h
∥x −f(y)∥2i
= E
h
∥y −f(y)∥2i
+ 2σ2E[tr ∇f(y)] −σ2d,
(27)
proving the Stein’s Unbiased Risk Estimator of the MSE.
22

Published as a conference paper at ICLR 2024
D.4
OPTIMAL THRESHOLDING IN A BASIS
For completeness, we derive here the error of the fixed-basis oracle denoiser (Donoho & Johnstone,
1994; Donoho, 1995; Mallat, 2008).
We consider an oracle denoiser which computes
X
k
λk(x) ⟨y, ek⟩ek.
In practice, the denoiser does not have access to the clean image x, and the shrinkage factors λk
thus have to be estimated from the noisy image y alone. Note however that optimizing this oracle
estimator is non-trivial as the shrinkage factors have to be independent from the noise.
We can then compute its denoising error on a clean image x by averaging over the noise
E


x −
X
k
λk(x) ⟨y, ek⟩ek

2
x

= E
"X
k
(⟨x, ek⟩−λk(x) ⟨y, ek⟩)2
 x
#
= E
"X
k
((1 −λk(x))⟨x, ek⟩−λk(x)⟨z, ek⟩)2
 x
#
=
X
k

(1 −λk(x))2⟨x, ek⟩2 + λk(x)2σ2
,
(28)
where the last step used the fact that ⟨z, ek⟩∼N(0, σ2) independently from x. For each x and k, the
optimal oracle shrinkage factor λk(x) thus minimizes the quadratic function
(1 −λk(x))2⟨x, ek⟩2 + λk(x)2σ2,
which is achieved when
λk(x) =
⟨x, ek⟩2
⟨x, ek⟩2 + σ2 .
(29)
Injecting eq. (29) into eq. (28) gives the denoising error on x as
E


x −
X
k
λk(x) ⟨y, ek⟩ek

2
x

=
X
k
σ2⟨x, ek⟩2
⟨x, ek⟩2 + σ2 .
(30)
Incidentally, this error is also equal to σ2 P
k λk(x), similarly to the optimal denoiser as shown in
eq. (10).
The fraction
σ2⟨x,ek⟩2
⟨x,ek⟩2+σ2 is of the same order as min(⟨x, ek⟩2, σ2) up to a factor of 2, as we have the
inequalities for any a, b > 0
1
2 min(a, b) ≤
ab
a + b ≤min(a, b),
which follow from ab = min(a, b) max(a, b) and max(a, b) ≤a + b ≤2 max(a, b). We thus have
E


x −
X
k
λk(x) ⟨y, ek⟩ek

2
x

∼
X
k
min

⟨x, ek⟩2, σ2
=
X
⟨x,ek⟩2>σ2
σ2
+
X
⟨x,ek⟩2<σ2
⟨x, ek⟩2.
(31)
Let M be the number of terms in the left sum (that is, the number of ranks k such that ⟨x, ek⟩2 > σ2),
and xM = P
⟨x,ek⟩2>σ2⟨x, ek⟩ek be the M-term approximation of x. We then have
∥x −xM∥2 =

X
⟨x,ek⟩2<σ2
⟨x, ek⟩ek

=
X
⟨x,ek⟩2<σ2
⟨x, ek⟩2,
(32)
23

Published as a conference paper at ICLR 2024
so that plugging eq. (32) into eq. (31) gives
E


x −
X
k
λk(x) ⟨y, ek⟩ek

2
x

∼Mσ2 + ∥x −xM∥2.
(33)
This realizes a decomposition of the oracle denoising error into a denoising bias ∥x −xM∥2, which
corresponds to the signal variance that has been lost, and a denoising variance Mσ2, which cor-
responds to the noise variance that has been preserved (note that denoising bias and variance are
different than the model variance and model bias studied in the paper). The sum of the two terms
captures the efficiency of the approximation of x in the basis (ek).
Let us reorder the coefficients so that ⟨x, e1⟩2 ≥· · · ≥⟨x, ed⟩2(note that the ordering depends on
x), and assume that ⟨x, ek⟩2 ∼k−(α+1) for some α > 0. More precisely, we assume that there
exists two constants c, c′ independent of x and k such that c k−(α+1) ≤⟨x, ek⟩2 ≤c′ k−(α+1). By
definition of M,
⟨x, eM⟩2 > σ2 ≥⟨x, eM+1⟩2,
so that
c′ M −(α+1) > σ2 ≥c (M + 1)−(α+1).
We then have M −(α+1) ∼σ2, i.e., M ∼σ−2/(α+1), and thus Mσ2 ∼σ2α/(α+1). We also have
X
k>M
⟨x, ek⟩2 ≤c′ X
k>M
k−(α+1) ≤c′
Z +∞
M
t−(α+1)dt = c′
α M −α,
X
k>M
⟨x, ek⟩2 ≥c
X
k>M
k−(α+1) ≥c
Z +∞
M+1
t−(α+1)dt = c
α(M + 1)−α,
so that ∥x −xM∥2 ∼M −α ∼σ2α/(α+1). Finally, we have shown that the two terms in eq. (33) are
of the same order, and it follows that
E


x −
X
k
λk(x) ⟨y, ek⟩ek

2
x

∼Mσ2 + ∥x −xM∥2 ∼σ2α/(α+1).
Because the constants have been assumed to be independent of x, one can average over x to obtain
that the oracle MSE is ∼σ2α/(α+1).
E
GEOMETRIC Cα IMAGES
A continuous image x: [0, 1]2 →R is part of the geometric Cα class (Korostelev & Tsybakov, 1993;
Donoho, 1999; Peyré & Mallat, 2008) if it is uniformly α-Lipschitz over [0, 1]2 \ {γi}, where the
γi are uniformly α-Lipschitz curves in [0, 1]2 which do not intersect tangentially. A function f is
uniformly α-Lipschitz over a domain Ωif there exists a constant C such that for all x ∈Ω, there
exists a polynomial qx of degree ⌊α⌋such that for all y ∈Ω,
|f(y) −qx(y)| ≤C |x −y|α.
(34)
We explain how to generate numerically such images in Algorithm 2.
24

Published as a conference paper at ICLR 2024
Algorithm 2 Synthesis of a Cα image via integration
Require: regularity α, Fast Fourier Transform FFT
1: Make a contour
2: Define a 1D filter f1(ω) = |ω|−α
3: Draw a random 1D C0 function with i.i.d. uniform entries c(t) ∼U([−0.5, 0.5])
4: Integrate in the Fourier domain to define C = FFT−1(f1 × FFT(c))
5: Make the background
6: Define a 2D filter f2(ω) = (ω2
1 + ω2
2)−α/2
7: Draw two random 2D C0 functions with i.i.d. uniform entries b1(x, y), b2(x, y) ∼U([−0.5, 0.5])
8: Integrate in the Fourier domain to define Bi = FFT−1(f2 × FFT(bi)) (i = 1, 2)
9: Make a mask and combine
10: Define a binary mask M = 1y>C
11: Let x = M × B1 + (1 −M) × B2
12: return x
25
