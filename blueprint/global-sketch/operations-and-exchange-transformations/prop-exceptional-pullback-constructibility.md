+++
id = "prop-exceptional-pullback-constructibility"
kind = "theorem"
title = "Exceptional-pullback constructibility"
order = 67
tags = ["latex:proposition"]
uses = ["def-exceptional-inverse-image", "def-exceptional-pullback-exchange", "def-finite-reduction", "def-weil-finite-coefficient-datum", "prop-compact-support-base-change", "prop-ramified-coefficient-change", "thm-qbar-functor-descent"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$, and let
$\Lambda\in\{\mathcal O_E/\varpi_E^n,\mathcal O_E,E,\Qlb\}$, with
$n\geq1$ in the finite case. If $f:X\to Y$ is exceptional-adjoint
admissible, then

$$
Rf^!:D^b_c(Y,\Lambda)\longrightarrow D^b_c(X,\Lambda)
$$

is exact and right adjoint to $Rf_!$. It preserves the finite-Tor domain
specified by admissibility. For integral $L$,

$$
\operatorname{red}_{X,n}(Rf^!L)
\xrightarrow{\sim}Rf_n^!\operatorname{red}_{Y,n}(L).
$$

The mate $\operatorname{Ex}^{!}$, adjunction unit, and adjunction counit
commute with finite reduction, ramified scalar extension, and common-stage
descent.
If both horizontal maps of the Cartesian square are isomorphisms, then
$\operatorname{Ex}^{!}$ is an isomorphism; in particular this applies to
every Frobenius square.
