+++
id = "definition-ind-etale-pro-etale-weakly"
kind = "definition"
title = "Ind-étale, pro-étale and weakly étale morphisms"
order = 27
lean = ["Algebra.IndEtale", "RingHom.IndEtale", "AlgebraicGeometry.proAffineEtale", "AlgebraicGeometry.proAffineEtale_Spec_iff", "AlgebraicGeometry.WeaklyEtale", "AlgebraicGeometry.WeaklyEtale.hasRingHomProperty", "RingHom.WeaklyEtale", "Algebra.WeaklyEtale"]
+++
A ring map $R\to B$ is *ind-étale* if
$B=\varinjlim_\alpha B_\alpha$ for a filtered system of étale
$R$-algebras $B_\alpha$. A *pro-étale affine over $X$* is a scheme
$U=\varprojlim_iU_i$ that is the limit of a cofiltered system of affine
schemes $U_i$ étale over $X$. If $X=\operatorname{Spec}(R)$ is affine,
the pro-étale affines over $X$ are the schemes

$$
\operatorname{Spec}(B)=\varprojlim_\alpha
\operatorname{Spec}(B_\alpha)\longrightarrow X
$$

with $R\to B$ ind-étale.

A scheme morphism $u:U\to X$ is *weakly étale* if $u$ and its
diagonal $\Delta_u:U\to U\times_XU$ are flat. On affine charts this
means that both

$$
R\longrightarrow B,
\qquad B\otimes_RB\longrightarrow B
$$

are flat.
