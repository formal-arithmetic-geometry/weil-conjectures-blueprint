+++
id = "def-sfb-open-immersion-shriek-iso"
kind = "definition"
title = "Extension of scalars commutes with $j_!$"
order = 2599
uses = ["sk-def-sfb-coefficient-change", "sk-def-sfb-module-lower-shriek", "det-def-sfb-change-of-scalars", "def-sfb-conjugate-pull-iso", "def-sfb-comap-upper-star-iso"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.openImmersionShriekIso"]
+++
Let $a\colon\Lambda\to\Lambda'$ be a morphism of commutative condensed rings
([sk-def-sfb-coefficient-change]) and $j\colon U\to X$ an open immersion. The natural isomorphism

$$
\operatorname{Ext}_{a_X}\circ j_!\;\cong\;j_!\circ\operatorname{Ext}_{a_U}\colon
\Mod_{\Lambda_U}\longrightarrow\Mod_{\Lambda'_X}
$$

is the conjugate, in the sense of [def-sfb-conjugate-pull-iso], of the isomorphism
$\operatorname{Res}_{a_U}\circ j^*\cong j^*\circ\operatorname{Res}_{a_X}$ of
[def-sfb-comap-upper-star-iso] along the adjunctions $j_!\dashv j^*$
([sk-def-sfb-module-lower-shriek]) and $\operatorname{Ext}\dashv\operatorname{Res}$
([det-def-sfb-change-of-scalars]).
