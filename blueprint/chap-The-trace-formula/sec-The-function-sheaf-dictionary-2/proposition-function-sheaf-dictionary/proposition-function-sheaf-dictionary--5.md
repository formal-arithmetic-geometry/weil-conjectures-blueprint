+++
id = "proposition-function-sheaf-dictionary--5"
kind = "proposition"
title = "The function–sheaf dictionary (5)"
name_showing = false
order = 1028006
aliases = ["bp-r315-5"]
lean = ["AlgebraicGeometry.WeilComplex.finsum_trace_compactlySupportedCohomology_eq"]
uses = ["definition-weil-structure", "definition-trace-function"]
+++
Let $\ell$ be a prime with $\ell\nmid q$, let $X_0$ be separated of finite type over $\Fq$, and
put $X=X_0\times_{\Fq}\overline{\Fq}$. For a bounded constructible Weil
$\Qbarl$-complex $K$ on $X$ and every $m\geq1$,
$$
\sum_{x\in X_0(\mathbf F_{q^m})}t_{K,m}(x)
=\sum_{r\in\mathbf Z}(-1)^r\operatorname{Tr}_{\Qbarl}
\bigl(\operatorname{Frob}_{X,K}^m\mid
H_c^r(X_{\mathrm{pro}\acute{e}t},K)\bigr).
$$
Only finitely many terms occur. This is the $\Qbarl$-cohomological form of
[theorem-grothendieck-lefschetz-trace-formula].
