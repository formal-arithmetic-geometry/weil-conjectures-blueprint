+++
id = "prop-ag-det-weight-finite-tensor"
kind = "theorem"
title = "Determinant weights of a finite tensor power (conditional)"
order = 2763
uses = ["cor-mg-central-determinant-weight", "d-weights", "def-mg-weil-composition-series", "def-mg-weil-semisimplification", "lem-mg-common-positive-central-element", "lem-mg-composition-series-exists", "lem-mg-degree-component-functoriality", "lem-mg-filtered-finite-tensor-product", "lem-mg-filtration-refinement", "lem-mg-jordan-holder", "lem-wf-schur-scalar"]
+++
Fix a real weight character $\lambda$ as in [d-weights]. Let
$\mathcal F_0$ be a nonzero lisse Weil sheaf on a normal geometrically
connected curve $X_0$, choose a composition series in the sense of
[def-mg-weil-composition-series] with simple factors
$A_1,\ldots,A_n$, and put $\alpha_i=\dw_\lambda(A_i)$. Let $k\ge1$.
Assume that every $A_i$ and every Jordan–Holder constituent of
$\mathcal F_0^{\otimes k}$ has finite geometric determinant. Then every
Jordan–Holder constituent of $\mathcal F_0^{\otimes k}$ has
determinant weight

$$
\alpha_{i_1}+\cdots+\alpha_{i_k}
$$

for some indices $i_1,\ldots,i_k$, and every such sum occurs for at
least one constituent. In particular, if $\beta=\max_i\alpha_i$, the
largest determinant weight of $\mathcal F_0^{\otimes k}$ is
$k\beta$. Neither $\mathcal F_0$ nor the tensor power is assumed
semisimple.

## Proof

Write $V$ for the Weil representation and use the chosen composition
series, with simple factors $A_i$ (their multiset is independent of the
series by [lem-mg-jordan-holder]). The Weil semisimplification
$V^{\mathrm{ss}}=\bigoplus_iA_i$ of [def-mg-weil-semisimplification]
is a semisimple Weil representation. Apply
[lem-mg-common-positive-central-element] to $V^{\mathrm{ss}}$, and
let $z$ be the resulting central element of degree $d>0$. Its image
on the summand $A_i$ is central by
[lem-mg-degree-component-functoriality], hence is a scalar $c_i$ by
[lem-wf-schur-scalar], and

$$
\alpha_i=\frac{\lambda(c_i)}{d}
$$

by [cor-mg-central-determinant-weight], whose finite-determinant
hypothesis is assumed for $A_i$.

Apply [lem-mg-filtered-finite-tensor-product] to $k$ copies of
the chosen series. Every successive quotient is
$Q_{\boldsymbol i}=A_{i_1}\otimes\cdots\otimes A_{i_k}$, a tensor
construction on subquotients of $V^{\mathrm{ss}}$, so
[lem-mg-degree-component-functoriality] applies to it. The element
$z$ acts on it by $c_{i_1}\cdots c_{i_k}$. For any simple factor
$C$ of $Q_{\boldsymbol i}$, functoriality makes the induced element
central of degree $d$, and Schur's lemma followed by
[cor-mg-central-determinant-weight] (applicable because $C$ has finite
geometric determinant by assumption) gives

$$
\dw_\lambda(C)
=\frac{\lambda(c_{i_1}\cdots c_{i_k})}{d}
=\alpha_{i_1}+\cdots+\alpha_{i_k}.
$$

The refinement lemma [lem-mg-filtration-refinement] puts every
composition factor of $V^{\otimes k}$ in one of these quotients.
Conversely, each $Q_{\boldsymbol i}$ is nonzero and has a simple factor
by [lem-mg-composition-series-exists], so every displayed sum occurs.
The largest sum is $k\beta$.
