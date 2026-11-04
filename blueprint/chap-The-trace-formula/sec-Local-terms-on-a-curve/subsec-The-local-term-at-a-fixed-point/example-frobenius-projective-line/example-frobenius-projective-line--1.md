+++
id = "example-frobenius-projective-line--1"
kind = "example"
title = "Frobenius on the projective line (1)"
name_showing = false
order = 996001
aliases = ["bp-r304-1"]
+++
Let $X=\mathbf P^1_k$, $K=A_X$, and let $\psi$ be the constant Frobenius
correspondence, so that $\psi_m$ is the identity on every stalk. Both sides of
the Lefschetz–Verdier formula for the graph $c_m$ can be computed explicitly. The
fixed points of $\Phi_X^m$ are the $q^m+1$ points of
$\mathbf P^1(\mathbf F_{q^m})$. By the proposition each has local term
$\operatorname{tr}_A(1\mid A)=1$, so the local side is $q^m+1$. On the global
side, $R\Gamma(\mathbf P^1,A)=A\oplus A(-1)[-2]$. By
Lemma [lemma-scheme-frobenius-geometric-frobenius] the operator
$T_{c_m}(\psi_m)$ is the $m$-th power of geometric Frobenius. It acts by $1$
on $H^0$ and by $q^m$ on $H^2=A(-1)$, and both degrees are even, so its trace
is $1+q^m$ with no signs. Compare the identity correspondence at the start
of Section [sec-Trace-classes-and-local-terms]. There the fixed locus is all of $\mathbf P^1$
and the answer $2$ is a self-intersection. Here the fixed locus is finite
and each point counts once.
