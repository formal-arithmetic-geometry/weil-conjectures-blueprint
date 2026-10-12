+++
id = "def-sfb-bounded-constructible-extend-scalars"
kind = "definition"
title = "Extension of scalars on bounded constructible complexes"
order = 1645
uses = ["lem-sfb-extend-scalars-bounded-constructible"]
lean = ["AlgebraicGeometry.ProEtale.boundedConstructibleExtendScalars", "AlgebraicGeometry.ProEtale.boundedConstructibleExtendScalarsCompatibility"]
+++
For a scheme $X$, the functor
$$
E\otimes^{\mathrm L}_{\cO_E}-\colon D_{\mathrm{cons}}(X_{\mathrm{proét}},\cO_E)\to D_{\mathrm{cons}}(X_{\mathrm{proét}},E)
$$
is the restriction of $L(\operatorname{Ext}_\varphi)$ to the full subcategories of bounded
constructible complexes [lem-sfb-extend-scalars-bounded-constructible]. Composing it with
the inclusion of $D_{\mathrm{cons}}(X_{\mathrm{proét}},E)$ into $D(\Mod_{E_X})$ gives,
up to a canonical isomorphism, the inclusion of
$D_{\mathrm{cons}}(X_{\mathrm{proét}},\cO_E)$ followed by $L(\operatorname{Ext}_\varphi)$.
