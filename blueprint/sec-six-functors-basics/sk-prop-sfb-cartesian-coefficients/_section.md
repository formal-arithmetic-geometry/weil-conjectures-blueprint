+++
id = "sk-prop-sfb-cartesian-coefficients"
kind = "proposition"
title = "Cartesian coefficient system"
order = 1509
uses = ["sk-def-sfb-coefficient-morphisms"]
lean = ["AlgebraicGeometry.ProEtale.isIso_condensedPullbackHom", "AlgebraicGeometry.ProEtale.condensedPushforwardHom_id", "AlgebraicGeometry.ProEtale.condensedPushforwardHom_comp"]
tags = ["sketch"]
+++
Let $\Lambda$ be a condensed ring, and let $\alpha_f$ and $\eta_f$ be the
coefficient morphisms of [sk-def-sfb-coefficient-morphisms].

1. For every morphism of schemes $f\colon X\to Y$,
   $\alpha_f\colon f^*\Lambda_Y\to\Lambda_X$ is an isomorphism.
2. $\eta$ is compatible with identities. For every scheme $X$,
   $\eta_{\mathrm{id}_X}\colon\Lambda_X\to(\mathrm{id}_X)_*\Lambda_X$ is the
   inverse of the identity isomorphism
   $(\mathrm{id}_X)_*\cong\mathrm{id}$ of
   [sk-def-sfb-finite-pushforward-pullback] at $\Lambda_X$.
3. $\eta$ is compatible with composition. For $f\colon X\to Y$ and
   $g\colon Y\to Z$,
   $$
   \eta_{g\circ f}=c_{f,g}\circ g_*(\eta_f)\circ\eta_g\colon
   \Lambda_Z\to g_*\Lambda_Y\to g_*f_*\Lambda_X\to(g\circ f)_*\Lambda_X ,
   $$
   where $c_{f,g}\colon g_*f_*\cong(g\circ f)_*$ is the composition
   isomorphism of [sk-def-sfb-finite-pushforward-pullback], taken at
   $\Lambda_X$.
