+++
id = "proposition-isomorphisms-reduce-finite-coefficients--2"
kind = "proposition"
title = "Integral reduction detects isomorphisms"
order = 653004
aliases = ["bp-r199-2"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isIso_of_isIso_etaleReduction_map"]
uses = ["definition-small-pro-etale-site", "definition-constructible-sheaves", "proposition-comparison-morphism-inverse-image"]
+++
Let $\ell$ be a prime, let $k$ be a field, and let $X$ be a separated scheme of finite type over $k$. Let $E\subset\overline{\mathbf Q}_\ell$ be a finite extension of $\mathbf Q_\ell$, and let $n\geq 1$. Write $A=\mathcal O_E/\ell^n$ and let
$$
\rho_n:\Dbc(X,\mathcal O_E)\longrightarrow D(X_{\acute{e}t},A),
\qquad K\longmapsto R\nu_{X,*}(K\otimes^{\mathbf L}_{\mathcal O_E}A)
$$
be reduction followed by the finite-coefficient comparison with the étale site. Here $\Dbc(X,\mathcal O_E)$ is realized as bounded constructible complexes of modules over the condensed coefficient sheaf on $X_{\mathrm{pro}\acute{e}t}$.

If $\varphi:K\to L$ is a morphism in $\Dbc(X,\mathcal O_E)$ and $\rho_n(\varphi)$ is an isomorphism, then $\varphi$ is an isomorphism. No separate finite Tor-amplitude hypothesis, or restriction on the characteristic of $k$, is required.
