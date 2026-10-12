+++
kind = "proof"
of = "lem-weil-pbc-affine-free-finite-stalk-generation"
uses = ["def-weil-pbc-geometric-stalks"]
+++
Represent a stalk element by a section z on a pointed etale neighbourhood (V,v). In Lean use Point.toPresheafFiber_jointly_surjective after shrinking the universe of the filtered-colimit preservation instance for forget (ModuleCat Λ). ([def-weil-pbc-geometric-stalks], `CategoryTheory.Limits.Concrete.isColimit_exists_rep, CategoryTheory.Limits.Concrete.isColimit_rep_eq_iff_exists, ModuleCat.FilteredColimits.forget_preservesFilteredColimits` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Limits/ConcreteCategory/Basic.lean))).

Choose an affine open Spec R→V through v(default). The geometric point factors through it by the universal property of an open immersion. Restrict z along this open immersion and use Point.toPresheafFiber_w to keep the same germ. (`AlgebraicGeometry.Scheme.exists_affine_mem_range_and_range_subset, AlgebraicGeometry.IsOpenImmersion.lift, AlgebraicGeometry.IsOpenImmersion.lift_fac, AlgebraicGeometry.IsOpenImmersion.lift_uniq` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/OpenImmersion.lean))).

For the resulting affine object W and section z, explicitly define a presheaf map η sending the generator indexed by h:V→W to F(h)(z). ModuleCat.freeDesc gives its linear components and functoriality proves naturality. Sheafify this map with sheafifyLift; toSheafify_sheafifyLift proves that the generator indexed by id_W maps to z. Point.toPresheafFiber_naturality therefore puts the chosen germ in the range of the stalk of the sheaf map. (`PresheafOfModules.sheafification` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Category/ModuleCat/Presheaf/Sheafification.lean))).

Unpack Module.Finite.fg_top into a finite set T spanning the stalk. Choose one affine free map for each t∈T and take the finite image S of these choices. Each chosen map factors through the S-indexed coproduct injection. Applying the stalk functor and Sigma.ι_desc shows T is contained in the range of the total stalk map. The range is a submodule; Submodule.span_le and span(T)=top give range=top, hence surjectivity. Empty T produces empty S.
