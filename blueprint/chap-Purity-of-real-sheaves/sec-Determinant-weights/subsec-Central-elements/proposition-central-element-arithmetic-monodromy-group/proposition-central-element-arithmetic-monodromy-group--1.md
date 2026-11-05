+++
id = "proposition-central-element-arithmetic-monodromy-group--1"
kind = "proposition"
title = "A central element of the arithmetic monodromy group (1)"
name_showing = false
order = 1138001
aliases = ["bp-r350-1"]
lean = ["AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.exists_isPositiveCentralPair"]
uses = ["definition-monodromy-groups"]
+++
Let $k$ be an algebraically closed field of characteristic zero, let $W$
be a group with a surjective homomorphism $\deg:W\to\Z$, and choose
$s\in W$ of degree one. Let $\rho:W\to\GL(k^n)$ be a semisimple
representation. Write $G$ and $H$ for the Zariski closures of $\rho(W)$
and $\rho(\ker\deg)$, respectively, as in
[definition-monodromy-groups], and put $F=\rho(s)$.

There are an integer $N>0$ and $z\in\GL_n(k)$ such that

$$
z\in Z(G(k))\cap H(k)F^N.
$$

Thus $z=hF^N$ for some $h\in H(k)$ and commutes with every element
of $G(k)$. Such a pair $(N,z)$ is called a positive central pair.
Over the algebraically closed field $k$, this is the required central
element of the arithmetic monodromy group. No topology on $W$ is needed.
