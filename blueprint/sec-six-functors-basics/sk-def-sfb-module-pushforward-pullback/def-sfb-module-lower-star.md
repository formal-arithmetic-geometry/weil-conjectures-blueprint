+++
id = "def-sfb-module-lower-star"
kind = "definition"
title = "Pushforward of module objects"
order = 1682
uses = ["sk-def-sfb-finite-pushforward-pullback", "sk-def-sfb-pulled-back-coefficients", "sk-def-sfb-coefficient-morphisms", "sk-def-sfb-module-objects", "sk-def-sfb-change-of-scalars", "sk-def-sfb-transport"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.lowerStar"]
+++
Let $\Lambda$ be a commutative condensed ring and $f\colon X\to Y$ a morphism of
schemes, with coefficient rings $\Lambda_X=p_X^*\Lambda$
([sk-def-sfb-pulled-back-coefficients]) and categories of module objects
$\Mod_{\Lambda_X}$ ([sk-def-sfb-module-objects]). The *pushforward of module objects* is

$$
f_*:=\operatorname{Res}_{\eta_f}\circ\operatorname{mapMod}(f^{\Ab}_*)\colon
\Mod_{\Lambda_X}\to\Mod_{\Lambda_Y},
$$

where the transport ([sk-def-sfb-transport]) $\operatorname{mapMod}(f^{\Ab}_*)$ makes $f^{\Ab}_*M$ an
$f^{\Ab}_*\Lambda_X$-module through the lax monoidal structure of the pushforward
$f^{\Ab}_*$ of abelian sheaves, and $\operatorname{Res}_{\eta_f}$ restricts scalars
along $\eta_f\colon\Lambda_Y\to f^{\Ab}_*\Lambda_X$ ([sk-def-sfb-coefficient-morphisms]). Thus the underlying sheaf of $f_*M$ is
$f^{\Ab}_*M$, and $\Lambda_Y$ acts by

$$
\Lambda_Y\otimes f^{\Ab}_*M\xrightarrow{\eta_f\otimes1}
f^{\Ab}_*\Lambda_X\otimes f^{\Ab}_*M\xrightarrow{\mu}
f^{\Ab}_*(\Lambda_X\otimes M)\to f^{\Ab}_*M .
$$

The functor $f_*$ is additive and left exact.
