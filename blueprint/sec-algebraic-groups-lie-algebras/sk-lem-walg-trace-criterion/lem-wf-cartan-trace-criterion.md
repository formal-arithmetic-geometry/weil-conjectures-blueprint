+++
id = "lem-wf-cartan-trace-criterion"
kind = "lemma"
title = "Cartan's trace criterion"
lean = ["LieSubalgebra.isSolvable_of_trace_mul_eq_zero"]
order = 3701
uses = ["lem-wf-engel-matrix"]
+++
Let $M$ be a finite-dimensional vector space over $\Qlb$, and let
$\mathfrak a\subseteq\operatorname{End}(M)$ be a
finite-dimensional Lie algebra. If

$$
\operatorname{tr}(XY)=0
\quad\text{for all }X\in[\mathfrak a,\mathfrak a]
\text{ and }Y\in\mathfrak a,
$$

then $\mathfrak a$ is solvable.
