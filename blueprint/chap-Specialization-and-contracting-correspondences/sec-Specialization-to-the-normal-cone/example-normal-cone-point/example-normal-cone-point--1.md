+++
id = "example-normal-cone-point--1"
kind = "example"
title = "Normal cones of a point (1)"
name_showing = false
order = 1630001
aliases = ["bp-r504-1"]
lean = ["IsLocalRing.exists_mvPolynomial_residueField_ringEquiv_associatedGraded", "MvPolynomial.nonempty_cusp_ringEquiv_associatedGraded", "Polynomial.associatedGradedPieceEquivXPow"]
+++
If $X$ is smooth at a point $Z=\{y\}$, then
$\bigoplus_rI^r/I^{r+1}$ is the symmetric algebra of $I/I^2$ and
$N_ZX$ is the tangent space at $y$. At a singular point the normal cone
is the tangent cone, and it need not be reduced. For the cusp
$X=V(y^2-x^3)\subset\mathbf A^2$ and $Z$ the origin, with $I=(x,y)$, the
graded algebra is $k[\xi,\eta]/(\eta^2)$, where $\xi,\eta$ are the
classes of $x,y$ in $I/I^2$ and $\eta^2$ is the lowest-degree part of
$y^2-x^3$; so $N_ZX$ is a double line. For a nonreduced point
$Z=V(x^m)\subset\mathbf A^1$, each $I^r/I^{r+1}=(x^{mr})/(x^{m(r+1)})$ is
free of rank one over $\mathcal O_Z=k[x]/(x^m)$, and
$N_ZX=Z\times\mathbf A^1$ is a line thickened along $Z$; this is the case
treated in Lemma [lemma-case-z-v-x-m].
