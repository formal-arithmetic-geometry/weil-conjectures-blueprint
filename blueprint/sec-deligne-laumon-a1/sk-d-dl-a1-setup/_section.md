+++
id = "sk-d-dl-a1-setup"
kind = "remark"
title = "Affine-line and weight conventions"
order = 3026
lean = ["AlgebraicGeometry.LAdicWeilSheaf.IsGeometricallyConstant", "AlgebraicGeometry.LAdicWeilSheaf.IsUnramifiedAtInfinity"]
tags = ["sketch"]
+++
Fix $k_0=\mathbf F_q$, its algebraic closure $k$, a prime $\ell\ne \operatorname{char}(k_0)$, and $\iota:\DLAQ\simeq\mathbf C$. Write
$A_0=\mathbf A^1_{k_0}$, $A=A_0\otimes k$, and use a prime to denote the
dual affine line. All cohomology is geometric, with geometric Frobenius.
A lisse Weil sheaf is *pure of weight $w$* if every eigenvalue
$\alpha$ at a closed point $x$ satisfies
$|\iota\alpha|=q_x^{w/2}$; replace equality by $\leq$ for an upper bound.
The twist $(-1)$ raises weights by two.

For a dense open $j:U_0\hookrightarrow A_0$, $j_*F$ denotes the
*ordinary* sheaf direct image. Its stalks at missing points are
inertia invariants; its curve perverse intermediate extension is
$j_{!*}(F[1])=(j_*F)[1]$. A lisse Weil sheaf $F$ on $U_0$ is *unramified at infinity* if it
extends to a lisse Weil sheaf on the open $U_0\cup\{\infty\}$ of
$\mathbf P^1_{k_0}$ (with $A_0\subset\mathbf P^1_{k_0}$ the standard chart);
equivalently, inertia
at $\infty\in\mathbf P^1_k$ acts trivially on the geometric generic fiber.
A Weil sheaf on $U_0$ is *geometrically constant* if its underlying étale
sheaf is constant on every connected open of $U=U_0\otimes k$; for $U$
connected this means that the geometric fundamental group acts
trivially, while its Frobenius module may be nontrivial.
