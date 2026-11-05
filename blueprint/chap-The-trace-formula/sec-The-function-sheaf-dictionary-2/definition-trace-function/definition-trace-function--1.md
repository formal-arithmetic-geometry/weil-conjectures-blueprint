+++
id = "definition-trace-function--1"
kind = "definition"
title = "Trace function (1)"
name_showing = false
order = 1023001
aliases = ["bp-r312-1"]
lean = ["AlgebraicGeometry.WeilComplex.traceFunction"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "definition-small-pro-etale-site--1", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "definition-weil-structure--1", "definition-weil-structure--3", "theorem-grothendieck-lefschetz-trace-formula--6"]
+++
Let $(K,\phi)$ be a Weil complex on $X$ as in
Theorem [theorem-grothendieck-lefschetz-trace-formula], and let $m\geq1$.
The *trace function* of $K$ is

$$
t_{K,m}:X_0(\mathbf F_{q^m})\longrightarrow\Lambda,\qquad
t_{K,m}(x)=\operatorname{tr}_\Lambda\bigl(\operatorname{Frob}_{x,m}
\mid K_{\bar x}\bigr).
$$
