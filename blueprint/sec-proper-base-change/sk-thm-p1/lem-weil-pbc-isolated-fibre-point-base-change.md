+++
id = "lem-weil-pbc-isolated-fibre-point-base-change"
kind = "lemma"
title = "Points isolated in their fibre stay isolated after base change"
uses = ["def-pc-scheme", "def-weil-finite-type-morphism"]
lean = ["AlgebraicGeometry.isolated_fiber_point_base_change"]
+++
Let $f:X\to S$ be a morphism of schemes [def-pc-scheme] which is locally of finite type [def-weil-finite-type-morphism], let $g:S'\to S$ be a morphism of schemes, and let $X'=X\times_SS'$ be the fibre product `CategoryTheory.Limits.pullback` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Limits/Shapes/Pullback/HasPullback.lean)) with projections $g':X'\to X$ and $f':X'\to S'$. Let $x'\in X'$, and put $x=g'(x')$, $s'=f'(x')$, $s=f(x)=g(s')$. If $x$ is an isolated point of the fibre $X_s$ of $f$ at $s$ `AlgebraicGeometry.Scheme.Hom.fiber` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Fiber.lean)) (the singleton is open in $X_s$), then $x'$ is an isolated point of the fibre $X'_{s'}=X'\times_{S'}\operatorname{Spec}\kappa(s')$ of $f'$ at $s'$.
