+++
kind = "proof"
of = "lem-weil-pbc-etale-cech-sectionwise-short-exact"
uses = ["def-sp-left-exact-additive"]
+++
For degree p restrict the underlying presheaves to the discrete category of tuples a : Fin (p+1) -> T, evaluated at the corresponding iterated fibre products. This functor Q preserves finite limits and zero morphisms. Apply ShortComplex.Exact.map_of_mono_of_preservesKernel to hS.exact and the mono hS.mono_f; Q also preserves that mono. Each component of Q.map S.g is epi by the assumed surjectivity and AddCommGrpCat.epi_iff_surjective. NatTrans.epi_of_epi_app supplies the epi in the functor category, hence S.map Q is short exact. (`CategoryTheory.Sheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/Sheaf.lean)), [def-sp-left-exact-additive]).

Apply ShortComplex.ShortExact.map_of_exact to the limit functor on the discrete tuple category. Mathlib.Algebra.Category.Grp.AB supplies preservation of finite colimits by this limit functor, while limits preserve finite limits. Identify the resulting sequence with the degree-p Cech sequence using the inverses of Pi.isoLimit on its three objects. For the two commutativity squares, apply Pi.hom_ext, Pi.map_pi, Pi.isoLimit_inv_pi and limMap_pi. This works for arbitrary indexing types, including empty types. (`CategoryTheory.cechComplexFunctor` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/SheafCohomology/Cech.lean))).

Apply HomologicalComplex.shortExact_of_degreewise_shortExact to the short exact degree-p sequences obtained above. (`HomologicalComplex.shortExact_iff_degreewise_shortExact` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Homology/HomologicalComplexAbelian.lean))).
