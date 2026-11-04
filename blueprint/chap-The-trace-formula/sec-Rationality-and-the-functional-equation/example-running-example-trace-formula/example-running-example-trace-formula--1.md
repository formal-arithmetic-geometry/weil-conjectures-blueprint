+++
id = "example-running-example-trace-formula--1"
kind = "example"
title = "The running example: the trace formula (1)"
name_showing = false
order = 1036001
aliases = ["bp-r319-1"]
+++
For the elliptic curve $C_0\colon y^2=x^3-x$ over $\mathbf F_3$,
geometric Frobenius acts on $H^0(C,\mathbf Q_\ell)=\mathbf Q_\ell$ by $1$ and on
$H^2(C,\mathbf Q_\ell)=\mathbf Q_\ell(-1)$ by $3$, and $H^1(C,\mathbf Q_\ell)$ is a plane
(Example [example-running-example-duality]). The point-counting formula reads

$$
N_m=1-\operatorname{Tr}\bigl(F^m\mid H^1(C,\mathbf Q_\ell)\bigr)+3^m .
$$

From $N_1=4$ we get $\operatorname{Tr}(F\mid H^1)=0$. Duality gives
$\det(F\mid H^1)=3$, so $\det(1-TF\mid H^1)=1+3T^2$.
