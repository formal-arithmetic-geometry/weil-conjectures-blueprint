+++
id = "theorem-smooth-base-change-all-admissible--1"
kind = "theorem"
title = "Finite coefficients"
order = 701002
aliases = ["bp-r210-1"]
lean = ["AlgebraicGeometry.ProEtale.isIso_derivedBaseChangeMap_app_of_smooth"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "proposition-comparison-morphism-inverse-image--2", "definition-pro-etale-base-change-map--1"]
+++
For the finite-coefficient step we use the following more general
statement. In the cartesian square (8.1), let $g$ be
smooth and $f$ quasi-compact and quasi-separated. Let $A$ be a discrete
commutative ring killed by a positive integer $N$ whose image in
$\Gamma(Y,\mathcal O_Y)$ is a unit. Suppose that
$K\in D(X_{\mathrm{pro}\acute{e}t},A)$ is of bounded constructible étale origin: there
are a $K_{\acute{e}t}\in\Dbc(X_{\acute{e}t},A)$ and an isomorphism
$\nu_X^*K_{\acute{e}t}\simeq K$. Then the map (4.5)

$$
g^*_{A}Rf_{*,A}K\longrightarrow Rf'_{*,A}g'^*_{A}K
\tag{8.2}
$$

is an isomorphism. No finite Tor amplitude or finite-type hypothesis over
$k$ is required in this statement. In particular, under the hypotheses of
the theorem, (8.2) is an isomorphism for every
$K\in D^b_{\mathrm{ctf}}(X_{\mathrm{pro}\acute{e}t},A)$ when $A$ is a finite ring killed by a power of
$\ell$.
