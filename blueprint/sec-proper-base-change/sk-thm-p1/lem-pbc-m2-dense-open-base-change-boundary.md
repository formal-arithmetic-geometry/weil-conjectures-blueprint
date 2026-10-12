+++
id = "lem-pbc-m2-dense-open-base-change-boundary"
kind = "lemma"
title = "Finite closed separably closed boundary after extension of an algebraically closed field"
uses = ["def-kun-separably-closed", "def-weil-pbc-curve-setting", "def-weil-pbc-extension-pullback"]
lean = ["AlgebraicGeometry.IsCurve.dense_open_baseChange_boundary"]
source = "literature/stacks-project/etale-cohomology.tex, Tag 0GJA (lemma-restrict-to-open), proof, first sentence and remark (c); boundary geometry under field extension"
+++
Let $k,k'$ be algebraically closed fields, $f:X\to\operatorname{Spec}k$ a separated finite-type scheme with $\dim X\leq1$ [def-weil-pbc-curve-setting], and let $a:X'\to X$ be the top arrow of a cartesian field-extension square [def-weil-pbc-extension-pullback] with bottom arrow $\operatorname{Spec}k'\to\operatorname{Spec}k$. For every dense open $U\subseteq X$, put $V=a^{-1}(U)$. Then $X'\setminus V$ is finite, every $y\in X'\setminus V$ is closed `closedPoints` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Topology/JacobsonSpace.lean)), and its residue field $\kappa(y)$ `AlgebraicGeometry.Scheme.residueField` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/ResidueField.lean)) is separably closed [def-kun-separably-closed]. There are no irreducibility, reducedness or nonemptiness assumptions.
