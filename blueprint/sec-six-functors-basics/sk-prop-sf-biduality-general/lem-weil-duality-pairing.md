+++
id = "lem-weil-duality-pairing"
kind = "lemma"
title = "The duality pairing and the double-dual morphism"
lean = ["AlgebraicGeometry.Etale.verdierDualEvaluation", "AlgebraicGeometry.Etale.verdierDualDoubleDual", "AlgebraicGeometry.Etale.verdierDualDoubleDual_app", "AlgebraicGeometry.Etale.isIso_map_verdierDualDoubleDual_app_congr", "AlgebraicGeometry.Etale.isIso_map_verdierDualDoubleDual_app_iff_of_iso", "CategoryTheory.Adjunction.isIso_unit_app_iff_of_iso", "CategoryTheory.MonoidalClosed.ihomFlipSelfAdjunction", "CategoryTheory.MonoidalClosed.ihomFlipSelfAdjunction_unit_app", "CategoryTheory.MonoidalClosed.isIso_toIhomIhom_tensor_iff", "CategoryTheory.Pretriangulated.isIso_app_obj\u2082_of_distTriang", "AlgebraicGeometry.Etale.verdierDual_map", "AlgebraicGeometry.Etale.exists_distTriang_verdierDual_verdierDual", "AlgebraicGeometry.Etale.isIso_verdierDualDoubleDual_app_iff_of_iso", "AlgebraicGeometry.Etale.isIso_verdierDualDoubleDual_app_shift_iff", "AlgebraicGeometry.Etale.isIso_verdierDualDoubleDual_app_obj\u2082", "AlgebraicGeometry.Etale.verdierBidualityLocus", "AlgebraicGeometry.Etale.verdierBidualityLocus_isClosedUnderIsomorphisms", "AlgebraicGeometry.Etale.verdierBidualityLocus_isStableUnderShift", "AlgebraicGeometry.Etale.verdierBidualityLocus_isTriangulatedClosed\u2082", "AlgebraicGeometry.Etale.verdierBidualityLocus_containsZero", "AlgebraicGeometry.Etale.verdierBidualityLocus_isTriangulated"]
order = 2466
uses = ["def-weil-derived-pullback-tensor-hom", "lem-sf-hom-triangulated", "thm-amb-etale-exceptional-adjoint"]
+++
Let $X$ be a separated finite-type scheme over a field, with finite
coefficients invertible on that field. On the ambient etale derived
category put $\omega_X=Ra_X^{\times}A$, using the right adjoint of
[thm-amb-etale-exceptional-adjoint], and let
$D_X=R\mathcal Hom_A(-,\omega_X)$. For every complex $K$, the
evaluation of internal Hom is a natural pairing

$$
\mathrm{ev}_K:D_XK\otimes_A^LK\longrightarrow\omega_X.
$$

Its transpose is the natural double-dual morphism
$\delta_K:K\to D_XD_XK$. It is compatible with shifts and is a
morphism of distinguished triangles. The same formal construction
applies on the pro-etale site whenever its ambient dualizing object is
specified; it does not assume that $D_XK$ is constructible.
