+++
id = "definition-local-cohomology--1"
kind = "definition"
title = "Local cohomology (1)"
name_showing = false
order = 204001
aliases = ["bp-r059-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.closedSupport"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "lemma-stability--5", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "corollary-finite-quotients-their-transition-maps--3", "lemma-inverse-image-coefficient-sheaves--1"]
+++
The *local cohomology functor*
$R\underline\Gamma_Z:D(X_{\mathrm{pro}\acute{e}t},\mathcal R)\to D(Z_{\mathrm{pro}\acute{e}t},i^*\mathcal R)$
is the right derived functor of the functor of sections supported on $Z$,

$$
F\longmapsto i^*\ker(F\longrightarrow j_*j^*F),
$$

where $F\to j_*j^*F$ is the unit of $j^*\dashv j_*$.
