+++
id = "lem-weil-pbc-artinian-local-essentially-finite-type-residue"
kind = "lemma"
title = "An Artinian local algebra is essentially of finite type when its residue field is"
lean = ["RingHom.essFiniteType_of_artinian_local_residue"]
source = "literature/stacks-project/algebra.tex, Algebra, Lemma Tag 07DT (lemma-essentially-of-finite-type-into-artinian-local, line 12869), part (3), direction 'if'; proof lines 12911-12923 (uses part (1) and Lemma Tag 07DS, lemma-composition-essentially-of-finite-type); tags verified in literature/stacks-project/tags/tags"
+++
Let $R\to S$ be a homomorphism of commutative rings, where $S$ is an Artinian local ring (a local ring in which every descending chain of ideals is eventually constant) with maximal ideal $\mathfrak m$. If the composite $R\to S\to S/\mathfrak m$ is essentially of finite type `Algebra.EssFiniteType` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/EssentialFiniteness.lean)), then $R\to S$ is essentially of finite type.
