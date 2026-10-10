+++
id = "sk-def-zeta"
kind = "definition"
title = "The point-count zeta series"
order = 2853
lean = ["AlgebraicGeometry.Scheme.Hom.pointCount", "AlgebraicGeometry.Scheme.Hom.zetaSeries"]
tags = ["sketch"]
+++
Let $k_0=\Fq$ be a finite field of characteristic $p$, with algebraic closure
$k=\Fbar$, and let $X_0$ be a $k_0$-scheme. For $n\ge1$ let $\Fqn$ be the
degree-$n$ extension of $k_0$ (the splitting field of $T^{q^{n}}-T$ over
$k_0$), and put

$$
N_n(X_0)=\#X_0(\Fqn)=\#\operatorname{Hom}_{k_0}(\Spec\Fqn,X_0),
$$

the number of $k_0$-morphisms, taken to be $0$ if this set is infinite.
Define the *zeta series*

$$
Z(X_0,T)=\exp\Bigl(\sum_{n\ge1}N_n(X_0)\frac{T^{n}}{n}\Bigr)
\in 1+T\Q[[T]],
$$

where $\exp$ is the formal power-series exponential.
For a closed point $x\in|X_0|$ put $\deg(x)=[\kappa(x):k_0]$.

A priori $Z$ only lies in $1+T\Q[[T]]$. The point counts are recovered from
$Z$ by the logarithmic derivative, $T\,Z'/Z=\sum_{n\ge1}N_nT^{n}$; the
coefficients of $Z$ itself are *not* the $N_n$ (for instance
$[T^{2}]Z=(N_1^{2}+N_2)/2$, which for $\mathbf P^{1}_{\Fq}$ is $q^{2}+q+1$
while $N_2=q^{2}+1$). That $Z$ has integer coefficients is not automatic for
the exponential of an arbitrary integer sequence ($N_1=1$, $N_n=0$ for
$n\ge2$ gives $\exp(T)$); for $X_0$ of finite type it follows from the
closed-point Euler product of [sk-prop-euler].
