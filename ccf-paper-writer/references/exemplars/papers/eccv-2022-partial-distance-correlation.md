# Partial Distance Correlation in Deep Learning


> **Venue:** ECCV2022

> **Source:** <https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136860318.pdf>


--- On the Versatile Uses of Partial Distance Correlation in Deep Learning Xingjian Zhen1 , Zihang Meng1 , Rudrasis Chakraborty2 , and Vikas Singh1 1 University of Wisconsin-Madison {xzhen3, zmeng29}@wisc.edu, vsingh@biostat.wisc.edu 2 Butlr rudrasischa@gmail.com


## Abstract


els, whether it is a single network over time or two (or more networks) during or post-training, is an essential step in understanding what they are learning (and what they are not), and for identifying strategies for regularization or efficiency improvements. Despite recent progress, e.g., comparing vision transformers to CNNs, systematic comparison of function, especially across different networks, remains difficult and is often

carried out layer by layer. Approaches such as canonical correlation analysis (CCA) are applicable in principle, but have been sparingly used so

far. In this paper, we revisit a (less widely known) from statistics, called distance correlation (and its partial variant), designed to evaluate correlation between feature spaces of different dimensions. We describe the steps

necessary to carry out its deployment for large scale models this opens the door to a surprising array of applications ranging from conditioning one deep model w.r.t. another, learning disentangled representations as well as optimizing diverse models that would directly be more robust to adversarial attacks. Our experiments suggest a versatile regularizer (or constraint) with many advantages, which avoids some of the common difficulties one faces in such analyses 1.



## Introduction


The extent to which popular architectures in computer vision even partly mimic human vision continues to be studied (and debated) in our community. But consider the following hypothetical scenario. Let us say that a fully functional computational model of the visual system perhaps a modern version of the Neocognitron [20] was somehow provided to us. And we wished to compare its behavior to modern CNN models [33,28]. To do so, two options appear sensible.

The first inspired by analogies between computational vision and biological vision would draw a correspondence between how simple/complex cells in the visual cortex process scenes and their induced receptive fields with those of activations of units/blocks in a modern deep neural network architecture [60].

While this process is often difficult to carry out systematically, it is powerful and, 1 Code is at https://github.com/zhenxingjian/Partial_Distance_Correlation

X. Zhen et al.

in some ways, has contributed to interest in biologically inspired deep learning, see [67]. Updated forms of this intuition associating different subsets of cells (or neural network units) to different semantic/visual concepts remains the default


## Approach


the hypothetical setting above is to pose it in an information theoretic setting.

That is, for two models ΘX and ΘY , we ask the following question: what has ΘX learned that ΘY has not? Or vice versa. The asymmetry is intentional because if we consider two random variables (r.v.) X, Y , the question simply takes the form of conditioning, i.e., compare P(X) versus P(X|Y ). This form suffices if our interest is restricted to the predictions of the two models. If we instead wish to capture the models behavior more globally when X and Y denote the full set of feature responses we can use divergence measures on high dimensional probability measures given by the two models (ΘX and ΘY ) responses on the training samples. Importantly, notice that our description assumes that, at least, the probability measures are defined on the same domain.

More general use cases. While the above discussion was cast as comparing two networks, it is representative of a broad basket of tasks in deep learning.

(a) Consider the problem of learning fair representations [71,17,70,44] where the model must be invariant to one (or more) sensitive attributes. We seek latent representations, say Ψpred(X) for the prediction task, which minimizes mutual information w.r.t. the latent representation relevant for predicting the sensitive attribute Ψsens(X). Indeed, if information regarding the sensitive attribute is partially preserved or leaks into Ψpred(X), the relative entropy will be low [49].

Observe that this calculation is possible partly because the latent space specifies the same probability space for the two distributions. (b) The setting is identical in common approaches for learning disentangled representations, where disentanglement is measured via various information theoretic measures [8,1,21,61]. If we

now segue back to comparing two different networks, but without the convenience of a common coordinate system to measure divergence, the options turn out to be limited. (c) Recently, in trying to understand whether vision Transformers see similar to convolutional neural networks [56], one option utilized recently was a kernel-based representation similarity, in a layer-by-layer manner. What we may actually want is a mechanism for conditioning for example, if one of the models is thought of a nuisance variable, we wish to check the residual in the other after the first has been controlled for (or marginalized out). Importantly, this should be possible without assuming that the probability distributions live in the same space (or networks ΘX and ΘY are the same).

A direct application of CCA? Consider two different feature spaces (X and Y), say in dimensions Rp and Rq, pertaining to feature activations from two different models. Comparison of these two feature spaces is possible. One natural choice is canonical correlation analysis (CCA) [5], a generalization of correlation, specifically suited when p ̸= q. The idea has been utilized for studying representation similarity in deep neural network models [48], albeit in a posttraining setting for reasons that will be clear shortly, as well as for identifying

more efficient training regimes (i.e., can lower layers be sequentially frozen after

On the Versatile Uses of Partial Distance Correlation in Deep Learning a certain number of timesteps). CCA has also been shown to be implementable within DNN pipelines for multi-view training, called DeepCCA [4], although efficiency can be a bottleneck limiting its broader deployment. A stochastic version of CCA suitable for DNN training with mini-batches has been proposed very recently, and strong experimental evidence was presented [47], also see [25].

Given that a stochastic CCA is now available, its extensions to the partial CCA setting are not yet available. If successful, this may eventually provide a scheme, suitable for deep learning, for controlling the influence of one model (or a set of variables) on another model.

This work. The starting point of this work is a less widely used statistical concept to measure the correlation between two different feature spaces (X, Y) of different dimensions, called distance correlation (and the method of dissimilarities). In shallow settings, CCA and distance correlation offers very similar functionality for the most part, they can be used interchangeably although distance correlation would also need specification of distances (or dissimilarities). In other words, CCA may be easier to deploy. On the other hand, deep variants of CCA involve specialized algorithms [4,47]. Further, deep versions of partial CCA have not been reported. In contrast, as long as feature distances can be calculated, the differences between the shallow and the deep versions of distance correlation are minimal at best, and adjustments needed are quite minor. These advantages carry over to partial distance correlation, directly enabling conditioning one model w.r.t. another (or using such a term as a regularizer). The main contribution of this paper is to study distance correlation (and partial distance correlation) as a powerful measure in a broad suite of tasks in vision. We review the relevant technical steps which enable its instantiation in deep learning settings and show its broad applications ranging from learning disentangled representations to understanding the differences between what two (or more) networks are learning to training mutually distinct deep models (akin to earlier works on M best solutions to MAP estimation in graphical models [19,69]) or training M diverse models for foreground-background segmentation as well as other tasks [27].

