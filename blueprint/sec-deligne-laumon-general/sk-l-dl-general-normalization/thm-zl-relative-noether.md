+++
id = "thm-zl-relative-noether"
kind = "theorem"
title = "Relative Noether normalization"
order = 3164
lean = ["AlgebraicGeometry.exists_partition_isFinite_toIteratedAffineLine"]
uses = ["def-sbc-affine-space", "def-weil-pbc-scheme-conventions"]
+++
Let $f:X_0\to Y_0$ be a morphism of finite type to a Noetherian
scheme $Y_0$ (for instance a separated finite-type morphism of
separated finite-type $k_0$-schemes).
There are finite partitions of source and target by locally closed
reduced subschemes such that each source piece $X'_0$ maps into
a target piece $Y'_0$ through a
factorization

$$
X'_0\xrightarrow{\nu}\mathbf A^d_{Y'_0}
\longrightarrow\mathbf A^{d-1}_{Y'_0}\longrightarrow\cdots
\longrightarrow\mathbf A^1_{Y'_0}\longrightarrow Y'_0
$$

of the restriction of $f$, with $\nu$ finite and all subsequent arrows
the coordinate projections of the iterated relative affine line.
For $d=0$, the factorization consists just of the finite map
$X'_0\to Y'_0=\mathbf A^0_{Y'_0}$.
