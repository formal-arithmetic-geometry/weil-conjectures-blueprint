+++
id = "definition-trace-function"
kind = "definition"
title = "Trace function"
order = 1023
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.weilStalkTraceAlternatingSum", "AlgebraicGeometry.WeilSheaf.traceFunction"]
uses = ["proposition-etale-implications", "lemma-stability", "proposition-topos-functoriality", "proposition-pro-etale-affines-form-basis", "proposition-pro-etale-site-separably-closed", "definition-constructible-sheaves", "definition-lisse-sheaves"]
+++
Let $(K,\phi)$ be a Weil complex on $X$ as in
Theorem [theorem-grothendieck-lefschetz-trace-formula], and let $m\geq1$.
The *trace function* of $K$ is

$$
t_{K,m}:X_0(\mathbf F_{q^m})\longrightarrow\Lambda,\qquad
t_{K,m}(x)=\operatorname{tr}_\Lambda\bigl(\operatorname{Frob}_{x,m}
\mid K_{\bar x}\bigr).
$$
