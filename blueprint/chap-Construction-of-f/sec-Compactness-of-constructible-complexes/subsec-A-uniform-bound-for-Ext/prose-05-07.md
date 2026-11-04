+++
id = "prose-05-07"
kind = "hidden"
title = "A uniform bound for Ext (1)"
order = 435
+++
The idea of the bound is to count cohomological dimensions modulo
$\pi_E^n$, add one degree for the derived limit over $n$, and invert
$\pi_E$ by passing to a colimit. For torsion coefficients the count is
direct. By (3.1), $R\!\operatorname{Hom}(a_!L,N)$ is the cohomology
on the stratum $S$ of a complex obtained from $N$ by restriction and
$Rj_*$. Each of these steps raises degrees by a bounded amount that
does not depend on $N$. With coefficients $E$ we cannot count in this
way, because $E$-sheaves are not torsion and $\operatorname{cd}_\ell$
only controls torsion sheaves. This is why we choose lattices on the
strata. Inverting $\pi_E$ at the end then needs the continuity of Ext
from Section [sec-Continuity-of-Ext].

The bound $d_C$ on $\Ext^q(C,-)$ is a sum of the cohomological
dimensions $\operatorname{cd}_\ell$ of Definition [definition-cohomological-dimension]. In the
proof we compute $R\!\operatorname{Hom}(a_!L_0,K)$, for a derived complete
$K\in D(X_{\mathrm{pro}\acute{e}t},\mathcal O_E)$, as a derived inverse limit over the
reductions modulo $\pi_E^n$. For this, the functors in
(3.1) have to commute with derived inverse limits, and
we use the next lemma with $\Lambda=\mathcal O_E$.
