+++
id = "lem-sc-p1-monomial"
kind = "lemma"
title = "Cohomology of the twists on $\\mathbf P^1_k$"
lean = ["AlgebraicGeometry.ProjectiveLine.nonempty_H_zero_twist_equiv", "AlgebraicGeometry.ProjectiveLine.subsingleton_H_zero_twist_of_neg", "AlgebraicGeometry.ProjectiveLine.subsingleton_H_one_twist", "AlgebraicGeometry.ProjectiveLine.nonempty_H_one_twist_equiv_dual", "AlgebraicGeometry.ProjectiveSpace.nonempty_H_twist_top_linearEquiv_finsupp", "AlgebraicGeometry.ProjectiveLine.nonempty_relativeDifferentials_iso_twist"]
order = 641
uses = ["def-sc-kahler-differentials", "def-sc-p1-standard", "lem-pc-projective-space-canonical", "lem-sc-canonical-sheaf", "lem-sc-cech-spectral", "lem-sc-p1-twist-exists", "lem-sc-p1-twist-sections", "pqf-lem-affine-vanishing"]
+++
Let $k$ be a field. With the standard cover
and twists of [def-sc-p1-standard], for every $d\in\mathbf Z$:

1. **(i)** $H^0(\mathbf P^1_k,\mathcal O(d))$ is the space of
sections corresponding to the homogeneous polynomials of degree
$d$ in $k[x_0,x_1]$ (the monomial $x_0^ax_1^b$, $a+b=d$,
corresponding to the pair $(t^b,s^a)$), hence has dimension $d+1$
for $d\geq0$ and is zero for $d<0$;
1. **(ii)** $H^1(\mathbf P^1_k,\mathcal O(d))=0$ for $d\geq-1$;
for $d\leq-2$, $H^1(\mathbf P^1_k,\mathcal O(d))$ has the basis
$$
\bigl[t^{d+1}\bigr],\dots,\bigl[t^{-1}\bigr]
$$
of the classes of the monomials $t^j\in \Gamma(U_{01},\mathcal O(d))=k[t,t^{-1}]$, and has dimension
$-d-1$; in particular
$H^1(\mathbf P^1_k,\mathcal O(-2))\cong k$, with basis
$[t^{-1}]$;
1. **(iii)** $\omega_{\mathbf P^1}:=\Omega^1_{\mathbf P^1_k/k}$
([def-sc-kahler-differentials]) is a line bundle
([lem-sc-canonical-sheaf]), and
$\omega_{\mathbf P^1}\cong\mathcal O(-2)$: with the trivializations
$dt$ on $U_0$ and $ds$ on $U_1$ one has $ds=-s^{2}dt$,
equivalently $dt=-t^{2}ds$, and this transition function $-t^{2}$
is the transition function $t^{2}$ of $\mathcal O(-2)$ up to the
unit $-1$.
