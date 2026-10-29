+++
id = "lem-pc-degree-agrees-sc"
kind = "lemma"
title = "Degree agrees with the degree of file 06"
lean = ["AlgebraicGeometry.Scheme.Divisor.degree_dual_toModules_idealSheaf", "AlgebraicGeometry.Scheme.Divisor.degree_dual_toModules_idealSheaf_eq_degree"]
order = 730
uses = ["def-pc-curve", "def-pc-degree-line-bundle", "def-pc-divisor-line-bundle", "def-sc-divisor", "def-sc-pic0", "lem-pc-degree-base-change", "lem-pc-divisor-line-bundle-properties", "lem-pc-euler-additive"]
+++
Let $k$ be a field, $C$ a proper smooth
curve over $k$, and $D$ a
divisor of $C$ which is effective, $D=\sum_Pn_P[P]$ with $P$ closed points
and $n_P\ge0$. Then the
degree $\deg(\mathcal{O}_C(D))$ of
Definition [def-pc-degree-line-bundle] is
$\sum_Pn_P[\kappa(P):k]$; for $k$ algebraically closed this
equals $\deg D$ of [def-sc-pic0]. In particular for a $k$-rational point $P$,
$\deg(\mathcal{O}_C([P]))=1$.
