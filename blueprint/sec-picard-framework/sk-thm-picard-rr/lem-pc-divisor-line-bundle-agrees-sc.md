+++
id = "lem-pc-divisor-line-bundle-agrees-sc"
kind = "lemma"
title = "$\\mathcal{O}_X(D)$ agrees with the divisor module of file 06"
lean = ["AlgebraicGeometry.Scheme.Divisor.toMul_toPic_mapRange_eq_dual", "AlgebraicGeometry.Scheme.IdealSheafData.IsInvertible.toMul_toPic_eq"]
order = 723
uses = ["def-pc-divisor-line-bundle", "def-sc-divisor", "def-nagata-invertible-ideal", "lem-sc-cartier-divisor-points", "lem-sc-point-cartier", "lem-sc-regular-dim1-dvr", "lem-sc-smooth-regular"]
+++
Let $k$ be a field and $C$ a scheme smooth of relative dimension $1$ over
$k$.

1. Let $E=\sum_{i=1}^m n_i[P_i]$ be an effective divisor of $C$ (all
$n_i\ge0$), viewed as the effective Cartier divisor with ideal sheaf
$\mathcal{I}_E=\prod_i\mathcal{I}_{P_i}^{n_i}$. Then the class
$[\mathcal{O}_C(E)]\in\operatorname{Pic}(C)$ of [def-sc-divisor] equals the
class of the module $\mathcal{O}_C(E)=\mathcal{I}_E^\vee$ of
[def-pc-divisor-line-bundle].
1. If $C$ is moreover integral and Noetherian, every effective Cartier
divisor $D\subset C$ is of this form: with
$n_P=\operatorname{ord}_P(\mathcal{I}_D)$ the order of the ideal at the
closed point $P$ (only finitely many are nonzero) and $E=\sum_Pn_P[P]$, the
class $[\mathcal{O}_C(E)]$ of [def-sc-divisor] equals the class of
$\mathcal{I}_D^\vee$.
