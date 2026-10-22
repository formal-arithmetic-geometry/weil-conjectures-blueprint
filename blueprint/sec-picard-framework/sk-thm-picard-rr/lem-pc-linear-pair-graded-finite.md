+++
id = "lem-pc-linear-pair-graded-finite"
kind = "lemma"
title = "A degree bound for a pair of linear forms"
lean = ["GradedAlgebra.IsStandard.exists_grade_succ_eq_span_mul"]
order = 658
uses = ["def-pc-proj", "def-pc-standard-graded-algebra"]
+++
Let $S$ be a standard graded
$k$-algebra, and let $l_0,l_1\in S_1$ have no common zero on
$\operatorname{Proj}(S)$. There is an integer $N\ge1$ such that

$$
S_n=l_0S_{n-1}+l_1S_{n-1}\qquad(n\ge N).
$$
