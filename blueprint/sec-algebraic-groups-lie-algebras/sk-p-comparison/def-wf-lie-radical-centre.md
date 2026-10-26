+++
id = "def-wf-lie-radical-centre"
kind = "definition"
title = "Solvable radical and centre of a Lie algebra"
lean = ["LieAlgebra.isGreatest_radical", "LieAlgebra.mem_center_iff_forall_lie_eq_zero"]
order = 3692
uses = ["def-wf-lie-algebra"]
+++
For a finite-dimensional Lie algebra $\mathfrak g$, its solvable
radical $\operatorname{rad}(\mathfrak g)$ is the sum of all solvable
ideals (solvability and ideals as in [def-wf-lie-algebra]), and its centre is

$$
\mathfrak z(\mathfrak g)=\{X\in\mathfrak g:[X,Y]=0\text{ for all }Y\in\mathfrak g\}.
$$

The sum $\operatorname{rad}(\mathfrak g)$ is again solvable, and is
therefore the unique largest solvable ideal of $\mathfrak g$.
