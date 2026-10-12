+++
kind = "proof"
of = "lem-weil-pbc-filtered-module-sheaf-colimit-local-representatives"
+++
Define the subfunctor R of the underlying type presheaf of H = c.pt by sectionwise membership in the image of some coprojection. Cocone naturality proves restriction stability. IsFiltered.nonempty gives the zero section; IsFiltered.max and the cocone equations place sums in a common stage; linearity gives scalar stability. Thus each R(U) is a submodule.

Take Subfunctor.sheafify J R, the local-membership closure inside H. GrothendieckTopology.intersection_covering proves additive closure by intersecting the sieves witnessing membership of two sections. Scalar closure follows from superset_covering and linearity. These submodules form a module-valued presheaf K. Mathlib Subfunctor.sheafify_isSheaf says the underlying type presheaf is a sheaf. To use independent universes, represent the module forgetful functor by the lifted rank-one module ULift Λ using evaluation at 1, so it preserves limits of arbitrary site size; it reflects such limits by factorization through AddCommGrpCat. Presheaf.isSheaf_of_isSheaf_comp therefore proves K is a module-valued sheaf.

The coprojections of c factor through K, since R ≤ Subfunctor.sheafify J R. They form a cocone d. Its coprojections followed by the inclusion m : K → H equal those of c. IsColimit.hom_ext and IsColimit.fac show hc.desc d ≫ m = identity H. Apply this identity to t: t lies in the local-membership closure of R. By the definition of Subfunctor.sheafify, R.sieveOfSection t is covering, and its membership supplies precisely the required stage and section.
