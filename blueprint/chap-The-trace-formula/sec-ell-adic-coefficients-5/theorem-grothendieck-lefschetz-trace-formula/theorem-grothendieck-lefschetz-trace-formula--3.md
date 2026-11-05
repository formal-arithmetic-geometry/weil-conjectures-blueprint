+++
id = "theorem-grothendieck-lefschetz-trace-formula--3"
kind = "theorem"
title = "Trace formula: finite extension of $\\Ql$"
order = 1017006
aliases = ["bp-r311-3"]
lean = []
uses = ["definition-weil-structure", "definition-trace-function", "definition-frobenius-operator", "definition-categorical-trace"]
+++
This step with coefficients in a finite extension of $\Ql$ is bypassed by the Lean route, which proves the cohomological formula over $\Qlb$ through bounded constructible Weil objects. The following is the coefficient case of the human statement; it has no matching declaration in this route.

For $K\in D^b_{\mathrm{ctf}}(X_{\mathrm{pro}\acute{e}t},E)$ with the stated Weil structure and every $m\geq1$, one has in $E$:

$$
\operatorname{tr}_{E}
\bigl(\operatorname{Frob}_{X,K}^m\mid R\Gamma_c(X_{\mathrm{pro}\acute{e}t},K)\bigr)
=\sum_{y\in X_0(\mathbf F_{q^m})}
\operatorname{tr}_{E}
\bigl(\operatorname{Frob}_{y,m}\mid K_{\bar y}\bigr).
$$
