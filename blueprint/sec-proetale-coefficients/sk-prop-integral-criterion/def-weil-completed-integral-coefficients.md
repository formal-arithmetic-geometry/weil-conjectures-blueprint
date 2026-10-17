+++
id = "def-weil-completed-integral-coefficients"
kind = "definition"
title = "Completed integral coefficient sheaf"
order = 1814
uses = ["def-weil-derived-cohomology-sheaves", "def-weil-derived-tensor", "def-weil-finite-field-fiber", "def-weil-finite-torsion-constructibility", "def-weil-pbc-proetale-site", "sk-def-sfb-condensed-ring", "sk-def-sfb-pulled-back-coefficients", "det-prop-sfb-qlbar-colimit-x-integral-limit"]
+++
For the global finite-field datum [def-weil-finite-field-fiber], fix a prime
$\ell\neq p$, a finite extension $E/\Ql$, a scheme $Y$, and a uniformizer
$\varpi_E$ of the valuation ring $\mathcal O_E$. For each $n\in\mathbf
Z_{\geq1}$, set $A_{E,n}=\mathcal O_E/\varpi_E^n$ as in the finite-torsion
constructibility condition [def-weil-finite-torsion-constructibility], and
use the derived tensor product [def-weil-derived-tensor] on the small
pro-etale site [def-weil-pbc-proetale-site] of $Y$. The completed
coefficient sheaf is the pullback of the condensed ring
$\underline{\mathcal O}_E$ ([sk-def-sfb-condensed-ring]) from the point,

$$
 \widehat{\mathcal O}_{E,Y}:=\mathcal O_{E,Y}=p_Y^*\underline{\mathcal O}_E
$$

([sk-def-sfb-pulled-back-coefficients]). By
[det-prop-sfb-qlbar-colimit-x-integral-limit] there is a canonical isomorphism of
sheaves of rings

$$
 \widehat{\mathcal O}_{E,Y}\cong\varprojlim_n(A_{E,n})_Y,
$$

the limit of the constant sheaves taken in sheaves of rings, and we identify the
two sides along it. Let
$\Sh(Y_{\mathrm{proet}},\mathcal O_E)$ be the category of modules over
$\widehat{\mathcal O}_{E,Y}$, and let $D(Y_{\mathrm{proet}},\mathcal O_E)$ be
its localization at quasi-isomorphisms; this notation does not mean modules
over the discrete constant sheaf $(\mathcal O_E)_Y$. Cohomology sheaves of
complexes on $Y_{\mathrm{proet}}$ are those of the standard $t$-structure on
this derived category, as in [def-weil-derived-cohomology-sheaves]. For every
$n$ the surjection $\widehat{\mathcal
O}_{E,Y}\twoheadrightarrow(A_{E,n})_Y$, the projection from the limit, makes every $A_{E,n}$-module a module
over $\widehat{\mathcal O}_{E,Y}$, and

$$
 \operatorname{Res}_n:
 \Sh(Y_{\mathrm{proet}},A_{E,n})
 \longrightarrow\Sh(Y_{\mathrm{proet}},\mathcal O_E)
$$

denotes the resulting *restriction of scalars*. The reduction morphisms
$A_{E,n+1}\twoheadrightarrow A_{E,n}$ are the maps
$(A_{E,n+1})_Y\twoheadrightarrow(A_{E,n})_Y$ between constant sheaves.
