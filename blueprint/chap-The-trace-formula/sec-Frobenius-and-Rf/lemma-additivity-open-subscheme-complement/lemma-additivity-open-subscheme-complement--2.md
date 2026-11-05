+++
id = "lemma-additivity-open-subscheme-complement--2"
kind = "lemma"
title = "Additivity of the local trace of $Rf_!$"
name_showing = false
order = 1002002
aliases = ["bp-r306-2"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.weilStalkTraceAlternatingSum_weilLowerShriek_eq_add"]
uses = ["lemma-additivity-open-subscheme-complement--1", "proposition-construction-independence-rf-shriek"]
+++
In the setting of [lemma-additivity-open-subscheme-complement--1], assume
$k_0=\Fq$. Let $f_0:X_0\to Y_0$ be a morphism of separated schemes
of finite type over $k_0$, and let $e_Y$ be an automorphism over $k_0$
such that $e_Y\circ f_0=f_0\circ e_X$.
For every $m\geq1$ and every geometric point $\bar y$ over $k_0$
with $e_Y^m\circ\bar y=\bar y\circ\sigma^m$, one has

$$
\begin{aligned}
t_m(Rf_{0!}K;\bar y)
&=t_m(R(f_0j_0)_!j_0^*K;\bar y)\\
&\quad+t_m(R(f_0i_0)_!i_0^*K;\bar y).
\end{aligned}
$$

All direct images carry the induced Weil structures. The automorphisms
need not have finite order.

In particular, take $Y_0=\operatorname{Spec}k_0$, $e_Y=\operatorname{id}$
and $\bar y=\operatorname{Spec}\bar k_0$. Writing $X,U,Z$ for the geometric
base changes, the local trace of the direct image is the alternating
trace on compactly supported cohomology, and the equality becomes

$$
\begin{aligned}
\sum_r(-1)^r\operatorname{tr}(F_{c,m}\mid H_c^r(X,K))
&=\sum_r(-1)^r\operatorname{tr}(F_{c,m}\mid H_c^r(U,j^*K))\\
&\quad+\sum_r(-1)^r\operatorname{tr}(F_{c,m}\mid H_c^r(Z,i^*K)).
\end{aligned}
$$

Here the coefficient complexes on the geometric base changes are
understood by pullback.
