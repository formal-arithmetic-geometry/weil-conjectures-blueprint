+++
id = "prose-D-04"
kind = "hidden"
title = "Affine curves (1)"
order = 1583
+++
Every smooth connected curve over an algebraically closed field that
is not proper is affine and is the complement of a finite nonempty set
of closed points in a smooth proper connected curve.  To see this,
take a projective model of its function field and normalize it, and
recall that regular curves over a perfect field are smooth.

On the affine curve $U=\overline C\setminus D$ the Picard group is a
quotient of $\operatorname{Pic}^0(\overline C)$. It is therefore divisible,
and $H^2(U,\mu_n)=0$; this matches the fact that, topologically, a punctured Riemann surface is
homotopy equivalent to a graph. In degree one, on the other hand, new torsors appear, since a
Kummer torsor on $U$ need not extend over $\overline C$. The obstruction to extending it
at each puncture is the residue of the torsor, that is, the order modulo
$n$ of the corresponding rational section. For example, on
$\mathbf G_m=\mathbf P^1\setminus\{0,\infty\}$ the torsor $y^n=x$ has
residues $1$ and $-1$ at the two punctures. It generates
$H^1(\mathbf G_m,\mu_n)\simeq\mathbf Z/n$. In general the residues sum
to zero. The residue sequence of
Proposition [proposition-cohomology-smooth-affine-curve] shows that
$H^1(U,\mu_n)$ is free of rank $2g+\#D-1$ over $\mathbf Z/n$. This is the
first Betti number of a surface of genus $g$ with $\#D$ punctures.
