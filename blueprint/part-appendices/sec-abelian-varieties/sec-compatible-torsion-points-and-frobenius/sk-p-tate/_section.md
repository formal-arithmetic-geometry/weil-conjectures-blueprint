+++
id = "sk-p-tate"
kind = "proposition"
title = "No Frobenius-fixed vector"
order = 871
lean = ["AlgebraicGeometry.IsAbelianVariety.eq_zero_of_mem_tateModule_of_forall_geometricFrobenius_fixed", "AlgebraicGeometry.IsAbelianVariety.eq_zero_of_map_geometricFrobenius_eq_self", "AlgebraicGeometry.IsAbelianVariety.frobeniusSubOneLinearEquiv"]
uses = ["sk-prop-av-tate-rank", "sk-def-av"]
tags = ["sketch"]
+++
Let $A_0/\mathbf F_q$ be an abelian variety, let
$A=A_0\times_{\mathbf F_q}\overline{\mathbf F}_q$, and let $F$
be geometric Frobenius on $T_\ell A$. For every $m>0$,

$$
(T_\ell A)^{F^m}=0,
\qquad (V_\ell A)^{F^m}=0,
\qquad V_\ell A=T_\ell A\otimes_{\Zl}\Ql.
$$

Consequently $F^m-1$ is an automorphism of the finite-dimensional
$\Ql$-vector space $V_\ell A$, and hence of $V_\ell A\otimes_{\Ql}E$ for every
field extension $E$ of $\Ql$.
