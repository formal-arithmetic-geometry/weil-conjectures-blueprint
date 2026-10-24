+++
id = "prop-ag-det-weight-two-factor-tensor"
kind = "theorem"
title = "Determinant weights of a tensor product of two representations (conditional)"
order = 3775
uses = ["cor-mg-central-determinant-weight", "d-monodromy", "d-weights", "def-mg-weil-composition-series", "def-mg-weil-semisimplification", "lem-mg-common-positive-central-element", "lem-mg-composition-series-exists", "lem-mg-degree-component-functoriality", "lem-mg-filtered-tensor-product", "lem-mg-filtration-refinement", "lem-mg-jordan-holder", "lem-wf-schur-scalar"]
lean = ["Representation.exists_detWeight_eq_add_of_subquotient_tprod"]
+++
Fix a real weight character $\lambda$ as in [d-weights]. Let $V$ and
$E$ be nonzero Weil representations of one and the same degree datum
([d-monodromy]) over an algebraically closed field of characteristic
zero. Choose composition series in the sense of
[def-mg-weil-composition-series], with simple factors
$V_1,\ldots,V_t$ of $V$ and $E_1,\ldots,E_u$ of $E$. Assume that every
$V_i$, every $E_j$, and every Jordan–Holder constituent of
$V\otimes E$ has finite geometric determinant. Then for every
Jordan–Holder constituent $Q$ of $V\otimes E$ there is a pair $(i,j)$
with

$$
\dw_\lambda(Q)=\dw_\lambda(V_i)+\dw_\lambda(E_j).
$$

Conversely, every such sum occurs for at least one constituent. Neither
$V$, $E$ nor $V\otimes E$ is assumed semisimple.
