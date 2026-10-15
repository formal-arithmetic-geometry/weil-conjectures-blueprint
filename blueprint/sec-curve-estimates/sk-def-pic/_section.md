+++
id = "sk-def-pic"
kind = "definition"
title = "Picard group, degree, $\\Pic^0$"
order = 981
uses = ["sk-def-av-pic", "sk-def-curve", "sk-prop-hilbert90"]
lean = ["AlgebraicGeometry.Scheme.CohomologicalPicardGroup"]
tags = ["sketch"]
+++
For a scheme $X$ (for instance $C$ as in [sk-def-curve]), the
*(cohomological) Picard group* is $\Pic(X)=H^1(X_{\Et},\mathbb G_m)$,
$\mathbb G_m$ being the sheaf of units of the structure sheaf on the
small étale site. For $C$
smooth proper connected (in particular of dimension $1$,
[sk-def-curve]) there is a *degree* homomorphism
$\deg:\Pic(C)\to\Z$ and we set $\Pic^0(C)=\ker\deg$; for a group
$f$ and $n\ge1$, $f[n]$, $n\cdot f$, $f/n\cdot f$ denote kernel,
image and cokernel of the multiplication-by-$n$ map.

Two facts are asserted in the above:

- **(P1)** *(Equivalence of the definitions of $\Pic$.)* The
étale cohomology group $H^1(C_{\Et},\mathbb G_m)$ is canonically
isomorphic to the group of isomorphism classes of invertible
$\mathcal O_C$-modules under $\otimes$; equivalently, to
$H^1(C_{\mathrm{Zar}},\mathcal O_C^\times)$ and to the group of
divisors modulo principal divisors $\mathrm{Div}(C)/\mathrm{Princ}(C)$
when $C$ is moreover integral and regular.
- **(P2)** *(Well-definedness of $\deg$.)* For $C$ smooth
proper connected of dimension $1$,
$\deg\big(\sum_pn_p[p]\big)=\sum_pn_p[\kappa(p):k]$
kills principal divisors, hence descends to a homomorphism
$\Pic(C)\to\Z$; it is surjective and independent of all choices.
