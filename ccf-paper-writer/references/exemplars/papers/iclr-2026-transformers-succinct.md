# Transformers are Inherently Succinct

> **Venue:** ICLR2026
> **Award:** Outstanding Paper
> **Source:** <https://openreview.net/forum?id=Yxz92UuPLQ>

---
Published as a conference paper at ICLR 2026
Pascal Bergstr¨aßer
RPTU Kaiserslautern-Landau
Kaiserslautern, Germany
bergstraesser@cs.uni-kl.de
Ryan Cotterell
ETH Z¨urich
Zurich, Switzerland
ryan.cotterell@inf.ethz.ch
Anthony W. Lin
RPTU Kaiserslautern-Landau and MPI-SWS
Kaiserslautern, Germany
lin@cs.uni-kl.de


## Abstract

We study succinctness as a measure of the expressive power of transformers.
Succinctnesshow compactly a formalism can describe a language relative to
other formalismsis a classical notion in logic and automata theory. We prove
that fixed-precision transformers are remarkably succinct: they can be exponen-
tially more succinct than both linear temporal logic (LTL) and recurrent neural
networks, and, by extension, state-space models, and doubly exponentially more
succinct than finite automata. In other words, there exist families of languages
describable by polynomial-size transformers whose smallest equivalent LTL for-
mula or recurrent neural network is exponentially large, and whose smallest equiv-
alent automaton is doubly exponentially large. We also establish matching upper
bounds, showing that any fixed-precision transformer can be converted to an LTL
formula with at most an exponential blow-upimproving a prior doubly expo-
nential translation. As a consequence of this succinctness, we show that basic
verification problems for transformers, such as emptiness and equivalence, are
provably intractable: specifically, EXPSPACE-complete.


## Introduction

Transformers (Vaswani et al., 2017) are the dominant architecture underlying most modern large
language models. A substantial body of recent theoretical work has investigated their expressive
power (Strobl et al., 2024; Barcel´o et al., 2024; Yang et al., 2024; Hahn, 2020; P´erez et al., 2021;
Chiang and Cholak, 2022; Jerad et al., 2025), their trainability and ability to generalize to unseen
strings of longer lengths (Zhou et al., 2024; Huang et al., 2025; Chiang and Cholak, 2022), and
the extent to which their behavior can be formally verified (S¨alzer et al., 2025). A key finding of
this line of work is that transformers with finite precisionthe setting most faithful to real-world
hardwarerecognize various classes of subregular languages depending on the exact assumptions
made (Yang et al., 2024; Barcel´o et al., 2024; Jerad et al., 2025; Li and Cotterell, 2025).
Subregular languages constitute strict subclasses of the regular languages. For instance, the subreg-
ular class of star-free languages are precisely those definable by regular expressions that replace the
Kleene star with intersection and complementation. The language abis star-free because it can be
written as ∅· b · a · ∅, whereas (aa)is not star-free (Straubing, 1994). By contrast, recurrent neural
networks (RNNs) can recognize all regular languages under a fixed precision assumption (Minsky,
1967; Siegelmann and Sontag, 1995; Merrill et al., 2020; Svete and Cotterell, 2023), making them
strictly more expressive than transformers as language recognizers. However, the strong empirical
performance of transformers invites the question as to whether expressive capacity is the most
revealing lens through which to compare architectures.
In this paper, we propose succinctness as an alternative lens for understanding the expressivity of
transformers. The succinctness of a language L with respect to a class C of language recognizers
(e.g., transformers, finite automata, and formulas in FO[<]) measures the size of the smallest

Published as a conference paper at ICLR 2026
C ∈C that recognizes L. In other words, succinctness tells us how many symbols are needed to
describe L with respect to the class C. Succinctness is a classical notion in logic and computer
science (Stockmeyer, 1974; Grohe and Schweikardt, 2004), where it sharpens expressive power
into a complexity-theoretic refinement: rather than asking only which languages a formalism can
recognize, succinctness asks how compactly each such language can be described within it. Greater
succinctness comes at a pricemore succinct formalisms typically have correspondingly harder
decision problems, since their compact descriptions force any decision procedure to unfold a larger
amount of underlying structure.
A well-known example concerns linear temporal logic (LTL;
Pnueli, 1977), which is expressively equivalent to the star-free languages (Libkin, 2004), and, hence,
also to the counter-free automata of McNaughton and Papert (1971). Despite this equivalence in
expressive power, LTL can be exponentially more succinct than finite automata (Sistla and Clarke,
1985), i.e., certain languages admit polynomial-size LTL formulas but require exponentially larger
automata. A direct consequence is that decision problems for LTL, such as checking whether a
formula recognizes a trivial language, are provably harder than the corresponding problems for
automata (Sistla and Clarke, 1985).
This paper offers a formal result, which can be summarized as follows: transformers can describe
certain languages extremely succinctly. Specifically, we show that transformers can be exponentially
more succinct than LTL and RNNs, and hence also state-space models (SSMs; Gu and Dao, 2023;
Merrill et al., 2024). Moreover, they are doubly exponentially more succinct than finite automata.
In concrete terms, there exist families of languages describable by polynomial-size transformers
that require exponentially larger LTL formulas or RNNs, and doubly exponentially larger automata.
We also establish matching upper bounds: we give a translation from finite-precision transformers
to LTL formulas of exponential size, significantly improving the doubly exponential translation
of Yang et al. (2024). It follows that for any fixed-precision transformer, there is an equivalent
LTL formula of exponential size and an equivalent finite automaton of doubly exponential size.1
The key technical ingredient behind these results is showing that transformers can count from
0 to 22N that is, implement doubly exponentially large countersvia a subtle encoding using
attention.
We then prove that the resulting languages require exponentially larger descriptions
as LTL formulas or RNNs, and doubly exponentially larger descriptions as finite automata. A
natural consequence of this succinctness is that analyzing transformers should be computationally
challenging. And, indeed, we show that checking whether a given transformer recognizes a trivial
language, is EXPSPACE-complete. Under standard complexity-theoretic assumptions, this means
that no algorithm can solve the problem in less than double exponential time.
The specific transformer model we study is the unique-hard attention transformer (UHAT), a simple
and widely used abstraction of self-attention (Yang et al., 2024; Jerad et al., 2025; Strobl et al., 2024;
Hao et al., 2022; Li and Cotterell, 2025; Hahn, 2020; Barcel´o et al., 2024; Bergstr¨aßer et al., 2024).
In particular, Jerad et al. (2025) show that expressivity bounds on UHATs entail corresponding
bounds on softmax transformers with fixed precision. Different results in this paper hold under
different precision assumptions: the UHAT upper bounds are stated for arbitrary rational weights,
whereas the corresponding RNN results assume fixed (finite) precision. Importantly, this means our
conclusions are valid in the setting that most faithfully mirrors real-world implementationsfixed
precision arithmetic.
PRELIMINARIES
We adopt the following notational conventions in this paper. We write N
def= {1, 2, 3, ...} for the
natural numbers and N0
def= {0, 1, 2, 3, ...} for the natural numbers including zero. Given N ∈
N, we define [N]
def= {1, ..., N}. Furthermore, we write Q for the rational numbers. We denote
scalars by lowercase italicized Latin letters, vectors by boldface lowercase italicized Latin letters,
and matrices by boldface uppercase italicized Latin letters. For a vector v = (v1, ..., vD), we write
vi:j
def= (vi, ..., vj) for all 1 i j D, and vi for its ith component. An alphabet is a finite, non-
empty set Σ of symbols. A word (also called a string) is a finite sequence of symbols a = a1...aN.
1This holds without exception: the LTL bound is the constructive translation of Prop. 13, and the automaton
bound is its composition with the standard exponential LTL-to-automaton conversion (Sistla and Clarke, 1985;
Vardi and Wolper, 1994); both are unconditional upper bounds on every fixed-precision transformer.

Published as a conference paper at ICLR 2026
We denote symbols using lowercase Latin letters and words as boldfaced lowercase Latin letters.
We write |a| = |a1...aN| = N for the length of a word a. We write Σfor the set of all words
including the empty word and Σ+ def= Σ\ {}. A language is a subset L ⊆Σ.
We assume familiarity with basic formal language theory and complexity theory; see Kozen (1997)
and Sipser (1997) for standard references. In particular, we work with finite automata and the
following complexity classes (Sipser, 1997):
P ⊆NP ⊆PSPACE ⊆EXP ⊆NEXP ⊆EXPSPACE.
P and NP are problems solvable by a Turing machine in polynomial and nondeterministic poly-
nomial time, respectively, and EXP and NEXP are their exponential-time counterparts. PSPACE
and EXPSPACE are problems solvable by a Turing machine in polynomial and exponential space,
respectively.
LINEAR TEMPORAL LOGIC
A formula in linear temporal logic (LTL) over an alphabet Σ is defined by the grammar
φ ::= ⊤| ⊥| Qa (a ∈Σ) | φ ∧φ | φ ∨φ | ¬φ | φ S φ | φ U φ.
Satisfaction of an LTL formula φ on a word a = a1...aN ∈Σ+ at position n ∈[N], written
a, n |= φ, is defined inductively (omitting the trivial cases for ⊤and ⊥):
a, n |= Qa
iff
an = a
(a ∈Σ)
a, n |= φ1 ∧φ2
iff
a, n |= φ1 and a, n |= φ2
a, n |= φ1 ∨φ2
iff
a, n |= φ1 or a, n |= φ2
a, n |= ¬φ1
iff
a, n ̸|= φ1
a, n |= φ1 S φ2
iff
for some j with 1 j < n: a, j |= φ2 and
for all k with j < k < n: a, k |= φ1
a, n |= φ1 U φ2
iff
for some j with n < j N: a, j |= φ2 and
for all k with n < k < j: a, k |= φ1
We also use the standard abbreviations
Pφ := ⊤S φ
Fφ := ⊤U φ
Yφ := ⊥S φ
An LTL formula φ recognizes the language L(φ) consisting of all words a ∈Σ+ where a, N |= φ.2
Example 1. The star-free language (ab)+ can be defined in LTL as
Qb ∧H
 Qb YQa
 (Qa ∧Y⊤) YQb
