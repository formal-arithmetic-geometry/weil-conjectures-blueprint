+++
id = "thm-sc-proper-cohomology"
kind = "theorem"
title = "Kummer computation on a proper curve"
lean = ["AlgebraicGeometry.IsConnectedCurve.sheafH_constantZMod_of_isProper"]
order = 1434
uses = ["def-sc-curves", "def-sc-kummer-sequence", "def-sc-mu-trivialization", "lem-sc-cohomological-dimension", "lem-sc-kummer-les", "lem-sc-pic-proper-ntorsion", "lem-sc-primitive-root"]
+++
Let $k$ be algebraically closed, let $C$ be a
smooth proper connected curve of genus $g$ over
$k$, and let $n\geq1$ be prime to $\operatorname{char}k$.
Then, under the canonical trivialization
$\theta_\zeta$ for a primitive root $\zeta$
([def-sc-mu-trivialization], existence by
[lem-sc-primitive-root]), the constant sheaf
$\mathbf F_n$ satisfies

$$
H^0(C_{\Et},\mathbf F_n)\cong\mathbf Z/n\mathbf Z,\qquad
H^1(C_{\Et},\mathbf F_n)\cong(\mathbf Z/n\mathbf Z)^{2g},\qquad
H^2(C_{\Et},\mathbf F_n)\cong\mathbf Z/n\mathbf Z,
$$

and $H^q(C_{\Et},\mathbf F_n)=0$ for $q>2$.
