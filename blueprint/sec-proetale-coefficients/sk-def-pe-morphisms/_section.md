+++
id = "sk-def-pe-morphisms"
kind = "definition"
title = "Ind-étale, pro-étale and weakly étale morphisms"
order = 901
lean = ["Algebra.IndEtale", "AlgebraicGeometry.proAffineEtale", "AlgebraicGeometry.proAffineEtale_Spec_iff", "AlgebraicGeometry.WeaklyEtale", "AlgebraicGeometry.WeaklyEtale.hasRingHomProperty", "AlgebraicGeometry.etale_le_weaklyEtale", "AlgebraicGeometry.proAffineEtale_le_weaklyEtale", "AlgebraicGeometry.WeaklyEtale.etale"]
tags = ["sketch"]
+++
A ring map $R\to B$ is *ind-étale* if $B=\varinjlim_\alpha B_\alpha$ for a filtered
system of finitely presented étale $R$-algebras. For an affine base
$X=\operatorname{Spec}(R)$, the corresponding morphism

$$
\operatorname{Spec}(B)=\varprojlim_\alpha\operatorname{Spec}(B_\alpha)\longrightarrow X
$$

is called *affine pro-étale*. More generally, a *pro-étale affine over $X$* is an inverse
limit of affine schemes étale over $X$.

A scheme morphism $u\colon U\to X$ is *weakly étale* if $u$ and its diagonal
$\Delta_u\colon U\to U\times_XU$ are flat. On affine charts this means that both

$$
R\longrightarrow B,\qquad B\otimes_RB\longrightarrow B
$$

are flat. Thus every étale morphism, and every affine pro-étale morphism, is weakly étale.
A weakly étale morphism locally of finite presentation is étale.

Flatness of the diagonal takes the place of finite presentation; flatness of $u$ alone is
too weak to define an object of the pro-étale site. A weakly étale morphism need not have a
global presentation as a limit of étale morphisms; what holds instead is the covering
refinement of [sk-thm-pe-indetale-refinement] (Stacks, Tag 097Z).
