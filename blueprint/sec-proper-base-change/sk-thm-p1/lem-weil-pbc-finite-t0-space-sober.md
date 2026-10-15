+++
id = "lem-weil-pbc-finite-t0-space-sober"
kind = "lemma"
title = "A finite T0 space is sober"
lean = ["existsUnique_isGenericPoint_of_finite"]
+++
Let $Y$ be a topological space whose underlying set is finite and which is $T_0$: for any two distinct points $y\ne y'$ of $Y$ there is an open subset of $Y$ containing exactly one of them. Then $Y$ is sober: for every irreducible closed subset $Z\subseteq Y$ `irreducibleComponents` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Topology/Irreducible.lean)) there is exactly one point $\eta\in Z$ whose closure $\overline{\{\eta\}}$ in $Y$ equals $Z$.
