+++
id = "thm-sc-proper-cohomology"
kind = "theorem"
title = "Kummer computation on a proper curve"
order = 4537
lean = ["AlgebraicGeometry.Curve.etaleCohomology_constant_of_isProper"]
uses = ["lem-sc-pic-proper-ntorsion", "lem-sc-cohomological-dimension"]
+++
Let $k$ be algebraically closed, let $C$ be a smooth proper curve of genus
$g$ over $k$, and let $n\geq1$ be prime to $\operatorname{char}k$. Then,
under the canonical trivialization $\theta_\zeta$ for a primitive root
$\zeta$, the constant sheaf $\mathbf F_n$ satisfies
$$
H^0(C_{\Et},\mathbf F_n)\cong\mathbf Z/n\mathbf Z,\qquad
H^1(C_{\Et},\mathbf F_n)\cong(\mathbf Z/n\mathbf Z)^{2g},\qquad
H^2(C_{\Et},\mathbf F_n)\cong\mathbf Z/n\mathbf Z,
$$
and $H^q(C_{\Et},\mathbf F_n)=0$ for $q>2$.

## Proof

Use $\theta_\zeta$ to replace $\mathbf F_n$ by $\mu_n$. By the Kummer long
exact sequence (the unit group of the proper connected curve is
$k^\times$, $n$-divisible since $k$ is algebraically closed, so the exact
sequence degenerates),
$$
H^1(C,\mu_n)=\operatorname{Pic}(C)[n],\quad
H^2(C,\mu_n)=\operatorname{coker}(n:\operatorname{Pic}(C)\to\operatorname{Pic}(C)),
$$
which by [lem-sc-pic-proper-ntorsion] are $(\mathbf Z/n\mathbf Z)^{2g}$ and
$\mathbf Z/n\mathbf Z$; and $H^0(C,\mu_n)=\mu_n(k)=\mathbf Z/n\mathbf Z$.
The vanishing for $q>2$ is [lem-sc-cohomological-dimension].

Unresolved dependencies: def:sc-mu-trivialization, lem:sc-primitive-root, def:sc-curves, def:sc-kummer-sequence, lem:sc-kummer-les
