+++
id = "lem-pc-cech-computes"
kind = "lemma"
title = "The Cech complex computes cohomology"
order = 623
uses = ["def-pc-morphism-conventions", "def-pc-scheme", "pqf-lem-affine-vanishing", "lem-sc-cech-spectral"]
lean = ["AlgebraicGeometry.Scheme.Modules.nonempty_cechComplex_linearEquiv_H"]
+++
Let $X$ be a scheme and let $\mathcal U:X=\bigcup_{i\in I}U_i$ be an
open covering such that all finite intersections $U_{i_0\dots i_p}$ are
affine. Then for any quasi-coherent $\mathcal{O}_X$-module $\mathcal{F}$
there is, for every $p\ge0$, an isomorphism of
$\Gamma(X,\mathcal O_X)$-modules

$$
\check H^p(\mathcal U,\mathcal{F})\cong H^p(X,\mathcal{F}).
$$
