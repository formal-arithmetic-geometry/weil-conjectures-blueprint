+++
id = "lem-weil-pbc-kollar-regular-element-alternatives"
kind = "lemma"
title = "Kollar alternatives when the maximal ideal is associated modulo a regular element"
lean = ["IsLocalRing.kollar_regular_element_alternatives"]
source = "literature/stacks-project/algebra.tex, Tag 0BHZ, proof fourth and fifth paragraphs (also https://stacks.math.columbia.edu/tag/0BHZ)"
+++
Let $(R,\mathfrak m)$ be a Noetherian local commutative ring `IsNoetherianRing` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Noetherian/Defs.lean)). Let $x\in\mathfrak m$ act injectively on $R$, and suppose $\mathfrak m$ is an associated prime of $R/xR$, meaning that some nonzero class has annihilator exactly $\mathfrak m$. Then either $R$ is regular local `IsRegularLocalRing, IsRegularRing` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/RegularLocalRing/Defs.lean)) of Krull dimension one `ringKrullDim` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/KrullDimension/Basic.lean)), or there exists a nonzero commutative ring $S$ and a ring map $\varphi:R\to S$, finite as an $R$-module `Module.Finite` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Finiteness/Defs.lean)), not bijective, such that for some integer $n\ge1$ we have $\mathfrak m^n\ker\varphi=0$ and $\mathfrak m^n S\subseteq\varphi(R)$, and there is no $z\in S$ with $\{a\in R:\varphi(a)z=0\}=\mathfrak m$.
