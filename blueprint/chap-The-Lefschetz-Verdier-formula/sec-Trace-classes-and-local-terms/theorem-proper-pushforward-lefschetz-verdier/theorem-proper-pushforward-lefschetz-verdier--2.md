+++
id = "theorem-proper-pushforward-lefschetz-verdier--2"
kind = "theorem"
title = "The global trace as an integral"
name_showing = false
order = 925002
aliases = ["bp-r281-2"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.trace_globalOperator_eq_integral_traceClass"]
uses = ["definition-correspondence", "definition-action-correspondence", "definition-trace-class-local-terms", "definition-categorical-trace"]
+++
Let $k$ be a field of characteristic $p>0$, let $\ell\ne p$ be prime,
and put $A=\Qbarl$. Let $X$ be proper over $k$, let
$K\in\Dbc(X,A)$, and let $u:c_2^*K\to c_1^!K$ be a cohomological
correspondence with $C$ separated of finite type over $k$ and $c_2$
proper. Choose a fixed locus $F=\Fix(c)$ proper over $k$, and assume
that $\RGammac(X,K)$ has a right dual in $\Dbc(s,A)$, where
$s=\operatorname{Spec}k$. Then

$$
\operatorname{tr}_A(T_c(u)\mid\RGammac(X,K))
=\int_F\operatorname{Tr}_c(u)
$$

in $\End_{\Dbc(s,A)}(A_s)$. Since $X$ is proper,
$\RGammac(X,K)\simeq R\Gamma(X,K)$, so this also gives the trace on
ordinary cohomology.
