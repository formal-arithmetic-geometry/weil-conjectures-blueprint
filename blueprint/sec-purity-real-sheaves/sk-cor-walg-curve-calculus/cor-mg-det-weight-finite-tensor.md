+++
id = "cor-mg-det-weight-finite-tensor"
kind = "theorem"
title = "Determinant weights of a finite tensor power"
lean = ["AlgebraicGeometry.WeilGroup.detWeight_subquotient_tensorPower", "AlgebraicGeometry.WeilGroup.isGreatest_detWeight_subquotient_tensorPower"]
order = 3847
tags = ["latex:corollary"]
uses = ["def-mg-determinantal-weight-multiset", "def-mg-weil-composition-series", "def-real-weil-representation-operations", "def-wf-determinantal-weight", "def-wf-geometric-monodromy-group", "lem-mg-jordan-holder", "lem-rp-determinant-weights-agree", "prop-ag-det-weight-two-factor-tensor"]
+++
Let $\mathcal F_0$ be a nonzero lisse Weil sheaf on a smooth
geometrically connected curve $X_0$, and let
$\alpha_1,\ldots,\alpha_n$ be its determinant weights, counted with
multiplicity in [def-mg-determinantal-weight-multiset]. For every
$k\ge1$, every Jordan–Holder constituent of the tensor power
$\mathcal F_0^{\otimes k}$ (constituents and tensor products of Weil
representations as in [def-real-weil-representation-operations]) has
determinant weight

$$
\alpha_{i_1}+\cdots+\alpha_{i_k}
$$

for some indices $i_1,\ldots,i_k$, and every such sum occurs for at
least one constituent. In particular, if $\beta=\max_i\alpha_i$, the
largest determinant weight of $\mathcal F_0^{\otimes k}$ is
$k\beta$.
