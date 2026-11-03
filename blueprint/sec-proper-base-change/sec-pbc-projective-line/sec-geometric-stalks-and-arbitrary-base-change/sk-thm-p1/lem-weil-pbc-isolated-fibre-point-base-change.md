+++
id = "lem-weil-pbc-isolated-fibre-point-base-change"
kind = "lemma"
title = "Points isolated in their fibre stay isolated after base change"
uses = ["def-pc-scheme", "def-weil-finite-type-morphism"]
lean = ["AlgebraicGeometry.isolated_fiber_point_base_change"]
order = 1967
+++
Let $f:X\to S$ be a morphism of schemes [def-pc-scheme] which is locally of finite type [def-weil-finite-type-morphism], let $g:S'\to S$ be a morphism of schemes, and let $X'=X\times_SS'$ be the fibre product with projections $g':X'\to X$ and $f':X'\to S'$. Let $x'\in X'$, and put $x=g'(x')$, $s'=f'(x')$, $s=f(x)=g(s')$. If $x$ is an isolated point of the fibre $X_s=X\times_S\operatorname{Spec}\kappa(s)$ of $f$ at $s$ (the singleton is open in $X_s$), then $x'$ is an isolated point of the fibre $X'_{s'}=X'\times_{S'}\operatorname{Spec}\kappa(s')$ of $f'$ at $s'$.
