+++
id = "def-sfb-finite-lower-star-lax-monoidal"
kind = "definition"
title = "$g_*$ is lax symmetric monoidal"
order = 1511
uses = ["def-sfb-finite-lower-star", "sk-def-sfb-sheaf-tensor"]
lean = ["AlgebraicGeometry.ProEtale.laxMonoidal_lowerStar", "AlgebraicGeometry.ProEtale.laxBraided_lowerStar"]
+++
Let $\mathcal A$ be moreover symmetric monoidal such that $\Sh(Y_{\mathrm{proét}},\mathcal A)$
and $\Sh(Z_{\mathrm{proét}},\mathcal A)$ carry the tensor product of
[sk-def-sfb-sheaf-tensor] (for instance $\mathcal A$ closed). For $g\colon Z\to Y$, the
pushforward $g_*$ of [def-sfb-finite-lower-star] is lax symmetric monoidal, with
structure maps

$$
\mathbf 1\to g_*\mathbf 1,\qquad g_*F\otimes g_*G\to g_*(F\otimes G)
$$

compatible with the symmetries.
