+++
id = "def-sc-picard-group"
kind = "definition"
title = "The Picard group"
lean = ["AlgebraicGeometry.Scheme.Pic"]
order = 443
uses = ["def-sc-curves", "def-sc-invertible-module"]
+++
Let $C$ be a curve. The
*Picard group* $\operatorname{Pic}(C)$ is the set of
isomorphism classes of
invertible $\mathcal O_C$-modules, with the group law induced by tensor product: the
unit is $\mathcal O_C$ and the inverse of an invertible module
$\mathcal L$ is its dual $\mathcal L^{\vee}$.

The tensor product of two invertible modules and the dual
$\mathcal L^{\vee}$ of an invertible module are again invertible, and
this law satisfies the group axioms.
