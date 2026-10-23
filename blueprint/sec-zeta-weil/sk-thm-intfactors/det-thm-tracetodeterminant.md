+++
id = "det-thm-tracetodeterminant"
kind = "theorem"
title = "Trace-to-determinant identity"
lean = ["TraceDatum.zeta_mul_prod_even_eq_prod_odd"]
order = 4129
uses = ["det-def-cohfamily", "det-def-zeta", "sk-prop-logdet", "sk-cor-tf-point-counting"]
+++
Let $X_0/\Fq$ be smooth, proper and geometrically connected of pure dimension
$d$, and let $(V_{i,\ell},F_{i,\ell},P_{i,\ell})$ be the family of
[det-def-cohfamily]. Then

$$
Z(X_0,T)=\prod_{i=0}^{2d}P_{i,\ell}(T)^{(-1)^{i+1}}
\qquad\text{in }\Ql(T)\cap\Ql[[T]] .
$$
