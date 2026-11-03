+++
id = "sk-def-pe-site"
kind = "definition"
title = "The small pro-étale site"
order = 31
lean = ["AlgebraicGeometry.Scheme.ProEt", "AlgebraicGeometry.Scheme.ProEt.topology", "AlgebraicGeometry.Scheme.proetalePrecoverage", "AlgebraicGeometry.Scheme.etalePrecoverage_le_proetalePrecoverage"]
uses = ["sk-def-pe-morphisms", "sk-lem-pe-weakly-etale-stability"]
tags = ["sketch"]
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
$W$. See [Stacks, Tag 0989](https://stacks.math.columbia.edu/tag/0989), [Stacks, Tag 098A](https://stacks.math.columbia.edu/tag/098A).
