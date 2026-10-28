+++
id = "sk-lem-sf-kunneth-star"
kind = "proposition"
title = "Ordinary external Künneth"
order = 3438
uses = ["sk-lem-tf-independent-base-change", "sk-thm-pe-constructible-comparison", "sk-thm-pe-direct-image-comparison", "sk-thm-sf-ctf-stability", "sk-prop-scalar-six", "sk-lem-sf-flat-model", "sk-prop-sf-comparison", "sk-prop-sf-kunneth-ordinary"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_externalProduct_rightDerivedLowerStar"]
tags = ["sketch"]
+++
Here $k=\overline{\mathbf F}_q$, $A$ is a finite commutative $\ell$-primary ring with
$\ell\ne\operatorname{char}k$, all schemes are separated $k$-schemes of finite type,
and $M\boxtimes N=p_1^*M\dt p_2^*N$ is the external tensor product on a product, with
$p_1,p_2$ the two projections. For morphisms $f_i:X_i\to Y_i$ and
$M_i\in\Dctf(X_i,A)$, $i=1,2$, the Künneth map in
$D((Y_1\times Y_2)_{\mathrm{pro\acute et}},A)$

$$
Rf_{1*}M_1\boxtimes Rf_{2*}M_2
\longrightarrow R(f_1\times f_2)_*(M_1\boxtimes M_2)
$$

is an isomorphism. In particular, for $f:X\to Y$, $T$ as in
Lemma [sk-lem-tf-independent-base-change], $M\in\Dctf(X,A)$ and $Q\in\Dctf(T,A)$, its
identity-factor form is the isomorphism in $D((Y\times T)_{\mathrm{pro\acute et}},A)$

$$
k_{f,M,Q}:Rf_*M\boxtimes Q
\longrightarrow R(f\times\operatorname{id}_T)_*(M\boxtimes Q).
\tag{1}
$$
