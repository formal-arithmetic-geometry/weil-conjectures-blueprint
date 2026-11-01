+++
id = "lem-zl-euler-product-identity"
kind = "lemma"
title = "Euler-product identity for a Frobenius module"
lean = ["LinearMap.inv_charpolyRev_eq_exp"]
order = 3859
uses = ["def-zl-frobenius-trace-series", "lem-zl-log-det-identity"]
+++
Let $(V,F)$ be a Frobenius module, as in
the trace-series definition,
and put $N_n=\Tr(F^n\mid V)$ for every $n\geq1$. Then

$$
\exp\left(\sum_{n\geq1}N_n\frac{T^n}{n}\right)
=\det(1-TF\mid V)^{-1}
\quad\text{in }\Qlb[[T]].
$$
