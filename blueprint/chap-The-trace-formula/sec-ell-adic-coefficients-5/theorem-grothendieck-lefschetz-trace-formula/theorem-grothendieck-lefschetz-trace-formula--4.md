+++
id = "theorem-grothendieck-lefschetz-trace-formula--4"
kind = "theorem"
title = "Trace formula for bounded constructible Weil objects"
order = 1017008
aliases = ["bp-r311-4"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.weilTraceFormula"]
uses = ["definition-weil-structure", "definition-trace-function", "definition-categorical-trace"]
+++
Let $X_0$ be separated of finite type over $\Fq$, let $\ell\nmid q$, and let $e:X_0\xrightarrow{\sim}X_0$ be an automorphism over $\Fq$ of finite order. Let $K'$ be a bounded constructible complex of condensed $\Qlb$-modules on $(X_0)_{\mathrm{pro}\acute{e}t}$, with an isomorphism $Le^*K'\xrightarrow{\sim}K'$. Write $\sigma$ for the geometric Frobenius of $\operatorname{Spec}\overline{\Fq}$ and, for $m\geq1$, put

$$
\operatorname{Fix}_m(e)=\{\bar x:\operatorname{Spec}\overline{\Fq}\to X_0
\text{ over }\Fq:\ e^m\circ\bar x=\bar x\circ\sigma^m\}.
$$

Let $t_m(K';\bar x)$ be the alternating sum of the categorical traces on the cohomology stalks, and let $L_m(X_0,K')$ be the corresponding local trace at the geometric point of $\operatorname{Spec}\Fq$ of the Weil direct image $Ra_!^{\mathrm{Weil}}K'$, where $a:X_0\to\operatorname{Spec}\Fq$. Then

$$
L_m(X_0,K')=\sum_{\bar x\in\operatorname{Fix}_m(e)}t_m(K';\bar x).
$$

The equality takes values in the endomorphism ring of the tensor unit in the category of condensed $\Qlb$-modules on $(\operatorname{Spec}\overline{\Fq})_{\mathrm{pro}\acute{e}t}$. The set of points is finite. The mainline uses this formula with $e=1$.
