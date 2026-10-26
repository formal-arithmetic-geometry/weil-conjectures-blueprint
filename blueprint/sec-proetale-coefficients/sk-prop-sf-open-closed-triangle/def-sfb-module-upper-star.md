+++
id = "def-sfb-module-upper-star"
kind = "definition"
title = "Pullback of module objects"
order = 1154
uses = ["def-sfb-finite-upper-star", "def-sfb-finite-upper-star-monoidal", "det-def-sfb-pulled-back-coefficients", "det-def-sfb-coefficient-morphisms", "det-def-sfb-module-objects", "det-def-sfb-change-of-scalars", "det-def-sfb-transport"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.upperStar"]
+++
Let $\Lambda$ be a commutative condensed ring and $f\colon X\to Y$ a morphism of
schemes, with coefficient rings $\Lambda_X=p_X^*\Lambda$
([det-def-sfb-pulled-back-coefficients]) and categories of module objects
$\Mod_{\Lambda_X}$ ([det-def-sfb-module-objects]). The *pullback of module objects* is

$$
f^*:=\operatorname{Ext}_{\alpha_f}\circ\operatorname{mapMod}(f^*_{\Ab})\colon
\Mod_{\Lambda_Y}\to\Mod_{\Lambda_X},
$$

where the transport ([det-def-sfb-transport]) $\operatorname{mapMod}(f^*_{\Ab})$ makes $f^*_{\Ab}M$ an
$f^*\Lambda_Y$-module through the strong monoidal structure of the pullback
$f^*_{\Ab}$ of abelian sheaves ([def-sfb-finite-upper-star],
[def-sfb-finite-upper-star-monoidal]), and
$\operatorname{Ext}_{\alpha_f}$ extends scalars ([det-def-sfb-change-of-scalars])
along $\alpha_f\colon f^*\Lambda_Y\to\Lambda_X$ ([det-def-sfb-coefficient-morphisms]). Thus

$$
f^*M=\Lambda_X\otimes_{f^*\Lambda_Y}f^*_{\Ab}M,
$$

the ringed-topos pullback. The functor $f^*$ is additive.
