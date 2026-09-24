+++
id = "lemma-weil-pbc-derived-complete-reconstruction"
kind = "lemma"
title = "Derived-complete reconstruction"
order = 1939
uses = ["def-weil-pbc-intrinsic-koszul-completion", "lemma-weil-pbc-koszul-quotient-limit"]
+++
If $K$ is intrinsically derived $I$-complete, then

$$
\operatorname{comp}_K:K\xrightarrow{\sim}R\varprojlim_nK_n
$$

is an isomorphism, functorially in $K$.

## Proof

By intrinsic completeness, $\kappa_K$ is an isomorphism. The preceding
lemma identifies $\operatorname{comp}_K$ with the composite
$c_K\kappa_K$, so it too is an isomorphism. For $u:K\to L$, naturality of
the Koszul augmentations and of the product-cone construction gives

$$
(R\varprojlim u_n)\operatorname{comp}_K
=\operatorname{comp}_Lu.
$$

Conjugating by the two reconstruction isomorphisms proves functoriality,
including functoriality of their inverses. This is the explicit
Koszul-to-adic argument behind Tag `099M`.
