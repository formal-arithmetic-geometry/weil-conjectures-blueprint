+++
id = "theorem-proper-pushforward-lefschetz-verdier--3"
kind = "theorem"
title = "Decomposition of the integral into local terms"
name_showing = false
order = 925003
aliases = ["bp-r281-3"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.BorelMooreSection.integral_eq_sum_localTerm"]
uses = ["definition-trace-class-local-terms", "definition-correspondence"]
+++
Let $k$ be a field of characteristic $p>0$, let $\ell\ne p$ be prime,
and put $A=\Qbarl$. Let $Z$ be proper over $k$, and let
$\alpha:A_Z\to\omega_Z$ be a Borel–Moore section in $\Dbc(Z,A)$.
Suppose that $j_i:B_i\hookrightarrow Z$, indexed by a finite set $I$,
are open and closed immersions with $B_i$ proper over $k$, whose images
are pairwise disjoint and cover $Z$. Then

$$
\int_Z\alpha=\sum_{i\in I}\operatorname{LT}_{B_i}(\alpha),
\qquad
\operatorname{LT}_{B_i}(\alpha)=\int_{B_i}\alpha|_{B_i}.
$$

In particular, for a proper fixed locus $Z=\Fix(c)$ and
$\alpha=\operatorname{Tr}_c(u)$, this gives

$$
\int_{\Fix(c)}\operatorname{Tr}_c(u)
=\sum_{i\in I}\operatorname{LT}_{B_i}(u).
$$
