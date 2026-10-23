+++
id = "lem-sc-canonical-degree"
kind = "lemma"
title = "Degree of the canonical bundle"
order = 720
lean = ["AlgebraicGeometry.Scheme.degree_relativeDifferentials", "AlgebraicGeometry.Scheme.finrankH_relativeDifferentials_zero_eq_arithmeticGenus", "AlgebraicGeometry.Scheme.serreDuality", "AlgebraicGeometry.Scheme.Hom.isInvertible_relativeDifferentials"]
uses = ["def-sc-pic0", "lem-sc-canonical-sheaf", "thm-sc-serre-duality-curve"]
+++
Let $k$ be a field and $C$ a scheme which is smooth of relative
dimension $1$ and proper over $k$ with $H^0(C,\mathcal O_C)=k$; put
$g=\dim_kH^1(C,\mathcal O_C)$. Then the invertible module
$\omega_C=\Omega^1_{C/k}$ satisfies

$$
\dim_kH^0(C,\omega_C)=g,\qquad \dim_kH^1(C,\omega_C)=1,\qquad
\deg\omega_C=2g-2,
$$

with $\deg$ the degree of [def-sc-pic0].
