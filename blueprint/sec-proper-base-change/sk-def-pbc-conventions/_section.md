+++
id = "sk-def-pbc-conventions"
kind = "definition"
title = "Conventions for proper base change"
order = 1043
uses = ["sk-def-conv"]
tags = ["sketch"]
+++
In this section, schemes are arbitrary unless an additional hypothesis is
stated. The theorem concerns the classical part of
$D^+(T_{\mathrm{proét}},\Lambda)$, for a discrete commutative ring $\Lambda$.
The intermediate acyclicity, curve and Chow calculations are made on
$T_{\Et}$, with abelian sheaves or modules over its discrete constant ring. We
write $D^+(T_{\Et},\Lambda)$ for the bounded below derived category. Inverse
image on these sheaves is denoted by $u^{-1}$; for $u:S\to T$ it is a functor
$\Sh(T_{\Et})\to\Sh(S_{\Et})$, and likewise on module sheaves and
$D^+(T_{\Et},\Lambda)\to D^+(S_{\Et},\Lambda)$. It is exact and agrees with
$u^*$ for the constant coefficient rings under consideration. The derived
direct image is $Ru_*$. Torsion always means torsion of the underlying abelian
sheaves.

The proper base change theorem imposes no invertibility condition on the
torsion coefficients, so a prime $r$ appearing in this section may equal a
residue characteristic. The standing condition on $\ell$ from the introduction
returns with the $\ell$-adic constructible theory.

*Module and abelian cohomology.* Cohomology of a sheaf of $\Lambda$-modules is
canonically the cohomology of its underlying abelian sheaf (Stacks Project,
Tag 03FD), because an injective module sheaf is acyclic for the underlying
section functor on every object of the site. Applying this on the étale
objects over the target gives the same compatibility for $R^qu_*$ and, by
bounded below resolutions, for $Ru_*$. Forgetting the module structure need
not preserve injectives; only acyclicity is used.
