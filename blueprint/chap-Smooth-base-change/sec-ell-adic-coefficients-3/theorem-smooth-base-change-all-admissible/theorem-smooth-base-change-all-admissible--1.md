+++
id = "theorem-smooth-base-change-all-admissible--1"
kind = "theorem"
title = "Finite coefficients"
order = 700002
aliases = ["bp-r210-1"]
lean = ["AlgebraicGeometry.ProEtale.isIso_derivedBaseChangeMap_app_of_smooth"]
uses = ["definition-small-pro-etale-site", "definition-constructible-sheaves", "definition-pro-etale-base-change-map", "proposition-comparison-morphism-inverse-image"]
+++
For the finite-coefficient step we use the following more general statement.
In the cartesian square (8.1), let $g$ be smooth and $f$ quasi-compact and
quasi-separated. Let $A$ be a discrete commutative ring killed by a positive
integer $N$ whose image in $\Gamma(Y,\mathcal O_Y)$ is a unit. Suppose that
$K\in D(X_{\mathrm{pro}\acute{e}t},A)$ is of bounded constructible étale
origin: there is a $K_{\acute{e}t}\in D^b_c(X_{\acute{e}t},A)$ and an
isomorphism $\nu_X^*K_{\acute{e}t}\simeq K$. Then the map (4.5)

$$
g^*_{A}Rf_{*,A}K\longrightarrow Rf'_{*,A}g'^*_{A}K
$$

is an isomorphism. No finite Tor amplitude or finite-type hypothesis over
$k$ is required in this statement.
