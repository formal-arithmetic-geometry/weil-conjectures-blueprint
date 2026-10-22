+++
id = "def-pc-derived-direct-image"
kind = "definition"
title = "Derived direct image"
lean = ["AlgebraicGeometry.Scheme.Modules.derivedPushforward", "AlgebraicGeometry.Scheme.Modules.higherDirectImage"]
order = 650
uses = ["def-pc-derived-category", "def-pc-scheme"]
+++
Let $f:X\to S$ be a morphism of schemes. The *derived direct
image* is the total derived functor
$Rf_*:D(\mathcal{O}_X)\to D(\mathcal{O}_S)$ of the direct image $f_*$. The
*higher direct images* $R^if_*$ are the right derived functors of $f_*$ on
$\mathcal O_X$-modules; for a module $E$, $R^if_*E=H^i(Rf_*E)$.
