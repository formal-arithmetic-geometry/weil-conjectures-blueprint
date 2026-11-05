+++
id = "proposition-proper-base-change-projective-line--2"
kind = "proposition"
title = "Proper base change for $\\mathbf P^1$ (2)"
name_showing = false
order = 380002
aliases = ["bp-r115-2"]
lean = []
uses = ["definition-injective-acyclicity"]
+++
The Lean proof of the main theorem bypasses this consequence, using the
base change property of $\mathbf P^1$ directly.

Let $S$ be a scheme, $\Lambda$ a commutative ring, and
$\pi:\mathbf P^1_S\to S$ the projection. Then
$\mathrm{IA}_\Lambda(\pi)$ holds: for every base change $g:T\to S$ and
every torsion injective sheaf $I$ of $\Lambda$-modules on
$\mathbf P^1_{S,\acute{e}t}$, one has

$$
R^q\pi'_*g'^*I=0\qquad(q>0).
$$