Related Works Four distinct lines of work are related to our development, which we review next.

Similarity between networks. Understanding the similarity between different networks is an active topic [38,24,50] also relevant in adversarial models [15,9].

Early attempts to compare neural network representations were approached via linear regression [58], whose applicability to nonlinear models is limited. As noted above, canonical correlation analysis (CCA) [3,31] is a suitable off-the-shelf


## Method


Projection-Weighted CCA [48], DeepCCA [4], and stochastic CCA [23] are all potentially useful. Recently, [37] studied the invariance properties for a good similarity measurement and proposed the centered kernel alignment (CKA). CKA offers invariance to invertible linear transformations, orthogonal transformations, and isotropic scaling. Separately, [51,56] used CKA to study similarities between deep and wide neural networks and also between different network structures.


X. Zhen et al.

Information theoretic divergence measures. Another body of related work pertains to approximately measuring the mutual information [12] to remove this information, mainly in the context of fair representation learning. Here, mutual information (MI) is measured between features and the sensitive attribute [49].

In [63], another information theoretic bound for learning maximally expressive representations subject to the given attributes is presented. In [10], MI between prediction and the sensitive attributes is used to train a fair classifier whereas [2] describes the use of inverse contrastive loss. Group-theoretic approaches have also been described in [11,45]. The work in [41] gives an empirical solution to remove specific visual features from the latent variables using adversarial training.

Repulsion/Diversity. If we consider the ensemble of neural networks, there are several different strategies to maintain functional diversity between ensemble members we acknowledge these results here because they are loosely related to one of the use cases we evaluate later. SVGD [14] shows the benefits of choosing the kernel to measure the similarity between ensemble members. In [13], the authors introduce a kernelized repulsive term in the training loss, which endows deep ensembles with Bayesian convergence properties. The so-called quality diversity (QD) is interesting: [53] tries to maximize a given objective function with diversity to a set of pre-defined measure functions [22,57]. When both the objective and measure functions in QD are differentiable, [18] offers an efficient way to explore the latent space of the objective w.r.t. the measure functions.

Distance correlation (DC). The central idea motivating our work is distance correlation described in [65]. It has been used in the analysis of nonlinear dependence in time-series [72], and feature screening in ultra high-dimensional data

analysis tasks [42] and we will review it in detail shortly.

Review: Distance (and Partial Distance) Correlation Given two random variables X, Y ∈R (in the same domain), correlation (say, the Pearson correlation) helps measure their association. One can derive meaningful conclusions by statistical testing. As noted in 1, one generalization of correlation to a higher dimension is CCA, which seeks to find projection matrices such that correlation among the projected data is maximized, see [5].

Benefits of Distance Correlation. In many applications, the notion of distances or dissimilarities appears quite naturally. Motivated by the need for a

scheme that can capture both linear and non-linear correlations when provided with such dissimilarity information, in [65], the authors proposed a new measure of dependence between random vectors, called distance correlation. The key benefits of distance correlation are: 1. The distance correlation R satisfies 0 R 1, and R = 0 if and only if X, Y are independent.

2. R(X, Y ) is defined for X and Y in arbitrary dimensions, e.g., R(X, Y ) is well-defined when X is of dimension p while Y is of dimension q for p ̸= q.

We focus on empirical distance correlation for n samples drawn from the unknown joint distribution, and review its calculation.


