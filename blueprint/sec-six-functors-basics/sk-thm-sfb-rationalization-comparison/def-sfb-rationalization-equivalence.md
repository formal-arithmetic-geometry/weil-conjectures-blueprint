+++
id = "def-sfb-rationalization-equivalence"
kind = "definition"
title = "$D_{\\mathrm{cons}}(X,E)$ as the rationalization of $D_{\\mathrm{cons}}(X,\\mathcal O_E)$"
order = 1647
uses = ["thm-sfb-extend-scalars-localization", "sk-def-sfb-rationalization"]
lean = ["AlgebraicGeometry.ProEtale.rationalizationEquivalence", "AlgebraicGeometry.ProEtale.rationalizationQCompEquivalenceIso"]
+++
Let $X$ be a scheme whose underlying topological space is Noetherian. There is an
equivalence of categories
$$
D_{\mathrm{cons}}(X_{\mathrm{proét}},\cO_E)[\ell^{-1}]\simeq D_{\mathrm{cons}}(X_{\mathrm{proét}},E)
$$
from the rationalization at the powers of $\ell$ [sk-def-sfb-rationalization]. Composed
with the localization functor
$Q\colon D_{\mathrm{cons}}(X_{\mathrm{proét}},\cO_E)\to D_{\mathrm{cons}}(X_{\mathrm{proét}},\cO_E)[\ell^{-1}]$,
it is isomorphic to $E\otimes^{\mathrm L}_{\cO_E}-$.
