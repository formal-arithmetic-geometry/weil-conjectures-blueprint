+++
id = "proposition-p-torsion-smooth-proper-curve--4"
kind = "proposition"
title = "$p$-torsion on a smooth proper curve in characteristic $p$ (4)"
name_showing = false
order = 1584004
aliases = ["bp-r494-4"]
lean = ["AlgebraicGeometry.IsCurve.finite_sheafH_constantModSheaf_of_isProper", "AlgebraicGeometry.IsCurve.bijective_cohomologyMap_constantModSheaf_of_isProper"]
uses = []
+++
Let $C$ be smooth, proper and connected over an algebraically closed
field $k$, of finite type and dimension at most one. Let $\Lambda$ be
a commutative ring, let $r$ be a prime, and write $A$ for the constant
sheaf $\Lambda/r\Lambda$ on $C_{\acute{e}t}$. Cohomology is taken with
values in the underlying abelian sheaf.

If $\Lambda/r\Lambda$ is finite, then $H^q(C,A)$ is finite for every
$q\geq0$. For every algebraically closed extension $k\subset k'$ and
every base change $\iota:C'\to C$, the pullback map

$$
H^q(C,A)\longrightarrow H^q(C',\iota^*A)
$$

is an isomorphism for every $q\geq0$; this assertion does not require
$\Lambda/r\Lambda$ to be finite. In particular, taking
$r=p=\operatorname{char}k$ and $\Lambda=\mathbf F_p$ gives finiteness
and invariance under algebraically closed extension for
$H^1(C,\mathbf F_p)$.
