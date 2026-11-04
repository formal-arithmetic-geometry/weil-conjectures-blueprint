+++
id = "lemma-base-change-along-product-projection"
kind = "lemma"
title = "Base change along a product projection"
order = 700
lean = ["AlgebraicGeometry.Etale.isIso_tensorBaseChangeMap"]
+++
Let $f:X\to Y$ be a morphism of separated $k$-schemes of finite type,
let $T$ be a separated $k$-scheme of finite type, and let
$M\in\Dbc(X,A)$.  Let
$p_X:X\times T\to X$ and $p_Y:Y\times T\to Y$ be the
projections.  Then the base change map

$$
p_Y^*Rf_*M\longrightarrow R(f\times\operatorname{id}_T)_*p_X^*M
$$

is an isomorphism.
