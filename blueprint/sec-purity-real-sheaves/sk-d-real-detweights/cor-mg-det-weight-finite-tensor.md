+++
id = "cor-mg-det-weight-finite-tensor"
kind = "theorem"
title = "Determinant weights of a finite tensor power"
order = 2823
tags = ["latex:corollary"]
uses = ["def-mg-determinantal-weight-multiset", "def-mg-weil-composition-series", "def-wf-determinantal-weight", "def-wf-geometric-semisimplicity", "lem-mg-jordan-holder", "lem-rp-determinant-weights-agree", "prop-ag-det-weight-finite-tensor"]
+++
Let $\mathcal F_0$ be a nonzero lisse Weil sheaf with
semisimple geometric
representation on a normal geometrically connected curve $X_0$, and let
$\alpha_1,\ldots,\alpha_n$ be its determinant weights, counted with
multiplicity in [def-mg-determinantal-weight-multiset]. For every
$k\ge1$, every Jordan–Holder constituent of
$\mathcal F_0^{\otimes k}$ has
determinant weight

$$
\alpha_{i_1}+\cdots+\alpha_{i_k}
$$

for some indices $i_1,\ldots,i_k$, and every such sum occurs for at
least one constituent. In particular, if $\beta=\max_i\alpha_i$, the
largest determinant weight of $\mathcal F_0^{\otimes k}$ is
$k\beta$.

## Proof

Choose a composition series of the Weil representation in the sense of
[def-mg-weil-composition-series], with simple factors $A_i$. By
[lem-mg-jordan-holder] and [def-mg-determinantal-weight-multiset], after
reindexing, $\alpha_i=\dw_\iota(A_i)$ (the geometric semisimplicity of
[def-wf-geometric-semisimplicity] is not needed for the argument). By
[lem-rp-determinant-weights-agree], every $A_i$ and every
Jordan–Holder constituent of $\mathcal F_0^{\otimes k}$ has finite
geometric determinant, and for each of them the determinant weight
$\dw_\iota$ of [def-wf-determinantal-weight] equals
$\dw_{\lambda_\iota}$. Hence [prop-ag-det-weight-finite-tensor], applied with
$\lambda=\lambda_\iota$, gives both assertions.
