+++
id = "definition-pro-etale-base-change-map--1"
kind = "definition"
title = "Pro-étale base change map (1)"
name_showing = false
order = 322001
aliases = ["bp-r096-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.baseChangeMap", "AlgebraicGeometry.ProEtale.derivedBaseChangeMap"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "lemma-stability--3", "lemma-stability--5", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "lemma-inverse-image-coefficient-sheaves--1"]
+++
Let $K\in D(X_{\mathrm{pro}\acute{e}t},\Lambda)$. The *base change map*

$$
g^*Rf_*K\longrightarrow Rf'_*g'^*K
\tag{4.5}
$$

in $D(Y'_{\mathrm{pro}\acute{e}t},\Lambda)$ is the adjoint transpose, for
$f'^*\dashv Rf'_*$, of the composite

$$
f'^*g^*Rf_*K\simeq g'^*f^*Rf_*K
\xrightarrow{g'^*\varepsilon_f}g'^*K,
$$

where $\varepsilon_f:f^*Rf_*\to\mathrm{id}$ is the counit of
$f^*\dashv Rf_*$.
