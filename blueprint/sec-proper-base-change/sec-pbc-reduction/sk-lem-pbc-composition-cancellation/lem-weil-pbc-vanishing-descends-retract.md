+++
id = "lem-weil-pbc-vanishing-descends-retract"
kind = "lemma"
title = "Vanishing descends to a retract"
lean = ["AlgebraicGeometry.Etale.isZero_homology_rightDerivedFunctorPlus_of_retract"]
order = 2048
uses = ["def-weil-pbc-direct-image"]
+++
Let $h:X\to Y$ be a morphism of schemes and $\Lambda$ a commutative ring, and let
$I$ be a retract of $M$ in the category of sheaves of $\Lambda$-modules on
$X_{\Et}$, i.e. there are $s:I\to M$ and $r:M\to I$ with $rs=\mathrm{id}_I$. If
$R^qh_*M=0$ for some $q$ [def-weil-pbc-direct-image], then $R^qh_*I=0$.
