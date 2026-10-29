+++
id = "def-sfb-comap-open-immersion-shriek-iso"
kind = "definition"
title = "Restriction of scalars commutes with $j_!$"
order = 2831
uses = ["det-def-sfb-coefficient-change", "det-def-sfb-module-lower-shriek", "det-def-sfb-change-of-scalars"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.comapOpenImmersionLowerShriekIso"]
+++
Let $a\colon\Lambda\to\Lambda'$ be a morphism of commutative condensed rings
([det-def-sfb-coefficient-change]) and $j\colon U\to X$ an open immersion. With $j_!$ the
extension by zero of module objects ([det-def-sfb-module-lower-shriek]) there is a natural
isomorphism

$$
\operatorname{Res}_{a_X}\circ j_!\;\cong\;j_!\circ\operatorname{Res}_{a_U}\colon
\Mod_{\Lambda'_U}\longrightarrow\Mod_{\Lambda_X}.
$$
