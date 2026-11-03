+++
id = "prose-D-04"
kind = "hidden"
title = "Affine curves, torsion prime to the characteristic"
order = 916
+++
Every smooth connected curve over an algebraically closed field that
is not proper is affine and is the complement of a finite nonempty set
of closed points in a smooth proper connected curve. To see this,
take a projective model of its function field and normalize it, and
recall that regular curves over a perfect field are smooth.

On the affine curve $U=\overline C\setminus D$ the Picard group is a
quotient of $\operatorname{Pic}^0(\overline C)$, hence divisible, so
$H^2(U,\mu_n)=0$; topologically, a punctured Riemann surface is homotopy
equivalent to a graph. In degree one, new torsors appear: a Kummer
torsor on $U$ need not extend over $\overline C$, and the obstruction at
each puncture is its residue, the order modulo $n$ of the corresponding
rational section. For $\mathbf G_m=\mathbf P^1\setminus\{0,\infty\}$ the
torsor $y^n=x$ has residues $1$ and $-1$ at the two punctures, and it
generates $H^1(\mathbf G_m,\mu_n)\simeq\mathbf Z/n$. In general the
residues sum to zero, and the residue sequence of
Proposition [sk-prop-curve-affine-kummer] shows that $H^1(U,\mu_n)$ is free
of rank $2g+\#D-1$ over $\mathbf Z/n$, matching the first Betti number of
a surface of genus $g$ with $\#D$ punctures.
