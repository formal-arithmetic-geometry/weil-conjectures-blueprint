+++
id = "def-cohomology-complexes"
kind = "definition"
title = "Ordinary and compactly supported cohomology"
order = 88
uses = ["def-all-coefficient-compact-support", "def-derived-direct-image", "def-point-coefficient-categories", "def-point-fiber-functor", "def-weil-finite-coefficient-datum", "prop-compact-support-coefficient-passage", "prop-direct-image-constructibility"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum], and let
$\Lambda\in\{\mathcal O_E/\varpi_E^n,\mathcal O_E,E,\Qlb\}$, with
$n\geq1$ in the finite case. Let $Y$ be separated and of finite type
over $k$, with structure map
$a_Y:Y\to s=\Spec k$. For $K\in D^b_c(Y,\Lambda)$, define

$$
\RGamma(Y,K)=\operatorname{Fib}_{s,\Lambda}(Ra_{Y*}K),\qquad
\RGammac(Y,K)=\operatorname{Fib}_{s,\Lambda}(Ra_{Y!}K),
$$

and, for every $i\in\mathbf Z$,

$$
H^i(Y,K)=\mathrm H^i\RGamma(Y,K),\qquad
H_c^i(Y,K)=\mathrm H^i\RGammac(Y,K).
$$

Finite-dimensionality and the proper comparison are theorem-level
statements recorded below, not part of this definition.
