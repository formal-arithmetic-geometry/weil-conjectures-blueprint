+++
id = "def-weil-pbc-etale-mayer-vietoris-section-complex"
kind = "definition"
title = "The explicit two-open section short complex"
uses = ["def-pc-scheme"]
lean = ["AlgebraicGeometry.Etale.etaleSectionShortComplex"]
+++
For a scheme X [def-pc-scheme], opens U,V of X, and a nonnegative cochain complex I of abelian etale sheaves `CategoryTheory.Sheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/Sheaf.lean)), define Sec(I,W) by applying evaluation at the etale object W degreewise. Define etaleSectionShortComplex(U,V,I) `CategoryTheory.ShortComplex.Exact` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Homology/ShortComplex/Exact.lean)) to have objects Sec(I,X), Sec(I,U) direct-sum Sec(I,V), Sec(I,U intersection V), first arrow the restriction pair and second arrow the difference of restrictions. Restriction maps commute with differentials by naturality. The composite is zero because both composites are restriction from X to the intersection. The auxiliary etaleSectionFunctor and etaleSectionMap are the evaluation functor and its induced map on complexes.
