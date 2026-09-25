+++
id = "thm-sf-uniform-models-constant-tower"
kind = "theorem"
title = "Stage-independent local models for a constant tower"
order = 2326
uses = ["def-weil-derived-cohomology-sheaves", "def-weil-derived-direct-image", "def-weil-finite-tor-amplitude", "def-weil-pbc-bounded-constructible-tower", "lem-sf-finite-level-comparison", "lem-sf-stage-independent-model-criterion", "lem-weil-pbc-reconstruction-uniform-tower"]
+++
Let $T$ be a scheme on which $\ell$ is invertible and let
$M_0\in D^b_c(T,\mathcal O_E)$ be a bounded constructible complex, with
reduction tower $M_n=M_0\otimes^L_{\mathcal O_E}A_{E,n}$; this is the
completed-integral situation of
[def-weil-derived-direct-image], in which every stage is the base
change of the single complex $M_0$. Assume that for every $n$ the
stage $M_n$ is a bounded complex whose
cohomology sheaves are
locally constant with finite $A_{E,n}$-module stalks, vanish outside an
interval $[a,b]$, and that $M_n$ has
finite Tor amplitude in $[a,b]$.
Then $M_\bullet$ is uniformly bounded constructible in the sense of
[def-weil-pbc-bounded-constructible-tower], and consequently

$$
\Bigl(R\varprojlim_nM_n\Bigr)\otimes^L_{\mathcal O_E}A_{E,n}
\xrightarrow{\ \sim\ }M_n
\qquad(n\geq1)
$$

by [lem-weil-pbc-reconstruction-uniform-tower]. In particular the
finite-level comparison isomorphisms of
[lem-sf-finite-level-comparison] hold for such a tower without any
further hypothesis.

## Proof

The tower $M_\bullet$ is an adic tower with the normalization isomorphisms
$M_{n+1}\otimes^L_{A_{E,n+1}}A_{E,n} =M_0\otimes^L_{\mathcal O_E}A_{E,n+1}\otimes^L_{A_{E,n+1}}A_{E,n} =M_0\otimes^L_{\mathcal O_E}A_{E,n}=M_n$ of
[def-weil-pbc-bounded-constructible-tower], by associativity of the
derived tensor product. The identity of $T$ is a finite étale
surjective morphism, and its restriction hypothesis is exactly the
hypothesis of the statement. Hence
[lem-sf-stage-independent-model-criterion] applies with $U=T$, and
gives that $M_\bullet$ is uniformly bounded constructible. The displayed
isomorphism is the reconstruction of
[lem-weil-pbc-reconstruction-uniform-tower] applied to that tower, and
the finite-level comparison is the same statement read in
[lem-sf-finite-level-comparison].
