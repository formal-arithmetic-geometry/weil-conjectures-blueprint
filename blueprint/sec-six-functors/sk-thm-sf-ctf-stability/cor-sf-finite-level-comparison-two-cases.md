+++
id = "cor-sf-finite-level-comparison-two-cases"
kind = "theorem"
title = "The finite-level comparison isomorphisms in the two cases"
order = 2329
tags = ["latex:corollary"]
uses = ["def-weil-derived-direct-image", "lem-sf-finite-level-comparison", "thm-sf-uniform-models-constant-tower", "thm-sf-uniform-models-lisse-tower"]
+++
Fix the global finite-field datum and a separated finite-type morphism
$f:X\to Y$ of finite-type $k$-schemes, and let
$K\in D^b_c(X,\mathcal O_E)$ be derived complete with reductions
$K_n=K\otimes^L_{\mathcal O_E}A_{E,n}$. Suppose that the reduction tower
of the direct images $\lbrace Rf_{*,n}K_n\rbrace_{n\geq1}$ satisfies the
hypothesis of [thm-sf-uniform-models-constant-tower] or that of
[thm-sf-uniform-models-lisse-tower]. Then the finite-level comparison
map of [def-weil-derived-direct-image],

$$
(Rf_*K)\otimes^L_{\mathcal O_E}A_{E,n}\longrightarrow Rf_{*,n}K_n,
$$

is an isomorphism for every $n\geq1$, compatibly with composition of
morphisms and with scalar extension of the coefficient field. That is,
the direct-image comparison of [lem-sf-finite-level-comparison],
proved from the uniform local-model
hypothesis, holds in these two cases with no hypothesis beyond the one
displayed.

## Proof

In either case the reduction tower of the direct images is uniformly bounded
constructible, by [thm-sf-uniform-models-constant-tower] respectively
[thm-sf-uniform-models-lisse-tower]; the tower of the statement is a
tower of that form, with the same interval of bounds. Hence the hypothesis
of [lem-sf-finite-level-comparison] is satisfied, and that lemma is
exactly the assertion, including the compatibility with composition and with
scalar extension.
