+++
id = "sk-def-sfb-pullback-from-point"
kind = "definition"
title = "Pulling back from the point"
order = 1478
uses = ["def-weil-pbc-proetale-site", "sk-def-sfb-condensed-ring", "sk-def-sfb-finite-pushforward-pullback", "sk-def-sfb-sheaf-tensor", "sec-nagata-compactification", "sec-picard-framework"]
lean = ["AlgebraicGeometry.ProEtale.weaklyEtale_toSpecZ_profiniteToScheme", "AlgebraicGeometry.ProEtale.profiniteToProEt", "AlgebraicGeometry.ProEtale.preservesFiniteLimits_profiniteToProEt", "AlgebraicGeometry.ProEtale.coverPreserving_profiniteToProEt", "AlgebraicGeometry.ProEtale.isContinuous_profiniteToProEt", "AlgebraicGeometry.ProEtale.profiniteToProEtOf", "AlgebraicGeometry.ProEtale.pointLowerStar", "AlgebraicGeometry.ProEtale.hasLeftKanExtension_op_profiniteToProEt", "AlgebraicGeometry.ProEtale.pointUpperStar", "AlgebraicGeometry.ProEtale.pointUpperStarLowerStarAdjunction", "AlgebraicGeometry.ProEtale.isIso_η_pointUpperStar", "AlgebraicGeometry.ProEtale.isIso_δ_pointUpperStar", "AlgebraicGeometry.ProEtale.laxBraided_pointUpperStar", "AlgebraicGeometry.ProEtale.upperStarFromPoint", "AlgebraicGeometry.ProEtale.isLeftAdjoint_upperStarFromPoint"]
tags = ["sketch"]
+++
Let $*_{\mathrm{proét}}$ be the pro-étale site of a point: profinite sets with
the coherent topology ([sk-def-sfb-condensed-ring]). For a scheme $X$ let
$X_{\mathrm{proét}}$ be its small pro-étale site ([def-weil-pbc-proetale-site]),
and let $\pi_X\colon X\to\Spec\Z$ be the structure morphism. Since $\Spec\Z$ is
terminal, $\pi_Y\circ f=\pi_X$ for every morphism $f\colon X\to Y$.

1. **Profinite sets as pro-étale schemes.** For a profinite set $S$, let
   $LC(S,\Z)$ be the ring of locally constant functions $S\to\Z$. If $S_i$ runs
   over the finite quotients of $S$, then
   $$
   \Spec LC(S,\Z)=\lim_i\coprod_{S_i}\Spec\Z .
   $$
   The morphism $\Spec LC(S,\Z)\to\Spec\Z$ is weakly étale. Precomposition
   makes $S\mapsto\Spec LC(S,\Z)$ a functor
   $$
   u\colon *_{\mathrm{proét}}\longrightarrow(\Spec\Z)_{\mathrm{proét}} .
   $$
   It preserves finite limits, it sends finite jointly surjective families to
   pro-étale coverings, and it is continuous.

2. **Test objects.** For a scheme $X$ and a profinite set $S$, put
   $$
   X[S]:=\Spec LC(S,\Z)\times_{\Spec\Z}X=\lim_i\coprod_{S_i}X .
   $$
   The functor $u_X\colon *_{\mathrm{proét}}\to X_{\mathrm{proét}}$,
   $S\mapsto X[S]$, is $u$ followed by base change along $\pi_X$.

3. **Inverse image from the point.** Let
   $p_*\colon\Sh((\Spec\Z)_{\mathrm{proét}},\Ab)\to\Sh(*_{\mathrm{proét}},\Ab)$,
   $(p_*G)(S)=G(\Spec LC(S,\Z))$, be restriction along $u$. Define
   $$
   p^*:=\mathrm{sheafify}\circ\operatorname{Lan}_{u^{\mathrm{op}}}\colon
   \Sh(*_{\mathrm{proét}},\Ab)\longrightarrow\Sh((\Spec\Z)_{\mathrm{proét}},\Ab).
   $$
   Then $p^*$ is left adjoint to $p_*$. For the tensor products of
   [sk-def-sfb-sheaf-tensor], $p^*$ is strong monoidal and braided.

4. **Inverse image to $X$.** Define
   $$
   p_X^*:=\pi_X^*\circ p^*\colon
   \Sh(*_{\mathrm{proét}},\Ab)\longrightarrow\Sh(X_{\mathrm{proét}},\Ab),
   $$
   where $\pi_X^*$ is the pullback of [sk-def-sfb-finite-pushforward-pullback]
   for $\mathcal A=\Ab$. It is strong monoidal and braided. It is a left
   adjoint, with right adjoint $G\mapsto\bigl(S\mapsto G(X[S])\bigr)$; so
   $p_X^*$ is the inverse image along $u_X$.
