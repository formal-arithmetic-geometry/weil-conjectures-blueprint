+++
id = "lemma-vanishing-restrictions-after-blowing-up--1"
kind = "lemma"
title = "Vanishing of restrictions in principal equations"
order = 979001
aliases = ["bp-r298-1"]
lean = ["AlgebraicGeometry.Etale.blowupRestriction_eq_zero"]
+++
Let $k$ be an algebraically closed field, let $\ell$ be a prime invertible
in $k$, and let $A$ be a finite commutative $\ell$-primary ring. Let
$T=\operatorname{Spec}R$ be the strict localization of a smooth surface
over $k$ at a closed point $t$, and let $\m$ be the maximal ideal of $R$.
Choose $f,g,h\in R$ with

$$
f\ne0,\qquad 0\ne g\in\m,\qquad h\in\m-\m^2.
$$

Put $D=V(f)$, $C=V(g)$ and $H=V(h)$. Suppose that the tangent cone
of $D$ meets those of $C$ and $H$ only in $0$. Let
$j':T-(D\cup H)\hookrightarrow T-D$ be the open immersion, and let $N$
be a bounded complex of étale $A$-modules on $T-(D\cup H)$. Assume
that each cohomology sheaf of $N$ becomes constant with finite fibre
on a finite étale Galois cover whose group is a finite $\ell$-group.
Then the restriction map

$$
R\Gamma(T-D,j'_!N)\longrightarrow
R\Gamma(C-t,(j'_!N)|_{C-t})
$$

is zero in $D(A)$.
