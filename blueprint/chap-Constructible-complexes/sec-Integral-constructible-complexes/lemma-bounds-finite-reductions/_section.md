+++
id = "lemma-bounds-finite-reductions"
kind = "lemma"
title = "Bounds for the finite reductions"
order = 228
lean = ["AlgebraicGeometry.ProEtale.integral_finite_levels"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "definition-derived-adic-completeness", "definition-constructible-sheaves", "lemma-proper-direct-image-unbounded-complexes"]
+++
Let $X$ be Noetherian and let $K\in D(X_{\mathrm{pro}\acute{e}t},\mathcal O_E)$ be
derived complete with $K_1\in\Dbc(X,\mathbf F_E)$. Choose $[a,b]$
containing the cohomology of $K_1$. Then every $K_n$ lies in
$\Dbc(X,\mathcal O_E/\pi_E^n)$ and has Tor amplitude in $[a,b]$, and
$K$ has cohomology only in $[a,b]$. If the cohomology sheaves of $K_1$
are locally constant on a stratum, then so are those of every $K_n$.
