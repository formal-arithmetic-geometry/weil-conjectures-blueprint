+++
id = "def-sfb-alpha-bundled"
kind = "definition"
title = "$\\alpha_f$ as an isomorphism of ring objects"
order = 1557
uses = ["def-sfb-pullback-from-point-comp-iso", "lem-sfb-pullback-from-point-comp-monoidal", "sk-def-sfb-pulled-back-coefficients"]
lean = ["AlgebraicGeometry.ProEtale.coefficientPullbackIso"]
+++
Let $\Lambda$ be a condensed ring and $f\colon X\to Y$ a morphism of schemes.
The isomorphism of ring objects of $\Sh(X_{\mathrm{proét}},\Ab)$
$$
f^*\Lambda_Y\ \cong\ \Lambda_X
$$
is the composite of two isomorphisms. The first identifies $f^*$ applied to
the ring object $p_Y^*\Lambda$ with the ring object $(f^*\circ p_Y^*)\Lambda$.
The second is the component at $\Lambda$ of the monoidal natural isomorphism
$f^*\circ p_Y^*\cong p_X^*$ ([def-sfb-pullback-from-point-comp-iso]), as an
isomorphism of ring objects. Here $\Lambda_X$ and $\Lambda_Y$ are as in
[sk-def-sfb-pulled-back-coefficients].
