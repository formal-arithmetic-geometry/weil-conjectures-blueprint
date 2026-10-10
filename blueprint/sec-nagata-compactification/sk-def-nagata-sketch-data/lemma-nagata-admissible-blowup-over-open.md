+++
id = "lemma-nagata-admissible-blowup-over-open"
kind = "lemma"
title = "An admissible blow-up is unchanged over the preserved open"
order = 62
lean = ["AlgebraicGeometry.IsAdmissible.isIso_blowupMap_restrict"]
uses = ["def-nagata-admissible-blowup", "def-nagata-global-blowup", "lemma-nagata-affine-blowup-complement", "lemma-nagata-ideal-unit-off-support", "prop-nagata-global-blowup-cover-independent", "thm-nagata-global-blowup-complement"]
+++
Let $\mathcal I$ be a $U$-admissible blow-up center on $X$ and let
$\pi\colon\operatorname{Bl}_{\mathcal I}(X)\to X$ be the associated
$U$-admissible blow-up. Then the restriction
$\pi^{-1}(U)\to U$ of $\pi$ is an isomorphism.

## Proof

By [def-nagata-admissible-blowup] the support $V(\mathcal I)$ is disjoint
from $U$, so $U$ is an open subset of $X\setminus V(\mathcal I)$. By
[thm-nagata-global-blowup-complement] the restriction of $\pi$ over
$X\setminus V(\mathcal I)$ is an isomorphism; restricting further over the
open $U$ gives that $\pi^{-1}(U)\to U$ is an isomorphism.
