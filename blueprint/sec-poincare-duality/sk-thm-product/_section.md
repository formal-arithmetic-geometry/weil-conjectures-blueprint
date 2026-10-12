+++
id = "sk-thm-product"
kind = "theorem"
title = "Supported product over a relative base"
order = 2774
uses = ["sk-def-ops", "sk-thm-sf-kunneth-relative"]
tags = ["sketch"]
+++
In the setting of [sk-def-set], let $B$ be a finite-type $k$-scheme,
$f:X\to B$, $g:Y\to B$ separated of finite type,
$h=f\times_Bg:X\times_BY\to B$ with projections $p,q$, and
$K\boxtimes L=p^*K\otimes^L_\Lambda q^*L$. For closed immersions
$i:Z\hookrightarrow X$, $j:W\hookrightarrow Y$, with
$i\times_Bj:Z\times_BW\hookrightarrow X\times_BY$,

$$
Rf_!\bigl(i_*i^*K\bigr)\otimes^L_{\Lambda_B}Rg_!\bigl(j_*j^*L\bigr)\cong
Rh_!\bigl((i\times_Bj)_*(i\times_Bj)^*(K\boxtimes L)\bigr).
$$

For $B=\Spec k$ this reads
$R\Gamma_c(Z,i^*K)\otimes^L_\Lambda R\Gamma_c(W,j^*L)\cong R\Gamma_c\bigl(Z\times W,(K\boxtimes L)|_{Z\times W}\bigr)$.
