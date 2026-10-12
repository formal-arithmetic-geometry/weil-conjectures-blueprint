+++
id = "sk-d-lines"
kind = "remark"
title = "The affine and projective lines"
order = 2714
uses = ["sk-d-setup"]
lean = ["AlgebraicGeometry.ProjectiveSpace"]
tags = ["sketch"]
+++
Over a finite field $F$ from the coefficient setup, the projective line
$\mathbf P^1_F$ is the projective space over $\operatorname{Spec}F$ with
homogeneous coordinates $T_0,T_1$, that is, the base change
$\operatorname{Spec}F\times_{\operatorname{Spec}\mathbf Z}\operatorname{Proj}\mathbf Z[T_0,T_1]$
of the integral model. Put $\mathbf A^1_F=\operatorname{Spec}F[t]$.
Concretely, $\mathbf P^1_F$ is obtained by gluing $\operatorname{Spec}F[t]$
to $\operatorname{Spec}F[z]$ along
$F[t,t^{-1}]=F[z,z^{-1}]$, with $t=T_1/T_0$ and $z=t^{-1}=T_0/T_1$.
The first chart is $\mathbf A^1_F$ and its complement is the point
$\infty$ defined by $z=0$. Frobenius acts by $t\mapsto t^{|F|}$ and
$z\mapsto z^{|F|}$ on these charts.
