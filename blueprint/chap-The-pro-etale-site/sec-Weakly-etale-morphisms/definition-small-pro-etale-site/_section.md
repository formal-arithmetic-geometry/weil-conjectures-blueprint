+++
id = "definition-small-pro-etale-site"
kind = "definition"
title = "The small pro-étale site"
order = 34
lean = ["AlgebraicGeometry.Scheme.ProEt", "AlgebraicGeometry.Scheme.ProEt.precoverage", "AlgebraicGeometry.Scheme.proetalePrecoverage", "AlgebraicGeometry.QuasiCompactCover", "AlgebraicGeometry.Scheme.ProEt.topology"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability"]
+++
The objects of $X_{\mathrm{pro}\acute{e}t}$ are weakly étale $X$-schemes, with all
$X$-morphisms as arrows. A family $\{U_i\to U\}_{i\in I}$ is a
covering if it is an fpqc covering. Explicitly, for every affine open
$W\subset U$ there must be finitely many indices
$i_1,\ldots,i_m$ and affine opens
$V_j\subset U_{i_j}\times_UW$ with

$$
W=\bigcup_{j=1}^m\operatorname{image}(V_j\to W).
$$

The indices may depend on $W$, and $I$ may be infinite.
Equivalently one may use finitely many quasi-compact opens above each
$W$. See [Stacks, [0989](https://stacks.math.columbia.edu/tag/0989), [098A](https://stacks.math.columbia.edu/tag/098A)].
