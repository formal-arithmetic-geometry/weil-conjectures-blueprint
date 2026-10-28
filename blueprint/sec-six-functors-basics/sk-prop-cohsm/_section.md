+++
id = "sk-prop-cohsm"
kind = "proposition"
title = "The exceptional inverse image of a smooth morphism"
order = 2624
uses = ["sk-prop-sf-existence", "sk-lem-geo-affine-local"]
lean = ["AlgebraicGeometry.Etale.isInvertible_dualizingComplex", "AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_obj_derivedTensor", "AlgebraicGeometry.Etale.nonempty_iso_leftDerivedUpperStar_comp_rightDerivedUpperShriek"]
tags = ["sketch"]
+++
Let $f:X\to S$ be separated, smooth and of finite type, of pure relative
dimension $d$, and let
$\omega_f=f^!\Lambda_S\in D_{\mathrm{class}}(X_{\mathrm{proét}},\Lambda)$ be its
dualizing complex (with $f^!$ the right adjoint of $Rf_!$ of
[sk-prop-sf-existence]). Let $N\in D_{\mathrm{class}}(S_{\mathrm{proét}},\Lambda)$.

1. On an open $U\subset X$ with $f|_U=p_d\circ e$, where
   $e:U\to\mathbf A^d_S$ is separated and étale, we have
   $(f^!N)|_U\simeq e^*p_d^*N(d)[2d]$, with counit the sum over the fibres of
   $e$ followed by the counit of [sk-lem-geo-affine-local](1). In particular
   $\omega_f|_U\simeq\Lambda_U(d)[2d]$, and $\omega_f[-2d]$ is a locally
   constant sheaf of free $\Lambda$-modules of rank one.
2. The canonical map

   $$
   f^*N\otimes_\Lambda^{\mathbf L}\omega_f\longrightarrow f^!N
   \qquad\text{(G11)}
   $$

   is an isomorphism.
3. Let $g:S'\to S$ be a morphism, let $X'=X\times_SS'$, and let
   $f':X'\to S'$, $g':X'\to X$ be the projections. Then the canonical base
   change map

   $$
   g'^*f^!N\longrightarrow f'^!g^*N
   \qquad\text{(G12)}
   $$

   is an isomorphism. It identifies $g'^*\omega_f$ with $\omega_{f'}$ and is
   compatible with (G11).
