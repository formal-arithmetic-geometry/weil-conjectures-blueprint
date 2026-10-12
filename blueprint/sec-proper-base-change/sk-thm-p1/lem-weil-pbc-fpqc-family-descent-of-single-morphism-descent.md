+++
id = "lem-weil-pbc-fpqc-family-descent-of-single-morphism-descent"
kind = "lemma"
title = "Fpqc family descent from single-morphism descent (proved source-library tool)"
uses = ["def-pc-scheme"]
lean = ["AlgebraicGeometry.Scheme.of_isPullback_of_ofArrows_mem_fpqcTopology"]
source = "literature/stacks-project/descent.tex, Tag 02KP, fpqc case, with Topologies Tag 022E; already proved as AlgebraicGeometry.Scheme.of_isPullback_of_ofArrows_mem_fpqcTopology in lean/WeilConjectures/Mathlib/AlgebraicGeometry/Sites/Fpqc.lean, lines 77-139."
+++
Let $P$ be a property of morphisms of schemes [def-pc-scheme], Zariski local on the target, stable under arbitrary base change, and descending along surjective flat quasi-compact morphisms. Let $f:Z\to T$ and let $\{g_i:T_i\to T\}_{i\in I}$ generate a covering sieve for the fpqc topology `AlgebraicGeometry.Scheme.fpqcPrecoverage` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Sites/Fpqc.lean)). For each $i$ let $a_i:Z_i\to Z$ and $b_i:Z_i\to T_i$ form a cartesian square with $f,g_i$ `CategoryTheory.Limits.pullback` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Limits/Shapes/Pullback/HasPullback.lean)). If $P(b_i)$ for all $i$, then $P(f)$.
