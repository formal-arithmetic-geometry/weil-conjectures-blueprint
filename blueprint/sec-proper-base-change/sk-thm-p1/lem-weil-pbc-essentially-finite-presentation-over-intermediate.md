+++
id = "lem-weil-pbc-essentially-finite-presentation-over-intermediate"
kind = "lemma"
title = "Essentially of finite presentation over an intermediate algebra essentially of finite type"
lean = ["RingHom.essentially_finite_presentation_over_intermediate"]
+++
Let $\varphi:R\to S$ and $\psi:S\to S'$ be homomorphisms of commutative rings. Assume that $S$ is essentially of finite type over $R$ via $\varphi$ `Algebra.EssFiniteType` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/EssentialFiniteness.lean)), and that $S'$ is essentially of finite presentation over $R$ via $\psi\circ\varphi$: $S'$ is isomorphic, as an $R$-algebra, to a localization $W^{-1}P$ of a finitely presented $R$-algebra $P$ `Algebra.FinitePresentation` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/FinitePresentation.lean)) at a multiplicative subset $W\subseteq P$. Then $S'$ is essentially of finite presentation over $S$ via $\psi$: there are a finitely presented $S$-algebra $P'$ and a multiplicative subset $V\subseteq P'$ such that $S'\cong V^{-1}P'$ as $S$-algebras.
