+++
id = "prose-02-30"
kind = "hidden"
title = "Classical sheaves (1)"
order = 110
+++
From here until Section [sec-Continuous-cohomology], $\Lambda$ denotes a discrete
commutative ring and $\Lambda_X$ its constant sheaf on $X_{\mathrm{pro}\acute{e}t}$. To use
the torsion arguments of étale cohomology, we must know which pro-étale
sheaves come from étale sheaves. The main result answers this: étale sheaves
embed fully faithfully, and the essential image consists of the sheaves
whose sections on a limit $\varprojlim U_i$ are the colimit of the sections
on the $U_i$. In particular, the reductions $\mathbf Z/\ell^n$ lie in this image, while the
$\ell$-adic coefficient sheaves themselves, such as $\mathbf Z_{\ell,X}$, do
not (Example [example-coefficient-sheaf-outside-classical-part]).

The colimit condition is forced on us by the way étale sheaves extend
to limits. If $F$ is an étale sheaf and $\bar x$ a geometric point, the
only reasonable value of the pullback of $F$ on the strict henselization
$\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{X,\bar x}=\varprojlim(U,\bar u)$
is $\varinjlim F(U)=F_{\bar x}$. In this way stalks of étale sheaves
become sections of pro-étale sheaves.
Proposition [proposition-comparison-morphism-inverse-image] defines
the pullback $\nu_X^*$ by this rule, and
Theorem [theorem-classical-sheaves-essential-image] characterizes its
image by it. The part that is not formal is cohomology, because pro-étale covers
are not étale covers. In the next subsection we show that they create
no new cohomology classes for classical sheaves.
