+++
id = "prop-verdier-duality"
kind = "theorem"
title = "Verdier duality"
order = 70
tags = ["latex:proposition"]
uses = ["def-verdier-duality-functor", "def-weil-finite-coefficient-datum", "prop-direct-image-constructibility", "prop-exceptional-pullback-constructibility", "prop-internal-hom-constructibility"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$, and let
$\Lambda\in\{\mathcal O_E/\varpi_E^n,\mathcal O_E,E,\Qlb\}$, with
$n\geq1$ in the finite case. Let
$a_Y:Y\to\Spec k$ be exceptional-adjoint admissible. For every
$K\in D^b_{ctf}(Y,\Lambda)$, biduality

$$
K\xrightarrow{\sim}D_YD_YK
$$

makes $D_Y$ a contravariant equivalence. For separated finite-type
$f:X\to Y$ such that $a_X=a_Y\circ f$ is also
exceptional-adjoint admissible, and $K\in D^b_{ctf}(X,\Lambda)$, the evaluation and
adjunction maps give

$$
D_YRf_!K\xrightarrow{\sim}Rf_*D_XK.
$$

The biduality and exchange arrows commute with finite reduction, ramified
scalar extension, and common-stage descent.
