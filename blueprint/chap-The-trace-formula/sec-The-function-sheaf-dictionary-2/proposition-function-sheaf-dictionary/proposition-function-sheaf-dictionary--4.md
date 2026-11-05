+++
id = "proposition-function-sheaf-dictionary--4"
kind = "proposition"
title = "The function–sheaf dictionary (4)"
name_showing = false
order = 1028005
aliases = ["bp-r315-4"]
lean = ["AlgebraicGeometry.WeilComplex.traceFunction_eq_add_of_distTriang", "AlgebraicGeometry.WeilComplex.HasLocalWeilObjectComparison.of_openClosed"]
uses = ["definition-weil-structure", "definition-trace-function", "definition-categorical-trace", "proposition-function-sheaf-dictionary--3"]
+++
The pointwise open–closed identity for geometric Weil complexes is bypassed
by Lean's comparison route, which uses the following statements.

Let $\ell$ be a prime with $\ell\nmid q$ and let $X_0$ be locally of finite type over $\Fq$.
For a distinguished triangle $K_1\to K_2\to K_3\to K_1[1]$ of bounded
constructible Weil $\Qbarl$-complexes on its geometric base change, one has
$$
t_{K_2,m}(x)=t_{K_1,m}(x)+t_{K_3,m}(x)
\qquad(m\geq1,\ x\in X_0(\mathbf F_{q^m})).
$$

For the open–closed comparison, suppose $X_0$, $U_0$, and $Z_0$ are
separated of finite type over $\Fq$, and let $j_0:U_0\hookrightarrow X_0$
be an open immersion and $i_0:Z_0\hookrightarrow X_0$ a closed immersion
whose image is its complement. Write $j$ and $i$ for their geometric base
changes, and let $K$ be a bounded constructible Weil $\Qbarl$-complex on
$X$. Fix an additive map
$\iota:\End(\mathbf1_{\bar s})\to\Qbarl$, with categorical stalk traces
$\tau$ as in [proposition-function-sheaf-dictionary--3]. Suppose there are
bounded constructible Weil objects $K'_U$ and $K'_Z$ for the identity
automorphisms of $U_0$ and $Z_0$ such that, for every $m\geq1$,
$$
\iota(\tau_{K'_U,m}(u))=t_{j^*K,m}(u),\qquad
\iota(\tau_{K'_Z,m}(z))=t_{i^*K,m}(z)
$$
at every rational point. Then there is a bounded constructible Weil object
$K'$ for the identity automorphism of $X_0$ satisfying
$$
\iota(\tau_{K',m}(x))=t_{K,m}(x)
\qquad(m\geq1,\ x\in X_0(\mathbf F_{q^m})).
$$
