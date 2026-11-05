+++
id = "lemma-kunneth-one-identity-factor--1"
kind = "lemma"
title = "Künneth formula with one identity factor (1)"
name_showing = false
order = 717001
aliases = ["bp-r216-1"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_externalProduct_rightDerivedLowerStar"]
uses = ["definition-constructible-sheaves", "definition-kunneth-map"]
+++
Let $k$ be a field and let $A$ be a finite commutative ring whose additive
exponent is invertible in $k$. Let $f:X\to Y$ be a morphism of separated
$k$-schemes of finite type, let $T$ be another separated $k$-scheme of finite
type, and put $h=f\times\operatorname{id}_T$. Work on the small étale sites,
and let $M\in D^b_{\mathrm{ctf}}(X_{\acute{e}t},A)$ and
$Q\in D^b_{\mathrm{ctf}}(T_{\acute{e}t},A)$, with constructibility and finite
Tor amplitude as in [definition-constructible-sheaves]. There exists an
isomorphism

$$
Rf_*M\boxtimes Q\simeq Rh_*(M\boxtimes Q)
$$

in $D((Y\times_k T)_{\acute{e}t},A)$, where both external products are over
$k$ as in [definition-kunneth-map].
