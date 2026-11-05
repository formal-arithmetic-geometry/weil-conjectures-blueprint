+++
id = "proposition-central-element-arithmetic-monodromy-group--1"
kind = "proposition"
title = "A central element of the arithmetic monodromy group (1)"
name_showing = false
order = 1141001
aliases = ["bp-r350-1"]
lean = ["AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.exists_isPositiveCentralPair"]
+++
Let $k$ be an algebraically closed field of characteristic zero, let $W$
be a group with a surjective homomorphism $\deg:W\to\mathbf Z$, and choose
$s\in W$ of degree one. Let $\rho:W\to\GL(V)$ be a semisimple
representation on a finite-dimensional $k$-vector space $V$. Write $G$
and $H$ for the Zariski closures of $\rho(W)$ and $\rho(\ker\deg)$,
respectively, as in [definition-monodromy-groups], and put $F=\rho(s)$.

There are an integer $N>0$ and $z\in\GL(V)$ such that

$$
z\in Z(G(k))\cap H(k)F^N.
$$

Thus $z=hF^N$ for some $h\in H(k)$ and commutes with every element
of $G(k)$. Such a pair $(N,z)$ is called a positive central pair.
No topology on $W$ is needed.

In particular, for semisimple Weil representations $V_1,\ldots,V_n$, this
applies to $W=W(U_0)$, $k=\overline{\mathbf Q}_\ell$ and
$V=\bigoplus_iV_i$, and gives
$z=h\,\rho(s)^N\in Z(G)(\overline{\mathbf Q}_\ell)$.
