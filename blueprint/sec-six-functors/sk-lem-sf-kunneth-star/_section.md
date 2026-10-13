+++
id = "sk-lem-sf-kunneth-star"
kind = "lemma"
title = "Ordinary Künneth with an identity factor"
order = 2561
uses = ["sk-lem-sf-flat-model", "sk-prop-sf-comparison", "sk-prop-sf-kunneth-ordinary"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_externalProduct_rightDerivedLowerStar"]
tags = ["sketch"]
+++
Let $f:X\to Y$ be a morphism of separated finite-type $k$-schemes, let $Z$ be
a further such scheme, and let $L\in\Dctf(X,\Lambda)$,
$Q\in\Dctf(Z,\Lambda)$. Then the canonical comparison

$$
Rf_*L\boxtimes Q\ \xrightarrow{\ \sim\ }\
R(f\times\operatorname{id}_Z)_*\bigl(L\boxtimes Q\bigr)
$$

is an isomorphism, natural in $L$ and $Q$.
