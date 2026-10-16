+++
id = "lem-sc-pullback-degree"
kind = "lemma"
title = "Degree of pullbacks of divisors"
lean = ["AlgebraicGeometry.Scheme.finsum_ord_eq_finrank", "AlgebraicGeometry.Scheme.Hom.finrank_genericPoint_eq_finrank_functionField", "AlgebraicGeometry.Scheme.Divisor.pullback", "AlgebraicGeometry.Scheme.Divisor.degree_pullback_single", "AlgebraicGeometry.Scheme.Divisor.degree_pullback", "AlgebraicGeometry.Scheme.Divisor.degree_pullback_eq_finrank_functionField_mul"]
order = 706
uses = ["def-sc-curves", "def-sc-divisor", "lem-sc-point-cartier"]
+++
Let $\pi:C\to C'$ be a finite flat morphism of proper smooth
connected curves over an algebraically closed field
$k$, of degree $d=[k(C):k(C')]$, and let
$D'=\sum_Pn_P[P']$ be a divisor on $C'$. Then

$$
\deg(\pi^*D')=d\cdot\deg D',
$$

where $\pi^*D'$ is the pullback divisor
$\sum_{P'}n_{P'}\sum_{\pi(P)=P'}v_P(t_{P'})[P]$ ($t_{P'}$ a local
equation of $P'$); in particular
$\deg\pi^*[P']=d$ for every closed point $P'$.
