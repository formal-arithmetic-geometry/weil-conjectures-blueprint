+++
id = "lem-cbc-open-closed-recollement"
kind = "lemma"
title = "Open-closed recollement"
lean = ["AlgebraicGeometry.Etale.openClosedShortComplex", "AlgebraicGeometry.Etale.shortExact_openClosedShortComplex", "AlgebraicGeometry.Etale.exists_distTriang_openClosed"]
order = 1217
uses = ["def-weil-open-closed-recollement", "def-weil-pbc-derived-categories", "def-weil-pbc-extension-by-zero", "def-weil-pbc-scheme-conventions", "lemma-weil-pbc-finite-direct-image-exact", "prop-weil-open-closed-recollement-adjunctions"]
+++
Let $i:Z\hookrightarrow X$ be a closed immersion with complementary open
immersion $j:U\hookrightarrow X$, and let $\Lambda$ be a commutative ring,
for instance a finite one (more generally, the coefficients may be any
Grothendieck abelian category with the monoidal structure used for derived
tensor products, such as $\Lambda$-modules). For every etale sheaf $F$ on $X$
the sequence
$$
0\longrightarrow j_!j^{-1}F\longrightarrow F\longrightarrow i_*i^{-1}F
\longrightarrow0,
$$
whose maps are the counit of $j_!\dashv j^{-1}$ and the unit of
$i^{-1}\dashv i_*$, is exact. For every $K\in D(X_{\Et},\Lambda)$ the counit
$j_!j^{-1}K\to K$ and the unit $K\to Ri_*i^{-1}K$ of the derived adjunctions
extend to a distinguished triangle
$$
j_!j^{-1}K\longrightarrow K\longrightarrow Ri_*i^{-1}K
\longrightarrow j_!j^{-1}K[1],
$$
where $Ri_*=i_*$ is the (exact) direct image of the closed immersion.
