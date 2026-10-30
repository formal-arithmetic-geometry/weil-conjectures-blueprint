+++
id = "prose-02-23"
kind = "hidden"
title = "Classical sheaves"
order = 77
+++
In order to use the torsion arguments of étale cohomology, we identify the part
of the pro-étale topos that comes from the étale topos. The main
result is that étale sheaves embed fully faithfully, with essential
image the sheaves whose sections on a limit $\varprojlim U_i$ are the
colimit of the sections on the $U_i$. The $\ell$-adic coefficient
sheaves, such as $\mathbf Z_{\ell,X}$, lie outside this part
(Example [sk-rem-pe-nonclassical-example]), while their reductions
$\mathbf Z/\ell^n$ lie inside it. From here until Section [sec-pe-coefficient-bridge], $\Lambda$ denotes a discrete commutative ring and
$\Lambda_X$ its constant sheaf on $X_{\mathrm{pro}\acute{e}t}$.

The colimit condition is forced on us by the way étale sheaves extend
to limits. If $F$ is an étale sheaf and $\bar x$ a geometric point, the
only reasonable value of the pullback of $F$ on the strict henselization
$\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{X,\bar x}=\varprojlim(U,\bar u)$
is $\varinjlim F(U)=F_{\bar x}$, so stalks of étale sheaves become
sections of pro-étale sheaves. The pullback $\nu_X^*$ is defined by
this rule (Proposition [sk-prop-pe-comparison-morphism]), and its image is
characterized by it (Theorem [sk-thm-pe-classical-sheaves]). The difficulty,
taken up in the next subsection, is cohomological: pro-étale covers are
not étale covers, and we must show that they do not create new
cohomology classes for classical sheaves.
