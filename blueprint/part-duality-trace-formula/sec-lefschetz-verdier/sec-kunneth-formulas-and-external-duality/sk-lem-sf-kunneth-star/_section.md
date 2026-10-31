+++
id = "sk-lem-sf-kunneth-star"
kind = "proposition"
title = "Ordinary external Künneth"
order = 551
lean = ["AlgebraicGeometry.Etale.nonempty_iso_externalProduct_rightDerivedLowerStar"]
uses = ["sk-lem-tf-independent-base-change", "sk-thm-pe-constructible-comparison", "sk-thm-pe-direct-image-comparison", "sk-thm-sf-ctf-stability", "sk-prop-scalar-six", "sk-lem-sf-flat-model", "sk-prop-sf-comparison", "sk-prop-sf-kunneth-ordinary"]
tags = ["sketch"]
+++
For morphisms $f_i:X_i\to Y_i$ and $M_i\in D^b_{\mathrm{ctf}}(X_i,A)$, $i=1,2$, the
Künneth map

$$
Rf_{1*}M_1\boxtimes Rf_{2*}M_2
\longrightarrow R(f_1\times f_2)_*(M_1\boxtimes M_2)
$$

is an isomorphism. In particular, for $f:X\to Y$, $T$ as in
Lemma [sk-lem-tf-independent-base-change], $M\in D^b_{\mathrm{ctf}}(X,A)$ and
$Q\in D^b_{\mathrm{ctf}}(T,A)$, the case where one factor is an identity is the isomorphism

$$
Rf_*M\boxtimes Q
\longrightarrow R(f\times\operatorname{id}_T)_*(M\boxtimes Q).
\tag{12.2}
$$
