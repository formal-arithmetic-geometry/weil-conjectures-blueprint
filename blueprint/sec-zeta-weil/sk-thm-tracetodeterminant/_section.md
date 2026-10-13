+++
id = "sk-thm-tracetodeterminant"
kind = "theorem"
title = "Trace-to-determinant identity"
order = 3221
lean = ["TraceDatum.zeta_mul_prod_even_eq_prod_odd"]
uses = ["sk-def-cohfamily", "sk-def-zeta", "sk-prop-logdet", "sk-thm-trace-formula", "sk-thm-trace-transport"]
tags = ["sketch"]
+++
Let $X_0/\Fq$ be smooth, proper and geometrically connected of pure dimension
$d$, and let $(V_{i,\ell},F_{i,\ell},P_{i,\ell})$ be the family of
[sk-def-cohfamily]. Then

$$
Z(X_0,T)=\prod_{i=0}^{2d}P_{i,\ell}(T)^{(-1)^{i+1}}
\qquad\text{in }\Ql(T)\cap\Ql[[T]] .
$$
