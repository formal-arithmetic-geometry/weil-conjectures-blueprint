+++
id = "sk-prop-divisor-gen"
kind = "proposition"
title = "Divisor sequence"
order = 903
uses = ["sk-def-curve"]
lean = ["AlgebraicGeometry.Scheme.exists_shortExact_divisorSequence"]
tags = ["sketch"]
+++
Let $X$ be an integral regular locally noetherian scheme (e.g. a
smooth variety over a field) with generic point $\eta$, $i:\eta\to X$,
and let $X^{(1)}$ be the set of codimension-$1$ points of $X$. There
is a morphism $\operatorname{div}$ of étale sheaves on $X$ such that
the sequence

$$
0\longrightarrow\mathbb G_m\longrightarrow i_*\mathbb G_{m,\eta}
\xrightarrow{\ \operatorname{div}\ }
\bigoplus_{x\in X^{(1)}}i_{x*}\Z\longrightarrow0 ,
$$

whose first map is the unit
$\mathbb G_m\to i_*i^*\mathbb G_m=i_*\mathbb G_{m,\eta}$, is exact.
