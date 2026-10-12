+++
id = "lem-sfb-derived-tensor-modules-derived"
kind = "lemma"
title = "The derived relative tensor product is a two-variable left derived functor"
order = 1567
uses = ["def-sfb-derived-tensor-modules"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isLeftDerivedFunctor₂_derivedTensor", "CategoryTheory.Mod.isLeftDerivedFunctor₂_curriedTensor"]
+++
The derived tensor product $-\otimes^{\mathrm L}_R-$ of [def-sfb-derived-tensor-modules]
(in particular $-\otimes^{\mathrm L}_{\Lambda_X}-$), together with the lax monoidal
structure map of the localization functor, is the left derived functor in two variables
of the relative tensor product of complexes of $R$-modules, with respect to the
quasi-isomorphisms in each variable.
