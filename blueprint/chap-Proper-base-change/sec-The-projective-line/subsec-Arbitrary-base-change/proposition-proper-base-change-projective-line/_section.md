+++
id = "proposition-proper-base-change-projective-line"
kind = "proposition"
title = "Proper base change for $\\mathbf P^1$"
order = 380
lean = ["AlgebraicGeometry.Etale.hasInjectiveAcyclicity_projectiveLine", "AlgebraicGeometry.Etale.hasTorsionBaseChange_projectiveLine"]
uses = ["definition-derived-base-change-map"]
+++
Let $S$ be a scheme and $\Lambda$ a commutative ring.  In the
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
