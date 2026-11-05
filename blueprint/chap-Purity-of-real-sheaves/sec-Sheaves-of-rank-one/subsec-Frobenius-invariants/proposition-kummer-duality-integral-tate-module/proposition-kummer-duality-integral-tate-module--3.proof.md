+++
kind = "proof"
of = "proposition-kummer-duality-integral-tate-module--3"
order = 1094006
uses = ["proposition-kummer-duality-integral-tate-module--1", "corollary-degree-jacobian", "proposition-smooth-proper-curves-torsion-prime"]
+++
Pullback along $f$ commutes with the Kummer maps, both from
$H^1(X,\mu_m)$ to $\operatorname{Pic}(X)[m]$ and from
$\operatorname{Pic}(X)$ to $H^2(X,\mu_m)$. The latter map is
surjective. Since degree is unchanged by an automorphism lying over
an automorphism of the ground field, the trace is unchanged by
pullback along $f$.

The morphism $h$ gives the corresponding naturality square for the
torsor extensions defining cup product. Apply trace invariance to
$t'\mathbin{\cup}K_m^{-1}(y)$, use this square, and then use the
compatibility of $K_m$ with pullback. The result is
$P_{t'}(y)=P_t(f^*y)$, as in
`AlgebraicGeometry.Scheme.EtaleTorsor.picPairing_transport`.
