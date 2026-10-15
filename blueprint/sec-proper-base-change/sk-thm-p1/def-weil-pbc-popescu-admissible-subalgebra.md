+++
id = "def-weil-pbc-popescu-admissible-subalgebra"
kind = "definition"
title = "Admissible subalgebra for the Popescu construction"
lean = ["Subalgebra.IsPopescuAdmissible"]
+++
Let $k$ be a field, $B$ a commutative $k$-algebra, and $\mathfrak m\subset B$ an ideal. A $k$-subalgebra $A\subset B$ is admissible relative to $\mathfrak m$ if it is an Artinian local ring, essentially of finite type over $k$ `Algebra.EssFiniteType` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/EssentialFiniteness.lean)), its inclusion $A\to B$ is flat `Module.Flat, RingHom.Flat` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Flat/Basic.lean)), and $\mathfrak m_A B=\mathfrak m$. In the Popescu construction $B=\bar\Lambda$ and $\mathfrak m$ is its maximal ideal.
