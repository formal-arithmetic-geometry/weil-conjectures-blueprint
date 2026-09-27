+++
id = "sk-def-zeta"
kind = "section"
title = "The point-count zeta series"
order = 2853
lean = ["AlgebraicGeometry.Scheme.Hom.pointCount", "AlgebraicGeometry.Scheme.Hom.zetaSeries"]
+++
*Definition (sketch).*

Let $k_0=\Fq$ be a finite field of characteristic $p$, with algebraic closure
$k=\Fbar$, and let $X_0$ be a finite-type $k_0$-scheme. Put

$$
N_n(X_0)=\#X_0(\Fqn)=\#\operatorname{Hom}_{k_0}(\Spec\Fqn,X_0),
$$

and define the *zeta series*

$$
Z(X_0,T)=\exp\Bigl(\sum_{n\ge1}N_n(X_0)\frac{T^{n}}{n}\Bigr)
\in 1+T\Z[[T]].
$$

For a closed point $x\in|X_0|$ put $\deg(x)=[\kappa(x):k_0]$. The
coefficients of $Z$ are the point counts $N_n$; the exponential is formal, so
$Z$ lies in $1+T\Z[[T]]$ by construction.
