+++
id = "thm-sf-uniform-models-lisse-tower"
kind = "theorem"
title = "Stage-independent local models for a lisse tower with a uniform trivializing cover"
order = 3457
uses = ["def-weil-derived-cohomology-sheaves", "def-weil-finite-tor-amplitude", "def-weil-pbc-bounded-constructible-tower", "lem-sf-finite-level-comparison", "lem-sf-stage-independent-model-criterion", "lem-weil-pbc-reconstruction-uniform-tower"]
+++
Let $T$ be a scheme on which $\ell$ is invertible, let $M_\bullet$ be
an adic tower on $T$ with the normalization isomorphisms
$M_{n+1}\otimes^L_{A_{E,n+1}}A_{E,n}\simeq M_n$ of
[def-weil-pbc-bounded-constructible-tower], and let $u:U\to T$ be a
finite étale surjective morphism over which the tower is *uniformly*
locally constant: for every $n$ the restriction $M_n|_U$ is a bounded
complex whose
cohomology sheaves are
locally constant with finite $A_{E,n}$-module stalks, vanish outside one
interval $[a,b]$, and $M_n|_U$ has
finite Tor amplitude in $[a,b]$.
Then $M_\bullet$ is uniformly bounded constructible in the sense of
[def-weil-pbc-bounded-constructible-tower]: the local models are
stage-independent, being bounded complexes of finite locally constant
module sheaves supported in $[a,b]$, and consequently

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

The hypotheses are exactly those of
[lem-sf-stage-independent-model-criterion], which therefore gives the
stage-independent local model on a pro-étale covering member and the
uniform bounded constructibility of the tower. The displayed isomorphism is
[lem-weil-pbc-reconstruction-uniform-tower], and the finite-level
comparison is its reading in [lem-sf-finite-level-comparison].
