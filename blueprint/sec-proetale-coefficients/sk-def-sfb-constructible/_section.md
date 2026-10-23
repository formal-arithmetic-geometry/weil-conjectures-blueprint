+++
id = "sk-def-sfb-constructible"
kind = "definition"
title = "Local models and constructible sheaves"
order = 1238
uses = ["def-weil-pbc-proetale-site", "def-constructible-stratification", "sk-prop-sf-open-closed-triangle"]
lean = ["CategoryTheory.Mod.IsFinitelyPresented", "AlgebraicGeometry.ProEtale.IsLocallyFinitelyPresented", "AlgebraicGeometry.ProEtale.IsConstructibleModuleObject"]
tags = ["sketch"]
+++
The definition of a constructible sheaf makes sense for any condensed ring. Recall that for
$g\colon Z\to X$ the restriction $M|_Z=g^*M$ of a $\Lambda_X$-module is a
$\Lambda_Z$-module, since $g^{-1}\Lambda_X\simeq\Lambda_Z$
([det-def-sfb-pulled-back-coefficients], [det-def-sfb-transport]); thus
$g^*\colon\Mod(X_{\mathrm{proét}},\Lambda)\to\Mod(Z_{\mathrm{proét}},\Lambda)$.

Let $\Lambda$ be a commutative condensed ring.

1. A $\Lambda_X$-module $M$ has a *finite constant local model* if there is a pro-étale
   cover $\{U_i\to X\}$ ([def-weil-pbc-proetale-site]) and finitely presented modules $P_i$
   over the scalar ring $\Lambda(*)$ such that
   $$
   M|_{U_i}\simeq\Lambda_{U_i}\otimes_{\Lambda(*)}P_i .
   $$
   Here $\Lambda(*)$ and $P_i$ are constant sheaves on $U_i$, acting through
   $\Lambda(*)\to\Lambda_{U_i}$. Equivalently, on each $U_i$ the module $M$ has a
   presentation by a finite matrix with entries in the scalar ring $\Lambda(*)$.
2. For qcqs $X$, a $\Lambda_X$-module $M$ is *constructible* if there is a finite
   stratification $X=\coprod_aX_a$ by constructible locally closed subschemes
   ([def-constructible-stratification]) such that each $M|_{X_a}$ has a finite constant
   local model. On an arbitrary scheme this condition is imposed locally on affine opens.
   The word constructible requires each stratum to be a constructible subset; for
   Noetherian schemes this is automatic for locally closed strata.

We write $\Cons(X,\Lambda)\subset\Mod(X_{\mathrm{proét}},\Lambda)$ for the full subcategory
of constructible sheaves, and $\Dbc(X,\Lambda)\subset D(X_{\mathrm{proét}},\Lambda)$ for the
full subcategory of bounded complexes with constructible cohomology sheaves (compare
[det-def-sfb-bounded-constructible]). A complex $K$ has *Tor amplitude in $[a,b]$* if
$K\otimes^{\mathbf L}_{\Lambda_X}N$ has cohomology only in $[a,b]$ for every sheaf $N$ of
$\Lambda_X$-modules. We write $\Dctf(X,\Lambda)$ for the full subcategory of
$\Dbc(X,\Lambda)$ of complexes of finite Tor amplitude (compare [sk-def-sf-categories]).
