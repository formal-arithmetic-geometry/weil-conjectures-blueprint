+++
id = "theorem-grothendieck-lefschetz-trace-formula--9"
kind = "theorem"
title = "Comparison of global and local traces"
name_showing = false
order = 1017018
lean = ["AlgebraicGeometry.WeilComplex.exists_weilBoundedConstructible_comparison"]
uses = ["definition-weil-structure", "definition-trace-function", "definition-categorical-trace", "theorem-grothendieck-lefschetz-trace-formula--4"]
+++
For a bounded constructible $\Qlb$-Weil complex $K$ on $X$, there exist a bounded constructible Weil object $K'$ on $X_0$ for the identity automorphism and an additive map

$$
\iota:\operatorname{End}(\mathbf 1_{\mathcal M})\longrightarrow\Qlb,
$$

where $\mathcal M$ is the category of condensed $\Qlb$-modules on $(\operatorname{Spec}\overline{\Fq})_{\mathrm{pro}\acute{e}t}$, such that for every $m\geq1$,

$$
\iota\bigl(L_m(X_0,K')\bigr)
=\sum_i(-1)^i\operatorname{Tr}
\bigl(\operatorname{Frob}_{X,K}^m\mid H_c^i(X,K)\bigr).
$$

For each $y\in X_0(\mathbf F_{q^m})$, let $\bar y$ be its geometric point obtained from the chosen embedding $\mathbf F_{q^m}\hookrightarrow\overline{\Fq}$. Then

$$
\iota\bigl(t_m(K';\bar y)\bigr)=t_{K,m}(y).
$$

Here $L_m$ and $t_m$ denote the global and local alternating traces of the Weil object, as in [theorem-grothendieck-lefschetz-trace-formula--4]. The assertion compares traces; it does not assert that $K$ descends to $X_0$.
