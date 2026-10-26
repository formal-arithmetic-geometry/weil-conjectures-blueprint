+++
id = "def-sfb-derived-open-immersion-shriek-iso"
kind = "definition"
title = "Extension by zero commutes with $T$"
order = 2600
uses = ["sk-def-sfb-coefficient-change", "sk-def-sfb-module-lower-shriek", "sk-prop-sfb-module-derived-factorization", "det-def-sfb-derived-extension-of-scalars", "def-sfb-conjugate-pull-iso", "def-sfb-derived-comap-upper-star-iso"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.derivedOpenImmersionShriekIso"]
+++
Let $a\colon\Lambda\to\Lambda'$ be a morphism of commutative condensed rings, with derived
extensions of scalars $T^X$ ([sk-def-sfb-coefficient-change]), and $j\colon U\to X$ an open
immersion. The natural isomorphism

$$
T^X\circ D(j_!)\;\cong\;D(j_!)\circ T^U\colon D(\Mod_{\Lambda_U})\longrightarrow
D(\Mod_{\Lambda'_X})
$$

on the unbounded derived categories, with $D(j_!)$ the levelwise extension by zero
([sk-def-sfb-module-lower-shriek]), is the conjugate ([def-sfb-conjugate-pull-iso]) of the
isomorphism $D(\operatorname{Res}_{a_U})\circ D(j^*)\cong D(j^*)\circ D(\operatorname{Res}_{a_X})$
of [def-sfb-derived-comap-upper-star-iso] along the adjunctions $D(j_!)\dashv D(j^*)$
([sk-prop-sfb-module-derived-factorization]) and $T\dashv D(\operatorname{Res})$
([det-def-sfb-derived-extension-of-scalars]). No flatness of $a$ is needed.
