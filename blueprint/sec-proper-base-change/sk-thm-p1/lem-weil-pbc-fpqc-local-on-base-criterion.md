+++
id = "lem-weil-pbc-fpqc-local-on-base-criterion"
kind = "lemma"
title = "Criterion for a property of morphisms to descend along fpqc coverings (Stacks 02KP, fpqc case)"
uses = ["def-pc-scheme"]
lean = ["AlgebraicGeometry.fpqc_local_on_base_criterion"]
+++
Let $\mathcal P$ be a class of morphisms of schemes [def-pc-scheme] satisfying the following four conditions.
(0) (Invariance under isomorphism.) If $f:X\to S$ has $\mathcal P$ and $\tilde f:\tilde X\to\tilde S$ is a morphism for which there are isomorphisms of schemes $a:X\to\tilde X$, $b:S\to\tilde S$ with $\tilde f\circ a=b\circ f$, then $\tilde f$ has $\mathcal P$.
(1) (Stable under flat base change.) If $f:X\to S$ has $\mathcal P$ and $g:S'\to S$ is a flat morphism `AlgebraicGeometry.Flat` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/Flat.lean)), then the second projection $X\times_SS'\to S'$ of the fibre product `CategoryTheory.Limits.pullback` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Limits/Shapes/Pullback/HasPullback.lean)) has $\mathcal P$.
(2) (Zariski local on the base.) If $f:X\to S$ is a morphism and $S=\bigcup_{k\in K}V_k$ is a covering of $S$ by open subschemes such that for every $k$ the restriction $f^{-1}(V_k)\to V_k$ of $f$ (a morphism from the open subscheme $f^{-1}(V_k)$ of $X$ to the open subscheme $V_k$ of $S$) has $\mathcal P$, then $f$ has $\mathcal P$.
(3) (Descent along faithfully flat morphisms of affine schemes.) If $S$ and $S'$ are affine schemes, $g:S'\to S$ is a flat and surjective `AlgebraicGeometry.Surjective` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/UnderlyingMap.lean)) morphism, and $f:X\to S$ is a morphism such that the second projection $X\times_SS'\to S'$ has $\mathcal P$, then $f$ has $\mathcal P$.
Then for every morphism of schemes $f:X\to S$ and every fpqc covering $\{g_i:S_i\to S\}_{i\in I}$ of $S$ `AlgebraicGeometry.Scheme.fpqcPrecoverage` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Sites/Fpqc.lean)) such that for every $i\in I$ the second projection $f_i:X\times_SS_i\to S_i$ has $\mathcal P$, the morphism $f$ has $\mathcal P$.
