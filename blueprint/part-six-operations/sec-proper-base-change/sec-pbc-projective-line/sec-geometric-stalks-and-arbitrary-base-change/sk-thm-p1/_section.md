+++
id = "sk-thm-p1"
kind = "proposition"
title = "Proper base change for the projective line"
order = 211
lean = ["AlgebraicGeometry.Etale.hasTorsionBaseChange_projectiveLine", "AlgebraicGeometry.Etale.hasInjectiveAcyclicity_projectiveLine"]
uses = ["sk-thm-br", "sk-def-pbc", "sk-thm-curveestimate", "sk-def-exchange", "sk-def-ia", "sk-prop-pbc-p1-henselian", "sk-lem-pbc-curve-field-extension"]
tags = ["sketch"]
+++
Let $S$ be a scheme and $\Lambda$ a commutative ring. In the
cartesian square

$$
\begin{CD}
\mathbf P^1_T @>{g'}>> \mathbf P^1_S\\
@V{\pi'}VV @VV{\pi}V\\
T @>{g}>> S,
\end{CD}
$$

the base change map

$$
g^*R\pi_*K\longrightarrow R\pi'_*g'^*K
$$

is an isomorphism for every
$K\in D^+(\mathbf P^1_{S,\acute{e}t},\Lambda)$ with torsion cohomology sheaves.
In particular, $\mathrm{IA}_\Lambda(\pi)$ holds.
