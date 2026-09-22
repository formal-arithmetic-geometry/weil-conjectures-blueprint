+++
id = "def-amb-etale-compact-support"
kind = "definition"
title = "Compact supports on the ordinary étale category"
order = 5603
lean = ["AlgebraicGeometry.Etale.derivedPushforwardCompactSupport"]
uses = ["def-asd-compactifiable"]
+++
For a compactification $c=(j,r)$ of $f:X\to S$ between Noetherian schemes,
define the ordinary étale compact-support candidate by
$$
Rf_!^c=Rr_*j_!:D(X_{\mathrm{et}},A)\longrightarrow D(S_{\mathrm{et}},A).
$$
Here $j_!$ is the étale extension by zero, and $Rr_*$ is the ordinary
derived direct image.

For a proper refinement take the comparison which is the identity over $X$;
[lem-amb-etale-compact-comparisons] proves that these maps give a
compactification-independent functor, denoted $Rf_!$.

This definition concerns the étale category; it does not identify it with a
functor on the pro-étale category. The notation refers to ordinary derived
categories.

Unresolved dependencies: def:weil-compactifications-refinements, def:weil-pbc-extension-by-zero, def:weil-pbc-direct-image, def:weil-pbc-derived-categories
