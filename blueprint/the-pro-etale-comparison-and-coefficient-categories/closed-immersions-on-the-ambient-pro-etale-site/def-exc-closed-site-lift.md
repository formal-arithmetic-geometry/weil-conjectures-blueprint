+++
id = "def-exc-closed-site-lift"
kind = "definition"
title = "Lifting affine objects of the closed site"
order = 2731
lean = ["AlgebraicGeometry.Proetale.closedSiteLift"]
uses = ["def-weil-pbc-ind-etale-basis", "def-exc-ind-etale-closed-lift"]
+++
For $X=\operatorname{Spec}A$, $Z=\operatorname{Spec}(A/I)$, write
$u:\mathcal B_X\to\mathcal B_Z$ for base change. For
$V=\operatorname{Spec}\overline C$ in the basis of
[def-weil-pbc-ind-etale-basis], set
$$
 v(V)=\operatorname{Spec}H_A(\overline C),
$$
using [def-exc-ind-etale-closed-lift]. Maps are the opposites of the maps
supplied by that algebra construction.
