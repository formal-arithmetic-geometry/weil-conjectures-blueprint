+++
id = "def-sfb-coefficient-map"
kind = "definition"
title = "The coefficient change $a_X$"
order = 1704
uses = ["sk-def-sfb-condensed-ring", "sk-def-sfb-pullback-from-point", "sk-def-sfb-pulled-back-coefficients"]
lean = ["AlgebraicGeometry.ProEtale.coefficientMap"]
+++
Let $a\colon\Lambda\to\Lambda'$ be a morphism of condensed rings, i.e. a morphism of ring
objects of condensed abelian groups ([sk-def-sfb-condensed-ring]), and let $X$ be a scheme. The
*coefficient change* on $X$ is

$$
a_X:=p_X^*a\colon\Lambda_X=p_X^*\Lambda\longrightarrow\Lambda'_X=p_X^*\Lambda',
$$

the image of $a$ under the inverse image $p_X^*$ of [sk-def-sfb-pullback-from-point]. It is a
morphism of ring objects of $\Sh(X_{\mathrm{proét}},\Ab)$ between the coefficient rings of
[sk-def-sfb-pulled-back-coefficients].
