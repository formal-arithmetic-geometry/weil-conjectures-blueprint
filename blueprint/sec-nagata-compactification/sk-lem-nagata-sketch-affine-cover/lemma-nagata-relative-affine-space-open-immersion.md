+++
id = "lemma-nagata-relative-affine-space-open-immersion"
kind = "lemma"
title = "The standard affine chart in relative projective space"
order = 317
lean = ["AlgebraicGeometry.AffineSpace.isOpenImmersion_toRelativeProjectiveSpace"]
uses = ["def-nagata-affine-proj", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-projective-space-base-change", "def-nagata-relative-affine-space", "def-nagata-relative-projective-space", "lemma-nagata-relative-affine-space-charts", "lemma-nagata-relative-proj-exists"]
+++
For every index set $n$ and every scheme $S$, the morphism
$\mathbb A^n_S\to\mathbf P(\{0\}\sqcup n;S)$ over $S$ induced by
$T_i\mapsto T_i/T_0$ (the standard chart at the extra homogeneous
coordinate $T_0$) is an open immersion.
