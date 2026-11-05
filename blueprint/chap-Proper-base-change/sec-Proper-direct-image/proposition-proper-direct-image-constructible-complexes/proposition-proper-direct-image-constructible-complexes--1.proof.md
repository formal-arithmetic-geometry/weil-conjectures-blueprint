+++
kind = "proof"
of = "proposition-proper-direct-image-constructible-complexes--1"
order = 425003
uses = ["proposition-proper-direct-image-finite-coefficients", "theorem-bounded-below-cohomology-comparison"]
+++
Write $K\simeq\nu_X^*K_0$ with $K_0$ bounded constructible on the étale site.
The étale proper finiteness theorem over the Noetherian $k$-scheme $Y$ gives
$Rp_*K_0\in\Dbc(Y_{\acute{e}t},A)$, the bounded-constructibility part of
[proposition-proper-direct-image-finite-coefficients]. Since $p$ is quasi-compact
and quasi-separated, the bounded-below comparison
[theorem-bounded-below-cohomology-comparison] identifies
$Rp_*\nu_X^*K_0$ with $\nu_Y^*Rp_*K_0$. This gives the required étale-origin
witness on $Y$. In Lean this is
`AlgebraicGeometry.ProEtale.boundedConstructible_rightDerivedLowerStar_of_etale`.
