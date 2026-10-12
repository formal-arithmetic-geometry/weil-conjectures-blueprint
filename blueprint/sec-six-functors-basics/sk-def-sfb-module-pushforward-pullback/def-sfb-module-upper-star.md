+++
id = "def-sfb-module-upper-star"
kind = "definition"
title = "Pullback of module objects"
order = 1632
uses = ["sk-def-sfb-finite-pushforward-pullback", "sk-def-sfb-pulled-back-coefficients", "sk-def-sfb-coefficient-morphisms", "sk-def-sfb-module-objects", "sk-def-sfb-change-of-scalars", "sk-def-sfb-transport"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.upperStar"]
+++
Let $\Lambda$ be a commutative condensed ring and $f\colon X\to Y$ a morphism of
schemes, with coefficient rings $\Lambda_X=p_X^*\Lambda$
([sk-def-sfb-pulled-back-coefficients]) and categories of module objects
$\Mod_{\Lambda_X}$ ([sk-def-sfb-module-objects]). The *pullback of module objects* is

$$
f^*:=\operatorname{Ext}_{\alpha_f}\circ\operatorname{mapMod}(f^*_{\Ab})\colon
\Mod_{\Lambda_Y}\to\Mod_{\Lambda_X},
$$

where the transport ([sk-def-sfb-transport]) $\operatorname{mapMod}(f^*_{\Ab})$ makes $f^*_{\Ab}M$ an
$f^*\Lambda_Y$-module through the strong monoidal structure of the pullback
$f^*_{\Ab}$ of abelian sheaves ([sk-def-sfb-finite-pushforward-pullback]), and
$\operatorname{Ext}_{\alpha_f}$ extends scalars ([sk-def-sfb-change-of-scalars])
along $\alpha_f\colon f^*\Lambda_Y\to\Lambda_X$ ([sk-def-sfb-coefficient-morphisms]). Thus

$$
f^*M=\Lambda_X\otimes_{f^*\Lambda_Y}f^*_{\Ab}M,
$$

the ringed-topos pullback. The functor $f^*$ is additive.
