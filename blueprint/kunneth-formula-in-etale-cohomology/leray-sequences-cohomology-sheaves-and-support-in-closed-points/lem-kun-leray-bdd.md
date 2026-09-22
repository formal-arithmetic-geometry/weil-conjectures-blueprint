+++
id = "lem-kun-leray-bdd"
kind = "lemma"
title = "Leray: composition of derived functors"
order = 6057
lean = ["AlgebraicGeometry.Etale.RGamma_comp_derivedPushforward"]
uses = ["def-kun-rgamma-unbounded", "lem-kun-rgamma-unbounded-well-defined", "lem-kun-rgamma-unbounded-bounded"]
+++
For a morphism of schemes $f:X\to Y$ and $E\in\Dplus(X_{\Et})$ there is a
canonical isomorphism
$$
R\Gamma(X_{\Et},E)\cong R\Gamma\bigl(Y_{\Et},Rf_*E\bigr)
$$
in $\Dplus(\mathbf Z)$, compatible with the functorialities (this is the
composition of the derived functors of
$\Gamma(X_{\Et},-)=\Gamma(Y_{\Et},-)\circ f_*$).

## Proof

Choose a K-injective resolution $E\to I$. Then $Rf_*E=f_*I$, and
$$
R\Gamma(X_{\Et},E)=\Gamma(X_{\Et},I)=\Gamma(Y_{\Et},f_*I),
$$
while $R\Gamma(Y_{\Et},Rf_*E)=\Gamma(Y_{\Et},J)$ for any K-injective model
$J$ of $f_*I$; these objects are independent of the chosen K-injective
models by [lem-kun-rgamma-unbounded-well-defined], and for the
bounded-below object $E$ they agree with the ambient derived global sections
by [lem-kun-rgamma-unbounded-bounded].

Both $\Gamma(Y_{\Et},f_*I)$ and $\Gamma(Y_{\Et},J)$ compute the derived
functors of the composite
$\Gamma(Y_{\Et},-)\circ f_*=\Gamma(X_{\Et},-)$: this is the Grothendieck
spectral sequence applied to the composite, whose $E_2$-page involves
$R^qf_*$ and the higher direct images of $\Gamma(Y_{\Et},-)$, and which
computes the right derived functors of the composite functor. Hence the
comparison $\Gamma(Y_{\Et},f_*I)\to\Gamma(Y_{\Et},J)$ is a
quasi-isomorphism, and the canonical map
$R\Gamma(X_{\Et},E)\to R\Gamma(Y_{\Et},Rf_*E)$ is an isomorphism, natural in
$E$ and compatible with the functorialities.

Unresolved dependencies: def:weil-pbc-direct-image, def:weil-pbc-derived-categories, def:weil-pbc-etale-cohomology, lem:weil-pbc-grothendieck-spectral-sequence, prop:weil-pbc-kinjective-resolutions-exist
