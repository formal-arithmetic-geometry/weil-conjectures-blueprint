+++
id = "def-sfb-padic-condensed-ring"
kind = "definition"
title = "The condensed ring $\\underline{\\mathbf Q}_\\ell$"
order = 1526
uses = ["def-sfb-continuous-map-condensed-ring", "def-sfb-continuous-map-condensed-ring-map", "def-sfb-padic-int-condensed-ring"]
lean = ["Profinite.padicCondensedRing"]
+++
For a prime $\ell$, the condensed ring $\underline{\mathbf Q}_\ell$ is the condensed ring
$\underline T$ of [def-sfb-continuous-map-condensed-ring] for $T=\mathbf Q_\ell$ with the
$\ell$-adic topology:

$$
\underline{\mathbf Q}_\ell(S)=C(S,\mathbf Q_\ell).
$$

Its underlying ring object is commutative. Postcomposition with the inclusion
$\mathbf Z_\ell\subseteq\mathbf Q_\ell$ ([def-sfb-continuous-map-condensed-ring-map]) gives
the inclusion $\underline{\mathbf Z}_\ell\to\underline{\mathbf Q}_\ell$
([def-sfb-padic-int-condensed-ring]), a morphism of condensed rings.
