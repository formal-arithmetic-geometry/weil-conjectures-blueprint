+++
id = "definition-trace-function"
kind = "definition"
title = "Trace function"
order = 1023
lean = ["AlgebraicGeometry.WeilComplex.traceFunction", "AlgebraicGeometry.WeilSheaf.traceFunction", "AlgebraicGeometry.ProEtale.CondensedRing.weilStalkTraceAlternatingSum"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-pro-etale-site-separably-closed", "lemma-inverse-image-coefficient-sheaves", "definition-constructible-sheaves", "definition-lisse-sheaves", "definition-weil-structure", "definition-categorical-trace"]
+++
Let $(K,\phi)$ be a Weil complex on $X$ as in
Theorem [theorem-grothendieck-lefschetz-trace-formula], and let $m\geq1$.
The *trace function* of $K$ is

$$
t_{K,m}:X_0(\mathbf F_{q^m})\longrightarrow\Lambda,\qquad
t_{K,m}(x)=\operatorname{tr}_\Lambda\bigl(\operatorname{Frob}_{x,m}
\mid K_{\bar x}\bigr).
$$