(1)
Eq. (1) asserts that the last letter is b, every b is preceded by a, and every a that has a predecessor
is preceded by b.
UNIQUE-HARD ATTENTION TRANSFORMERS
Symbol Embedding.
Let Σ be an alphabet. A symbol embedding is a function emb: Σ QD
for some D > 0.3 A symbol embedding naturally extends to a homomorphism Σ(QD), where
emb(a1...aN) = emb(a1), ..., emb(aN) for a1, ..., aN ∈Σ.
2For fragments that only allow U or F, we use a, 1 |= φ instead.
3We define transformers over arbitrary rational numbers, as this is the most general setting in which our
upper bounds hold. All results, however, carry over to fixed-precision arithmetic, i.e., a constant number of
bits per value, independent of input length. The lower bounds hold under the even stronger restriction to fixed-
precision integers. The precise statement of this carry-over depends on the formalization of fixed-precision
arithmetic adopted: standard floating-point representations (Goldberg, 1991) are not associative, so the value
of, for example, a dot product in an attention head can depend on the order in which its summands are evaluated.
Our claim should therefore be understood with respect to a fixed, deterministic evaluation order; algebraic
identities used in the proofs that rely on associativity (such as the order of summation) need to be re-checked
under any other choice.

Published as a conference paper at ICLR 2026
Attention layer.
A unique hard-attention (UHA) layer of width R > 0 is specified by:
Three affine transformations: A, B : QR QR and C : (QR QR) QS;
A mask predicate M : N N {0, 1}, defined as one of M(n, m)
def= 1 (no masking),
M(n, m)
def= 1[m < n] (strict future masking), or M(n, m)
def= 1[m > n] (strict past masking);
A tie-breaking function τ that selects an element of a finite, non-empty subset of N, defined
as either min (leftmost) or max (rightmost).
Given a sequence of N vectors v1, ..., vN ∈QR with N 1, the layer operates as follows. The
score function is defined as the dot product
S(vn, vm)
def= ⟨A(vn), B(vm)⟩
(2)
for all n, m ∈[N]. For each position n ∈[N], let
def= {m ∈[N] | M(n, m) = 1}
(3a)
def= {m ∈Un | ∀m′ ∈Un : S(vn, vm) S(vn, vm′)}
(3b)
be the set of unmasked positions and the subset of those that maximize the score, respectively. The
attention vector at position n is defined as an
def= vτ(Bn) if Un ̸= ∅and an
def= 0 otherwise. The
layer outputs the sequence C(v1, a1), ..., C(vN, aN).
ReLU layer.
A ReLU layer of width R > 0 applies, for a designated coordinate r ∈[R], the
ReLU function to the rth component of each input vector. Formally, define ρr : QR QR by
ρr(v)
def= (v1:r−1, max(0, vr), vr+1:R).
(4)
Given a sequence of N input vectors v1, ..., vN ∈QR with N 1, the layer outputs the sequence
ρr(v1), ..., ρr(vN) obtained by applying ρr position-wise. Equivalently, one could place a feed-
forward network at the end of each encoder layer (Hao et al., 2022; Barcel´o et al., 2024).
Transformer.
A unique hard-attention transformer (UHAT) is a length-preserving function
T : Σ+ (QS)+ obtained by composing a symbol embedding with a finite sequence of UHA and
ReLU layers of conformable width. To use a UHAT T : Σ+ (QS)+ as a language recognizer, we
equip it with an acceptance vector t ∈QS. The language recognized by T , denoted L(T ), consists
of all words a ∈Σ+ such that ⟨t, vN⟩> 0 with T (a) = v1, ..., vN ∈QS.4
BOOLEAN RASP
As an intermediate step in proving EXPSPACE-hardness for UHATs, we use Boolean RASP
(B-RASP; Yang et al., 2024), a programming language shown to be expressively equivalent to
UHATs. A B-RASP program P is a finite sequence of predicates P1, ..., PΠ ∈{0, 1}[N]. The
program operates on an input word a = a1...aN ∈Σ+. The first |Σ| predicates are defined as fol-
lows. For each a ∈Σ, there is a lookup function Qa ∈{0, 1}[N] defined by Qa(n) = 1 iff an = a.
We label these predicates P1, ..., P|Σ|. Each remaining predicate Pt+1, for t |Σ|, is built from
P1, ..., Pt by one of two operations.
A position-wise operation sets Pt+1(i) := R(i), where R(i) is a Boolean combination of
P1(i), ..., Pt(i).
An attention operation sets
Pt+1(i) := ◀▶j [M(i, j), S(i, j)] V (i, j) : D(i)
(5)
where ◀▶∈{◀, ▶} and we define the following operations
◀and ▶indicate leftmost and rightmost tie-breaking, respectively;
M(i, j) is a mask predicate as in the definition of a UHAT;
S(i, j) and V (i, j) are Boolean combinations of P1(i), ..., Pt(i) and P1(j), ..., Pt(j),
called the score predicate and value predicate, respectively;
4For fragments that only allow strict past masking, we use ⟨t, v1⟩instead.

Published as a conference paper at ICLR 2026
D(i) is a Boolean combination of P1(i), ..., Pt(i).
The semantics of the attention operation are as follows. For each i ∈[N], let
o(i)
def=
min{j ∈[N] | M(i, j) = 1 and S(i, j) = 1},
for ◀
max{j ∈[N] | M(i, j) = 1 and S(i, j) = 1},
for ▶.
(6)
Then Pt+1(i)
def= V (i, o(i)) if o(i) exists, and Pt+1(i)
def= D(i) otherwise.
We can view a B-RASP program as a language recognizer by asking whether PΠ(N) = 1.5
RECURRENT NEURAL NETWORKS
As with transformers, we treat recurrent neural networks as language acceptors, following Merrill
et al. (2020) and Weiss et al. (2018; 2024). We define a recurrent neural network (RNN) as
a quadruple (Σ, g, h0, f) where Σ is an alphabet, g: (QD Σ) QD is a transition function,
h0 ∈QD is an initial hidden state, and f : QD {⊥, ⊤} is an acceptance function. Consider
string a = a1...aN. For n 1, we define the nth hidden state hn
def= g(hn−1, an) inductively.
We say a is accepted iff f(hN) = ⊤. As a computational model, it is natural to assume RNNs
operate over a fixed precision, i.e., computation is always performed over rational numbers that
can be represented with a constant k number of bits. The details of the actual representation are not
important for our analysis. Therefore, the state space of the above RNN can be mapped to D-vectors
over {0, 1}k (instead of Q). The following proposition is now immediate.
Proposition 1. An RNN (Σ, g, h0, f) with g: (QD Σ) QD with fixed precision k can be
represented by a finite automaton with 2kD many states.
SIZE MEASURES AND SUCCINCTNESS
Let R be a finite representation of a language, i.e., in our case a UHAT, LTL formula, finite au-
tomaton, RNN, or B-RASP program. We define the size of R, denoted by |R|, as the length of its
minimal binary encoding. In measuring succinctness of RNN, we put the precision k in unary also
as part of the size measure; since we do not want to compare a transformer that uses a fixed precision
k and allow an RNN that uses a fixed precision 2k.
Definition 2 (f-more succinct). Let C(1) and C(2) be classes of finite representations of languages,
and let f : N N be a function. We say C(1) is f-more succinct than C(2) if there is a family of
languages {Ln}
n=1 together with representations R(1)
∈C(1) of Ln such that every R(2)
∈C(2)
representing Ln satisfies |R(2)
n | f(|R(1)
n |).
We say C(1) is exponentially more succinct than C(2) if it is f-more succinct for some f(n) ∈
Ω(2cnd) with c, d > 0, and doubly exponentially more succinct if for some f(n) ∈Ω(22cnd
) with
c, d > 0.
Definition 3 (g-bounded expansion). Let C(1) and C(2) be classes of finite representations of lan-
guages, and let g: N N be a function. We say C(1) has g-bounded expansion over C(2) if for
every language L and every choice of representation R(2) ∈C(2) of L, there is a representation
R(1) ∈C(1) of L with |R(1)| g(|R(2)|).
We say C(1) has polynomially bounded expansion over C(2) if it has g-bounded expansion for some
polynomial g, and exponentially bounded expansion if for some g(n) ∈O(2cnd) with c, d > 0.
Def. 2 and Def. 3 are duals. On one hand, Def. 2 is an existential lower-bound: it asks for a
witness family on which C(2) is forced to be at least f times bigger than C(1). On the other, Def. 3
is a universal upper-bound: it asks that on every language, every C(2) representation has a C(1)
translation of size at most g. Neither definition alone is antisymmetric, but together they pin the gap:
C(1) is f-more succinct and has g-bounded expansion over C(2) exactly when the size gap is at least
f on a witness family and at most g uniformly.
5As for UHATs, we use PΠ(1) = 1 if only strict past masking is allowed.

