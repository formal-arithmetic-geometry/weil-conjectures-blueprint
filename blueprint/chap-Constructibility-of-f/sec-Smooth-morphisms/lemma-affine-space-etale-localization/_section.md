+++
id = "lemma-affine-space-etale-localization"
kind = "lemma"
title = "Affine space and étale localization"
order = 558
lean = ["AlgebraicGeometry.Etale.affineSpaceAdjunction_baseChange", "AlgebraicGeometry.Etale.nonempty_rightDerivedLowerShriek_adjunction_affineSpace", "AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_comp_leftDerivedUpperStar_of_etale"]
uses = ["definition-constructible-sheaves", "definition-underived-base-change-map", "theorem-proper-base-change-classical-pro", "proposition-construction-independence-rf-shriek", "proposition-composition-open-restriction-compactifications-f", "definition-exceptional-base-change-finite", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-finite-direct-images"]
+++
Let $S$ be of finite type over the base field $k$.

1. For the projection $p_d:\mathbf A^d_S\to S$, the right adjoint
   [$p_d^!$](@theorem-existence-exceptional-inverse-image) of $\href{@proposition-construction-independence-rf-shriek}{Rp_{d!}}:D((\mathbf A^d_S)_{\acute{e}t},A)
\to D(S_{\acute{e}t},A)$ is $p_d^*\href{@definition-tate-twists}{(d)}[2d]$. Its counit
   $\href{@proposition-construction-independence-rf-shriek}{Rp_{d!}}p_d^*N\href{@definition-tate-twists}{(d)}[2d]\to N$ is compatible with base change: for a morphism
   $g:S'\to S$ of finite type over $k$, with base change
   $p'_d:\mathbf A^d_{S'}\to S'$, the pullback $g^*$ of the counit for $N$ is,
   under the [base change isomorphism](@proposition-composition-base-change-rf-shriek) for [$Rp_{d!}$](@proposition-construction-independence-rf-shriek), the counit for $g^*N$.
   The same holds for the unit, which is determined by the counit through
   the triangle identities.
2. Let $f:X\to S$ be separated of finite type, let
   $N\in D(S_{\acute{e}t},A)$, and let $u:U\to X$ be separated, étale
   and of finite type. There is a canonical isomorphism
   $$
   u^*\href{@theorem-existence-exceptional-inverse-image}{f^!N}\simeq\href{@theorem-existence-exceptional-inverse-image}{(fu)^!N}
   \tag{6.12}
   $$
   under which the counit of $\href{@proposition-construction-independence-rf-shriek}{R(fu)_!}\dashv\href{@theorem-existence-exceptional-inverse-image}{(fu)^!}$ is the composite
   $$
   \href{@proposition-construction-independence-rf-shriek}{R(fu)_!}u^*\href{@theorem-existence-exceptional-inverse-image}{f^!N}\simeq \href{@proposition-construction-independence-rf-shriek}{Rf_!}u_!u^*\href{@theorem-existence-exceptional-inverse-image}{f^!N}\longrightarrow \href{@proposition-construction-independence-rf-shriek}{Rf_!}\href{@theorem-existence-exceptional-inverse-image}{f^!N}
   \longrightarrow N
   $$
   of the [composition isomorphism](@proposition-composition-base-change-rf-shriek), the counit of $u_!\dashv u^*$ and the
   counit of $\href{@proposition-construction-independence-rf-shriek}{Rf_!}\dashv \href{@theorem-existence-exceptional-inverse-image}{f^!}$. For a second separated étale morphism
   $u':U'\to U$ of finite type, the isomorphism (6.12) for $uu'$ is
   the composite of $u'^*$ of (6.12) for $u$ and
   (6.12) for $u'$ and $fu$.
