+++
id = "proposition-base-change-fourier-inversion"
kind = "proposition"
title = "Base change and stalks"
order = 1232
lean = ["AlgebraicGeometry.nonempty_iso_fourierTransform_comp_upperStar", "AlgebraicGeometry.nonempty_iso_tensorLisse_upperStar_comp_fourierTransform", "AlgebraicGeometry.nonempty_iso_fourierTransform_comp_upperStar_rationalPointHom", "AlgebraicGeometry.nonempty_equiv_stalk_homologySheaf_fourierTransform_rationalPoint"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-sp-unique-adjoint", "lemma-artin-schreier-character-sheaf", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
Let $g:S'\to S$ be a morphism of schemes with $S'$ of finite type over
$k_0$ or over $k$, let $V'=V\times_SS'$, and
let $g_V:V'\to V$ and $g_{V^\vee}:V'^\vee\to V^\vee$ be the projections.

1. The proper base change isomorphism for $p_2$ induces an
   isomorphism $g_{V^\vee}^*\operatorname{FT}_\psi(K)\simeq
  \operatorname{FT}_\psi(g_V^*K)$.
2. For $N\in\Dbc(S,E)$, the projection formula for $p_2$ induces an
   isomorphism $\operatorname{FT}_\psi(K\otimes\pi^*N)\simeq
  \operatorname{FT}_\psi(K)\otimes\pi^{\vee*}N$, where $\pi:V\to S$ and
   $\pi^\vee:V^\vee\to S$ are the projections.
3. For a geometric point $\bar y$ of $V^\vee$, the proper base change
   map gives
   $$
   (\operatorname{FT}_\psi K)_{\bar y}
   \simeq
   R\Gamma_c\bigl(V_{\bar y},
   K|_{V_{\bar y}}\otimes
   \mathcal L_{\psi\langle x,y\rangle}\bigr)[r].
   \tag{16.2}
   $$
