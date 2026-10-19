+++
id = "d-real-boundary"
kind = "definition"
title = "Boundary extension and inertia"
lean = ["AlgebraicGeometry.BoundaryDatum.conj", "AlgebraicGeometry.BoundaryDatum.boundaryStalk_conj", "AlgebraicGeometry.BoundaryDatum.boundaryStalkConjEquiv"]
order = 2985
uses = ["d-real-setup", "def-real-weil-representation-operations", "def-wf-fundamental-representation", "def-wf-weil-group"]
+++
Let $j:U_0\hookrightarrow C_0$ be a nonempty open in a
curve in the sense of [d-real-setup], with finite complement $S_0$, and let
$\mathcal F$ be lisse Weil on $U_0$, with Weil fundamental representation
$\rho$ of [def-wf-fundamental-representation].
Write $J=j_*\mathcal F$ for the ordinary sheaf direct image of the underlying
lisse $\overline{\mathbf Q}_{\ell,U}$-module on the pro-étale sites, defined by
sections over the inverse image of a neighborhood (for finite coefficients, an
étale neighborhood); it is $\mathcal H^0(Rj_*\mathcal F)$.
For $s\in S_0$, let $K_s$ be the fraction field of the henselization of
$\mathcal O_{C_0,s}$, and put

$$
I_s=\ker\bigl(\Gal(\overline K_s/K_s)\to
\Gal(\overline{k(s)}/k(s))\bigr).
$$

Henselization is the universal local henselian extension with unchanged
residue field; a henselian ring lifts simple roots of monic polynomials.
Choose a geometric point over $\operatorname{Spec}K_s\to U_0$ and a path
from it to the base point of $\rho$; this gives a
decomposition-group homomorphism $\Gal(\overline K_s/K_s)\to\pi_1(U_0)$
carrying $I_s$ into $\pi_1(U)$ and the inverse image $W(K_s)$ of the
integer powers of geometric Frobenius of $k(s)$ into the Weil group
$W(U_0)$ of [def-wf-weil-group].
The local generic stalk $V_s$ is the space of $\rho$ with $W(K_s)$ acting through $\rho$.
Residue Frobenius lifts in $W(K_s)$ differ by elements of $I_s$, so they act
unambiguously on the invariants $V_s^{I_s}$ in the sense of
[def-real-weil-representation-operations].
Another choice of path changes the homomorphism by conjugation, and
$V_s^{I_s}$ with its residue Frobenius action is independent of the choice up to Frobenius-equivariant isomorphism.
