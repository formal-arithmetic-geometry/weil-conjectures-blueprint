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

## Proof

The shift conditions and the orthogonality of a t-structure, namely
$\Hom(A,B[-1])=0$ for $A\in(\Dbc)^{\le0}$, $B\in(\Dbc)^{\ge0}$, are the
corresponding ambient statements for the standard t-structure of
$D(T_{\Proet},A)$, since $\Dbc(T_{\Proet},A)$ is a full subcategory and its
objects' cohomology sheaves are the ambient ones. The truncation axiom and
the truncation triangles are [thm-weil-pbc-integral-truncations] (ii)--(iii)
with the cohomology formulas of (ii) showing the end terms to lie in the
claimed subcategories. Boundedness: by the reconstruction lemma for uniform
towers (and its use in [thm-weil-pbc-integral-truncations]), an object's
local models are supported in a finite interval $[d_0,d_1]$, so its
cohomology vanishes outside it; the interval is part of the data of
[def-weil-pbc-bounded-constructible-complete]. Finally the truncation
functors are additive and $A_T$-linear, so if $\varpi^n\cdot1_K=0$ in
$\Dbc(T_{\Proet},A)$, then
$\varpi^n\cdot1_{\tau^{\le m}K}=\tau^{\le m}(\varpi^n\cdot1_K)=0$, and
similarly for $\tau^{\ge m+1}$.
