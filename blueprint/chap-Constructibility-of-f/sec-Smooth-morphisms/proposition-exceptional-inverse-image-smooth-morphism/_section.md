+++
id = "proposition-exceptional-inverse-image-smooth-morphism"
kind = "proposition"
title = "The exceptional inverse image of a smooth morphism"
order = 561
lean = ["AlgebraicGeometry.Etale.exists_dualizingComplex_iso_and_tensor", "AlgebraicGeometry.Etale.isIso_rightDerivedUpperShriekBaseChangeMap_of_smoothOfRelativeDimension", "CategoryTheory.Adjunction.projectionTensorMap_mateEquiv"]
uses = ["definition-relative-dualizing-complex", "definition-exceptional-base-change-map", "theorem-existence-exceptional-inverse-image", "lemma-affine-space-etale-localization"]
+++
Let $f:X\to S$ be separated, smooth and of finite type, of pure relative
dimension $d$, and let
$\omega_f=f^!A_S\in D(X_{\acute{e}t},A)$ be its
dualizing complex. Let $N\in D(S_{\acute{e}t},A)$.

1. On an open $U\subset X$ with $f|_U=p_d\circ e$, where
   $e:U\to\mathbf A^d_S$ is separated and étale, we have
   $(f^!N)|_U\simeq e^*p_d^*N(d)[2d]$, with counit the sum over the fibres of
   $e$ followed by the counit of Lemma [lemma-affine-space-etale-localization](1). In
   particular $\omega_f|_U\simeq A_U(d)[2d]$, and $\omega_f[-2d]$ is a
   locally constant sheaf of free $A$-modules of rank one.
2. The canonical map
   $$
   \mu_N:f^*N\otimes_A^{\mathbf L}\omega_f\longrightarrow f^!N
   \tag{6.11}
   $$
   is an isomorphism.
3. Let $g:S'\to S$ be a morphism, let $X'=X\times_SS'$, and let
   $f':X'\to S'$, $g':X'\to X$ be the projections. Then the canonical
   base change map
   $$
   \beta_N:g'^*f^!N\longrightarrow f'^!g^*N
   \tag{6.12}
   $$
   is an isomorphism. It identifies $g'^*\omega_f$ with $\omega_{f'}$ and is
   compatible with $\mu_N$.
