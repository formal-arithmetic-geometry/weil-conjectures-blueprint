+++
id = "def-sfb-module-upper-lower-adjunction"
kind = "definition"
title = "The adjunction $f^*\\dashv f_*$ on module objects"
order = 1199
uses = ["def-sfb-module-lower-star", "def-sfb-module-upper-star", "def-sfb-finite-upper-lower-star-adjunction", "lem-sfb-finite-monoidal-adjunction", "det-def-sfb-coefficient-morphisms", "det-def-sfb-change-of-scalars", "det-def-sfb-transport"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.upperStarLowerStarAdjunction"]
+++
Let $\Lambda$ be a commutative condensed ring and $f\colon X\to Y$ a morphism of
schemes, and let $u\colon\Lambda_Y\to f^{\Ab}_*f^*_{\Ab}\Lambda_Y$ be the unit of
$f^*_{\Ab}\dashv f^{\Ab}_*$. The pullback $f^*$ of [def-sfb-module-upper-star] is left
adjoint to the pushforward $f_*$ of [def-sfb-module-lower-star], by the adjunction
obtained by composing

- the lift $\operatorname{mapMod}(f^*_{\Ab})\dashv
  \operatorname{Res}_u\circ\operatorname{mapMod}(f^{\Ab}_*)$ of the monoidal adjunction
  $f^*_{\Ab}\dashv f^{\Ab}_*$ to module objects ([det-def-sfb-transport]), and
- the adjunction $\operatorname{Ext}_{\alpha_f}\dashv\operatorname{Res}_{\alpha_f}$
  ([det-def-sfb-change-of-scalars]),

and transporting the right adjoint along the isomorphism

$$
\operatorname{Res}_u\circ\operatorname{mapMod}(f^{\Ab}_*)\circ\operatorname{Res}_{\alpha_f}
\cong f_* .
$$

Concretely, a $\Lambda_X$-linear map $\Lambda_X\otimes_{f^*\Lambda_Y}f^*_{\Ab}M\to N$
is the same as an $f^*\Lambda_Y$-linear map $f^*_{\Ab}M\to N$, which is the same as a
$\Lambda_Y$-linear map $M\to f_*N$.
