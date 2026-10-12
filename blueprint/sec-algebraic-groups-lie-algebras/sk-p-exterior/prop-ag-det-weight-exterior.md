+++
id = "prop-ag-det-weight-exterior"
kind = "theorem"
title = "Determinant weights of an exterior power (conditional)"
order = 2899
uses = ["cor-mg-central-determinant-weight", "d-weights", "def-mg-weil-composition-series", "def-mg-weil-semisimplification", "def-wf-monodromy-data", "def-wf-weil-category", "lem-mg-common-positive-central-element", "lem-mg-composition-series-exists", "lem-mg-degree-component-functoriality", "lem-mg-filtered-exterior-power", "lem-mg-filtration-refinement", "lem-wf-schur-scalar"]
lean = ["Representation.exists_multiset_le_and_detWeight_eq_sum_of_exteriorPower"]
+++
Let $X_0$ be a normal geometrically connected curve over $k_0$, put
$|k_0|=q$, fix a real weight character $\lambda$ as in [d-weights], and let
$\mathcal F_0$ be a nonzero lisse
Weil sheaf on $X_0$. Choose a
composition series in the sense of
[def-mg-weil-composition-series], with simple factors
$A_1,\ldots,A_t$. Write $d_a=\dim A_a$ and let
$\gamma_a=\dw_\lambda(A_a)$.
Let $R$ be the set of distinct values among the $\gamma_a$, and put

$$
r(\gamma):=\sum_{\gamma_a=\gamma}d_a,
$$

Thus $\dim V=\sum_{\gamma\in R}r(\gamma)$. Let
$0\le r\le\dim V$, and assume that every $A_a$ and every
Jordan–Holder constituent of $\bigwedge^r\mathcal F_0$ has finite
geometric determinant. Then every Jordan–Holder constituent of
$\bigwedge^r\mathcal F_0$ has
determinant weight

$$
\sum_{\gamma\in R}n_\gamma\gamma,
\qquad 0\le n_\gamma\le r(\gamma),
\qquad \sum_{\gamma\in R}n_\gamma=r.
$$

Conversely every admissible tuple $(n_\gamma)$ occurs as the
determinant weight of at least one
Jordan–Holder constituent. The input factors
$\gamma_a$ are counted with multiplicity; the assertion concerns the
possible weights and their non-emptiness, not an equality of output
multiplicities for coincident sums.
