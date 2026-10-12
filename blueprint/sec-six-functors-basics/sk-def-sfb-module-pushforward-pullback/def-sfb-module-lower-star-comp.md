+++
id = "def-sfb-module-lower-star-comp"
kind = "definition"
title = "Composition isomorphism of pushforwards of module objects"
order = 1673
uses = ["def-sfb-module-lower-star"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.lowerStarComp"]
+++
Let $\Lambda$ be a commutative condensed ring and $f\colon X\to Y$, $g\colon Y\to Z$
morphisms of schemes. There is a natural isomorphism

$$
g_*\circ f_*\cong(g\circ f)_*\colon\Mod_{\Lambda_X}\to\Mod_{\Lambda_Z}
$$

of pushforwards of module objects ([def-sfb-module-lower-star]) whose underlying
isomorphism of sheaves is the composition isomorphism
$g^{\Ab}_*f^{\Ab}_*M\cong(g\circ f)^{\Ab}_*M$ of pushforwards of abelian sheaves.
