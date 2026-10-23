+++
id = "prop-pod-degree-of-the-pairing"
kind = "theorem"
title = "Degree of the pairing"
lean = ["AlgebraicGeometry.Etale.TateOrientation.degreeZeroPairing", "AlgebraicGeometry.Etale.TateOrientation.degreewisePairing", "AlgebraicGeometry.Etale.TateOrientation.degreewisePairing_apply", "AlgebraicGeometry.Etale.TateOrientation.untwistedDegreewisePairing", "AlgebraicGeometry.Etale.TateOrientation.degreewisePoincarePairing", "AlgebraicGeometry.Etale.TateOrientation.untwistedPoincarePairing", "AlgebraicGeometry.Etale.TateOrientation.untwistedDegreewisePoincarePairing"]
order = 3421
tags = ["latex:proposition"]
uses = ["def-coefficient-twists-detailed", "def-pod-derived-poincare-pairing"]
+++
In the Poincare duality conventions of this chapter (the fixed setting), let $\Lambda\in\{A,\mathcal O_E,E,\overline{\mathbf Q}_{\ell}\}$ and let $K\in D^b_{ctf}(X,\Lambda)$ be perfect over $\Lambda_X$. The shift convention $H^r(C[m])=H^{r+m}(C)$ identifies the degree-zero part of the derived pairing $\beta _K$ of [def-pod-derived-poincare-pairing] with the pairings

$$
\langle -,-\rangle _i:\   H_c^i(X,K)\times H^{2d-i}\bigl(X,K^\vee (d)\bigr) \longrightarrow \Lambda \qquad (i\in \mathbf Z).
$$

Before inserting the Tate twist, the same morphism is the line-valued pairing

$$
H_c^i(X,K)\times H^{2d-i}(X,K^\vee ) \longrightarrow \Lambda(-d),
$$

obtained by eliminating the invertible twist $\Lambda _X(d)$ of the second factor through the canonical isomorphism $H^{2d-i}(X,K^\vee (d))\cong H^{2d-i}(X,K^\vee )\otimes _\Lambda \Lambda (d)$ and using the twist inverse.