On the Versatile Uses of Partial Distance Correlation in Deep Learning For an observed random sample (x, y) = {(Xi, Yi) : i = 1, · · · , n} from the joint distribution of random vectors X in Rp and Y in Rq, define: &a _ {k, l } = \|X_k - X \quad \bar { a}_{k, \cdo t rac { 1}{n} \sum _{l= 1 }^n a _ {k,l} , \quad \bar {a}_{\cdot , l}=\frac {1}{n}a_{k,l}, \nonumber \\[-1em] &\bar {a}_{\cdot , \cdot } = \frac {1}{n^2} \sum _{k,l=1}^n a_{k,l}, \quad A_{k,l} = a_{k,l} - \bar {a}_{k,\cdot } -\bar {a}_{\cdot , l} + \bar {a}_{\cdot , \cdot } \label {eq:DC_A} (1) where k, l ∈{1, · · · , n}. Similarly, we can define bk,l = ∥Yk −Yl∥, and Bk,l = bk,l −¯bk,· −¯b·,l + ¯b·,·, and based on these quantities we have.

Definition 1. (Distance correlation) [65]. The empirical distance correlation Rn(x, y) is the square root of

\mat hc a R}_n^2 x, y) = \left \{ \b egin {ar ray} {c l }

\ fr ac { \mat hcal { V }_n^2(x, y)}{\sqrt {\mathcal {V}_n^2(x, x)\mathcal {V}_n^2(y, y)}} &, \mathcal {V}_n^2(x, x)\mathcal {V}_n^2(y, y) > 0\\ 0 &, \mathcal {V}_n^2(x, x)\mathcal {V}_n^2(y, y) = 0 \end {array} \right .

(2) where the empirical distance covariance (variance) Vn(x, y), Vn(x, x) are defined as V2 n(x, y) = k,l=1 Ak,lBk,l, V2 n(x, x) = k,l=1 A2 k,l, with A in (1).

Examples. We show a few simple 2D examples to contrast Pearson Correlation and Distance Correlation in Fig. 1. Notice that if the relationship between the two random variables is not linear, Pearson Correlation might be small while Distance Correlation remains meaningful.

Extensions to conditioning. Given three random variables X, Y , and Z, we want to measure the correlation between X and Y but controlling for Z (thinking of it as a nuisance variable), i.e., we want to estimate R(X|Z, Y |Z) = R(X, Y ; Z). Such a quantity is key in existing approaches in disentangled learning, deriving invariant representations and understanding what one or more networks are learning after concepts learned by another network have been accounted for. Consider how this task would be accomplished in linear regression.

We would project X and Y into the space of Z, and only use the residuals to measure the correlation. Nonetheless, defining partial distance correlation is more involved in [64], the authors introduced a new Hilbert space where we can define the projection of distance matrix. To do so, the authors calculate a U-centered matrix ˜A from the distance matrix (ak,l) so that the inner product of the U-centered matrices will be the distance covariance.

Definition 2. Let A = (ak,l) be a symmetric, real valued n n matrix (n > 2) with zero diagonal. Define the U-centered matrix ˜A = (˜akl) as follows.

\t il de {a}_{ kl } = \le ft \{ \begi n { array}{c l}\displays ty le a_{k,l } - \frac {1}{n-2}\sum _{i=1}^n a_{i,l} - \frac {1}{n-2}\sum _{j=1}^n a_{k,j} + \frac {1}{(n-1)(n-2)}\sum _{i,j=1}^n a_{i,j} &, k\neq l\\ 0 &, k=l \end {array} \right .


X. Zhen et al.

˜akl = ak,l − n −2 i=1 ai,l − n −2 j=1 ak,j + (n −1)(n −2) i,j=1 ai,j , k ̸= l , k = l (3) Further, the inner product between ˜A, ˜B is defined as ( ˜A· ˜B) := n(n−3) k̸=l ˜Ak,l ˜Bk,l, and is an unbiased estimator of squared population distance covariance V2(x, y).

Before defining partial distance covariance formally, we recall the definition of orthogonal projection on these matrices.

Definition 3. Let ˜A, ˜B, ˜C corresponding to samples x, y, z respectively, and let Pz⊥(x) = ˜A −( ˜ ( ˜ C) ˜C, Pz⊥(y) = ˜B −( ˜ ( ˜ C) ˜C denote the orthogonal projection of ˜A(x) onto ( ˜C(z))⊥and the orthogonal projection of ˜B(y) onto ( ˜C(z))⊥.

Now, we are ready to define the partial distance covariance and the partial distance correlation.

Definition 4. Let (x,y,z) be a random sample observed from the joint distribution of (X, Y, Z). The sample partial distance covariance is defined by: \label { eq : pdcov} \ text {p d ov} ( x, ;z)& = (P_{z^{\p erp }}(x) \cdot P_{z^{\perp }}(y)) = \frac {1}{n(n-3)}\sum _{i\neq j} \left (P_{z^{\perp }}(x) \right )_{i,j}\left (P_{z^{\perp }}(y)\right )_{i,j} (4) And the partial distance correlation is defined as: R2(x, y; z) := (Pz⊥(x)·Pz⊥(y)) ∥Pz⊥(x)∥∥Pz⊥(y)∥ where ∥Pz⊥(x)∥= (Pz⊥(x) · Pz⊥(x))1/2 is the norm.

Partial distance correlation enables asking various interesting questions. By projecting the original U-centered matrix ˜A onto ˜C, the correlation between the residual and ˜B will be a measure of what does X learn that Z does not.

Optimizing Distance Correlation in Neural Networks While distance correlation can be implemented in a differentiable way, and thereby used as an appropriate loss function in a neural network, we must take efficiency into account. For two p dimensional random variables, let the number of samples for the empirical estimate of DC be n. Observe that the total cost for computing (ak,l) is O(n2p), and the memory to store the intermediate matrices is also O(n2).

So, we use a stochastic estimate of DC by averaging over minibatches, with each minibatch containing m samples. We describe why this approximation is sensible.

Notation. We use ΘX, ΘY to denote the parameters of the neural networks, and X, Y as features extracted by the respective neural networks. Let the minibatch size be m, and the dataset D = (DX , DY) be of size n. We use (xt, yt)T t=1, xt ⊂ DX , yt ⊂DY to represent the data samples at step t, T is the total number of training steps. The distance matrices At, Bt are computed when given Xt, Yt using (1), which is of dimension m m for each minibatch. Further, we use (Xt)k to represent the kth element in Xt. And (At)k,l is the kth row and lth column element in the matrix At. The inner-product between two matrices A, B is defined as ⟨A, B⟩= Pm i,j(A)i,j(B)i,j.


On the Versatile Uses of Partial Distance Correlation in Deep Learning Objective function. Consider the case where we minimize DC between two networks ΘX, ΘY . Since the parameters between ΘX, ΘY are separable, we can use the block stochastic gradient iteration in [68] with some simple modifications.

To minimize the distance correlation, we need to solve the following problem \min _{\The ta _X,\ T het _Y} \ fra c {\l angle A( \ The ta _ X ;x) ,B( \Theta _Y;y) \ rangle } { \ sqrt { \langl e A(\ Th e ta _X;x) , A (\ Theta _X;x)\rangle \langle B(\Theta _Y;y),B(\Theta _Y;y)\rangle }} \\ (A)_{k,l} = & || (X)_k - (X)_l ||_2,\: X = \Theta _X(x), (B)_{k,l} = || (Y)_k - (Y)_l ||_2, \:\: Y = \Theta _Y(y) \nonumber We slightly abuse the notation of ΘX(x) as applying the network ΘX onto data x, and reuse A to simplify the notation A(ΘX; x) and the distance matrix. We can rewrite the expression (with A, B defined above) using: min _ {\T he ta _ X,\ Theta _ Y} \langle A, B \rangle \:\: \text {s.t.} \:\: & \max _{x\subset \mathcal {D_X}}\langle A,A\rangle \leq m; \:\: \max _{y\subset \mathcal {D_Y}}\langle B,B\rangle \leq m (6) where (x, y) are the minibatch of samples from the data space (DX , DY).

We can rewrite the above into the following equation similar to (1) in [68].

min _ {\The ta _ X,\Theta _Y } \P hi (\The t a _X,\Theta _Y) = \mathbb {E}_{x,y}f(\Theta _X,\Theta _Y;x,y) + \gamma (\Theta _X) + \gamma (\Theta _Y ) (7) where f(ΘX, ΘY ; x, y) is ⟨A, B⟩and (ΘX) encodes the convex constraint of network ΘX: maxx⊂DX ⟨A, A⟩m. Similarly, (ΘY ) encodes maxy⊂DY⟨B, B⟩ m. Φ(ΘX, ΘY ) is the constrained objective function to be optimized.

Block stochastic gradient iteration. We adjust Alg. 1 from [68] to our case in Alg. 1. Since we will need the entire minibatch (xt, yt) to compute the objective function, there will be no mean term when computing the sample gradient ˜gt Further, since both blocks (ΘX, ΘY ) are constrained, line 3, 5 will use (5) from [68]. The detailed algorithm is presented in Alg. 1. Algorithm 1 Block Stochastic Gradient for Updating Distance Correlation Input: Two neural network with starting point Θ1 X, Θ1 Y . Training data {(xt, yt)}T t=1, step size ηX, ηY , and batch size m.

Output: ˜ΘT X, ˜ΘT 1: for t = 1, · · · , T do Compute sample gradient for ΘX ˜gt X = ∇ΘX f(Θt X, Θt Y ; xt, yt) Θt+1 = arg minΘX ⟨˜gt X + ˜∇X(Θt X), ΘX −Θt X⟩+ X∥2 Compute sample gradient for ΘY ˜gt Y = ∇ΘY f(Θt+1 X , Θt Y ; xt, yt) Θt+1 = arg minΘY ⟨˜gt Y + ˜∇Y (Θt Y ), ΘY −Θt Y ⟩+ Y ∥2 6: end for 7: ˜ΘT X = 1 t=1 Θt 8: ˜ΘT Y = 1 t=1 Θt

X. Zhen et al.

Proposition 1. After T iterations of Algorithm 1 with step size ηX = ηY = T < 1 L, for some positive constant η < 1 L, where L is the Lipschitz constant of the partial gradient of f, by Theorem. 6 in [68], we know there exists an index subsequence T such that: lim _{t \rightarrow \infty ,t\in \mathcal {T}} \mathbb {E}[\text {dist}(\mathbf {0}, \nabla \Phi (\Theta _X^t,\Theta _Y^t))]=0 (8) where dist(y, X) = minx∈X ∥x −y∥.

But empirically, we find that simply applying Stochastic Gradient Decent (SGD) is sufficient, but this choice is available to the user.

Independent Features Help Robustness Goal. We show how distance correlation can help us train multiple deep networks that learn mutually independent features, roughly similar to finding diverse M-best solutions in structured SVM models [59]. We describe how such an


## Approach


Rationale. Recently, several efforts have explored generating of adversarial examples that can transfer to different networks and how to defend against such attacks [15,62,6]. It is often observed that an adversarial sample for one trained network is relatively easy to transfer to another network with the same architecture [15]. Here, we show that even for as few as two networks (same architecture;

trained on the same data), we can, to some extent, prevent adversarial examples from transferring between them by seeking independent features.

Setup. We formulate the problem considering a classification task as an example.

Given two deep neural networks with the same architecture denoted as f1(·), f2(·), we train them using image-label pairs (x, y) using the cross-entropy loss LossCE.

If we train f1 and f2 using only the cross-entropy loss, the adversarial examples generated on f1 can relatively easily transfer to f2 (see the performance of Baseline in Table 1). To enforce f1 and f2 to learn independent features, let the extracted feature of x in some intermediate layer of f be given as g(x) (in this section we use the feature before the last fully connected layer as an example).

We can still train f1 using LossCE, and then, we train f2 using, \text { L oss}_{\text { to t a l }} = \text {L oss}_{\text {CE}}(f_2(x),y) + \alpha \cdot \text {Loss}_{\text {DC}}(g_1(x), g_2(x)) \label {ce_dc_loss} (9) where is a constant scalar and LossDC is the distance correlation from Def. 1.

Note that we do not require g1(x) and g2(x) to be in the same dimension, so in principle we could easily use features from different layers for these two networks.

Experimental settings. We first conduct experiments on CIFAR10 [39] using Resnet 18 [28]. We then use four different architectures (mobilenet-v3-small [32], efficientnet-B0 [66], Resnet 34, and Resnet152) and train them on ImageNet [40].

For each network architecture, we first train two networks using only LossCE.

Next, we train a network using only LossCE before training a second network using the loss in (9). On CIFAR10, we utilize the SGD optimizer with momentum 0.9 and train for 200 epochs using an initial learning rate 0.1 with a cosine learning rate scheduler [52]. The mini-batch size is set to 128. On ImageNet [40],

On the Versatile Uses of Partial Distance Correlation in Deep Learning
Table 1: The test accuracy (%) of a model f2 on the adversarial examples generated

using f1 with the same architecture. Baseline: train without constraint. Ours: f2 is independent to f1. Clean: test accuracy without adversarial examples.

Dataset Network


## Method


CIFAR10 Resnet 18 Baseline 89.14 CIFAR10 Resnet 18 Ours ImageNet Mobilenet-v3-small Baseline 47.16 ImageNet Mobilenet-v3-small Ours ImageNet Efficientnet-B0 Baseline 57.85 ImageNet Efficientnet-B0 Ours ImageNet Resnet 34 Baseline 64.01 ImageNet Resnet 34 Ours ImageNet Resnet 152 Baseline 66.88 ImageNet Resnet 152 Ours we train for 40 epochs using an initial learning rate 0.1, which decays by 0.1 every 10 epochs. The mini-batch size is 512. Our in (9) is set to 0.05 for all cases. For each combination of the dataset and the network architecture, we train two networks f1 and f2, after which we generate adversarial examples on f1 and use them to attack f2 and measure its classification accuracy. We construct a baseline by training f1 and f2Baseline without constraints. And train f2Our using (9) to learn independent features w.r.t. f1. We report performance under two widely used attack methods: fast gradient sign method (FGM) [26] and projected gradient descent method (PGD) [46], where the latter is considered among the strongest attacks. The scale ϵ of the adversarial perturbation is chosen from {0.03, 0.05, 0.1} and the maximum number of iterations of PGD is set to 40.



## Results


improvement in accuracy over the baseline under adversarial attacks, with comparable performance on clean inputs. Notably, our method achieves more than

10% absolute improvement in accuracy under PGD attack on Resnet-18 and Mobilenet-v3-small. This provides evidence supporting the benefits of enforcing the networks to learn independent features using our distance correlation loss.

In Fig. 2, we show correlation results using Picasso [29,7] to lower the dimension of features for each network. The embedding dimension is 2 for visualization.


In Fig. 2(a), we show the embedding of different networks. f1 represents the Fig. 2: Picasso visualization of features space and the correlation between different models. (a) Feature space distribution. (b) Cross-correlation between the feature space of f1 and f2 trained with/without DC. We get better independence. (c) By increasing the balance parameter of DC loss, Mobilenet is more independent to f1.


X. Zhen et al.

network to generate the adversarial examples. f2Baseline denotes the baseline network, trained without distance correlation constraint. Also, f2Ours is the same network trained to be independent to f1. In Fig. 2(b), we visualize the correlation between f1 and f2Baseline for each dimension, and the correlation between f1 and f2Ours. If the scatter plot looks circle-like, we can infer that the two models are independent. We see that in different networks, the use of DC shows stronger independence. From Fig. 2/Tab. 1, we also see that the more independent the models are, the better is the gain for transferred attack robustness.

Informative Comparisons between Networks Overview. As discussed in 1, there is much interest in understanding whether two different models learn similar concepts from the data for example, whether vision Transformers see similar to convolutional neural networks [56]. Here, we first follow [56] and discuss similarities between different layers of ViT and ResNets using distance correlation. Next, we investigate that after taking out the influence of Resnets from ViT (or vice versa), what are the residual learned concepts remaining in the network.

Measure Similarity between Neural Networks Goal. We first want to understand whether ViTs represent features across all layers differently from CNNs (such as Resnets). However, analyzing the features in the hidden layers can be challenging, because the features are spread across neurons. Also, different layers have different numbers of neurons. Recently, [56] applied the Centered Kernel Alignment (CKA) for this task. CKA is effective because it involves no constraint on the number of neurons. It is also independent to

the orthogonal transformations of representations. Here, we want to demonstrate that distance correlation is a reasonable alternative for CKA in these settings.

Experimental settings. First, as described in [56], we show that similarity between layers within a single neural network can be assessed using distance correlation (see Fig. 3(a) ). We pick ViT Base with patch 16, and three commonly used Resnets. All networks are pretrained on ImageNet. For ViT, we pick the embedding layer and all the normalization, attention, and fully connected layers Fig. 3: (a) Left 4: Similarity between layers within one single model. ViT can be split into small blocks and the similarity from shallow layers to the deeper layers is higher.

Most Resnet models show few large blocks in the network, and the last few layers share minimal similarity with the shallow layers. (b) Right 3: Similarity between layers across ViT and Resnets. In the initial 1/6 layers (highlighted in green), the two networks share high similarity. And the last few layers share the least similarity

On the Versatile Uses of Partial Distance Correlation in Deep Learning within each block. The total number of layers is 63. For Resnets, we use all convolutional layers and the last fully connected layer, which is the same counting


## Method



## Results


we find that the ViT layers can be split into small blocks and the similarity between different blocks from shallow layers to the deeper layers is higher. For most Resnets, the feature similarity shows that there are a few large blocks in the network, which contains more than 30 layers each, and the last few layers share minimal similarity with the shallow layers.

Results (b). After within-model distance correlation, we perform across-model distance correlation comparisons between ViT and Resnets, see Fig. 3(b). We notice that in the initial 1/6 layers, the two networks share high similarities. But later, the similarity spreads across all different layers between ViT and Resnets.

Notably, the last few layers share the least similarity between two networks.

By using the distance correlation to calculate the heatmap of the similarity matrices, we can qualitatively describe the difference between the patterns of the features in different layers from different networks. What is even more interesting is to quantitatively show the difference, for example, to answer which network contains more information for the ground truth classes. We discuss this next.

What Remains When Taking out Y from X Goal. Even measuring information contained in one neural network is challenging, and often tackled by measuring the accuracy on the test dataset. But the association between accuracy and the information contained in a network may be weak. Based on existing literature, conditioning one network w.r.t. another remains unresolved. Despite the above challenges, we can indeed measure the similarity between the features of the network X and the ground truth labels.

If the similarity is higher, we can say that the feature space of X contains more information regarding the true labels. Distance correlation enables this.

Interestingly, partial distance correlation extends this idea to multiple networks allowing us to approach the conditioning question posed above.

Rationale/setup. Here, we choose the last layer before the final fully-connected layer as the feature layer similar to the setup in 4. Our first attempt involved directly applying the distance correlation measurement to feature X and the one-hot ground truth embedding. However, the one-hot embedding for the label contains very little information, e.g., it does not show the difference between cat vs. dog and cat vs. airplane. So, we use the pretrained BERT [16] to linguistically embed the class labels into the hidden space. We then measure the distance correlation between the feature space of X and the pretrained hidden space GT. R2(X, GT) = m Pn/m t=1 dCor(xt, gtt) where xt is the feature for one minibatch, and gtt is the BERT embedding vector of the corresponding label. To further extend this metric to measure the remaining or residual information, we apply the partial distance correlation calculation by removing Y out of X, or say X conditioned on Y . Then, we have R2 ((X|Y ), GT) = m Pn/m t=1 dCor ((xt|yt), gtt) using (4). This capability has not been shown before.


X. Zhen et al.

Table 2: Partial DC between the network ΘX conditioned on the network ΘY , and the

ImageNet class name embedding. The higher value indicates the more information.

Network ΘX Network ΘY R2(X, GT ) R2(Y, GT ) R2((X|Y ), GT ) R2((Y |X), GT ) ViT1 Resnet 182 ViT Resnet 503 ViT Resnet 1524 ViT VGG 19 BN5 ViT Densenet1216 ViT large7 Resnet 18 ViT large Resnet 50 ViT large Resnet 152 ViT large ViT ViT+Resnet 508 Resnet 18 Resnet 152 Resnet 18 Resnet 152 Resnet 50 Resnet 50 Resnet 18 Resnet 50 VGG 19 BN Accuracy: 1. 84.40%; 2. 69.76%; 3. 79.02%; 4. 82.54%; 5. 74.22%; 6. 75.57%; 7. 85.68%; 8. 84.13% Experimental settings. In order to measure the information remaining when conditioning network ΘY out of ΘX, we first use pretrained networks on ImageNet.

We use the validation set of the ImageNet for evaluation. We want to evaluate which network contains the richest information regarding linguistic embedding.

Interestingly, we can go beyond such an evaluation, instead, asking the network ΘX to learn concepts above and beyond what the network ΘY has learned. To do so, we include the partial distance correlation into the loss. Unlike the experiment discussed above (minimizing distance correlation), in this setup, we seek to maximize partial distance correlation. The Losstotal is \text {Loss }_ { \ t ext {CE }}(f_1(x),y) - \alpha \cdot \text {Loss}_{\text {PDC}}\left ( (g_1(x)| g_2(x)), gt \right ) \label {pdc_loss} (10) We take pretrained networks ΘX, ΘY and then finetune ΘX using (10). The learning rate is set to be 1e −5 and in the loss term is 1. To check the benefits of partial DC, we use Grad-CAM [60] to highlight the areas that each network is looking at, together with what ΘX conditioned on ΘY sees then.

Results (a). We first show information comparison between two networks. The details of DC and partial DC are shown in Table. 2. The reader will notice that since ViT achieves the best test accuracy, it also contains the most information.

Additionally, although better test accuracy normally coincides with more information, this is not always true. Resnet 50 contains more linguistic information than

the much deeper Resnet 152, perhaps a compensation mechanism. For Resnet 152, the network is deep enough to focus on local structures that overwhelm the linguistic information (or this information is unnecessary). This experiment suggests a new strategy to compare two networks beyond test accuracy.

Results (b). After using a pretrained network, we can also check that by including the partial distance correlation in the loss, which regions does the model pay attention to, using Grad-CAM. We replace the loss term of Grad- CAM with the partial distance correlation. The results are shown in Fig. 4. We see that the pretrained ViT sees across the whole image in different locations, while

On the Versatile Uses of Partial Distance Correlation in Deep Learning the Resnet (VGG) tends to focus on only one area of the image. After training, ViT (conditioned on Resnet) pays more attention to the subjects, especially locations outside the Resnet focus. Such experiments help understand how ViT learns beyond Resnets (CNNs).

Disentanglement Overview. This experiment studies disentanglement [30,36,8,43,21]. It is believed that the image data are generated from low dimensional latent variables

but isolating and disentangling the latent variables is challenging. A key in disentangled latent variable learning is to make the factors in the latent variables independent [2]. Distance correlation fits perfectly and can handle a variety of dimensions for the latent variables. When the distance correlation is 0, we know that the two variables are independent.

Experimental settings. We follow [21] which focuses on semi-supervised disentanglement to generate high-resolution images. In [21], one divides the latent

variables into two categories: (a) attributes of interest a set of semantic and interpretable attributes, e.g. hair color and age; (b) residual attributes the remaining information. Formally, xi = G(f 1 i , ..., f k i , ri), where G is the generator that uses the factors of interest f l i and the residual to generate image xi.

In order to enforce the condition that the information regarding the attributes of interest is not leaking into the residual representations, the authors of [21] introduced the loss Lres = Pn i=1 ||ri||2 to limit the residual information. This is Fig. 4: Grad-CAM results on ImageNet using ViT, Resnet18 and VGG16. After using Partial DC to remove the information learned by another network, ViT can focus on detail places and Resnet can only look in major spots. Similar issue happens to VGG.


X. Zhen et al.

sub-optimal as there can be cases where ri is not 0 but still independent to the factors of interest (f l i)k l=1. Thus, we use distance correlation to replace this loss: \t e xt {L}_ {\ t ex t {r e s}} =dCor([f^1;f^2;...;f^k], r) \label {eq:disent} (11) We use the same structure proposed in [21], while the generator architecture is adopted from StyleGAN2 [35]. The dataset is the human face dataset FFHQ [34], and the attributes are: age, gender, etc. We use CLIP [54] to partially label the attributes to generate the semi-supervised dataset for training. All losses from [21] are used, except that Lres is replaced by (11).

Results. (Shown in Fig. 5) Our model shows the ability to change specific attributes without affecting residual features, such as posture (also see supplement).


Conclusions In this paper, we studied how distance correlation (and partial distance correlation) has a wide variety of uses in deep learning tasks in vision. The measure

offers various properties that are often enforced using alternative means, that are often far more involved. Further, it is extremely simple to incorporate in contrast to various divergence-based measures often used in invariant representation learning. Notably, the use of partial distance correlation offers the ability of

conditioning, which is underexplored in the community. We showcase three very different settings, ranging from network comparison to training distinct/different models to disentanglement where the idea is immediately beneficial, and expect that numerous other applications will emerge in short order.

Acknowledgements. Research supported in part by NIH grants RF1 AG059312, RF1 AG062336, and RF1AG059869, and NSF grant CCF #1918211.

Fig. 5: Representative generated images using our training on FFHQ. Note that these results only use semi-supervised dataset by CLIP. Our methods shows the ability to disentangle the attributes of interest and the remaining information.


On the Versatile Uses of Partial Distance Correlation in Deep Learning References 1. Achille, A., Soatto, S.: Emergence of invariance and disentanglement in deep representations. The Journal of Machine Learning Research 19(1), 19471980 2. Akash, A.K., Lokhande, V.S., Ravi, S.N., Singh, V.: Learning invariant representations using inverse contrastive loss. In: Proceedings of the AAAI Conference on

Artificial Intelligence. vol. 35, pp. 65826591 (2021) 3. Anderson, T.W.: An introduction to multivariate statistical analysis. Tech. rep.

4. Andrew, G., Arora, R., Bilmes, J., Livescu, K.: Deep canonical correlation analysis.

In: International conference on machine learning. pp. 12471255. PMLR (2013) 5. Bach, F.R., Jordan, M.I.: A probabilistic interpretation of canonical correlation analysis (2005) 6. Chan, A., Tay, Y., Ong, Y.S.: What it thinks is important is important: Robustness transfers through input gradients. In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. pp. 332341 (2020) 7. Chari, T., Banerjee, J., Pachter, L.: The specious art of single-cell genomics. bioRxiv 8. Chen, R.T., Li, X., Grosse, R., Duvenaud, D.: Isolating sources of disentanglement in vaes. In: Proceedings of the 32nd International Conference on Neural Information Processing Systems. pp. 26152625 (2018) 9. Cheng, S., Dong, Y., Pang, T., Su, H., Zhu, J.: Improving black-box adversarial attacks with a transfer-based prior. Advances in neural information processing systems 32 (2019) 10. Cho, J., Hwang, G., Suh, C.: A fair classifier using mutual information. In: 2020 IEEE International Symposium on Information Theory (ISIT). pp. 25212526.

IEEE (2020) 11. Cohen, T., Welling, M.: Group equivariant convolutional networks. In: International conference on machine learning. pp. 29902999. PMLR (2016) 12. Cover, T.M.: Elements of information theory. John Wiley & Sons (1999) 13. DAngelo, F., Fortuin, V.: Repulsive deep ensembles are bayesian. Advances in Neural Information Processing Systems 34 (2021) 14. DAngelo, F., Fortuin, V., Wenzel, F.: On stein variational neural network ensembles.

arXiv preprint arXiv:2106.10760 (2021) 15. Demontis, A., Melis, M., Pintor, M., Jagielski, M., Biggio, B., Oprea, A., Nita- Rotaru, C., Roli, F.: Why do adversarial attacks transfer? explaining transferability of evasion and poisoning attacks. In: 28th {USENIX} Security Symposium

({USENIX} Security 19). pp. 321338 (2019) 16. Devlin, J., Chang, M.W., Lee, K., Toutanova, K.: Bert: Pre-training of deep bidirectional transformers for language understanding. arXiv preprint arXiv:1810.04805

17. Feldman, M., Friedler, S.A., Moeller, J., Scheidegger, C., Venkatasubramanian, S.: Certifying and removing disparate impact. In: proceedings of the 21th ACM SIGKDD international conference on knowledge discovery and data mining. pp.

18. Fontaine, M., Nikolaidis, S.: Differentiable quality diversity. Advances in Neural Information Processing Systems 34 (2021) 19. Fromer, M., Globerson, A.: An lp view of the m-best map problem. Advances in Neural Information Processing Systems 22, 567575 (2009)

X. Zhen et al.

20. Fukushima, K., Miyake, S., Ito, T.: Neocognitron: A neural network model for a mechanism of visual pattern recognition. IEEE transactions on systems, man, and cybernetics (5), 826834 (1983) 21. Gabbay, A., Cohen, N., Hoshen, Y.: An image is worth more than a thousand words: Towards disentanglement in the wild. Advances in Neural Information Processing Systems 34, 92169228 (2021) 22. Gaier, A., Asteroth, A., Mouret, J.B.: Discovering representations for black-box optimization. In: Proceedings of the 2020 Genetic and Evolutionary Computation Conference. pp. 103111 (2020) 23. Gao, C., Garber, D., Srebro, N., Wang, J., Wang, W.: Stochastic canonical correlation analysis. J. Mach. Learn. Res. 20, 1671 (2019)

24. Geirhos, R., Rubisch, P., Michaelis, C., Bethge, M., Wichmann, F.A., Brendel, W.: Imagenet-trained CNNs are biased towards texture; increasing shape bias improves accuracy and robustness. In: International Conference on Learning Representations (2019), https://openreview.net/forum?id=Bygh9j09KX 25. Gemp, I., Chen, C., McWilliams, B.: The generalized eigenvalue problem as a nash equilibrium. arXiv preprint arXiv:2206.04993 (2022) 26. Goodfellow, I.J., Shlens, J., Szegedy, C.: Explaining and harnessing adversarial examples. arXiv preprint arXiv:1412.6572 (2014) 27. Guzman-Rivera, A., Kohli, P., Batra, D., Rutenbar, R.: Efficiently enforcing diversity in multi-output structured prediction. In: Artificial Intelligence and Statistics. pp.

284292. PMLR (2014) 28. He, K., Zhang, X., Ren, S., Sun, J.: Deep residual learning for image recognition.

In: Proceedings of the IEEE conference on computer vision and pattern recognition.

pp. 770778 (2016) 29. Henderson, R., Rothe, R.: Picasso: A modular framework for visualizing the learning process of neural network image classifiers. arXiv preprint arXiv:1705.05627 (2017) 30. Higgins, I., Matthey, L., Pal, A., Burgess, C., Glorot, X., Botvinick, M., Mohamed, S., Lerchner, A.: beta-vae: Learning basic visual concepts with a constrained variational framework (2016) 31. Hotelling, H.: Relations between two sets of variates. In: Breakthroughs in statistics, pp. 162190. Springer (1992) 32. Howard, A., Sandler, M., Chu, G., Chen, L.C., Chen, B., Tan, M., Wang, W., Zhu, Y., Pang, R., Vasudevan, V., et al.: Searching for mobilenetv3. In: Proceedings of the IEEE/CVF International Conference on Computer Vision. pp. 13141324 33. Iandola, F., Moskewicz, M., Karayev, S., Girshick, R., Darrell, T., Keutzer, K.: Densenet: Implementing efficient convnet descriptor pyramids. arXiv preprint arXiv:1404.1869 (2014) 34. Karras, T., Laine, S., Aila, T.: A style-based generator architecture for generative adversarial networks. In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. pp. 44014410 (2019) 35. Karras, T., Laine, S., Aittala, M., Hellsten, J., Lehtinen, J., Aila, T.: Analyzing and improving the image quality of stylegan. In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. pp. 81108119 (2020) 36. Kim, H., Mnih, A.: Disentangling by factorising. In: International Conference on Machine Learning. pp. 26492658. PMLR (2018) 37. Kornblith, S., Norouzi, M., Lee, H., Hinton, G.: Similarity of neural network representations revisited. In: International Conference on Machine Learning. pp.

35193529. PMLR (2019)

On the Versatile Uses of Partial Distance Correlation in Deep Learning 38. Kornblith, S., Shlens, J., Le, Q.V.: Do better imagenet models transfer better?

In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. pp. 26612671 (2019) 39. Krizhevsky, A., Hinton, G., et al.: Learning multiple layers of features from tiny images (2009) 40. Krizhevsky, A., Sutskever, I., Hinton, G.E.: Imagenet classification with deep convolutional neural networks. Advances in neural information processing systems 41. Lample, G., Zeghidour, N., Usunier, N., Bordes, A., Denoyer, L., Ranzato, M.: Fader networks: Manipulating images by sliding attributes. In: NIPS (2017) 42. Li, R., Zhong, W., Zhu, L.: Feature screening via distance correlation learning.

Journal of the American Statistical Association 107(499), 11291139 (2012) 43. Locatello, F., Tschannen, M., Bauer, S., R¨atsch, G., Sch¨olkopf, B., Bachem, O.: Disentangling factors of variations using few labels. In: International Conference on Learning Representations (2019) 44. Lokhande, V.S., Akash, A.K., Ravi, S.N., Singh, V.: Fairalm: Augmented lagrangian


## Method


European Conference on Computer Vision: proceedings. European Conference on Computer Vision. vol. 12357, p. 365. NIH Public Access (2020) 45. Lokhande, V.S., Chakraborty, R., Ravi, S.N., Singh, V.: Equivariance allows handling multiple nuisance variables when analyzing pooled neuroimaging datasets.


In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. pp. 1043210441 (2022) 46. Madry, A., Makelov, A., Schmidt, L., Tsipras, D., Vladu, A.: Towards deep learning models resistant to adversarial attacks. In: International Conference on Learning Representations (2018), https://openreview.net/forum?id=rJzIBfZAb 47. Meng, Z., Chakraborty, R., Singh, V.: An online riemannian pca for stochastic canonical correlation analysis. In: Ranzato, M., Beygelzimer, A., Dauphin, Y., Liang, P., Vaughan, J.W. (eds.) Advances in Neural Information Processing Systems.

vol. 34, pp. 1405614068. Curran Associates, Inc. (2021), https://proceedings.

neurips.cc/paper/2021/file/758a06618c69880a6cee5314ee42d52f-Paper.pdf 48. Morcos, A.S., Raghu, M., Bengio, S.: Insights on representational similarity in neural networks with canonical correlation. In: NeurIPS (2018) 49. Moyer, D., Gao, S., Brekelmans, R., Galstyan, A., Ver Steeg, G.: Invariant representations without adversarial training. In: NeurIPS (2018)

50. Neyshabur, B., Sedghi, H., Zhang, C.: What is being transferred in transfer learning? In: Larochelle, H., Ranzato, M., Hadsell, R., Balcan, M., Lin, H. (eds.)

Advances in Neural Information Processing Systems. vol. 33, pp. 512523. Curran Associates, Inc. (2020), https://proceedings.neurips.cc/paper/2020/file/

0607f4c705595b911a4f3e7a127b44e0-Paper.pdf 51. Nguyen, T., Raghu, M., Kornblith, S.: Do wide and deep networks learn the same things? uncovering how neural network representations vary with width and depth.

In: International Conference on Learning Representations (2020) 52. Paszke, A., Gross, S., Massa, F., Lerer, A., Bradbury, J., Chanan, G., Killeen, T., Lin, Z., Gimelshein, N., Antiga, L., et al.: Pytorch: An imperative style, highperformance deep learning library. Advances in neural information processing

systems 32, 80268037 (2019) 53. Pugh, J.K., Soros, L.B., Stanley, K.O.: Quality diversity: A new frontier for evolutionary computation. Frontiers in Robotics and AI 3, 40 (2016)


X. Zhen et al.

54. Radford, A., Kim, J.W., Hallacy, C., Ramesh, A., Goh, G., Agarwal, S., Sastry, G., Askell, A., Mishkin, P., Clark, J., et al.: Learning transferable visual models from natural language supervision. In: International Conference on Machine Learning.

pp. 87488763. PMLR (2021) 55. Raghu, M., Gilmer, J., Yosinski, J., Sohl-Dickstein, J.: Svcca: Singular vector canonical correlation analysis for deep learning dynamics and interpretability. In: NIPS (2017) 56. Raghu, M., Unterthiner, T., Kornblith, S., Zhang, C., Dosovitskiy, A.: Do vision transformers see like convolutional neural networks? In: Ranzato, M., Beygelzimer, A., Dauphin, Y., Liang, P., Vaughan, J.W. (eds.) Advances in Neural Information Processing Systems. vol. 34, pp. 1211612128. Curran Associates, Inc. (2021), https://proceedings.neurips.cc/paper/2021/file/

652cf38361a209088302ba2b8b7f51e0-Paper.pdf 57. Rakicevic, N., Cully, A., Kormushev, P.: Policy manifold search: Exploring the manifold hypothesis for diversity-based neuroevolution. In: Proceedings of the Genetic and Evolutionary Computation Conference. pp. 901909 (2021) 58. Ramsay, J., ten Berge, J., Styan, G.: Matrix correlation. Psychometrika 49(3), 59. Schiegg, M., Diego, F., Hamprecht, F.A.: Learning diverse models: The coulomb structured support vector machine. In: ECCV (3). pp. 585599 (2016), https: //doi.org/10.1007/978-3-319-46487-9_36 60. Selvaraju, R.R., Cogswell, M., Das, A., Vedantam, R., Parikh, D., Batra, D.: Gradcam: Visual explanations from deep networks via gradient-based localization. In:

Proceedings of the IEEE international conference on computer vision. pp. 618626 61. Shu, R., Chen, Y., Kumar, A., Ermon, S., Poole, B.: Weakly supervised disentanglement with guarantees. In: International Conference on Learning Representations

62. Shumailov, I., Gao, X., Zhao, Y., Mullins, R., Anderson, R., Xu, C.Z.: Sitatapatra: Blocking the transfer of adversarial samples. arXiv preprint arXiv:1901.08121 (2019) 63. Song, J., Kalluri, P., Grover, A., Zhao, S., Ermon, S.: Learning controllable fair representations. In: The 22nd International Conference on Artificial Intelligence and Statistics. pp. 21642173. PMLR (2019) 64. Sz´ekely, G.J., Rizzo, M.L.: Partial distance correlation with methods for dissimilarities. The Annals of Statistics 42(6), 23822412 (2014)

65. Sz´ekely, G.J., Rizzo, M.L., Bakirov, N.K.: Measuring and testing dependence by correlation of distances. The annals of statistics 35(6), 27692794 (2007) 66. Tan, M., Le, Q.: Efficientnet: Rethinking model scaling for convolutional neural networks. In: International Conference on Machine Learning. pp. 61056114. PMLR 67. Wo´zniak, S., Pantazi, A., Bohnstingl, T., Eleftheriou, E.: Deep learning incorporating biologically inspired neural dynamics and in-memory computing. Nature

Machine Intelligence 2020(2), 325336 (2020) 68. Xu, Y., Yin, W.: Block stochastic gradient iteration for convex and nonconvex optimization. SIAM Journal on Optimization 25(3), 16861716 (2015) 69. Yadollahpour, P., Batra, D., Shakhnarovich, G.: Diverse m-best solutions in mrfs.

In: Workshop on Discrete Optimization in Machine Learning, NIPS (2011) 70. Zafar, M.B., Valera, I., Rogriguez, M.G., Gummadi, K.P.: Fairness constraints: Mechanisms for fair classification. In: Artificial Intelligence and Statistics. pp.

962970. PMLR (2017)

On the Versatile Uses of Partial Distance Correlation in Deep Learning 71. Zemel, R., Wu, Y., Swersky, K., Pitassi, T., Dwork, C.: Learning fair representations.

In: International conference on machine learning. pp. 325333. PMLR (2013) 72. Zhou, Z.: Measuring nonlinear dependence in time-series, a distance correlation


## Approach
