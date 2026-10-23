+++
id = "sk-p-central"
kind = "proposition"
title = "A common positive-degree central element"
lean = ["AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.exists_isPositiveCentralPair"]
order = 3768
uses = ["sk-i-restriction", "sk-p-geometry", "sk-p-product"]
tags = ["sketch"]
+++
The degree map does not extend to $G$ when $F$ has finite order. To keep
track of degrees, we introduce the abstract group

$$
\widetilde G=H(\overline{\mathbf Q}_\ell)\rtimes_{\operatorname{Ad}F}\mathbf Z,
\qquad
(h,n)(h',n')=(hF^nh'F^{-n},n+n').
$$

It has a degree map $(h,n)\mapsto n$ and a homomorphism
$\widetilde G\to G(\overline{\mathbf Q}_\ell)$, $(h,n)\mapsto hF^n$, which
is injective on the subgroup of degree zero.

Let $V_1,\ldots,V_a$ be semisimple Weil representations and form the
monodromy groups of $V=\bigoplus_iV_i$. There are an integer $N>0$ and
$h\in H(\overline{\mathbf Q}_\ell)$ such that

$$
z=hF^N\in Z(G)(\overline{\mathbf Q}_\ell).
$$

The element $\widetilde z=(h,N)$ is central in $\widetilde G$. Its action
on each tensor construction on $V$ preserves every $W$-stable subquotient
and is scalar on each simple subquotient.

*Complement.* For a semisimple representation $\rho\colon W\to\GL_n(k)$
over any algebraically closed field $k$ of characteristic zero, a
*positive central pair* is $(N,z)$ with $N\in\mathbf Z_{>0}$ and
$z\in Z(G)(k)\cap H(k)F^N$; the argument below shows that one exists. The
coset condition does not assert that $G/H$ is infinite cyclic or that the
cosets $HF^N$ for different $N$ are distinct.
