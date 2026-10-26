+++
id = "def-sfb-coefficient-map"
kind = "definition"
title = "The coefficient change $a_X$"
order = 1229
uses = ["det-def-sfb-condensed-ring", "det-def-sfb-pullback-from-point", "det-def-sfb-pulled-back-coefficients"]
lean = ["AlgebraicGeometry.ProEtale.coefficientMap"]
+++
Let $a\colon\Lambda\to\Lambda'$ be a morphism of condensed rings, i.e. a morphism of ring
objects of condensed abelian groups ([det-def-sfb-condensed-ring]), and let $X$ be a scheme. The
*coefficient change* on $X$ is

$$
a_X:=p_X^*a\colon\Lambda_X=p_X^*\Lambda\longrightarrow\Lambda'_X=p_X^*\Lambda',
$$

the image of $a$ under the inverse image $p_X^*$ of [det-def-sfb-pullback-from-point]. It is a
morphism of ring objects of $\Sh(X_{\mathrm{proét}},\Ab)$ between the coefficient rings of
[det-def-sfb-pulled-back-coefficients].
