+++
id = "det-pe-finite-tor-comparison-noetherian"
kind = "lemma"
title = "Tor amplitude under comparison for Noetherian coefficients"
lean = ["DerivedCategory.torAmplitudeIn_mapDerivedCategory_obj_iff", "AlgebraicGeometry.ProEtale.preservesFlat_comparisonUpperStar", "AlgebraicGeometry.ProEtale.bijective_comparisonUpperStar_mapDerivedCategory_map"]
order = 1273
uses = ["lem-exc-constant-inverse-image-flat", "lem-exc-comparison-tor-interval", "lem-sf-proetale-constructible-origin", "def-weil-finite-tor-amplitude"]
+++
Let $X$ be quasi-compact and quasi-separated, $\Lambda$ a discrete Noetherian
ring and $K\in D^b_c(X_{\Et},\Lambda)$. For integers $a\leq b$, $K$ has Tor
amplitude in $[a,b]$ (that is, $K\otimes^{\mathrm L}_\Lambda N$ has cohomology
only in degrees $[a,b]$ for every $\Lambda$-module sheaf $N$ on $X_{\Et}$) if and
only if $\nu_X^*K$ has Tor amplitude in $[a,b]$ on $X_{\Proet}$. Consequently,
the equivalence $\nu_X^*\colon D^b_c(X_{\Et},\Lambda)\simeq\Dbc(X,\Lambda)$ of
[lem-sf-proetale-constructible-origin] restricts to an
equivalence $D^b_{\mathrm{ctf}}(X_{\Et},\Lambda)\simeq\Dctf(X,\Lambda)$.
