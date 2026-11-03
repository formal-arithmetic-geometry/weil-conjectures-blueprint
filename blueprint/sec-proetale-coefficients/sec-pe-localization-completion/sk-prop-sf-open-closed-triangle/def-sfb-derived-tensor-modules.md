+++
id = "def-sfb-derived-tensor-modules"
kind = "definition"
title = "Derived tensor product of module objects"
order = 1189
uses = ["lem-sfb-derived-monoidal", "det-prop-sfb-module-category", "det-def-sfb-pulled-back-coefficients", "det-def-sfb-condensed-ring"]
lean = ["CategoryTheory.Mod.derivedMonoidalCategory", "AlgebraicGeometry.ProEtale.CondensedRing.derivedTensor"]
+++
Let $\mathcal C$ be a closed symmetric monoidal Grothendieck abelian category whose tensor
product is additive and which has functorial flat resolutions, and let $R$ be a
commutative ring object of $\mathcal C$. The derived category $D(\Mod_R(\mathcal C))$ is
monoidal for the *derived tensor product* $K\otimes^{\mathrm L}_RL$. This is the monoidal
structure of [lem-sfb-derived-monoidal] for the relative tensor product $\otimes_R$ of
module objects. In particular, for a commutative condensed ring $\Lambda$ and a scheme
$X$, with $\Lambda_X=p_X^*\Lambda$, it is the functor
$$
-\otimes^{\mathrm L}_{\Lambda_X}-\colon D(\Mod_{\Lambda_X})\times D(\Mod_{\Lambda_X})\to D(\Mod_{\Lambda_X}).
$$
