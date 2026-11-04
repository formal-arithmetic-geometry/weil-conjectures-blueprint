+++
id = "corollary-verdier-exchange-formulas"
kind = "corollary"
title = "Verdier exchange formulas"
order = 847
lean = ["AlgebraicGeometry.Etale.nonempty_iso_verdierDual_rightDerivedLowerShriek", "AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_dualizingComplex", "AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_verdierDual", "AlgebraicGeometry.Etale.nonempty_iso_leftDerivedUpperStar_verdierDual"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "theorem-proper-base-change-classical-pro", "definition-relative-dualizing-complex", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "proposition-pullback-multiplication-n", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "corollary-serre-duality-field-extension", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic"]
+++
For a morphism $f:X\to Y$ there are natural isomorphisms of functors on
$D^b_{\mathrm{ctf}}(X,\Lambda)$, respectively $D^b_{\mathrm{ctf}}(Y,\Lambda)$,

$$
\begin{aligned}
\mathbb D_YRf_!&\simeq Rf_*\mathbb D_X,&
\mathbb D_YRf_*&\simeq Rf_!\mathbb D_X,\\
\mathbb D_Xf^*&\simeq f^!\mathbb D_Y,&
\mathbb D_Xf^!&\simeq f^*\mathbb D_Y.
\end{aligned}
$$

In particular, for an open $j:U\hookrightarrow X$ and a closed
$i:Z\hookrightarrow X$,

$$
\mathbb D_Xj_!\simeq Rj_*\mathbb D_U,\qquad
\mathbb D_XRj_*\simeq j_!\mathbb D_U,\qquad
i^*\mathbb D_X\simeq\mathbb D_Zi^!.
$$

The isomorphisms in the left column are (10.3)
and (10.4); those in the right column are
obtained from them by biduality, as displayed in the proof.
