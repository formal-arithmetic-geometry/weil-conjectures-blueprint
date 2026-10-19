+++
id = "det-tf-ibc-proper-step"
kind = "lemma"
title = "Proper direct image and base change along a product projection"
uses = ["lem-fin-proper-bounded-constructible", "thm-weil-pbc-bounded-below", "prop-weil-pbc-comparison-direct-image", "lem-weil-pbc-comparison-pullback"]
+++
Let $A$ be a finite commutative $\ell$-primary ring with $\ell\ne\operatorname{char}k$,
let $\bar f:\bar X\to Y$ be a proper morphism of separated $k$-schemes of finite type,
let $T$ be a separated $k$-scheme of finite type, and let $N\in\Dbc(\bar X,A)$. Write
$\bar h=\bar f\times\operatorname{id}_T:\bar X\times T\to Y\times T$, and let
$p_{\bar X}\colon\bar X\times T\to\bar X$ and $p_Y\colon Y\times T\to Y$ be the
projections. Then $R\bar f_*N\in\Dbc(Y,A)$, and the base change map

$$
p_Y^*R\bar f_*N\longrightarrow R\bar h_*p_{\bar X}^*N
$$

is an isomorphism in $D((Y\times T)_{\mathrm{pro\acute et}},A)$.
