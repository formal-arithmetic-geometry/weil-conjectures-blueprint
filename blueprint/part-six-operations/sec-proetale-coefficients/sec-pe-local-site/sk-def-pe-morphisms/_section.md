+++
id = "sk-def-pe-morphisms"
kind = "definition"
title = "Ind-étale, pro-étale and weakly étale morphisms"
order = 26
lean = ["Algebra.IndEtale", "AlgebraicGeometry.proAffineEtale", "AlgebraicGeometry.proAffineEtale_Spec_iff", "AlgebraicGeometry.WeaklyEtale", "AlgebraicGeometry.WeaklyEtale.hasRingHomProperty", "AlgebraicGeometry.etale_le_weaklyEtale", "AlgebraicGeometry.proAffineEtale_le_weaklyEtale", "AlgebraicGeometry.WeaklyEtale.etale"]
tags = ["sketch"]
+++
A ring map $R\to B$ is *ind-étale* if
$B=\varinjlim_\alpha B_\alpha$ for a filtered system of finitely
presented étale $R$-algebras. For an affine base
$X=\operatorname{Spec}(R)$, the corresponding morphism

$$
\operatorname{Spec}(B)=\varprojlim_\alpha
\operatorname{Spec}(B_\alpha)\longrightarrow X
$$

is called *affine pro-étale*. More generally, a
*pro-étale affine over $X$* is an inverse limit of affine
schemes étale over $X$.

A scheme morphism $u:U\to X$ is *weakly étale* if $u$ and its
diagonal $\Delta_u:U\to U\times_XU$ are flat. On affine charts this
means that both

$$
R\longrightarrow B,
\qquad B\otimes_RB\longrightarrow B
$$

are flat.
