+++
id = "lem-weil-pbc-extended-completion-module-reduction"
kind = "lemma"
title = "Finite reduction of the completed algebra along an extended ideal"
lean = ["AdicCompletion.extendedCompletion_module_reduction"]
source = "literature/stacks-project/algebra.tex, Algebra, Lemma Tag 0394 (lemma-finite-after-completion), final paragraph; Lemma Tag 05GG (lemma-hathat-finitely-generated), parts (1) and (2). Source read at https://stacks.math.columbia.edu/tag/0394 and https://stacks.math.columbia.edu/tag/05GG because the local literature copy is absent."
+++
Let R and S be commutative rings, I a finitely generated ideal of R, and φ : R → S a ring homomorphism. Put J = IS, Â = lim R/I^k and B̂ = lim S/J^k `AdicCompletion` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/AdicCompletion/Basic.lean)). Assume S/J is a finitely generated R/I-module via the induced quotient homomorphism `Module.Finite` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Finiteness/Defs.lean)). Let ψ : Â → B̂ be a ring homomorphism such that for every k, x and r, if the kth coordinate of x is r modulo I^k then the kth coordinate of ψ(x) is φ(r) modulo J^k. Give B̂ the Â-module structure via ψ and put K = IÂ. Then B̂/KB̂ is a finitely generated Â/K-module via the quotient module action.
