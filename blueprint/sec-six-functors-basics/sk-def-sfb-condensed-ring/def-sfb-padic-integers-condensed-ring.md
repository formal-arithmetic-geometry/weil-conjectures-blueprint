+++
id = "def-sfb-padic-integers-condensed-ring"
kind = "definition"
title = "The condensed ring $\\underline{\\mathcal O}_E$"
order = 1524
uses = ["def-sfb-continuous-map-condensed-ring", "def-sfb-continuous-map-condensed-ring-map", "def-sfb-padic-int-condensed-ring", "def-sfb-padic-subfield-condensed-ring"]
lean = ["Profinite.padicIntegersCondensedRing"]
+++
Let $E$ be a field with an embedding $E\hookrightarrow\Qlb$, topologized as in
[def-sfb-padic-subfield-condensed-ring]. Let $\cO_E=\{x\in E:|x|_E\le1\}$ be its ring of
integers, the valuation subring of the restricted absolute value, with the subspace
topology. The condensed ring $\underline{\cO}_E$ is the condensed ring of
[def-sfb-continuous-map-condensed-ring] for $\cO_E$:

$$
\underline{\cO}_E(S)=C(S,\cO_E).
$$

Its underlying ring object is commutative. Postcomposition with continuous inclusions
([def-sfb-continuous-map-condensed-ring-map]) gives the morphism of condensed rings
$\underline{\cO}_E\to\underline E$ ([def-sfb-padic-subfield-condensed-ring]). When $E$ is
an extension of $\mathbf Q_\ell$ with $\mathbf Q_\ell$-linear embedding, it also gives
$\underline{\mathbf Z}_\ell\to\underline{\cO}_E$ ([def-sfb-padic-int-condensed-ring]).
