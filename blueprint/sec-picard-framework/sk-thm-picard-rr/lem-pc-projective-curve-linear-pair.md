+++
id = "lem-pc-projective-curve-linear-pair"
kind = "lemma"
title = "Two linear forms without a common zero on a projective curve"
lean = ["GradedAlgebra.IsStandard.exists_basicOpen_sup_eq_top"]
order = 647
uses = ["def-pc-curve", "def-pc-proj", "def-pc-standard-graded-algebra", "lem-pc-finite-linear-avoidance"]
+++
Let $k$ be an infinite field and $S$ an integral
standard graded $k$-algebra
such that $X=\operatorname{Proj}(S)$ has dimension one (for
instance, $X$ is a curve). There exist
$l_0,l_1\in S_1$ such that $D_+(l_0)\cup D_+(l_1)=X$.
