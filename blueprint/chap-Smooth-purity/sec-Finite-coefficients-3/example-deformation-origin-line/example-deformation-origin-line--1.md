+++
id = "example-deformation-origin-line--1"
kind = "example"
title = "The origin in the affine line (1)"
name_showing = false
order = 747001
aliases = ["bp-r225-1"]
+++
Let $S=\operatorname{Spec}k$, $V=\mathbf A^1_k$ with coordinate $x$, and let
$s$ be the origin. The blowup of $V\times\mathbf A^1=\mathbf A^2$, with
coordinates $(x,t)$, at the origin is covered by two charts. On the chart with
coordinates $(u,t)$ and $x=tu$ the exceptional divisor is $t=0$; on the chart
with coordinates $(x,v)$ and $t=xv$ it is $x=0$, and the strict transform of
the line $V\times\{0\}=\{t=0\}$ is $v=0$. A point of the second chart with
$v\neq0$ lies on the first chart, with $u=1/v$. Removing the strict
transform therefore leaves exactly the first chart:

$$
\mathcal D_{s(S)}V=\operatorname{Spec}k[u,t]\longrightarrow
V\times\mathbf A^1,\qquad (u,t)\longmapsto(tu,t),
$$

with $\widetilde g$ the projection to $t$ and $\widetilde s$ the line $u=0$.
For $t=c\neq0$ the fibre is the line $V$ itself, with coordinate $u=x/c$ and
the origin as section. For $t=0$ the fibre is the $u$-line, mapped to the
origin of $V$; it is the tangent line $N_s=T_0\mathbf A^1$, and $u$ is the
linear coordinate given by the class of $x$ in $\mathfrak m/\mathfrak m^2$.
So the family rescales the line by $1/t$ and in the limit keeps only the
first-order information at the section. Here the family is the product
$\mathbf A^1_u\times\mathbf A^1_t$, so $\widetilde s^*\omega_{\widetilde g}$
is visibly constant along $t$. In general this holds only étale locally,
after a choice of coordinates. The point of
Lemma [lemma-section-normal-bundle] is that the comparison normalized at
$t=1$ does not depend on that choice.
