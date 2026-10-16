+++
id = "lem-weil-geometric-generic-duality"
kind = "lemma"
title = "The double dual on a geometric generic fibre"
lean = ["AlgebraicGeometry.Etale.leftDerivedUpperStar_\u03bc_map_braiding_hom", "AlgebraicGeometry.Etale.leftDerivedUpperStarBraided", "AlgebraicGeometry.Etale.exists_iso_leftDerivedUpperStar_dualizingComplex_of_generic", "AlgebraicGeometry.Etale.isIso_leftDerivedUpperStar_map_verdierDualDoubleDual_app_iff_of_generic", "CategoryTheory.MonoidalClosed.isIso_toIhomIhom_tensor_right_iff", "CategoryTheory.MonoidalClosed.isIso_map_toIhomIhom_iff_of_iso_tensor", "AlgebraicGeometry.Etale.isIso_leftDerivedUpperStar_map_verdierDualDoubleDual_app_iff"]
order = 2471
uses = ["cor-amb-affine-space-adjunction", "lem-weil-delta-restriction", "lem-weil-duality-pairing", "lem-weil-geometric-generic-exchange", "lem-weil-verdier-preservation-strata", "thm-amb-etale-exceptional-adjoint"]
+++
Let $X$ be separated of finite type over $k$, let
$p:X\to\mathbf A^1_k$ be a morphism, and let $g$
be pullback to $X_{\bar\eta}$, where
$\bar\eta=\operatorname{Spec}\overline{k(t)}$.
Then, Zariski locally on $X$,

$$
g^*\omega_X\cong\omega_{X_{\bar\eta}}(1)[2].
$$

For every $K\in D^b_{ctf}(X_{\Et},A)$, this comparison identifies
$g^*\delta_K$ with $\delta_{g^*K}$; the displayed invertible
twist and shift cancel after taking the dual twice.
