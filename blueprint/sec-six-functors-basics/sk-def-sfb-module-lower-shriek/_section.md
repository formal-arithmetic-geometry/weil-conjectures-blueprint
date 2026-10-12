+++
id = "sk-def-sfb-module-lower-shriek"
kind = "definition"
title = "Extension by zero and lower shriek of module objects"
order = 1676
uses = ["sk-def-sfb-finite-lower-shriek", "sk-def-sfb-module-pushforward-pullback", "sk-def-nagata-sketch-data"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.hasProjectionFormula_openImmersion", "AlgebraicGeometry.ProEtale.CondensedRing.linearOpenImmersionLowerShriek", "AlgebraicGeometry.ProEtale.CondensedRing.linearOpenImmersionLowerShriekAdjunction", "AlgebraicGeometry.ProEtale.CondensedRing.openImmersionLowerShriek", "AlgebraicGeometry.ProEtale.CondensedRing.preservesHomology_openImmersionLowerShriek", "AlgebraicGeometry.ProEtale.CondensedRing.openImmersionLowerShriekUpperStarAdjunction", "AlgebraicGeometry.ProEtale.CondensedRing.compactificationLowerShriek", "AlgebraicGeometry.ProEtale.CondensedRing.lowerShriek", "AlgebraicGeometry.ProEtale.CondensedRing.preservesFiniteLimits_lowerShriek"]
tags = ["sketch"]
+++
Let $\Lambda$ be a commutative condensed ring, with module objects
$\Mod_{\Lambda_X}$ over $\Lambda_X=p_X^*\Lambda$ ([sk-def-sfb-pulled-back-coefficients],
[sk-def-sfb-module-objects]), and write $j^{\Ab}_!\dashv j^*_{\Ab}$
for the extension by zero and the pullback of abelian sheaves along an open immersion
$j\colon U\to X$ ([sk-def-sfb-finite-lower-shriek],
[sk-def-sfb-finite-pushforward-pullback] with $\mathcal A=\Ab$).

- *Projection formula.* For $L\in\Sh(X_{\mathrm{proét}},\Ab)$ and
  $M\in\Sh(U_{\mathrm{proét}},\Ab)$ the canonical map
  $j^{\Ab}_!(j^*_{\Ab}L\otimes M)\to L\otimes j^{\Ab}_!M$ is an isomorphism
  (tensor product of [sk-def-sfb-sheaf-tensor]).
- *Linear extension by zero.* By the projection formula, $j^{\Ab}_!$ linearizes
  ([sk-def-sfb-transport]) to a functor
  $j^{\mathrm{lin}}_!\colon\Mod_{j^*\Lambda_X}\to\Mod_{\Lambda_X}$, sending $M$ to
  $j^{\Ab}_!M$ with the action
  $\Lambda_X\otimes j^{\Ab}_!M\cong j^{\Ab}_!(j^*\Lambda_X\otimes M)\to j^{\Ab}_!M$;
  it is left adjoint to $\operatorname{mapMod}(j^*_{\Ab})$.
- *Extension by zero.* The extension by zero of module objects is
  $$
  j_!:=j^{\mathrm{lin}}_!\circ\operatorname{Res}_{\alpha_j}\colon
  \Mod_{\Lambda_U}\to\Mod_{\Lambda_X}
  $$
  ([sk-def-sfb-change-of-scalars], [sk-def-sfb-coefficient-morphisms]). The underlying
  sheaf of $j_!M$ is $j^{\Ab}_!M$; $j_!$ is exact, and $j_!\dashv j^*$ with $j^*$ the
  pullback of module objects ([sk-def-sfb-module-pushforward-pullback]).
- *Lower shriek.* For a compactification $c=(X\xrightarrow{i}\bar X\xrightarrow{g}Y)$
  of a morphism $f\colon X\to Y$, i.e. $f=g\circ i$ with $i$ an open immersion and $g$
  proper ([sk-def-nagata-sketch-data]),
  $$
  f^c_!:=g_*\circ i_!\colon\Mod_{\Lambda_X}\to\Mod_{\Lambda_Y},
  $$
  and for $f$ admitting a compactification, $f_!:=f^c_!$ for a chosen compactification
  $c$ of $f$. The underlying sheaf of $f_!M$ is the lower shriek of abelian sheaves
  of $M$ for the same compactification, and $f_!$ is left exact.
