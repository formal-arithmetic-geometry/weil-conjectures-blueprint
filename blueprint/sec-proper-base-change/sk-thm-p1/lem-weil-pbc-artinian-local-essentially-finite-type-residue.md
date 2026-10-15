+++
id = "lem-weil-pbc-artinian-local-essentially-finite-type-residue"
kind = "lemma"
title = "An Artinian local algebra is essentially of finite type when its residue field is"
lean = ["RingHom.essFiniteType_of_artinian_local_residue"]
+++
Let $R\to S$ be a homomorphism of commutative rings, where $S$ is an Artinian local ring (a local ring in which every descending chain of ideals is eventually constant) with maximal ideal $\mathfrak m$. If the composite $R\to S\to S/\mathfrak m$ is essentially of finite type `Algebra.EssFiniteType` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/EssentialFiniteness.lean)), then $R\to S$ is essentially of finite type.
