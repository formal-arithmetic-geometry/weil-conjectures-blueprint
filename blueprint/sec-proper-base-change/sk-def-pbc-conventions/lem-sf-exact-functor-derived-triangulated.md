+++
id = "lem-sf-exact-functor-derived-triangulated"
kind = "lemma"
title = "An exact functor of abelian categories induces a triangulated functor on derived categories"
order = 1369
uses = ["def-weil-abstract-derived-category", "def-weil-triangulated-category"]
lean = ["CategoryTheory.Functor.mapDerivedCategory", "CategoryTheory.Functor.IsTriangulated", "CategoryTheory.Functor.mapDerivedCategorySingleFunctor"]
tags = ["mathlib", "stacks-015F"]
+++
Let $F:\mathcal C_1\to\mathcal C_2$ be an exact (additive, preserving finite limits and colimits) functor between abelian categories, with derived categories $D(\mathcal C_1)$, $D(\mathcal C_2)$ [def-weil-abstract-derived-category]. Applying $F$ termwise to complexes induces a functor $F:D(\mathcal C_1)\to D(\mathcal C_2)$ which is triangulated [def-weil-triangulated-category] (it commutes with the shift and carries distinguished triangles to distinguished triangles) and which carries a complex $A[n ]$ concentrated in one degree to $F(A)[n ]$.
