+++
id = "det-def-pic"
kind = "definition"
title = "Picard group, degree, $\\Pic^0$"
order = 1426
uses = ["def-sc-curves", "def-sc-divisor", "def-sc-picard-group"]
lean = ["AlgebraicGeometry.Scheme.CohomologicalPicardGroup", "AlgebraicGeometry.Scheme.picDegreeHom", "AlgebraicGeometry.Scheme.nonempty_equiv_H_one_and_surjective_picDegreeHom", "AlgebraicGeometry.Scheme.Pic.toCohomologicalPicardGroupAddEquiv", "AlgebraicGeometry.Scheme.exists_divisorClassGroup_addEquiv_pic"]
+++
For a scheme $X$ (for instance a curve as in [def-sc-curves]), the
*(cohomological) Picard group* is $\Pic(X)=H^1(X_{\Et},\mathbb G_m)$,
$\mathbb G_m$ being the sheaf of units of the structure sheaf on the
small étale site. For $C$ a smooth proper connected curve over an
algebraically closed field $k$ ([def-sc-curves]; in particular $C$ has
dimension $1$) there is a *degree* homomorphism
$\deg:\Pic(C)\to\Z$ and we set $\Pic^0(C)=\ker\deg$; for an abelian
group $A$ and $n\ge1$, $A[n]$, $n\cdot A$, $A/n\cdot A$ denote kernel,
image and cokernel of the multiplication-by-$n$ map.

The definition rests on two facts:

- **(P1)** *(Equivalence of the definitions of $\Pic$.)* The
étale cohomology group $H^1(C_{\Et},\mathbb G_m)$ is canonically
isomorphic to the group of isomorphism classes of invertible
$\mathcal O_C$-modules under $\otimes$ ([def-sc-picard-group]); equivalently, to
$H^1(C_{\mathrm{Zar}},\mathcal O_C^\times)$ and to the group of
divisors modulo principal divisors $\mathrm{Div}(C)/\mathrm{Princ}(C)$
([def-sc-divisor]) when $C$ is moreover integral and regular.
- **(P2)** *(Well-definedness of $\deg$.)* For $C$ a smooth
proper connected curve over the algebraically closed field $k$,
$\deg\big(\sum_pn_p[p]\big)=\sum_pn_p[\kappa(p):k]$
kills principal divisors, hence descends to a homomorphism
$\Pic(C)\to\Z$; it is surjective and independent of all choices.
