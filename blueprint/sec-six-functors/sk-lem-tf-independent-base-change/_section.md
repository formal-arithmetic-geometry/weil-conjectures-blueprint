+++
id = "sk-lem-tf-independent-base-change"
kind = "lemma"
title = "Base change along a product projection"
order = 2394
uses = ["sk-thm-nagata-compactification", "sk-cor-geo-open-finiteness", "sk-thm-properbasechange"]
tags = ["sketch"]
+++
Here $k=\overline{\mathbf F}_q$, and $A$ is a finite commutative $\ell$-primary ring
with $\ell\ne\operatorname{char}k$. Let $f:X\to Y$ be a morphism of separated
$k$-schemes of finite type, let $T$ be a separated $k$-scheme of finite type, and
let $M\in\Dbc(X,A)$. Write $h=f\times\operatorname{id}_T:X\times T\to Y\times T$, and
let $p_X\colon X\times T\to X$ and $p_Y\colon Y\times T\to Y$ be the projections.
Then the base change map

$$
p_Y^*Rf_*M\longrightarrow Rh_*p_X^*M
$$

is an isomorphism in $D((Y\times T)_{\mathrm{pro\acute et}},A)$.
