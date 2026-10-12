+++
id = "prop-weil-pbc-integral-tstructure"
kind = "theorem"
title = "The standard t-structure on the integral category"
order = 1431
uses = ["def-weil-pbc-bounded-constructible-complete", "def-weil-t-structure", "lem-weil-pbc-reconstruction-uniform-tower", "thm-weil-pbc-integral-truncations"]
tags = ["latex:proposition"]
+++
In the setting of [thm-weil-pbc-integral-truncations], set
$$
 (\Dbc(T_{\Proet},A))^{\le0}:=\{K:\mathcal H^i(K)=0\ \forall i>0\},
$$
$$
 (\Dbc(T_{\Proet},A))^{\ge0}:=\{K:\mathcal H^i(K)=0\ \forall i<0\}.
$$
These form a bounded t-structure on $\Dbc(T_{\Proet},A)$, whose truncation
functors are the $\tau^{\le m},\tau^{\ge m}$ of
[thm-weil-pbc-integral-truncations] and whose heart consists of the objects
with cohomology concentrated in degree zero. The subcategory of
$\varpi$-power-torsion objects is stable under the truncation functors.
