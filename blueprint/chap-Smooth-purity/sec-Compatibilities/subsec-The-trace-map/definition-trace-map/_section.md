+++
id = "definition-trace-map"
kind = "definition"
title = "Trace map"
order = 804
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.smoothTrace"]
uses = ["definition-tate-twists", "proposition-six-operations-dctf--17", "theorem-smooth-purity-all-admissible-coefficients"]
+++
For $K\in D^b_{\mathrm{ctf}}(Y,\Lambda)$, the *trace map* is the composite

$$
\operatorname{Tr}_{f}(K):\quad
Rf_!\bigl(f^{*}K(d)[2d]\bigr)
\xrightarrow{\ Rf_!\gamma_{f}(K)\ }
Rf_!f^!K
\xrightarrow{\ \varepsilon_{f}(K)\ }K.
\tag{9.25}
$$
