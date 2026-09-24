+++
id = "cor-mg-det-weight-finite-tensor"
kind = "theorem"
title = "Determinant weights of a finite tensor power"
order = 4123
tags = ["latex:corollary"]
uses = ["cor-mg-central-determinant-weight", "def-mg-determinantal-weight-multiset", "def-mg-weil-composition-series", "def-wf-determinantal-weight", "def-wf-geometric-semisimplicity", "lem-mg-common-positive-central-element", "lem-mg-composition-series-exists", "lem-mg-degree-component-functoriality", "lem-mg-filtered-finite-tensor-product", "lem-mg-filtration-refinement", "lem-mg-jordan-holder", "lem-wf-schur-scalar"]
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

Write $V$ for the Weil representation and choose a composition series
in the sense of [def-mg-weil-composition-series], with simple factors
$A_i$. By
[lem-mg-jordan-holder], [def-mg-determinantal-weight-multiset], after
reindexing,
$\alpha_i=\dw_\iota(A_i)$. Since $V$ is geometrically
semisimple in the sense of
[def-wf-geometric-semisimplicity], so is $V^{\oplus k}$. Apply
[lem-mg-common-positive-central-element] to $V^{\oplus k}$, and
let $z$ be the resulting central element of degree $d>0$. Its image
on $A_i$ is a scalar $c_i$, by
[lem-mg-degree-component-functoriality] and
[lem-wf-schur-scalar], and

$$
\alpha_i=\frac{2\log_q|\iota(c_i)|}{d}
$$

by [cor-mg-central-determinant-weight] and the normalization in
[def-wf-determinantal-weight].

Apply [lem-mg-filtered-finite-tensor-product] to $k$ copies of
the chosen series. Every successive quotient is
$Q_{\boldsymbol i}=A_{i_1}\otimes\cdots\otimes A_{i_k}$. The element
$z$ acts on it by $c_{i_1}\cdots c_{i_k}$. For any simple factor
$C$ of $Q_{\boldsymbol i}$, functoriality makes the induced element
central of degree $d$, and Schur's lemma followed by
[cor-mg-central-determinant-weight] gives

$$
\dw_\iota(C)
=\frac{2\log_q|\iota(c_{i_1}\cdots c_{i_k})|}{d}
=\alpha_{i_1}+\cdots+\alpha_{i_k}.
$$

The refinement lemma [lem-mg-filtration-refinement] puts every
composition factor of $V^{\otimes k}$ in one of these quotients.
Conversely, each $Q_{\boldsymbol i}$ is nonzero and has a simple factor
by [lem-mg-composition-series-exists], so every displayed sum occurs.
The largest sum is $k\beta$.
