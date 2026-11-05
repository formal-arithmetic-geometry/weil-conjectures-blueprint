+++
id = "proposition-proper-base-change-projective-line--1"
kind = "proposition"
title = "Proper base change for $\\mathbf P^1$ (1)"
name_showing = false
order = 380001
aliases = ["bp-r115-1"]
lean = ["AlgebraicGeometry.Etale.isIso_baseChange_app_projectiveLine"]
uses = ["definition-derived-base-change-map", "definition-torsion-sheaves"]
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
