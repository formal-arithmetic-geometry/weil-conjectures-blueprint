+++
id = "corollary-trace-functions-direct-image-compact--1"
kind = "corollary"
title = "Direct image of trace functions for equivariant Weil objects"
name_showing = false
order = 1024001
aliases = ["bp-r313-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.weilShriekTraceFunction"]
uses = ["definition-weil-structure", "definition-trace-function", "proposition-construction-independence-rf-shriek", "proposition-composition-base-change-rf-shriek"]
+++
Let $k=\Fq$, let $\ell$ be a prime different from the characteristic of $k$,
and let $f_0:X_0\to Y_0$ be a morphism of separated $k$-schemes of finite
type. Let $e_X$ and $e_Y$ be automorphisms over $k$ satisfying
$f_0\circ e_X=e_Y\circ f_0$, and suppose that $e_X^r=\id$ for some $r>0$.
Let $K\in\Dbc(X_0,\Qbarl)$ carry an isomorphism
$\phi:e_X^*K\xrightarrow{\sim}K$. Here the complexes are complexes of
modules over the condensed coefficient ring $\Qbarl$ on the pro-étale
site of $X_0$. Give $Rf_{0,!}K$ the structure for $e_Y$ induced by compactly
supported base change and $Rf_{0,!}\phi$.

Write $\sigma$ for the geometric Frobenius of $\operatorname{Spec}\bar k$.
For $m\geq1$ put

$$
S_m(X_0,e_X)=
\{\bar x:\operatorname{Spec}\bar k\to X_0\text{ over }k:
e_X^m\circ\bar x=\bar x\circ\sigma^m\},
$$

and define $S_m(Y_0,e_Y)$ in the same way. For $\bar x\in S_m(X_0,e_X)$,
let $t_{K,m}(\bar x)$ be the alternating sum of the categorical traces
of the Frobenius operators on $H^j(K)_{\bar x}$, formed using the $m$-th
iterate of $\phi$. Then for every $\bar y\in S_m(Y_0,e_Y)$,

$$
t_{Rf_{0,!}K,m}(\bar y)=
\sum_{\substack{\bar x\in S_m(X_0,e_X)\\ f_0\circ\bar x=\bar y}}
t_{K,m}(\bar x).
$$

This is an equality in the endomorphism ring of the tensor unit of the
category of $\Qbarl$-module sheaves on
$(\operatorname{Spec}\bar k)_{\mathrm{pro}\acute{e}t}$. The sum is finite.
No finite-order hypothesis on $e_Y$ is needed. For $e_X=e_Y=\id$, the
point sets are $X_0(\mathbf F_{q^m})$ and $Y_0(\mathbf F_{q^m})$.
