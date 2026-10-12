+++
id = "lem-weil-pbc-filtered-colimit-factorization-descent"
kind = "lemma"
title = "Finite monic factorization data descends in a filtered colimit of pairs"
lean = ["filteredColimit_factorization_descent"]
source = "literature/stacks-project/more-algebra.tex, Lemma Tag 0FWT, proof, second paragraph (finite descent before applying henselianity)"
+++
Let Λ be a nonempty directed preorder, F : Λ ⥤ CommRingCat a diagram with colimit A `CategoryTheory.Limits.colimit` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Limits/HasLimits.lean)), and Jᵢ compatible ideals. Suppose I is an ideal of A whose elements are exactly the images of elements of the Jᵢ. Given a monic polynomial f over A and coprime monic polynomials g₀,h₀ over A/I with f mod I = g₀h₀, there exist a stage i and monic polynomials Fᵢ,Gᵢ,Hᵢ over F(i) such that Fᵢ maps to f, the reductions of Gᵢ,Hᵢ modulo Jᵢ are coprime and multiply to Fᵢ mod Jᵢ, and the images of Gᵢ,Hᵢ modulo I are g₀,h₀. No stage pair is assumed henselian.
