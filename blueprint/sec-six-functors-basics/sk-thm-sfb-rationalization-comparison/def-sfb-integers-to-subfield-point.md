+++
id = "def-sfb-integers-to-subfield-point"
kind = "definition"
title = "The inclusion of condensed rings $\\underline{\\mathcal O}_E\\to\\underline E$"
order = 1591
uses = ["sk-def-sfb-condensed-ring", "sk-def-sfb-ring-object"]
lean = ["AlgebraicGeometry.ProEtale.padicIntegersRingObjToContinuousMapRingObj"]
+++
Let $\ell$ be a prime and $E\subseteq\Qlb$ a finite extension of $\mathbf Q_\ell$. The
inclusion $\cO_E\hookrightarrow E$ is a continuous ring map, so it induces a morphism of
condensed rings $\underline{\cO}_E\to\underline E$, $f\mapsto f$ on
$C(S,\cO_E)\to C(S,E)$ [sk-def-sfb-condensed-ring]. Its underlying morphism of condensed
abelian groups is a morphism of ring objects of $\Sh(*_{\mathrm{proét}},\Ab)$
[sk-def-sfb-ring-object].
