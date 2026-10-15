+++
id = "sk-def-sfb-coefficient-morphisms"
kind = "definition"
title = "The canonical coefficient morphisms $\\alpha_f$, $\\eta_f$"
order = 1615
uses = ["sk-def-sfb-pullback-from-point-comp", "sk-def-sfb-pulled-back-coefficients"]
lean = ["AlgebraicGeometry.ProEtale.condensedPullbackHom", "AlgebraicGeometry.ProEtale.isMonHom_condensedPullbackHom", "AlgebraicGeometry.ProEtale.coefficientPullbackIso", "AlgebraicGeometry.ProEtale.condensedPushforwardHom", "AlgebraicGeometry.ProEtale.isMonHom_condensedPushforwardHom"]
tags = ["sketch"]
+++
Let $\Lambda$ be a condensed ring, let $f\colon X\to Y$ be a morphism of
schemes, and let $\Lambda_X$, $\Lambda_Y$ be the pulled-back coefficient rings
of [sk-def-sfb-pulled-back-coefficients]. The pullback
$f^*\Lambda_Y$ and the pushforward $f_*\Lambda_X$ are ring objects: $f^*$ is
strong monoidal and $f_*$ is lax monoidal
([sk-def-sfb-finite-pushforward-pullback]). Define
$$
\alpha_f\colon f^*\Lambda_Y\longrightarrow\Lambda_X,\qquad
\eta_f\colon\Lambda_Y\longrightarrow f_*\Lambda_X
$$
as follows.

- $\alpha_f$ is the component at $\Lambda$ of the natural isomorphism
  $f^*\circ p_Y^*\cong p_X^*$ of [sk-def-sfb-pullback-from-point-comp].
- $\eta_f$ is the mate of $\alpha_f$ under the adjunction $f^*\dashv f_*$: the
  unit $\Lambda_Y\to f_*f^*\Lambda_Y$ followed by $f_*\alpha_f$.

Both are morphisms of ring objects. Moreover, $\alpha_f$ underlies an
isomorphism of ring objects $f^*\Lambda_Y\cong\Lambda_X$.
