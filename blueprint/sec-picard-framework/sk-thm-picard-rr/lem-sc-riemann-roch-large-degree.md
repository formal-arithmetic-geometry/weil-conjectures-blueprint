+++
id = "lem-sc-riemann-roch-large-degree"
kind = "lemma"
title = "Sections of line bundles of degree at least $2g-1$"
order = 740
lean = ["AlgebraicGeometry.Scheme.Modules.finrankH_one_eq_zero_of_degree", "AlgebraicGeometry.Scheme.finrankH_zero_eq"]
uses = ["def-sc-pic0", "lem-pc-degree-base-change", "lem-sc-canonical-degree", "lem-sc-negative-degree-no-sections", "lem-sc-riemann-roch", "thm-sc-serre-duality-curve"]
+++
Let $k$ be a field, $C$ a scheme which is smooth of relative dimension
$1$ and proper over $k$ with $H^0(C,\mathcal O_C)=k$, of genus
$g=\dim_kH^1(C,\mathcal O_C)$, and $\mathcal L$ a line bundle on $C$ of
degree $d=\deg\mathcal L\ge2g-1$ ([def-sc-pic0]). Then
$H^1(C,\mathcal L)=0$ and

$$
h^0(\mathcal L):=\dim_kH^0(C,\mathcal L)=d+1-g.
$$
