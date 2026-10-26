+++
id = "lem-sf-projection-finite-constant"
kind = "lemma"
title = "The projection formula with a finitely presented constant coefficient"
order = 2388
uses = ["def-sf-uniform-direct-image-vanishing", "def-weil-derived-pullback-tensor-hom", "def-weil-derived-tensor", "def-weil-pbc-direct-image", "def-weil-pbc-inverse-image", "thm-sp-truncation-e2"]
+++
Let $f:X\to Y$ be a morphism of schemes, let $A$ be a Noetherian
commutative ring, assume $R^qf_*F=0$ for every sheaf of $A$-modules
$F$ and every $q>N$, for one integer $N\geq0$, and let
$K\in D^-(X_{\Et},A)$. Let $M$ be a finitely
presented $A$-module, with $M_X,M_Y$ the associated constant sheaves.
Then the canonical projection map

$$
Rf_*K\otimes^L_AM_Y\longrightarrow Rf_*\bigl(K\otimes^L_AM_X\bigr)
$$

is an isomorphism, the direct image and the tensor product being those of
[def-weil-pbc-direct-image] and [def-weil-derived-tensor] on the
small étale sites. The map is natural in $M$.
