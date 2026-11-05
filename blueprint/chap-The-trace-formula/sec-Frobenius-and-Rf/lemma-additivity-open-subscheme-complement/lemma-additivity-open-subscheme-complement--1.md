+++
id = "lemma-additivity-open-subscheme-complement--1"
kind = "lemma"
title = "Weil structures on an open–closed decomposition"
name_showing = false
order = 1002001
aliases = ["bp-r306-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.weilUpperStar", "AlgebraicGeometry.ProEtale.CondensedRing.weilLowerShriek", "AlgebraicGeometry.ProEtale.CondensedRing.exists_isDistTriang_openClosed", "AlgebraicGeometry.ProEtale.CondensedRing.weilStalkTraceAlternatingSum_weilUpperStar"]
uses = ["definition-weil-structure", "definition-categorical-trace"]
+++
Let $k_0$ be a field of characteristic $p>0$, and let $\ell\ne p$ be
prime. Let $j_0:U_0\hookrightarrow X_0$ be an open immersion of separated
schemes of finite type over $k_0$, and let $i_0:Z_0\hookrightarrow X_0$
be a closed immersion whose image is the complement of $U_0$.
Suppose that automorphisms $e_X,e_U,e_Z$ over $k_0$ satisfy
$e_X\circ j_0=j_0\circ e_U$ and $e_X\circ i_0=i_0\circ e_Z$.
Let $K\in D^b_c(X_0,\Qbarl)$ carry a Weil structure
$\phi:e_X^*K\xrightarrow{\sim}K$ as in [definition-weil-structure].

Pullback and direct image with compact support give Weil structures on
$j_0^*K$, $i_0^*K$, $Rj_{0!}j_0^*K$ and $Ri_{0!}i_0^*K$.
Here $Rj_{0!}=j_{0!}$ and $Ri_{0!}\simeq Ri_{0*}$.
There are equivariant maps extending to a distinguished triangle of
the underlying derived category

$$
Rj_{0!}j_0^*K\longrightarrow K\longrightarrow Ri_{0!}i_0^*K
\xrightarrow{\delta}Rj_{0!}j_0^*K[1],
$$

and $\delta$ also commutes with the Weil structures.
No reducedness assumption on $Z_0$ is needed.

If $k_0=\Fq$, put $\sigma=\operatorname{Fr}_{\operatorname{Spec}\bar k_0}$,
the geometric Frobenius over $k_0$. For a Weil object $M$ on $V_0$
with automorphism $e_V$, and a geometric point $\bar v$ over $k_0$
satisfying $e_V^m\circ\bar v=\bar v\circ\sigma^m$, write

$$
t_m(M;\bar v)=\sum_r(-1)^r
\operatorname{tr}(F_{\bar v,m}\mid\mathcal H^r(M)_{\bar v}).
$$

The traces are categorical traces in the endomorphism ring of the unit
on $\operatorname{Spec}\bar k_0$.
For $m\geq1$, these local alternating traces satisfy

$$
t_m(j_0^*K;\bar u)=t_m(K;j_0\bar u),\qquad
t_m(i_0^*K;\bar z)=t_m(K;i_0\bar z).
$$
