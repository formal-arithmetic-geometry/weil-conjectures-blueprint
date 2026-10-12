+++
id = "lem-weil-pbc-etale-cech-sectionwise-short-exact"
kind = "lemma"
title = "Sectionwise short exactness gives a short exact sequence of etale Cech complexes"
uses = ["def-weil-pbc-etale-site"]
lean = ["AlgebraicGeometry.Scheme.etale_cech_shortExact_of_sections"]
source = "literature/stacks-project/sites-cohomology.tex, Lemma Tag 03F9 (lemma-cech-vanish-collection), proof: short exact sequence of Cech complexes after sectionwise exactness"
+++
Let X be a scheme with small etale site [def-weil-pbc-etale-site], and let S be a short exact sequence of abelian sheaves `CategoryTheory.Sheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/Sheaf.lean)). Let U be an object, T any indexing type, and f_t : V_t -> U any family, not necessarily a covering. Suppose S.g is surjective on sections over every nonempty iterated fibre product V_(a_0) x_U ... x_U V_(a_p), for all p >= 0 and all tuples a : Fin(p+1) -> T. Then applying the Cech complex functor `CategoryTheory.cechComplexFunctor` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/SheafCohomology/Cech.lean)) to S gives a short exact sequence of cochain complexes of abelian groups. No injectivity or Cech-acyclicity assumption is needed.
