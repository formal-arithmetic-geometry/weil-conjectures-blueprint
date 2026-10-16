+++
id = "lem-zl-log-det-identity"
kind = "lemma"
title = "Logarithm of the Frobenius determinant"
lean = ["LinearMap.logOf_charpolyRev"]
order = 2736
uses = ["def-zl-frobenius-trace-series", "p-linear-triangular"]
+++
Let $(V,F)$ be a Frobenius module, as in
the trace-series definition.
Then, as formal power series in $\Qlb[[T]]$,

$$
\log\det(1-TF\mid V)
=-\sum_{n\geq1}\Tr(F^n\mid V)\frac{T^n}{n}
=-\operatorname{tr}_F(T).
$$

No semisimplicity assumption is imposed on $F$.
