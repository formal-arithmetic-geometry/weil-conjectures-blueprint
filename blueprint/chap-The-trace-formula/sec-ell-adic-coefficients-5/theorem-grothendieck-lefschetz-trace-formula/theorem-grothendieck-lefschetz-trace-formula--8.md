+++
id = "theorem-grothendieck-lefschetz-trace-formula--8"
kind = "theorem"
title = "Alternating cohomological trace over a field"
order = 1017016
aliases = ["bp-r311-8"]
lean = ["AlgebraicGeometry.WeilComplex.finsum_trace_compactlySupportedCohomology_eq"]
uses = ["definition-weil-structure", "definition-trace-function", "definition-frobenius-operator"]
+++
Let $X_0$ be separated of finite type over $\Fq$, let $X=X_0\times_{\Fq}\overline{\Fq}$, and let $\ell\nmid q$. For a bounded constructible $\Qlb$-Weil complex $K$ on $X$ and every $m\geq1$,

$$
\sum_i(-1)^i\operatorname{Tr}
\bigl(\operatorname{Frob}_{X,K}^m\mid H_c^i(X_{\mathrm{pro}\acute{e}t},K)\bigr)
=\sum_{y\in X_0(\mathbf F_{q^m})}t_{K,m}(y)
=\sum_{y\in X_0(\mathbf F_{q^m})}\sum_j(-1)^j
\operatorname{Tr}\bigl(\operatorname{Frob}_{y,m}\mid H^j(K_{\bar y})\bigr).
$$

The sums over degrees have finite support, and the set $X_0(\mathbf F_{q^m})$ is finite. This is the $\Qlb$ case of (12.4); the tagged declaration has this fixed coefficient field.
