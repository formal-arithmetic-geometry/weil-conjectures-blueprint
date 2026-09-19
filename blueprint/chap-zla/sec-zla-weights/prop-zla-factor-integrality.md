+++
id = "prop-zla-factor-integrality"
kind = "theorem"
title = "Integrality of an individual factor"
order = 1028
tags = ["latex:proposition"]
uses = ["def-zla-complete-weight-factor", "lem-zla-normalized-gauss", "prop-zla-weight-stratum-rational"]
+++
The recovered polynomial $P_i^{\mathrm{rec}}(T)$ belongs to $\mathbf Z[T]$.

## Proof

By [prop-zla-weight-stratum-rational] the polynomial
$P_i^{\mathrm{rec}}$ is a factor of $R_i$ in $\mathbf Q[T]$ whose
complementary factor $R_i/P_i^{\mathrm{rec}}$ is again rational, and both
have constant coefficient $1$. Now $R_i$ is $A$ or $B$, hence lies in
$\mathbf Z[T]$ with $R_i(0)=1$, and [lem-zla-normalized-gauss] applied to
this factorization gives $P_i^{\mathrm{rec}}\in\mathbf Z[T]$.
