+++
id = "sk-def-sfb-constructible"
kind = "definition"
title = "Locally finitely presented and constructible modules"
order = 1582
uses = ["def-weil-pbc-proetale-site", "def-constructible-stratification", "sk-def-sfb-transport"]
lean = ["CategoryTheory.Mod.IsFinitelyPresented", "AlgebraicGeometry.ProEtale.IsLocallyFinitelyPresented", "AlgebraicGeometry.ProEtale.IsConstructible"]
tags = ["sketch"]
+++
Let $\mathcal A$ be a closed symmetric monoidal Grothendieck abelian category whose tensor
product is additive, let $X$ be a scheme, and let $\mathcal R$ be a ring object of
$\Sh(X_{\mathrm{proét}},\mathcal A)$ [sk-def-sfb-ring-object], [sk-def-sfb-sheaf-tensor].
For a morphism of schemes $g\colon Z\to X$, the pullback $g^*$
[sk-def-sfb-finite-pushforward-pullback] is monoidal. So it sends $\mathcal R$ to a ring
object $g^*\mathcal R$ and $\mathcal R$-modules [sk-def-sfb-module-objects] to
$g^*\mathcal R$-modules: the *restriction* of an $\mathcal R$-module $M$ along $g$ is the
$g^*\mathcal R$-module $M|_Z=\operatorname{mapMod}(g^*)(M)$ [sk-def-sfb-transport]. Let $M$
be an $\mathcal R$-module.

- $M$ is *locally finitely presented* if there is a pro-étale cover $\{U_i\to X\}$
  [def-weil-pbc-proetale-site] such that each $M|_{U_i}$ is isomorphic to the cokernel of
  a morphism $(\mathcal R|_{U_i})^m\to(\mathcal R|_{U_i})^n$ of free modules of finite rank
  (torsion is allowed).
- $M$ is *constructible* if there is a stratification $(X_a\to X)_a$ of $X$
  [def-constructible-stratification] such that, for each stratum $g_a\colon X_a\to X$,
  the restriction $M|_{X_a}$ is locally finitely presented over $\mathcal R|_{X_a}$. A
  stratification is a finite partition into locally closed subsets, each the image of an
  immersion $g_a$.
