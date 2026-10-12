+++
id = "def-sfb-padic-int-condensed-ring"
kind = "definition"
title = "The condensed ring $\\underline{\\mathbf Z}_\\ell$"
order = 1521
uses = ["def-sfb-continuous-map-condensed-ring"]
lean = ["Profinite.padicIntCondensedRing"]
+++
For a prime $\ell$, the condensed ring $\underline{\mathbf Z}_\ell$ is the condensed ring
$\underline T$ of [def-sfb-continuous-map-condensed-ring] for $T=\mathbf Z_\ell$ with the
$\ell$-adic topology:

$$
\underline{\mathbf Z}_\ell(S)=C(S,\mathbf Z_\ell).
$$

Its underlying ring object of $\Sh(*_{\mathrm{proét}},\Ab)$ is commutative.
