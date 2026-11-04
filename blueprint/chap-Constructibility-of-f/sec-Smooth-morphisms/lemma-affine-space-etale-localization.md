+++
id = "lemma-affine-space-etale-localization"
kind = "lemma"
title = "Affine space and étale localization"
order = 551
lean = ["AlgebraicGeometry.Etale.affineSpaceAdjunction_baseChange", "AlgebraicGeometry.Etale.nonempty_rightDerivedLowerShriek_adjunction_affineSpace", "AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_comp_leftDerivedUpperStar_of_etale"]
+++
Let $S$ be of finite type over the base field $k$.

1. For the projection $p_d:\mathbf A^d_S\to S$, the right adjoint
   $p_d^!$ of $Rp_{d!}:D_{\mathrm{class}}((\mathbf A^d_S)_{\mathrm{pro}\acute{e}t},\Lambda)
\to D_{\mathrm{class}}(S_{\mathrm{pro}\acute{e}t},\Lambda)$ is $p_d^*(d)[2d]$. Its counit
   $Rp_{d!}p_d^*N(d)[2d]\to N$ is compatible with base change: for a morphism
   $g:S'\to S$ of finite type over $k$, with base change
   $p'_d:\mathbf A^d_{S'}\to S'$, the pullback $g^*$ of the counit for $N$ is,
   under the base change isomorphism for $Rp_{d!}$, the counit for $g^*N$.
   The same holds for the unit, which is determined by the counit through
   the triangle identities.
2. Let $f:X\to S$ be separated of finite type, let
   $N\in D_{\mathrm{class}}(S_{\mathrm{pro}\acute{e}t},\Lambda)$, and let $u:U\to X$ be separated, étale
   and of finite type. There is a canonical isomorphism
   $$
   u^*f^!N\simeq(fu)^!N
   \tag{6.10}
   $$
   under which the counit of $R(fu)_!\dashv(fu)^!$ is the composite
   $$
   R(fu)_!u^*f^!N\simeq Rf_!u_!u^*f^!N\longrightarrow Rf_!f^!N
   \longrightarrow N
   $$
   of the composition isomorphism, the counit of $u_!\dashv u^*$ and the
   counit of $Rf_!\dashv f^!$. For a second separated étale morphism
   $u':U'\to U$ of finite type, the isomorphism (6.10) for $uu'$ is
   the composite of $u'^*$ of (6.10) for $u$ and
   (6.10) for $u'$ and $fu$.
