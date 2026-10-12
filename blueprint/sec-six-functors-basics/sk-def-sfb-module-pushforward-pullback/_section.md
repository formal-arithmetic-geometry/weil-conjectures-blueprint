+++
id = "sk-def-sfb-module-pushforward-pullback"
kind = "definition"
title = "Pushforward and pullback of module objects"
order = 1630
uses = ["sk-def-sfb-finite-pushforward-pullback", "sk-def-sfb-condensed-ring", "sk-def-sfb-pulled-back-coefficients", "sk-def-sfb-coefficient-morphisms", "sk-def-sfb-module-objects", "sk-def-sfb-change-of-scalars", "sk-def-sfb-transport"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.lowerStar", "AlgebraicGeometry.ProEtale.CondensedRing.preservesFiniteLimits_lowerStar", "AlgebraicGeometry.ProEtale.CondensedRing.upperStar", "AlgebraicGeometry.ProEtale.CondensedRing.upperStarLowerStarAdjunction", "AlgebraicGeometry.ProEtale.isMonoidal_lowerStarComp", "AlgebraicGeometry.ProEtale.CondensedRing.lowerStarComp", "AlgebraicGeometry.ProEtale.CondensedRing.upperStarComp"]
tags = ["sketch"]
+++
Let $\Lambda$ be a commutative condensed ring ([sk-def-sfb-condensed-ring]),
with pulled-back coefficient rings $\Lambda_X=p_X^*\Lambda$
([sk-def-sfb-pulled-back-coefficients]), categories of module objects
$\Mod_{\Lambda_X}$ ([sk-def-sfb-module-objects]) and coefficient morphisms
$\alpha_f\colon f^*\Lambda_Y\to\Lambda_X$, $\eta_f\colon\Lambda_Y\to f^{\Ab}_*\Lambda_X$
([sk-def-sfb-coefficient-morphisms]) for morphisms of schemes $f\colon X\to Y$.
Everything below is stated for a general
$\Lambda$; the $\ell$-adic rings, including $\underline{\Qlb}$, are instances.
Write $f^{\Ab}_*$ and $f^*_{\Ab}$ for the pushforward and pullback of sheaves of
abelian groups ([sk-def-sfb-finite-pushforward-pullback] with $\mathcal A=\Ab$);
$f^{\Ab}_*$ is lax monoidal and $f^*_{\Ab}$ is strong monoidal, so both transport
module objects ([sk-def-sfb-transport]); applied to ring objects such as
$\Lambda_Y$, the symbols $f^*$ and $f_*$ always mean these functors of abelian
sheaves. Every functor on module objects is "transport
the $\Ab$-valued functor, then change scalars along $\eta_f$ or $\alpha_f$"
([sk-def-sfb-change-of-scalars]). For a morphism of schemes $f\colon X\to Y$:

- the *pushforward*
  $$
  f_*:=\operatorname{Res}_{\eta_f}\circ\operatorname{mapMod}(f^{\Ab}_*)\colon
  \Mod_{\Lambda_X}\to\Mod_{\Lambda_Y};
  $$
  the underlying sheaf of $f_*M$ is $f^{\Ab}_*M$, with $\Lambda_Y$ acting through
  $\eta_f$, and $f_*$ is additive and left exact;
- the *pullback*
  $$
  f^*:=\operatorname{Ext}_{\alpha_f}\circ\operatorname{mapMod}(f^*_{\Ab})\colon
  \Mod_{\Lambda_Y}\to\Mod_{\Lambda_X},
  \qquad f^*M=\Lambda_X\otimes_{f^*\Lambda_Y}f^*_{\Ab}M,
  $$
  the ringed-topos pullback. The extension of scalars along $\alpha_f$ is kept
  although $\alpha_f$ is invertible, so that the definition is the standard one and
  does not depend on a choice of inverse;
- the *adjunction* $f^*\dashv f_*$: the lift of the monoidal adjunction
  $f^*_{\Ab}\dashv f^{\Ab}_*$ to module objects, composed with
  $\operatorname{Ext}_{\alpha_f}\dashv\operatorname{Res}_{\alpha_f}$, using that
  $\eta_f$ is the mate of $\alpha_f$;
- for $g\colon Y\to Z$, the *composition isomorphisms*
  $$
  g_*\circ f_*\cong(g\circ f)_*,\qquad (g\circ f)^*\cong f^*\circ g^*,
  $$
  the first lifting the composition isomorphism of pushforwards of abelian sheaves,
  the second deduced from the first by uniqueness of left adjoints.

The constructions use only $\alpha_f$, $\eta_f$ and the mate relation between
them; that $\alpha_f$ is invertible enters proofs about these functors (exactness,
the adjunction $j_!\dashv j^*$), not their definitions.
