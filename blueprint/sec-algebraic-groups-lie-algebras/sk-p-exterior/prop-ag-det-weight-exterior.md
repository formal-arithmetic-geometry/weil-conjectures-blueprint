+++
id = "prop-ag-det-weight-exterior"
kind = "theorem"
title = "Determinant weights of an exterior power (conditional)"
order = 3777
uses = ["cor-mg-central-determinant-weight", "d-monodromy", "d-weights", "def-mg-weil-composition-series", "def-mg-weil-semisimplification", "def-wf-monodromy-data", "lem-mg-common-positive-central-element", "lem-mg-composition-series-exists", "lem-mg-degree-component-functoriality", "lem-mg-filtered-exterior-power", "lem-mg-filtration-refinement", "lem-wf-schur-scalar"]
lean = ["Representation.CompositionSeries.exteriorPower_detWeight", "Representation.exists_multiset_le_and_detWeight_eq_sum_of_exteriorPower", "Representation.exists_detWeight_eq_sum_of_exteriorPower"]
+++
Fix a real weight character $\lambda$ as in [d-weights], and let $V$ be
a nonzero Weil representation of a degree datum ([d-monodromy]) over an
algebraically closed field of characteristic zero. Choose a
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
Jordan–Holder constituent of $\bigwedge^rV$ has finite
geometric determinant. Then every Jordan–Holder constituent of
$\bigwedge^rV$ has
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
