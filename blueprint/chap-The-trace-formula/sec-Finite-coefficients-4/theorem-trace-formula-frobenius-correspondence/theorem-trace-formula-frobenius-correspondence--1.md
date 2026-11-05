+++
id = "theorem-trace-formula-frobenius-correspondence--1"
kind = "theorem"
title = "Trace formula for Weil objects"
name_showing = false
order = 1006001
aliases = ["bp-r307-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.weilTraceFormula"]
uses = ["definition-weil-structure", "definition-categorical-trace"]
+++
The finite-coefficient statement is bypassed by the Lean proof of the
main theorem. The formula used there is the following one for Weil
objects with $\overline{\mathbf Q}_\ell$ coefficients and an invertible
structure map.

Let $\ell$ be a prime with $\ell\nmid q$, let $X_0/\mathbf F_q$ be
separated and of finite type, and let $e:X_0\xrightarrow{\sim}X_0$ be an
automorphism over $\mathbf F_q$ such that $e^r=\operatorname{id}_{X_0}$
for some $r\geq1$. Let $K\in\Dbc(X_0,\overline{\mathbf Q}_\ell)$
on the pro-étale site, equipped with an isomorphism
$\phi:e^*K\xrightarrow{\sim}K$, a Weil object for $e$ in the sense of
[definition-weil-structure]. Put $k=\overline{\mathbf F}_q$, let
$s:\operatorname{Spec}k\to\operatorname{Spec}\mathbf F_q$ be the base
point, and let $\sigma$ be the geometric Frobenius of
$\operatorname{Spec}k$. For $m\geq1$, put

$$
P_m(e)=\{\bar x:\operatorname{Spec}k\to X_0\text{ over }s:
e^m\circ\bar x=\bar x\circ\sigma^m\}.
$$

For $\bar x\in P_m(e)$, write

$$
t_{K,m}(\bar x)=\sum_j(-1)^j
\operatorname{Tr}(F_{\bar x,m}\mid\mathcal H^j(K)_{\bar x}),
$$

where $F_{\bar x,m}$ is induced by the iterated Weil structure and the
displayed equality for $\bar x$. The traces are categorical traces as in
[definition-categorical-trace], valued in the endomorphism ring of the
tensor unit of the category of $\overline{\mathbf Q}_\ell$-modules on
$(\operatorname{Spec}k)_{\mathrm{pro}\acute{e}t}$.
For the structure morphism $a:X_0\to\operatorname{Spec}\mathbf F_q$,
give $Ra_!K$ its induced Weil structure for the identity of the base.
Then

$$
t_{Ra_!K,m}(s)=\sum_{\bar x\in P_m(e)}t_{K,m}(\bar x).
$$

The set $P_m(e)$ is finite, and the sums over cohomological degrees have
finite support. For $e=\operatorname{id}_{X_0}$, the points in $P_m(e)$
are the $\mathbf F_{q^m}$-rational points. This is
`AlgebraicGeometry.ProEtale.CondensedRing.weilTraceFormula`; it does not
assert the finite-ring formula for a possibly noninvertible $\psi$.
