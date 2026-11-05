+++
id = "proposition-dctf-x-qbar-2-colimit--1"
kind = "proposition"
title = "The coefficient cocone"
order = 648002
aliases = ["bp-r198-1"]
lean = ["AlgebraicGeometry.ProEtale.constructibleCocone"]
uses = ["definition-small-pro-etale-site", "definition-constructible-sheaves", "definition-sp-scalar-extension"]
+++
Let $\ell$ be a prime and $X$ a scheme. In this and the following two
details, $\Dbc(X,\Lambda)$ denotes the full subcategory of
$D(X_{\mathrm{pro}\acute{e}t},\Lambda_X)$ consisting of bounded complexes
whose cohomology sheaves are pro-étale locally finitely presented on the
strata of a finite stratification. Here $E_X$ is the pullback of the
condensed ring associated to the topological field $E$, and
$\overline{\mathbf Q}_{\ell,X}$ is the pullback of the filtered colimit
of these condensed rings over the finite subextensions
$E\subset\overline{\mathbf Q}_\ell$. No finite Tor amplitude condition
is imposed in these categories.

The extensions of scalars

$$
T_{E,F}=F_X\otimes^{\mathbf L}_{E_X}-:\Dbc(X,E)\longrightarrow\Dbc(X,F)
\qquad(E\subset F)
$$

and

$$
\Phi_E=\overline{\mathbf Q}_{\ell,X}\otimes^{\mathbf L}_{E_X}-:
\Dbc(X,E)\longrightarrow\Dbc(X,\overline{\mathbf Q}_\ell)
$$

form a cocone of ordinary categories, with structure isomorphisms
$\Phi_F\circ T_{E,F}\simeq\Phi_E$.
