+++
id = "lem-chow-affine-immersion"
kind = "lemma"
title = "An affine scheme of finite type immerses into projective space"
order = 1085
lean = ["AlgebraicGeometry.exists_isImmersion_projectiveSpace"]
uses = ["def-nagata-affine-proj", "def-nagata-projective-space-base-change", "def-weil-pbc-scheme-conventions"]
+++
Let $S$ be a scheme and let $V$ be an affine scheme equipped with a morphism
$g\colon V\to S$ that is locally of finite type. Then there are a finite set
$n$ and an immersion $j\colon V\to\mathbf P^n_S$ with
$j$ followed by $\mathbf P^n_S\to S$ equal to $g$, where the homogeneous
coordinates $T_i$ of $\mathbf P^n_S$ are indexed by the finite set $n$.
