+++
id = "theorem-verdier-biduality"
kind = "theorem"
title = "Verdier biduality"
order = 844
lean = ["AlgebraicGeometry.Etale.isIso_verdierDualDoubleDual_app", "AlgebraicGeometry.Etale.verdierDualEquivalence", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_verdierBiduality", "AlgebraicGeometry.ProEtale.CondensedRing.PadicIntegersRingObj.isIso_verdierBiduality"]
uses = ["definition-constructible-sheaves", "definition-relative-dualizing-complex", "definition-verdier-dual-evaluation", "definition-compactification-refinement"]
+++
For every admissible coefficient ring $\Lambda$ and every scheme $X$,

$$
\delta_K:K\xrightarrow{\sim}\mathbb D_X\mathbb D_XK
\qquad(K\in D^b_{\mathrm{ctf}}(X,\Lambda)).
$$

Thus $\mathbb D_X$ is an exact anti-equivalence of
$D^b_{\mathrm{ctf}}(X,\Lambda)$ with itself.
