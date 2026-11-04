+++
id = "prose-B-12"
kind = "hidden"
title = "Tate modules (1)"
order = 1507
+++
Fix a prime $\ell$ invertible in $k$. With this prime, compatible systems of
$\ell$-power torsion points of $A$ form the Tate module $T_\ell A$, a
$\mathbf Z_\ell$-module with an action of $\operatorname{Gal}(\bar k/k)$. For example, for a
complex torus $\mathbf C^g/\Lambda$ it is $\Lambda\otimes\mathbf Z_\ell$, the first
homology with $\ell$-adic coefficients. In general,
Proposition [proposition-integral-tate-module] shows that $T_\ell A$
is free of rank $2g$ over $\mathbf Z_\ell$. The input is the orders of the groups
$A[\ell^n](\bar k)$, which are known from
Proposition [proposition-multiplication-n], and these orders force each of
these groups to be free over $\mathbf Z/\ell^n$ of rank $2g$. Moreover, the
transition maps are surjective because $A(\bar k)$ is divisible.

Although Frobenius can have many fixed points on the finite levels, no
power of it has a nonzero fixed vector in the Tate module
(Proposition [proposition-no-frobenius-fixed-vector]). For example, for the elliptic curve $E_0:y^2=x^3-x$ over $\mathbf F_3$, the three roots
of $x^3-x$ lie in $\mathbf F_3$. So all of $E[2]$ is rational, and
Frobenius acts trivially on it. On $T_2E$, however, a fixed vector would
be an unbounded compatible system of $2$-power torsion points in the
finite group $E_0(\mathbf F_{3^m})$. For the Jacobian of a curve, Proposition [proposition-no-fixed-class-degree-one] turns this into
the statement that Frobenius has no fixed class in $H^1$ of the curve.
