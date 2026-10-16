+++
id = "lem-pc-divisor-line-bundle-agrees-sc"
kind = "lemma"
title = "$\\mathcal{O}_X(D)$ agrees with the divisor module of file 06"
lean = ["AlgebraicGeometry.Scheme.Divisor.toMul_toPic_mapRange_eq_dual", "AlgebraicGeometry.Scheme.IdealSheafData.IsInvertible.toMul_toPic_eq"]
order = 728
uses = ["def-pc-divisor-line-bundle", "def-sc-divisor", "def-sc-effective-cartier-divisor", "lem-sc-point-cartier", "lem-sc-regular-dim1-dvr", "lem-sc-smooth-regular"]
+++
Let $k$ be a field, $C$ a smooth connected curve over $k$
and $D=\sum_{i=1}^m n_i[P_i]$ a
divisor of $C$ which is an effective Cartier
divisor (e.g. all $n_i\ge0$). Then the module

$$
\mathcal{O}_C(D)
$$

of [def-sc-divisor] (a sub-$\mathcal{O}_C$-module of the constant sheaf
$k(C)$) and the module $\mathcal{O}_C(D)$ of
[def-pc-divisor-line-bundle] are canonically isomorphic.
