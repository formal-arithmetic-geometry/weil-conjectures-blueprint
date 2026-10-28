+++
id = "def-sfb-finite-lower-star-lax-monoidal"
kind = "definition"
title = "$g_*$ is lax braided monoidal"
order = 918
uses = ["def-sfb-finite-lower-star", "lem-weil-pbc-sheaf-tensor-closed"]
lean = ["AlgebraicGeometry.ProEtale.laxMonoidal_lowerStar", "AlgebraicGeometry.ProEtale.laxBraided_lowerStar"]
+++
Let $\mathcal A$ be moreover braided monoidal such that $\Sh(Y_{\mathrm{proét}},\mathcal A)$
and $\Sh(Z_{\mathrm{proét}},\mathcal A)$ carry the tensor product of
[lem-weil-pbc-sheaf-tensor-closed], i.e. the morphisms of presheaves inverted by sheafification are
stable under tensoring (for instance $\mathcal A$ closed). For $g\colon Z\to Y$, the
pushforward $g_*$ of [def-sfb-finite-lower-star] is lax braided monoidal, with structure maps

$$
\mathbf 1\to g_*\mathbf 1,\qquad g_*F\otimes g_*G\to g_*(F\otimes G)
$$

compatible with the braidings. When $\mathcal A$ is symmetric, $g_*$ is lax symmetric
monoidal.
