+++
id = "lem-chow-affine-immersion"
kind = "lemma"
title = "An affine scheme of finite type immerses into projective space"
order = 1053
lean = ["AlgebraicGeometry.exists_isImmersion_projectiveSpace"]
uses = ["def-nagata-affine-proj", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-projective-space-base-change", "def-nagata-relative-affine-space", "def-weil-pbc-scheme-conventions", "prop-nagata-proj-standard-open"]
+++
Let $S$ be a scheme and let $V$ be an affine scheme equipped with a morphism
$g\colon V\to S$ that is locally of finite type. Then there are a finite set
$n$ and an immersion $j\colon V\to\mathbf P^n_S$ with
$j$ followed by $\mathbf P^n_S\to S$ equal to $g$, where the homogeneous
coordinates $T_i$ of $\mathbf P^n_S$ are indexed by the finite set $n$.
