+++
id = "def-weil-pbc-property"
kind = "definition"
title = "Proper base-change property"
order = 1304
lean = ["AlgebraicGeometry.Etale.IsBaseChangeIso"]
uses = ["def-weil-pbc-cartesian-square", "def-weil-pbc-derived-exchange", "def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions"]
+++
Let $\mathcal A$ be a Grothendieck abelian category for which $\mathcal A$-valued
sheaves on small étale sites admit sheafification. For a morphism of schemes
$f:X\to Y$, write $\mathrm{PBC}_{\mathcal A}(f)$ if, for every morphism
$g:Y'\to Y$ and every associated cartesian square
[def-weil-pbc-cartesian-square] $\square$, the derived exchange morphism
[def-weil-pbc-derived-exchange]

$$
 \Ex_{\square}:g^{-1}Rf_*\longrightarrow Rf'_*g'^{-1}
$$

is an isomorphism of functors $\Dplus(X_{\Et},\mathcal A)\to
\Dplus(Y'_{\Et},\mathcal A)$, i.e. $\Ex_{\square,K}$ is an isomorphism for
every $K\in\Dplus(X_{\Et},\mathcal A)$. The assertion concerns the specified
map of [def-weil-pbc-derived-exchange], not an unnamed isomorphism.
