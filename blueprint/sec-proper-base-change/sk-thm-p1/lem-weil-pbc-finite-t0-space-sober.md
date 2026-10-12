+++
id = "lem-weil-pbc-finite-t0-space-sober"
kind = "lemma"
title = "A finite T0 space is sober"
lean = ["existsUnique_isGenericPoint_of_finite"]
source = "literature/stacks-project/topology.tex, Topology, the claim inside the proof of Lemma Tag 09XX (label lemma-spectral-inverse-limit-finite-sober-spaces, line 4704) that the images X_J (finite subspaces of a finite product of two-point spaces) are finite sober spaces, which Stacks asserts without argument; sober = quasi-sober and Kolmogorov as in the paragraph after Definition label definition-generic-point (line 972, paragraph at line 989)"
+++
Let $Y$ be a topological space whose underlying set is finite and which is $T_0$: for any two distinct points $y\ne y'$ of $Y$ there is an open subset of $Y$ containing exactly one of them. Then $Y$ is sober: for every irreducible closed subset $Z\subseteq Y$ `irreducibleComponents` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Topology/Irreducible.lean)) there is exactly one point $\eta\in Z$ whose closure $\overline{\{\eta\}}$ in $Y$ equals $Z$.
