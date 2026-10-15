+++
id = "def-sfb-module-upper-star-comp"
kind = "definition"
title = "Composition isomorphism of pullbacks of module objects"
order = 1691
uses = ["def-sfb-module-upper-star", "def-sfb-module-upper-lower-adjunction", "def-sfb-module-lower-star-comp"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.upperStarComp"]
+++
Let $\Lambda$ be a commutative condensed ring and $f\colon X\to Y$, $g\colon Y\to Z$
morphisms of schemes. The natural isomorphism

$$
(g\circ f)^*\cong f^*\circ g^*\colon\Mod_{\Lambda_Z}\to\Mod_{\Lambda_X}
$$

of pullbacks of module objects ([def-sfb-module-upper-star]) is the isomorphism of
left adjoints conjugate, under the adjunctions $(g\circ f)^*\dashv(g\circ f)_*$ and
$f^*\circ g^*\dashv g_*\circ f_*$ of [def-sfb-module-upper-lower-adjunction], to the
inverse of the composition isomorphism $g_*\circ f_*\cong(g\circ f)_*$ of
[def-sfb-module-lower-star-comp].
