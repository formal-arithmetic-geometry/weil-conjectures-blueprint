+++
id = "proposition-function-sheaf-dictionary--3"
kind = "proposition"
title = "The function–sheaf dictionary (3)"
name_showing = false
order = 1028004
aliases = ["bp-r315-3"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.weilShriekTraceFunction"]
uses = ["definition-weil-structure", "definition-trace-function", "definition-categorical-trace"]
+++
Let $\ell$ be a prime with $\ell\nmid q$, and let $f_0:X_0\to Y_0$ be a morphism of separated
$\Fq$-schemes of finite type. Let $e_X$ and $e_Y$ be automorphisms over
$\Fq$ with $f_0\circ e_X=e_Y\circ f_0$, and suppose $e_X$ has finite order.
Let $K'$ be a bounded constructible $\Qbarl$-Weil object on $X_0$ for
$e_X$, with structure $e_X^*K'\simeq K'$.

Write $\sigma$ for geometric Frobenius on $\Spec\overline{\Fq}$ and set
$$
X_0(e_X,m)=\{\bar x:\Spec\overline{\Fq}\to X_0\text{ over }\Fq
\mid e_X^m\circ\bar x=\bar x\circ\sigma^m\}.
$$
For $m\geq1$ let $\tau_{K',m}(\bar x)$ denote the alternating categorical
stalk trace (`weilStalkTraceAlternatingSum`) at such a point. These traces
take values in $\End(\mathbf1_{\bar s})$, where $\mathbf1_{\bar s}$ is the
tensor unit in the category of coefficient modules at the geometric base
point. Then for $\bar y\in Y_0(e_Y,m)$,
$$
\tau_{Rf_{0!}^{\mathrm{Weil}}K',m}(\bar y)
=\sum_{\substack{\bar x\in X_0(e_X,m)\\ f_0\circ\bar x=\bar y}}
  \tau_{K',m}(\bar x).
$$
For $e_X=e_Y=\id$, the indexing sets identify with the usual
$\mathbf F_{q^m}$-rational points. This is the Weil-object form of
[corollary-trace-functions-direct-image-compact]; the object $K'$ is on
$X_0$, whereas a geometric Weil complex is on $X$.
