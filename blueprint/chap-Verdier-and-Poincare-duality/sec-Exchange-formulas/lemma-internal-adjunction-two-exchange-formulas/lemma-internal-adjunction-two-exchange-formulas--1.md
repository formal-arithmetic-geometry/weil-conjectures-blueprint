+++
id = "lemma-internal-adjunction-two-exchange-formulas--1"
kind = "lemma"
title = "Internal adjunction at finite and rational coefficients"
name_showing = false
order = 829001
aliases = ["bp-r248-1"]
lean = ["AlgebraicGeometry.Etale.derivedHomRightDerivedLowerShriekIsoOfFinite", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_verdierExchange"]
uses = ["definition-compactification-refinement", "definition-constructible-sheaves", "theorem-exceptional-inverse-image"]
+++
Let $\Lambda$ be a finite commutative ring and let $f:X\to Y$ admit a
compactification. For arbitrary complexes $K\in D(X_{\acute{e}t},\Lambda)$
and $L\in D(Y_{\acute{e}t},\Lambda)$ there is an isomorphism, natural in
both variables,

$$
Rf_*\cHom_X(K,f^!L)\simeq\cHom_Y(Rf_!K,L).
$$

No boundedness, constructibility or finite Tor amplitude hypothesis is
needed in this finite-coefficient statement.

For $\Lambda=\overline{\mathbf Q}_\ell$, let $k$ have positive
characteristic $p\ne\ell$, where $p$ and $\ell$ are prime, and let
$f:X\to Y$ be a morphism of separated schemes of finite type over $k$.
For $K\in\Dbc(X,\Lambda)$ and $L\in\Dbc(Y,\Lambda)$ on the pro-étale
sites, the exchange map (10.1)

$$
Rf_*\cHom_X(K,f^!L)\longrightarrow\cHom_Y(Rf_!K,L)
$$

is an isomorphism. Here the coefficient ring in Lean is the condensed
ring associated to $\overline{\mathbf Q}_\ell$.
