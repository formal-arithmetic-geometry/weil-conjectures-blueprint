+++
id = "thm-sf-verdier-exchange"
kind = "theorem"
title = "Verdier-duality exchange"
order = 3285
uses = ["def-sf-datum", "def-sf-pf", "def-trf-admissibility", "def-weil-exceptional-inverse-image", "fix-cor-verdier-exchange", "lem-sf-mate", "lem-sf-tensor-hom", "thm-sf-comp-composition"]
+++
In the setting of [def-sf-datum], let $f:X\to Y$ be a separated
finite-type morphism, with $Rf^!$ and the dualizing complexes
$\omega_X=Ra_X^!\Lambda$, $\omega_Y=Ra_Y^!\Lambda$ formed with the
constructible exceptional inverse image of [def-weil-exceptional-inverse-image]
(no admissibility datum is assumed; every separated finite-type morphism is
exceptionally admissible in the sense of [def-trf-admissibility]). Then for
$M\in D^b_{ctf}(X,\Lambda)$ there is a canonical isomorphism

$$
D_Y(Rf_!M)\xrightarrow{\ \sim\ }Rf_*D_X(M),
$$

natural in $M$ and compatible with shifts.
