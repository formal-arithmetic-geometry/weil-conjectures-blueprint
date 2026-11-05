+++
id = "theorem-grothendieck-lefschetz-trace-formula--1"
kind = "theorem"
title = "Trace formula: finite coefficients"
order = 1017002
aliases = ["bp-r311-1"]
lean = []
uses = ["definition-weil-structure", "definition-trace-function", "definition-frobenius-operator", "definition-categorical-trace"]
+++
This step with finite coefficients is bypassed by the Lean route, which proves the cohomological formula over $\Qlb$ through bounded constructible Weil objects. The following is the coefficient case of the human statement; it has no matching declaration in this route.

For $K\in D^b_{\mathrm{ctf}}(X_{\mathrm{pro}\acute{e}t},A)$ with the stated Weil structure and every $m\geq1$, one has in $A$:

$$
\operatorname{tr}_{A}
\bigl(\operatorname{Frob}_{X,K}^m\mid R\Gamma_c(X_{\mathrm{pro}\acute{e}t},K)\bigr)
=\sum_{y\in X_0(\mathbf F_{q^m})}
\operatorname{tr}_{A}
\bigl(\operatorname{Frob}_{y,m}\mid K_{\bar y}\bigr).
\tag{12.3}
$$
