+++
id = "prop-galois-weight-strata-integrality"
kind = "theorem"
title = "Integrality of the normalized stratum polynomials"
lean = ["Polynomial.weilStratumPoly", "Polynomial.exists_map_eq_weilStratumPoly", "Polynomial.exists_int_weilStratumPoly"]
order = 4137
tags = ["latex:proposition"]
uses = ["def-weil-numbers", "def-weil-ordinary-reciprocal-roots", "prop-galois-weight-strata"]
+++
In the situation of [prop-galois-weight-strata], for every integer
$i$ with $0\leq i\leq2d$ the normalized stratum polynomial

$$
Q_i(T)=\prod_{\alpha\in R_i}(1-\alpha T)
$$

over the $q$-Weil numbers of weight $i$
lies in $\mathbf Z[T]$.