Published as a conference paper at ICLR 2026
THE SIZE OF SMALLEST WITNESS VIA NON-EMPTINESS PROBLEM
We now consider the problem of checking whether the language recognized by a UHAT or B-RASP
program is non-empty. In particular, the technique is essentially a simulation of a Turing machine
with an 2O(N)-sized tape for a given N. As we will see later, there are Turing machines such that
the shortest accepted word by the constructed UHAT is of length at least 22Ω(N).
Example 2. We consider an example with N = 4. Let Σ = {0, 1, #, a, b, c}, and let H
def=
{(a, b), (b, c), (b, a), (c, b)} be a set of constraints specifying which symbols can appear in adjacent
positions. We now describe a B-RASP program that accepts words of the form
such that (an, an+1) ∈H for all 1 n < 24. We show how to construct a B-RASP programs that
(i) check that the bit counter is incremented, and (ii) check that the successive symbols are in H.6
To check (i), we use the following attention operation:
C+1(i) := ▶j [j < i, Q#(j)]
k=1
k−1
r=1
 ¬Cr(i) ∧Cr(j)
∧Ck(i) ∧¬Ck(j)
r=k+1
 Cr(i) ↔Cr(j)
: 1
(7)
Assume i is a #-position. Attention selects the rightmost #-position j left of position i. Let bi
1...bi
and bj
1...bj
4 be the bit words directly left of position i and j, respectively. We assume that we already
defined Ck(i) = bi
k and Ck(j) = bj
k for all k ∈[4]. Then, the above value predicate checks that
the bit word bi
1...bi
4 is the bit word bj
1...bj
4 incremented by 1. To check (ii), we can use the attention
operation
M(i) := ▶j [j < i, Qa(j) ∨Qb(j) ∨Qc(j)]
(h,h′)∈H
Qh(j) ∧Qh′(i) : 1.
(8)
If i is a position of a symbol ai, attention picks the rightmost position j of a symbol aj to the left of i
and checks with the value predicate that (aj, ai) ∈H. Two boundary conditions remain: the input
must begin with the counter 0000 and end with the counter 1111. The first is a position-wise check
at the leftmost #, requiring C1(i) = ... = C4(i) = 0 at that position; the second is the analogous
check at the rightmost #, requiring all four bits to be 1. We omit the construction of these gadgets
here, since they follow the same pattern as C+1 and M.
The construction given in Ex. 2 allows us to succinctly recognize a language whose shortest word
has length exponential in the number of bits of the binary counter. In the following, we describe how
to extend this idea such that we can reduce an EXPSPACE-complete problem to non-emptiness of a
certain B-RASP program. Intuitively, we place multiple such words as above on top of each other,
creating multiple rows and columns (separated by #). Moreover, we introduce vertical constraints,
i.e., between rows, in addition to the horizontal constraints H. Using this technique, we will see in
Thm. 15 how B-RASP programs can even succinctly recognize languages whose shortest word has
doubly exponential length.
Throughout the rest of this section, we build up to the proof of the following complexity bound.
Theorem 4. The non-emptiness problem for UHATs and B-RASP programs is EXPSPACE-
complete.
To prove Thm. 4, we start with the lower bound for B-RASP programs.
Proposition 5. The non-emptiness problem for B-RASP programs is EXPSPACE-hard.
For the proof, we use the construction sketched in Ex. 2 and reduce from the tiling problem.
Problem 6. We now describe the 2N-tiling problem. A tile is a quadruple t = ⟨a, b, c, d⟩∈N4
0. We
write left(t) = a, up(t) = b, right(t) = c, and down(t) = d.
6Filling in the remainder of the B-RASP program to enforce the remaining constraints is straightforward.

Published as a conference paper at ICLR 2026
Given: An instance I = (N, T, tfin), where N > 0 is an integer in unary, T is a finite set of tiles,
and tfin ∈T is a designated final tile.
Question: Do there exist a natural M ∈N and a function τ : [2N] [M] T such that
1. τ(2N, M) = tfin,
2. down(τ(i, 1)) = up(τ(i, M)) = 0 for all 1 i 2N,
3. left(τ(1, j)) = right(τ(2N, j)) = 0 for all 1 j M,
4. right(τ(i, j)) = left(τ(i + 1, j)) for all 1 i < 2N and 1 j M, and
5. up(τ(i, j)) = down(τ(i, j + 1)) for all 1 i 2N and 1 j < M?
A configuration of tiles, i.e., a candidate for the function τ, places tiles in 2N columns and an
arbitrary number (M) of rows.
Proposition 7. The 2N-tiling problem is EXPSPACE-complete.
Proof. The result follows from Theorem 5 in Schwarzentruber (2019) by choosing k = 1.
To prove Prop. 5, we construct a B-RASP program of size polynomial in N that accepts an encoding
of a configuration of tiles as a sequence of words, similar to those displayed in Ex. 2, if and only if
the configuration is a solution of the given 2N-tiling problem instance. The key observation is that
strict future masking with rightmost tie-breaking enables us to check conditions between successive
tiles in a row (Item 4) but also between the current tile and the tile at the most recent past occurrence
of the same counter value, i.e., in the same column of the previous row (Item 5). The proof of the
next lemma can be found in App. A.2.
Lemma 8. Given a 2N-tiling problem instance, one can construct in time polynomial in N a B-
RASP program, whose language is non-empty iff the 2N-tiling problem instance has a solution.
Lem. 8 reduces the 2N-tiling problem to the non-emptiness problem for B-RASP programs. Thus,
together with Prop. 7, it implies Prop. 5.
We observe that the B-RASP program constructed in Lem. 8 is of a special form, which allows for
a polynomial-time translation to UHAT.
Lemma 9. Given a B-RASP program P1, ..., PΠ where every attention operation is of the form
Pt+1(i) := ◀▶j [M(i, j), S(j) ∧
k∈K
Pk(i) ↔Pk(j)] V (i, j) : D(i),
(9)
where |Σ| t < Π, ◀▶∈{◀, ▶}, S(j) is a Boolean combinations of P1(j), ..., Pt(j), and K ⊆
{1, ..., t}, one can construct in polynomial time a UHAT that recognizes the same language.
Proof sketch. Any Boolean combination of position-wise predicates can be simulated by a sequence
of attention layers (each layer simply applies its affine map C to the current vector and disregards
the attention vector) and ReLU layers. For each B-RASP attention operation, we use a single UHA
layer ( 2.2) whose mask predicate is M, whose tie-breaker matches ◀▶, whose affine maps A, B
compute the relevant components of the score, and whose affine map C combines the positions
input vn with the attention-selected an. The value predicate V (i, j) is simulated as follows: the
layers affine map C copies the relevant components of aithe layer-ℓvector that attention selected
from position o(i) (the unique position whose layer-ℓvector wins the argmax in the UHA layer;
equivalently, o(i) = τ(Bi) in the UHAT notation of 2.2, with Bi the argmax set among the
unmasked positions and τ the tie-breaker)into the layers output at position i, and a small ReLU
sub-network applies the Boolean combination V to those copied components. The part S(j) of the
score predicate that only depends on j can be simulated using an additional preliminary layer that
already computes the result of S(j) at every position j. For the part V
k∈K Pk(i) ↔Pk(j) that
checks equality of two binary numbers, we provide a score function that maximizes the attention
score if the two binary numbers are equal. The full proof can be found in App. A.3.
Proposition 10. The non-emptiness problem for UHAT is EXPSPACE-hard.
Proof. Together, Prop. 7, Lem. 8 and Lem. 9 imply the EXPSPACE lower bound for UHAT.

Published as a conference paper at ICLR 2026
Corollary 11. The non-emptiness problem for UHATs in which every layer uses strict future
masking and rightmost tie-breaking (or, dually, strict past masking and leftmost tie-breaking) is
EXPSPACE-hard.
Proof. The B-RASP program constructed in Lem. 8 uses only strict future masking and right-
most tie-breaking, and it can be adapted to use only strict past masking and leftmost tie-breaking.7
The UHAT translation in Lem. 9 preserves the mask predicate and tie-breaking. Therefore the
EXPSPACE lower bound established by Prop. 7, Lem. 8, and Lem. 9 transfers to UHATs in either
of the two restricted classes.
We now prove the upper bounds in Thm. 4. To this end, we first note that any B-RASP program
can be converted in exponential time into an LTL formula using the construction given by Yang
et al. (2024). In Prop. 13 we prove that the same holds true for UHATs, which improves the doubly
exponential construction given by Yang et al. (2024) that translates UHATs into B-RASP programs
first. These constructions suffice for the exponential-space upper bounds in Thm. 4 since non-
emptiness of languages given by LTL formulas is in polynomial space (Sistla and Clarke, 1985).
To perform the translation from UHAT to LTL, we first have to make the crucial observation that the
values occurring during the computation of a UHAT are not too large. The proof of the following
proposition can be found in App. A.4.
Proposition 12. For every UHAT T , the precision required to evaluate T on any input is polynomial
in |T |, i.e., every rational value arising in the computation of T can be represented with at most
poly(|T |) bits.
By Prop. 12, the set of rationals that can arise in the computation of T is finite, and each member has
bit-length polynomial in |T |. The set therefore has cardinality at most 2poly(|T |), i.e., exponential
in |T |, and can be enumerated in exponential time. This is precisely what makes the layer-by-layer
LTL construction in the proof of Prop. 13 feasible: at each layer we have a finite, enumerable,
polynomial-bit-length set of vectors to range over, which implies that the LTL formula only has to
simulate the position-wise behavior of attention layers, i.e., masking and selecting the position of
the attention vector, but not the actual computation of values.
The proof of the following proposition can be found in App. A.5.
Proposition 13. Given a UHAT T recognizing a language L ⊆Σ+, one can construct in exponen-
tial time an LTL formula φ that recognizes L.
Note, if we start with a UHAT, where every attention layer uses strict future masking and leftmost
tie-breaking (resp. strict past masking and rightmost tie-breaking), then the LTL formula constructed
in the proof of Prop. 13 only uses the P (resp. F) operator. It was shown by Sistla and Clarke (1985)
that the non-emptiness problem for the fragments of LTL that only allow P or F is NP-complete.
Thus, we obtain an improved complexity upper bound for such restricted UHATs.
Corollary 14. The non-emptiness problem for UHATs, where each attention layer uses strict future
masking/leftmost tie-breaking (resp. strict past masking/rightmost tie-breaking), is in NEXP.
Note that it has been shown by Jerad et al. (2025) that such restricted UHATs are equally expressive
as the LTL fragment with only P (respectively, F).8 However, the construction by Jerad et al. (2025)
from UHAT to the LTL fragments incurs a doubly exponential blow-up, as opposed to our singly
exponential translation. The full proof of Thm. 4, combining the preceding lemmas, propositions,
and corollaries into the two directions of EXPSPACE-completeness, can be found in App. A.1.
SUCCINCTNESS ACROSS REPRESENTATIONS
We now study how succinctly transformers can represent languages compared to standard models
from formal language theory. We first compare transformers to LTL. One suggestion that trans-
7In case of strict past masking, we use the first coordinate in the acceptance condition.
8Note that LTL with a subset of the operators is often defined over EOS-padded strings; this choice affects
its expressive capacity when using LTL with a subset of the operators. For instance, Li and Cotterells (2026)
demonstration that LTL[P] can not accept {a, b}a with EOS-padding, but can without the padding.

Published as a conference paper at ICLR 2026
formers may be more succinct than LTL comes from Thm. 4, which shows that the non-emptiness
problem for UHATs is EXPSPACE-complete, whereas for LTL the corresponding problem is known
to be PSPACE-complete. The following result shows that this exponential gap is also manifested in
terms of the formalisms respective succinctness.
Theorem 15. UHATs are exponentially more succinct than LTL.
Proof. It suffices to exhibit a witness family {Ln}
n=1 together with UHATs Tn of size poly(n)
recognizing Ln such that every LTL formula recognizing Ln has size at least c12c2n for constants
c1, c2 > 0. Such a family is a witness in the sense of Def. 2: from |Tn| = poly(n), say |Tn| c0nd,
we get n (|Tn|/c0)1/d, and substituting into |φn| c12c2n gives |φn| c12c′ |Tn|1/d for c′
2 =
c2/c1/d
. This witnesses f-more succinctness for f(m) = c12c′
2 m1/d as required.
Polynomial-size UHAT.
This direction proceeds in 3 steps.
1. Let Mn be a (deterministic) Turing machine that implements a binary counter with 2n bits, i.e.,
it writes 02n on its tape and increments the binary number until it has written 12n on its tape and
accepts. In particular, Mn first checks that it was started with the empty tape and then writes
2n many 0s on its tape using an additional n-bit counter. To increment the 2n-bit counter, Mn
traverses the counter from left to right while flipping every 1 to 0 until it encounters the first 0,
which is then flipped to 1. To initialize the counter with 0s, Mn uses a linear number of states
in n. Incrementing can be done with a constant-sized Turing machine. Moreover, Mn uses an
exponential number of tape cells in n and the unique accepting run has length at least 22n.
2. Van Emde Boas (1997) gives a reduction from Turing machines to tiling problem instances that
encodes configurations of Turing machines in its rows and a correct tiling corresponds to a valid
execution of the Turing machine. We observe that the 2p(n)-tiling problem instance In, for some
polynomial p, constructed from Mn has size polynomial in n and it has the property that the
smallest correct tiling has at least 22n many rows.
3. Lem. 8 and Lem. 9 show that there is a UHAT Tn of size polynomial in the size of In that
recognizes encodings of correct tilings of In. Thus, Tn is of size polynomial in n and the
smallest accepted word has length at least 22n. We let Ln be the language recognized by Tn.
Exponential LTL lower bound.
Let φn be an LTL formula that recognizes Ln. Because the
smallest accepted word by any LTL formula has length at most exponential in the formula size,
using an exponential conversion from LTL to finite automata similar to Vardi and Wolper (1994), it
follows that the size of φn is at least exponential in n.
Conversely, the next result shows that UHATs have polynomially bounded expansion over LTL:
every LTL formula has an at most polynomially larger UHAT for the same language. Combined
with Thm. 15, this pins the gap between UHATs and LTL: at most polynomial universally, and at
least exponential on a witness family. The proof can be found in App. A.6.
Proposition 16. UHATs have polynomially bounded expansion over LTL. In particular, given an
LTL formula φ, one can construct in polynomial time a UHAT T such that L(T ) = L(φ).
We show next that UHATs are doubly exponentially more succinct than finite automata.
Theorem 17. UHATs are doubly exponentially more succinct than finite automata.
Proof. We reuse the witness family from Thm. 15: Ln is the language recognized by the UHAT
Tn constructed there. Tn is of size polynomial in n and the smallest accepted word has length at
least 22n. Because any automaton recognizing a non-empty language accepts a word of length at
most linear in the automaton size, the smallest automaton that recognizes Ln has size at least doubly
exponential in n. Combined with |Tn| = poly(n), this exhibits the witness family required by Def. 2
with f doubly exponential.
Conversely, the best known translation from counter-free automatathe class of finite automata
equivalent to LTLto LTL incurs an exponential blow-up (Maler and Pnueli, 1990). Compos-
ing this with Prop. 16 yields an at-most exponential-time translation from counter-free automata to

Published as a conference paper at ICLR 2026
UHATs, which shows that UHATs have exponentially bounded expansion over finite automata when
restricted to the star-free languages. The translation in Yang et al. (2024) also incurs an exponential
blow-up via Maler and Pnueli (1990).
Combining Thm. 17 with Prop. 1 yields the following succinctness gap between UHATs and RNNs.
Corollary 18. UHATs are exponentially more succinct than RNNs.
APPLICATIONS
As a consequence of our results, we can show that reasoning about the language accepted by a
UHAT, e.g., checking equivalence and emptiness, is intractable. Contrast this fact with determin-
istic finite automata, where these problems can be done in polynomial time (Kozen, 1997). As an
example, we give a precise statement about the complexity of equivalence problem, i.e., the problem
of checking whether two UHATs recognize the same language. The proof can be found in App. A.7.
Theorem 19. Deciding the equivalence between two UHATs is EXPSPACE-complete.
CONCLUDING REMARKS


## Related Work

Our work directly draws upon a number of recent results (Yang et al., 2024; Bar-
cel´o et al., 2024; Jerad et al., 2025; Li and Cotterell, 2025), which demonstrate the close connec-
tion between unique-hard attention transformers and LTL and, thus, the star-free regular languages.
However, none of these results concerns succinctness and computational complexity of verification.
Closer to our complexity-theoretic angle, S¨alzer et al. (2025) studied the verification problem for
transformers of various precisions and showed that fixed-precision transformers are at least NEXP-
hard (i.e., hard for the class of problems solvable by nondeterministic algorithms that run in expo-
nential time). Their technique implies that transformers can be (singly) exponentially more succinct
than finite automata, but yields no conclusion about their succinctness relative to representations like
LTL or RNNs. Our results substantially improve on this by showing that transformers can be doubly
exponentially more succinct than automata, and exponentially more succinct than LTL and RNNs.
Our model is also simpler: we use unique-hard attention, whereas S¨alzer et al. (2025) employs a
combination of soft and hard attention. Our setting also restricts positional information to positional
maskinga simple class of positional embeddings also considered by Yang et al. (2024), Jerad et al.
(2025) and Li and Cotterell (2025)in contrast to the arbitrary fixed-precision positional encodings
admitted by S¨alzer et al. (2025). Without position encodings, S¨alzer et al. (2026) recently showed
that verification is undecidable for average-hard-attention and softmax-attention transformers with
finite but unbounded precision.
Formal Verification of Transformers.
We close by situating our findings within the broader pro-
gram of formal verificationthe automated analysis, verification, and explanation of transformers
which is a central concern of explainable AI (Huang et al., 2020). Substantial practical progress has
been made on verifying feed-forward neural networks, with tools developed over the last decade and
benchmarked at the annual VNN competition (Brix et al., 2024); transformers, by contrast, remain
largely out of reach. Despite the high worst-case complexity (EXPSPACE-complete), we pose as a
challenge bringing techniques from automated verification (Clarke et al., 2018)symbolic methods,
simulation, inter aliato bear on transformer verification in practice. Because our EXPSPACE-
hardness proof requires transformers that encode large counters, a complementary direction is to
identify subclasses that cannot encode such counters and thus admit lower-complexity verification.
A related open question is the learnability of succinct transformers, on which the empirical evi-
dence remains mixed (Garg et al., 2022; Naim et al., 2025; Huang et al., 2025). Finally, our results
are a first step toward understanding how succinct transformers can be relative to other language-
acceptor models, e.g., fixed-precision softmax transformers (Li and Cotterell, 2025), which UHATs
overapproximate. We leave the succinctness of fixed-precision softmax and average-hard attention
transformers as future work; see Yang et al. (2026) for an initial attempt.

Published as a conference paper at ICLR 2026
ACKNOWLEDGMENTS
We thank David Chiang, Marco S¨alzer, Andy Yang and anonymous reviewers for their helpful feed-
back. Pascal Bergstr¨aßer and Anthony W. Lin are supported by Deutsche Forschungsgemeinschaft
(grant number 522843867) and European Union9
(ERC, LASD, 101089343).
REFERENCES
Pablo Barcel´o, Alexander Kozachinskiy, Anthony Widjaja Lin, and Vladimir V. Podolskii. 2024.
Logical languages accepted by transformer encoders with hard attention. In International Con-
ference on Learning Representations.
Pascal Bergstr¨aßer, Chris K¨ocher, Anthony Widjaja Lin, and Georg Zetzsche. 2024. The power
of hard attention transformers on data sequences: A formal language theoretic perspective. In
Advances in Neural Information Processing Systems.
Christopher Brix, Stanley Bak, Taylor T. Johnson, and Haoze Wu. 2024. The fifth international
verification of neural networks competition (VNN-COMP 2024): Summary and results.
David Chiang and Peter Cholak. 2022. Overcoming a theoretical limitation of self-attention. In
Annual Meeting of the Association for Computational Linguistics.
E.M. Clarke, O. Grumberg, D. Kroening, D. Peled, and H. Veith. 2018. Model Checking, 2 edition.
MIT Press.
Shivam Garg, Dimitris Tsipras, Percy Liang, and Gregory Valiant. 2022. What can transformers
learn in-context? A case study of simple function classes. In Advances in Neural Information
Processing Systems.
David Goldberg. 1991. What every computer scientist should know about floating-point arithmetic.
ACM Computing Surveys, 23(1).
Martin Grohe and Nicole Schweikardt. 2004. The succinctness of first-order logic on linear orders.
In IEEE Symposium on Logic in Computer Science.
Albert Gu and Tri Dao. 2023. Mamba: Linear-time sequence modeling with selective state spaces.
Michael Hahn. 2020. Theoretical limitations of self-attention in neural sequence models. Transac-
tions of the Association for Computational Linguistics, 8.
Yiding Hao, Dana Angluin, and Robert Frank. 2022. Formal language recognition by hard attention
transformers: Perspectives from circuit complexity. Transactions of the Association for Compu-
tational Linguistics, 10.
Xiaowei Huang, Daniel Kroening, Wenjie Ruan, James Sharp, Youcheng Sun, Emese Thamo, Min
Wu, and Xinping Yi. 2020. A survey of safety and trustworthiness of deep neural networks: Ver-
ification, testing, adversarial attack and defence, and interpretability. Computer Science Review,
Xinting Huang, Andy Yang, Satwik Bhattamishra, Yash Raj Sarrof, Andreas Krebs, Hattie Zhou,
Preetum Nakkiran, and Michael Hahn. 2025. A formal framework for understanding length gen-
eralization in transformers. In International Conference on Learning Representations.
Selim Jerad, Anej Svete, Jiaoda Li, and Ryan Cotterell. 2025. Unique hard attention: A tale of two
sides. In Annual Meeting of the Association for Computational Linguistics.
Dexter Kozen. 1997. Automata and Computability. Springer.
Jiaoda Li and Ryan Cotterell. 2025. Characterizing the expressivity of fixed-precision transformer
language models. In Advances in Neural Information Processing Systems.
9Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those
of the European Union or the European Research Council Executive Agency. Neither the European Union nor
the granting authority can be held responsible for them.

Published as a conference paper at ICLR 2026
Jiaoda Li and Ryan Cotterell. 2026. Characterizing the expressivity of local attention in transform-
ers. In Annual Meeting of the Association for Computational Linguistics.
Leonid Libkin. 2004. Elements of Finite Model Theory. Springer.
Oded Maler and Amir Pnueli. 1990. Tight bounds on the complexity of cascaded decomposition of
automata. In Symposium on Foundations of Computer Science.
Robert McNaughton and Seymour Papert. 1971. Counter-Free Automata. MIT Press.
William Merrill, Jackson Petty, and Ashish Sabharwal. 2024. The illusion of state in state-space
models. In International Conference on Machine Learning.
William Merrill, Gail Weiss, Yoav Goldberg, Roy Schwartz, Noah A. Smith, and Eran Yahav. 2020.
A formal hierarchy of RNN architectures. In Annual Meeting of the Association for Computa-
tional Linguistics.
Marvin L. Minsky. 1967. Computation: Finite and Infinite Machines. Prentice-Hall.
Omar Naim, Jerome Bolte, and Nicholas Asher. 2025. Analyzing limits for in-context learning. In
What Can(t) Transformers Do? Workshop at the Conference on Neural Information Processing
Systems.
Jorge P´erez, Pablo Barcel´o, and Javier Marinkovic. 2021. Attention is Turing-complete. Journal of
Machine Learning Research, 22.
Amir Pnueli. 1977. The temporal logic of programs. In Symposium on Foundations of Computer
Science.
Marco S¨alzer, Eric Alsmann, and Martin Lange. 2025. Transformer encoder satisfiability: Complex-
ity and impact on formal reasoning. In International Conference on Learning Representations.
Marco S¨alzer, Chris K¨ocher, Alexander Kozachinskiy, Georg Zetzsche, and Anthony Widjaja Lin.
2026. The counting power of transformers. In International Conference on Learning Represen-
tations.
Franc¸ois Schwarzentruber. 2019.
The complexity of tiling problems.
arXiv preprint
arXiv:1907.00102.
Hava T. Siegelmann and Eduardo D. Sontag. 1995. On the computational power of neural nets.
Journal of Computer and System Sciences, 50(1).
Michael Sipser. 1997. Introduction to the Theory of Computation. PWS Publishing.
A. Prasad Sistla and Edmund M. Clarke. 1985. The complexity of propositional linear temporal
logics. Journal of the ACM, 32(3).
Larry Joseph Stockmeyer. 1974. The Complexity of Decision Problems in Automata Theory and
Logic. Ph.D. thesis, Massachusetts Institute of Technology.
Howard Straubing. 1994. Finite Automata, Formal Logic, and Circuit Complexity. Birkh¨auser.
Lena Strobl, William Merrill, Gail Weiss, David Chiang, and Dana Angluin. 2024. What formal
languages can transformers express? A survey. Transactions of the Association for Computational
Linguistics, 12.
Anej Svete and Ryan Cotterell. 2023. Recurrent neural language models as probabilistic finite-state
automata. In Conference on Empirical Methods in Natural Language Processing.
Peter van Emde Boas. 1997. The convenience of tilings. In Complexity, Logic, and Recursion
Theory. CRC Press.
Moshe Y. Vardi and Pierre Wolper. 1994. Reasoning about infinite computations. Information and
Computation, 115(1).

Published as a conference paper at ICLR 2026
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez,
Lukasz Kaiser, and Illia Polosukhin. 2017. Attention is all you need. In Advances in Neural
Information Processing Systems.
Gail Weiss, Yoav Goldberg, and Eran Yahav. 2018. On the practical computational power of finite
precision RNNs for language recognition. In Annual Meeting of the Association for Computa-
tional Linguistics.
Gail Weiss, Yoav Goldberg, and Eran Yahav. 2024.
Extracting automata from recurrent neural
networks using queries and counterexamples (extended version). Machine Learning, 113(5).
Andy Yang, Pascal Bergstr¨aßer, Georg Zetzsche, David Chiang, and Anthony Widjaja Lin. 2026.
Length generalization bounds for transformers.
Preprint, arXiv:2603.02238.
(Accepted at
ICML26).
Andy Yang, David Chiang, and Dana Angluin. 2024. Masked hard-attention transformers recognize
exactly the star-free languages. In Advances in Neural Information Processing Systems.
Hattie Zhou, Arwen Bradley, Etai Littwin, Noam Razin, Omid Saremi, Joshua M. Susskind, Samy
Bengio, and Preetum Nakkiran. 2024. What algorithms can transformers learn? A study in length
generalization. In International Conference on Learning Representations.

Published as a conference paper at ICLR 2026
PROOFS
A.1
PROOF OF THEOREM 4
Theorem 4. The non-emptiness problem for UHATs and B-RASP programs is EXPSPACE-
complete.
Proof. The theorem asserts EXPSPACE-completeness of the non-emptiness problem for two for-
malisms simultaneously: B-RASP programs and UHATs. We prove the two directions of complete-
ness separately.
Hardness (lower bound).
We establish EXPSPACE-hardness first for B-RASP programs, then
transfer it to UHATs.
B-RASP. For B-RASP programs, Prop. 7 states that the 2N-tiling problem is EXPSPACE-
complete, so it is EXPSPACE-hard. By Lem. 8, any instance of the 2N-tiling problem can be
transformed, in time polynomial in N, into a B-RASP program whose recognized language
is non-empty if and only if the original tiling instance has a solution. Composing these two


## Results

emptiness. Thus, B-RASP non-emptiness is itself EXPSPACE-hard.
UHAT. For UHATs, we further compose the previous reduction with the polynomial-time,
language-preserving translation from B-RASP to UHATs of Lem. 9. The composed reduction
is again polynomial-time, so the EXPSPACE-hardness of 2N-tiling transfers to UHAT non-
emptiness; this is the content of Prop. 10.
Membership (upper bound).
We show that the non-emptiness problem for both formalisms lies
in EXPSPACE by translating to LTL and invoking the SistlaClarke decision procedure.
For B-RASP programs, the construction of Yang et al. (2024) converts any B-RASP program P
into an equivalent LTL formula φP in time exponential in |P |; consequently |φP | is itself at most
exponential in |P |.
For UHATs, the analogous translation is supplied by Prop. 13, which turns any UHAT T into an
equivalent LTL formula φT in exponential time (and hence of at most exponential size). The proof
of Prop. 13 relies crucially on Prop. 12: the latter guarantees that all rational values arising in the
computation of T admit representations of polynomially many bits, which is what makes the set of
layer-wise representations enumerable in exponential time.
In both cases we have, in exponential time, reduced the original non-emptiness problem to LTL
satisfiability for a formula of size at most exponential in the size of the original UHAT or B-RASP
program. Sistla and Clarke (1985) prove that LTL satisfiability is decidable in space polynomial in
the formula size; applied to φP or φT , this uses space polynomial in an exponential quantity, that
is, space exponential in |P | or |T |. The overall decision procedure therefore runs in EXPSPACE.
Combining the two halves yields EXPSPACE-completeness of non-emptiness for both B-RASP
programs and UHATs, as claimed.
A.2
PROOF OF LEMMA 8
Lemma 8. Given a 2N-tiling problem instance, one can construct in time polynomial in N a B-
RASP program, whose language is non-empty iff the 2N-tiling problem instance has a solution.
Proof. Fix a 2N-tiling problem instance I = (N, T, tfin) as in Prob. 6. We construct a B-RASP
program PI of size polynomial in N and |T| such that L(PI) ̸= ∅if and only if I admits a solution
τ : [2N] [M] T in the sense of Prob. 6.
Encoding.
We encode a candidate τ as a word over the alphabet Σ := T ∪{0, 1, #}. Define the
per-cell encoding enc: [2N] [M] Σ+ by
enc(i, j) := binN(i −1) τ(i, j) #,
(10)

Published as a conference paper at ICLR 2026
where binN(i −1) ∈{0, 1}N is the N-bit binary representation of i −1, most significant bit first.
The encoding of the full configuration scans columns within each row in order:
enc(τ) := enc(1, 1)...enc(2N, 1) enc(1, 2)...enc(2N, M).
(11)
Let LI := {enc(τ) | τ is a solution of I}.
It suffices to construct a B-RASP program that
recognizes LI.
Plan.
Throughout, let a = a1...aL ∈Σ+ denote the input, with L := |a|. We build PI as a
conjunction of five gadgets, each evaluated at the last position L:
Gadget Ashape: a ∈({0, 1}N T #).
Gadget Bcolumn counter: consecutive N-bit blocks count 0, 1, ..., 2N −1, 0, ....
Gadget Cfinal tile: a ends with 1N tfin # (Item 1).
Gadget Dboundary conditions: Item 2 and Item 3.
Gadget Eadjacency: Item 4 and Item 5.
The output predicate is Y (i) := A(i) ∧B(i) ∧C(i) ∧D(i) ∧E(i), and PI accepts a iff Y (L) = 1.
We define each gadget below and verify its soundness at L.
Gadget A: well-formed shape.
To check whether a ∈({0, 1}N T #), we construct the
following B-RASP predicates:
AT (i) := ▶j [j < i, 1]
t∈T
Qt(j) : 0
(12a)
Abit,1(i) := ▶j [j < i, 1] Q0(j) ∨Q1(j) : 0
(12b)
Abit,k(i) := ▶j [j < i, 1] Abit,k−1(j) : 0
for k = 2, ..., N
(12c)
A#,1(i) := ▶j [j < i, 1] Q#(j) : 1
(12d)
A#,k(i) := ▶j [j < i, 1] A#,k−1(j) : 1
for k = 2, ..., N + 1
(12e)
Aenc(i) := (Q#(i) AT (i)) ∧
t∈T
Qt(i)
k=1
Abit,k(i)
∧A#,N+1(i)
(12f)
We aggregate Aenc across all positions:
A(i) := ▶j [j < i, ¬Aenc(j)] 0 : Aenc(i).
(13)
Then A(L) = 1 iff Aenc(i) = 1 at every position, which holds iff a matches ({0, 1}N T #)up to
the requirement that the last symbol is #, which is enforced by Gadget C below.
Gadget B: column counter.
We check that the N-bit binary blocks separated by # encode the
integers 0, 1, ..., 2N −1, 0, ... in order, generalizing the increment predicate of Ex. 2 from 4 bits to
N bits.
B1(i) := ▶j [j < i, Q0(j) ∨Q1(j)] Q1(j) : 0
(14a)
Bk(i) := ▶j [j < i, Q0(j) ∨Q1(j)] Bk−1(j) : 0
for k = 2, ..., N
(14b)
B+1(i) := ▶j [j < i, Q#(j)]
k=1
 k−1
r=1
¬Br(i) ∧Br(j)
∧Bk(i) ∧¬Bk(j) ∧
r=k+1
Br(i) ↔Br(j)
: 0
(14c)
B10(i) := ▶j [j < i, Q#(j)]
k=1
¬Bk(i) ∧Bk(j) :
k=1
¬Bk(i)
(14d)
B(i) := ▶j [j < i, Q#(j) ∧¬B10(j) ∧¬B+1(j)] 0 : B10(i) ∧B+1(i)
(14e)
Then B(L) = 1 iff the binary blocks count up correctly.

Published as a conference paper at ICLR 2026
Gadget C: final tile.
For each tile t ∈T, we record whether the most recent prior tile equals t
via the predicate Tt at every position, and use this to check that a ends with 1N tfin # (Item 1):
Tt(i) := ▶j [j < i,
Qt′(j)] Qt(j) : 0
for all t ∈T
(15a)
C(i) := Q#(i) ∧Ttfin(i) ∧
k=1
Bk(i)
(15b)
Then C(L) = 1 iff a ends with 1N tfin #.
Gadget D: boundary conditions.
We enforce Item 2 and Item 3 of Prob. 6: the bottom row uses
tiles with down = 0, the top row uses tiles with up = 0, and the leftmost (resp. rightmost) column
uses tiles with left = 0 (resp. right = 0).
D⊥(i) := ▶j [j < i, Q#(j) ∧
k=1
Bk(i) ↔Bk(j)] 1 :
t∈T,
down(t)=0
Tt(i)
(16a)
D⊤(i) := ▶j
j < i, Q#(j) ∧
t∈T,
up(t)̸=0
Tt(j) ∨
k=1
¬Bk(j)
t∈T,
up(t)=0
Tt(j)
t∈T,
up(t)=0
Tt(i)
: 0
(16b)
D⊢(i) :=
k=1
¬Bk(i)
t∈T,
left(t)=0
Tt(i)
(16c)
D⊣(i) :=
k=1
Bk(i)
t∈T,
right(t)=0
Tt(i)
(16d)
D(i) := ▶j [j < i, Q#(j) ∧¬ (D⊥(j) ∧D⊢(j) ∧D⊣(j))] 0 : D⊥(i) ∧D⊤(i) ∧D⊢(i) ∧D⊣(i)
(16e)
Then D(L) = 1 iff Item 2 and Item 3 hold.
Gadget E: adjacency.
We enforce Item 4 and Item 5: horizontally adjacent tiles agree on
(right, left), and vertically adjacent tiles (same column, consecutive rows) agree on (down, up) as
follows:
E(i) := ▶j [j < i, Q#(j)]
k=1
Bk(i)
t,t′∈T,
left(t)=right(t′)
(Tt(i) ∧Tt′(j)) : 1
(17a)
E(i) := ▶j [j < i, Q#(j) ∧
k=1
Bk(i) ↔Bk(j)]
t,t′∈T,
down(t)=up(t′)
Tt(i) ∧Tt′(j) : 1
(17b)
E(i) := ▶j [j < i, Q#(j) ∧¬ (E(j) ∧E(j))] 0 : E(i) ∧E(i)
(17c)
Then E(L) = 1 iff Item 4 and Item 5 hold.
Wrap-up.
Define the output predicate
Y (i) := A(i) ∧B(i) ∧C(i) ∧D(i) ∧E(i),
(18)

Published as a conference paper at ICLR 2026
and let PI accept iff Y (L) = 1. By the soundness of each gadget, L(PI) = LI, so L(PI) ̸= ∅iff
I admits a solution. Each gadget uses O(N) predicates of size polynomial in N and |T|, so |PI|
is polynomial in N and |T|, hence in the size of I.
A.3
PROOF OF LEMMA 9
Lemma 9. Given a B-RASP program P1, ..., PΠ where every attention operation is of the form
Pt+1(i) := ◀▶j [M(i, j), S(j) ∧
k∈K
Pk(i) ↔Pk(j)] V (i, j) : D(i),
(9)
where |Σ| t < Π, ◀▶∈{◀, ▶}, S(j) is a Boolean combinations of P1(j), ..., Pt(j), and K ⊆
{1, ..., t}, one can construct in polynomial time a UHAT that recognizes the same language.
Proof. Let P = (P1, ..., PΠ) be a B-RASP program over the alphabet Σ = {a1, ..., a|Σ|}, where Pt
is the initial vector Qat for all 1 t |Σ|. We construct a UHAT over Σ that recognizes the same
language as P . We use a one-hot symbol embedding emb: Σ {0, 1}|Σ|, i.e., emb(at) := et for
all 1 t |Σ|, where et denotes the tth unit vector. Then Pt(i) coincides with the tth component
of the ith input vector of the UHAT after the symbol embedding is applied. The UHAT will preserve
these components in each layer and will gradually add new components to store the value of Pt(i)
for all |Σ| < t Π. So assume we already defined the layers of the UHAT that compute the vector
(P1(i), ..., Pt(i)) at position i for |Σ| t < Π. We now define additional layers whose output will
be (P1(i), ..., Pt+1(i)).
We first consider the case where Pt+1 is a position-wise operation, i.e., Pt+1(i) is defined by a
Boolean combination of P1(i), ..., Pt(i). We define UHAT layers to compute the result of that
Boolean combination bottom-up. Assume we already defined layers that output (R1(i), ..., Rs(i)),
where s t and R1(i), ..., Rs(i) contain P1(i), ..., Pt(i) and the results of previously computed
subformulas. To compute the result of ¬Rk(i) for some k ∈[s], we add an attention layer that
just forwards 1 −Rk(i) at position i in an additional component while leaving the first s compo-
nents unchanged. To compute Rk(i) ∧Rℓ(i) for some k, ℓ∈[s], we first use an attention layer
to forward Rk(i) + Rℓ(i) −1 in an additional component followed by a ReLU layer that forwards
the result of max{0, Rk(i) + Rℓ(i) −1} in this additional component, again leaving the first s
components unchanged. We do not have to deal with Rk(i) ∨Rℓ(i), since it can be rewritten as
¬(¬Rk(i) ∧¬(Rℓ(i)). After computing the results of all subformulas, we add an additional atten-
tion layer to only forward (P1(i), ..., Pt+1(i)), i.e., removing the intermediate results. Observe that
a Boolean combination has only linearly many subformulas.
Let us now consider the case where Pt+1 is an attention operation of the form
Pt+1(i) := ◀▶j [M(i, j), S(j) ∧
k∈K
Pk(i) ↔Pk(j)] V (i, j) : D(i)
(19)
as in the statement of Lem. 9. Throughout the construction below, K, M, ◀▶, S, V , and D are
the parameters of this input attention operation, as bound in the lemma statement; in particular,
K ⊆{1, ..., t} is the index set of predicates whose values at i and j are compared for equality
in the operations score predicate. We first use additional layers as in the case of position-wise
operations to compute the result of ¬S(i) at every position i in an additional component to output
(P1(i), ..., Pt(i), 1 −S(i)). Next we use an attention layer to add the result of 1 −Pk(i) for all
k ∈K at every position i in additional components. We then add an attention layer that uses mask
predicate M, tie-breaking according to ◀▶, and attention score
 X
k∈K
 Pk(i)Pk(j) + (1 −Pk(i))(1 −Pk(j))
 1 −S(j)
(20)
which is equal to |{k ∈K | Pk(i) = Pk(j)}| −(1 −S(j)) since
Pk(i)Pk(j) + (1 −Pk(i))(1 −Pk(j)) =
1,
if Pk(i) = Pk(j)
otherwise.
(21)
Thus, the score is maximized (equal to |K|) if Pk(i) = Pk(j) for all k ∈K and S(j) = 1. For every
position i let o(i) be the position of the vector that maximizes the attention score with respect to i.

Published as a conference paper at ICLR 2026
The attention layer forwards the vector (P1(i), ..., Pt(i), P1(o(i)), ..., Pt(o(i)), S(o(i))) at position
i. We now compute the result of
R(i) := S(o(i)) ∧
k∈K
Pk(i) ↔Pk(o(i))
(22)
at every position i as in the case of position-wise operations and forward the vector
(P1(i), ..., Pt(i), P1(o(i)), ..., Pt(o(i)), R(i)). Finally, we compute
 R(i) ∧V (i, o(i))
 ¬R(i) ∧D(i)
(23)
by again using additional layers as in the case of position-wise operations, whose result is exactly
Pt+1(i). We then forward (P1(i), ..., Pt+1(i)).
It remains to describe when the UHAT accepts. If Pt is the output vector of P , then we stop the
construction of the UHAT after the layers to compute Pt are constructed. The acceptance vector of
the UHAT is then defined as et, i.e., the tth unit vector. This means that the UHAT accepts if and
only if ⟨et, (P1(N), ..., Pt(N))⟩> 0, which holds if and only if Pt(N) = 1, where N is the length
of the input.
We observe that the resulting UHAT only has polynomially many layers since the result of each
operation Pt can be computed using an additional number of layers that is linear in the description
size of Pt.
A.4
PROOF OF PROPOSITION 12
Proposition 12. For every UHAT T , the precision required to evaluate T on any input is polynomial
in |T |, i.e., every rational value arising in the computation of T can be represented with at most
poly(|T |) bits.
Proof. Part 1: bounding the denominator.
Let K be the number of rationals in the description
of T , i.e., the entries of the embedding emb(a) for a ∈Σ, the entries of every affine transformation
Aℓ, Bℓ, Cℓat each layer ℓ, and the entries of the acceptance vector t. Each of these rationals is part
of T s binary encoding, so K |T | and the bit-length b of any individual rational satisfies b |T |
as well. Let D be the least common multiple (LCM) of the denominators of those K rationals. The
LCM of K integers each of bit-length at most b has bit-length at most K · b (an upper bound is the
product of the integers), so D has bit-length at most |T |2. By construction, every embedding entry
and every coefficient of an affine transformation can be written with denominator dividing D.
We now show by induction on the layer number ℓthat there is a denominator dℓ, of polynomial bit-
length, common to every value at layer ℓ. The base case ℓ= 0 is the embedding: d0
def= D works. For
the inductive step, suppose every layer-ℓvalue has denominator dividing dℓ. An attention layer takes
an affine combination of layer-ℓvalues, weighted by coefficients drawn from the description of T .
Each weight has denominator dividing D, and each input has denominator dividing dℓ. The product
of two fractions with denominators dividing D and dℓhas denominator dividing D · dℓ; a sum of
such products and the bias term (denominator dividing D, which divides D · dℓ) shares the same
denominator. So we may take dℓ+1
def= D · dℓ. A ReLU layer applies max{0, ·} pointwise, which
leaves denominators unchanged, so dℓ+1
def= dℓsuffices for that case. Iterating over at most |T | many
layers, the final denominator is at most D|T |+1, with bit-length (|T | + 1) log D, polynomial in |T |.
Part 2: bounding the numerator.
At an attention layer of width R, each output numerator is
an affine combination of 2R layer-ℓnumerators with integer weights and a bias each of bit-length
at most log D (the entries of C scaled by D). The magnitude is therefore at most 2R · 2log D
times the largest layer-ℓnumerators magnitudean additive per-layer bit-length increase of
log R + log D + O(1); ReLU leaves bit-lengths unchanged.
Since layer-0 numerators have
bit-length at most |T | + log D, iterating across the at-most-|T | many layers gives a final bit-length
of O(|T | · (log R + log D)), polynomial in |T |.
Note that the additive (rather than multiplicative) per-layer growth above follows because the
forwarded vector at an attention layer is C(vn, an), an affine combination of two layer-ℓvectors:

Published as a conference paper at ICLR 2026
the positions own input vn and the attention-selected an = vτ(Bn), which is just a verbatim
copy of whichever existing layer-ℓvector τ picks. The score function S(vn, ·)including the dot
productdoes enter the picture and a single score value would have bit-length quadratic in its
inputs. But the score is used only to rank positions; the argmax reduces it to a position index, and
that index alone is used to fetch an. The scores value never becomes a coordinate of any forwarded
vector, so its quadratic bit-length never enters the next layers input.
Combining the two parts: every value produced by T on any input has the form p/q with p and q
each of bit-length polynomial in |T |.
A.5
PROOF OF PROPOSITION 13
Proposition 13. Given a UHAT T recognizing a language L ⊆Σ+, one can construct in exponen-
tial time an LTL formula φ that recognizes L.
Proof. Setup.
Let T be a UHAT recognizing a language L ⊆Σ+ and let F be the set of binary
representations of rational numbers that may occur during the computation of T , as in Prop. 12. For
the ℓth layer of T and every v ∈F S, where S is the output dimension of layer ℓ, we construct an
LTL formula φℓ
v such that, on input a = a1...aN ∈Σ+, the ℓth layer outputs v at position n ∈[N]
if and only if a, n |= φℓ
v. We define φℓ
v inductively on ℓ.
Base case (ℓ= 0).
Let emb: Σ QD be the symbol embedding of T , and for all v ∈F D let
v :=
a∈emb−1(v)
Qa,
if emb−1(v) ̸= ∅
otherwise.
(24)
We now define the formula for layer ℓ+ 1, splitting on the type of layer.
Inductive stepReLU layer.
If layer ℓ+ 1 is a ReLU layer of width R applying ReLU to the kth
coordinate, we set
u∈F,
max{0,u}=vk
(v1:k−1, u, vk+1:R)
(25)
for all v ∈F R.
Inductive stepattention with strict masking.
If layer ℓ+ 1 is an attention layer with strict
future masking and rightmost tie-breaking defined by an affine transformation C : Q2R QS and
a score function S: Q2R QR, we let
u,a∈F R,
C(u,a)=v
u ∧
b∈F R,
S(u,b)<S(u,a)
a ∧¬P
b∈F R,
S(u,b)>S(u,a)
(26)
for all v ∈F S. To account for the special case where the set of unmasked positions is empty, we
take the disjunction of the previous formula with
u∈F R,
C(u,0)=v
(27)
We omit this special case in what follows. If the layer uses leftmost tie-breaking instead, we adapt
the formula as follows:
u,a∈F R,
C(u,a)=v
u ∧
a ∧¬P
b∈F R,
S(u,b)S(u,a)
b∈F R,
S(u,b)>S(u,a)
(28)
The case of strict past masking is similar, with U in place of S and F in place of P.

Published as a conference paper at ICLR 2026
Inductive stepattention without masking.
If the layer uses no masking and rightmost tie-
breaking, we distinguish three cases according to where the attention vector lies relative to the
current position: at the current position, strictly to the left, or strictly to the right. When the attention
vector is at the current position, we define φℓ+1
v,at as
v,at :=
u∈F R,
C(u,u)=v
u ∧
b∈F R,
S(u,b)>S(u,u)
b∈F R,
S(u,b)S(u,u)
(29)
When the attention vector is strictly to the left of the current position, we define φℓ+1
v,L as
v,L :=
u,a∈F R,
C(u,a)=v,
S(u,a)>S(u,u)
u ∧
b∈F R,
S(u,b)S(u,a)
b∈F R,
S(u,b)<S(u,a)
a ∧¬P
b∈F R,
S(u,b)>S(u,a)
(30)
Similarly, when the attention vector is strictly to the right, we define φℓ+1
v,R as
v,R :=
u,a∈F R,
C(u,a)=v,
S(u,a)S(u,u)
u ∧
b∈F R,
S(u,b)>S(u,a)
a ∧¬F
b∈F R,
S(u,b)S(u,a)
b∈F R,
S(u,b)>S(u,a)
. (31)
In the case of no masking and rightmost tie-breaking, we set
:= φℓ+1
v,at ∨φℓ+1
v,L ∨φℓ+1
v,R .
(32)
The case of no masking and leftmost tie-breaking is analogous.
Acceptance formula.
If T has m layers whose last layer outputs vectors of dimension S, and
t ∈QS is its acceptance vector, we define
φ :=
v∈F S,
⟨t,v⟩>0
v .
(33)
Then a, N |= φ if and only if a ∈L.
Complexity.
It remains to argue that φ can be computed in exponential time. By Prop. 12, |F|
is exponential in |T | and every representation in F has polynomial bit-length; moreover, F can
be computed in exponential time. At every layer ℓ+ 1 of width R, the formula φℓ+1
depends on
|F|O(R) formulas from layer ℓ, and can be computed in time polynomial in |F|R · |T |, since we
only have to evaluate affine transformations on vectors from F R, each of polynomial bit-length.
At the last layer m, the formulas φm
v depend on |F|O(R′m) formulas from layer 0, where R′ is the
maximum layer width. Hence φm
v , and therefore φ, has size exponential in |T | and is computable
in exponential time.
A.6
PROOF OF PROPOSITION 16
Proposition 16. UHATs have polynomially bounded expansion over LTL. In particular, given an
LTL formula φ, one can construct in polynomial time a UHAT T such that L(T ) = L(φ).
Proof sketch. We construct T by induction on the subformula structure of φ, maintaining the fol-
lowing invariant: after processing a subformula ψ, the UHAT built so far has, at every position n of
any input a, a designated output coordinate carrying the truth value of a, n |= ψ. Once the invariant
is established for ψ = φ, the acceptance vector reads off that coordinate at the last position.
Atomic formulas. For φ = Qa, the token embedding already provides the indicator 1[an = a] at
each position, which is precisely the required truth value.
Boolean combinations. The truth value of ¬ψ, ψ1 ∧ψ2, or ψ1 ∨ψ2 at position n depends only on
the childrens truth values at the same position n, so a single affine-and-ReLU layer computes the
required coordinate point-wise from coordinates produced by the inductive hypothesis.

Published as a conference paper at ICLR 2026
Since (φ = φ1 S φ2). By inductive hypothesis we have coordinates for φ1 and φ2 at every position;
an affine-and-ReLU layer computes ¬φ1 ∨φ2 at every position. We then use an attention layer with
strict future masking and rightmost tie-breaking to get for every position i the maximal position
j < i where ¬φ1 ∨φ2 holds and output at position i the truth value of φ2 from position j. For
positions ℓand subformulas ψ, we write ψ(ℓ) ∈{0, 1} for the indicator of a, ℓ|= ψ. By the
maximality of j, every k with j < k < i satisfies φ1(k) ∧¬φ2(k) (otherwise k would be a more
recent witness); in particular φ1(k) holds for all k ∈(j, i). Thus if φ2(j) = 1, then j witnesses
φ1 S φ2 at i under the semantics of 2, and if φ2(j) = 0 then ¬φ1(j) = 1 blocks any earlier j′ j
from witnessing S at i. When no such j exists, the attention layers default value outputs 0, which is
again consistent with the semantics.
The case where φ = φ1 U φ2 is similar using strict past masking and leftmost tie-breaking.
A.7
PROOF OF THEOREM 19
Theorem 19. Deciding the equivalence between two UHATs is EXPSPACE-complete.
Proof. To prove the lower bound, we reduce from the non-emptiness problem for UHATs, which
by Thm. 4 is EXPSPACE-complete. To this end, let T be a given UHAT and fix a UHAT T0
that recognizes the empty language. Then we have that T and T0 are equivalent if and only if T
recognizes the empty language.
To prove the upper bound, let the UHATs T1 and T2 be given. We apply Prop. 13 to turn T1 and T2
in exponential time into LTL formulas φ1 and φ2, respectively. Now, T1 and T2 are equivalent if and
only if φ1 and φ2 are equivalent. The latter can be decided in polynomial space (Sistla and Clarke,
1985), which results in an exponential-space algorithm in total.

