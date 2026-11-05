+++
id = "theorem-grothendieck-lefschetz-trace-formula--2"
kind = "theorem"
title = "Trace formula: integral coefficients"
order = 1017004
aliases = ["bp-r311-2"]
lean = []
uses = ["definition-weil-structure", "definition-trace-function", "definition-frobenius-operator", "definition-categorical-trace"]
+++
This step with integral coefficients is bypassed by the Lean route, which proves the cohomological formula over $\Qlb$ through bounded constructible Weil objects. The following is the coefficient case of the human statement; it has no matching declaration in this route.

For $K\in D^b_{\mathrm{ctf}}(X_{\mathrm{pro}\acute{e}t},\mathcal O_E)$ with the stated Weil structure and every $m\geq1$, one has in $\mathcal O_E$:

$$
\operatorname{tr}_{\mathcal O_E}
\bigl(\operatorname{Frob}_{X,K}^m\mid R\Gamma_c(X_{\mathrm{pro}\acute{e}t},K)\bigr)
=\sum_{y\in X_0(\mathbf F_{q^m})}
\operatorname{tr}_{\mathcal O_E}
\bigl(\operatorname{Frob}_{y,m}\mid K_{\bar y}\bigr).
$$
