+++
id = "lem-weil-pbc-proper-open-p-proper"
kind = "lemma"
title = "Properness of the projection of the comparison square"
order = 3305
lean = ["AlgebraicGeometry.Etale.properOpenComparison_proj_isProper"]
uses = ["def-weil-pbc-proper-open-comparison"]
+++
Let $u:T_1\to T_2$ be proper and let $j_2:X\hookrightarrow T_2$ be an open
immersion. For the fibre product $V=T_1\times_{T_2}X$ with projection
$p:V\to X$ of [def-weil-pbc-proper-open-comparison], the morphism $p$ is
proper and therefore separated.

## Proof

By construction in [def-weil-pbc-proper-open-comparison] the square with
sides $u:T_1\to T_2$, $j_2:X\to T_2$, $b:V\to T_1$ and $p:V\to X$ is
cartesian, so $p:V\to X$ is the base change of the proper morphism $u$ along
$j_2$. A base change of a proper morphism is proper, so $p$ is proper, and a
proper morphism is separated by the definition of properness.

Unresolved dependencies: def:weil-pbc-scheme-conventions, lem:weil-pbc-proper-base-change
