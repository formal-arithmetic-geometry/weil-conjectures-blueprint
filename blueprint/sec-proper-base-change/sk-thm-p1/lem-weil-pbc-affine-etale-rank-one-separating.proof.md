+++
kind = "proof"
of = "lem-weil-pbc-affine-etale-rank-one-separating"
uses = ["def-weil-pbc-etale-sum-extension", "lem-weil-pbc-etale-inverse-image-restriction"]
+++
For each affine etale U, compose the constant-sheaf/terminal-evaluation adjunction with etaleLowerShriekUpperStarAdjunction transported along upperStarIsoLocalizationRestriction. This identifies maps from the rank-one extension to F with linear maps from Lambda to F(U), naturally in F. The localized terminal object maps to U (proved by ext and rfl). ([def-weil-pbc-etale-sum-extension], [lem-weil-pbc-etale-inverse-image-restriction], `CategoryTheory.constantSheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/ConstantSheaf.lean))).

If f and g agree after all maps from the rank-one extension at U, apply this Hom equivalence to the inverse image of each linear map Lambda -> F(U). Naturality yields a composed equality. Use the linear map r |-> r*x and evaluate at 1 to obtain f_U(x)=g_U(x), for every x. ModuleCat.hom_ext gives equality of components.

The Spec functor from the affine etale site is cover-dense and full, by the affine-etale Mathlib leaf. Mathlib Functor.whiskerLeft_obj_map_bijective_of_isCoverDense makes restriction of morphisms into a sheaf injective. The preceding equality holds on all its affine source objects, so restriction of f and g agrees. Injectivity and Sheaf.hom_ext prove f=g. (`AlgebraicGeometry.Scheme.AffineEtale.instEssentiallySmall` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Sites/AffineEtale.lean))).
