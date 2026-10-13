+++
id = "lem-kun-leray-bdd"
kind = "lemma"
title = "Leray: composition of derived functors"
order = 2042
uses = ["def-kun-rgamma-unbounded", "def-weil-pbc-derived-categories", "def-weil-pbc-direct-image", "def-weil-pbc-etale-cohomology", "lem-kun-rgamma-unbounded-bounded", "lem-kun-rgamma-unbounded-well-defined", "lem-weil-pbc-grothendieck-spectral-sequence", "prop-weil-pbc-kinjective-resolutions-exist"]
+++
For a morphism of schemes $f:X\to Y$ and
$E\in\Dplus(X_{\Et})$ there is a canonical isomorphism

$$
\RGamma(X_{\Et},E)\cong\RGamma\bigl(Y_{\Et},Rf_*E\bigr)
$$

in $\Dplus(\mathbf Z)$, compatible with the functorialities (this is
the composition of the derived functors of
$\Gamma(X_{\Et},-)=\Gamma(Y_{\Et},-)\circ f_*$).
