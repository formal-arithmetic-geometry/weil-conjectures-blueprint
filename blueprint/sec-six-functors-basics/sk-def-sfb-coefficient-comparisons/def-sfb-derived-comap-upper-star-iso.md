+++
id = "def-sfb-derived-comap-upper-star-iso"
kind = "definition"
title = "Derived restriction of scalars commutes with $D(f^*)$"
order = 1720
uses = ["def-sfb-comap-upper-star-iso", "sk-def-sfb-derived-categories"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.derivedComapUpperStarIso"]
+++
In the situation of [def-sfb-comap-upper-star-iso], the levelwise functors on the unbounded
derived categories ([sk-def-sfb-derived-categories]) satisfy

$$
D(\operatorname{Res}_{a_X})\circ D(f^*)\;\cong\;D(f^*)\circ D(\operatorname{Res}_{a_Y})\colon
D(\Mod_{\Lambda'_Y})\longrightarrow D(\Mod_{\Lambda_X}).
$$
