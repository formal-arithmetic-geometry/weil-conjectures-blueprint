+++
id = "prose-06-03"
kind = "hidden"
title = "A uniform bound for Ext between constructible sheaves"
order = 268
+++
For torsion coefficients such a bound is a matter of cohomological
dimension. By (5.1), $R\!\operatorname{Hom}(a_!L,N)$ is the cohomology
on the stratum $S$ of a complex obtained from $N$ by restriction and
$Rj_*$, and each of these steps raises degrees by a bounded amount that
does not depend on $N$. With coefficients $E$ this count has no direct
meaning, because $E$-sheaves are not torsion and $\operatorname{cd}_\ell$
only controls torsion sheaves. We therefore choose lattices on the
strata, apply the torsion count modulo every $\pi_E^n$, pass to the
derived limit over $n$, which costs one degree, and finally invert
$\pi_E$ using the continuity of Ext from Section [sec-ext-continuity].

The bound $d_C$ on $\Ext^q(C,-)$ is a sum of the cohomological
dimensions $\operatorname{cd}_\ell$ of Definition [sk-def-cd]. In the
proof we compute $R\!\operatorname{Hom}(a_!L_0,K)$, for a derived complete
$K\in D(X_{\mathrm{pro}\acute{e}t},\mathcal O_E)$, as a derived inverse limit over the
reductions modulo $\pi_E^n$. For this, the functors in
(5.1) have to commute with derived inverse limits, and
we use the next lemma with $\Lambda=\mathcal O_E$.
