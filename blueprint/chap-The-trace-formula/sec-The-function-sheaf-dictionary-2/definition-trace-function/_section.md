+++
id = "definition-trace-function"
kind = "definition"
title = "Trace function"
order = 1022
lean = ["AlgebraicGeometry.WeilComplex.traceFunction"]
uses = ["definition-ind-etale-pro-etale-weakly", "definition-small-pro-etale-site", "proposition-topos-functoriality", "definition-weil-structure", "definition-categorical-trace", "proposition-properties-trace", "lemma-perfect-complexes-geometric-point"]
+++
Let $(K,\phi)$ be a Weil complex on $X$ as in
Theorem [theorem-grothendieck-lefschetz-trace-formula], and let $m\geq1$.
The *trace function* of $K$ is

$$
t_{K,m}:X_0(\mathbf F_{q^m})\longrightarrow\Lambda,\qquad
t_{K,m}(x)=\operatorname{tr}_\Lambda\bigl(\operatorname{Frob}_{x,m}
\mid K_{\bar x}\bigr).
$$
