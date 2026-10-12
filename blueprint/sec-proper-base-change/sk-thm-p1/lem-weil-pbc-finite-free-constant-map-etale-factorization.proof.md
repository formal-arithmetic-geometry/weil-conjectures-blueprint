+++
kind = "proof"
of = "lem-weil-pbc-finite-free-constant-map-etale-factorization"
uses = ["def-constructible-constant", "def-weil-pbc-geometric-stalks"]
+++
If n = 0, take the identity etale neighbourhood and the unique zero map.
For n > 0, write the standard basis of Λ^(Fin n).  The definition of the geometric
stalk is a filtered colimit over pointed etale neighbourhoods, so each image under l
is represented by a section of F on one such neighbourhood.  Cofilteredness of pointed
etale neighbourhoods gives one common refinement for the finitely many representatives.
The equality hl says that the two resulting germs in G agree.  Equality in the same
filtered colimit therefore gives a further common refinement on which the equalities
hold as sections.  The finite free universal property assembles these sections into a
Λ-linear map from Λ^(Fin n) to sections of F on that neighbourhood.  The
constant-sheaf/global-sections adjunction, together with the pullback comparison for
the constant sheaf, turns this linear map into β.  Checking on the standard basis gives
β ≫ upperStar(V.hom).map φ = upperStar(V.hom).map α.  The chosen pointed neighbourhood
contains x, so x lies in the range of V.hom.  This argument uses no monicity of φ and
works for the zero ring as well. ([def-weil-pbc-geometric-stalks], `AlgebraicGeometry.Scheme.instIsCofilteredElementsEtaleCompOverForgetObjOppositeFunctorTypeCoyonedaOpMk` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Sites/EtalePoint.lean)), `CategoryTheory.constantSheafAdj` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/ConstantSheaf.lean)), [def-constructible-constant]).
