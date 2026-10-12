+++
id = "sk-d-real-weil"
kind = "definition"
title = "Weil sheaves and their representations"
order = 2881
uses = ["sk-d-real-setup"]
lean = ["AlgebraicGeometry.WeilGroup", "AlgebraicGeometry.WeilGroup.IsLisse"]
tags = ["sketch"]
+++
Choose a geometric base point on the curve $C$.
Let $P=\pi_1(C)$ be its profinite etale fundamental group, defined by
the fiber functor on finite etale covers. The Weil group $W(C_0)$ is the
inverse image of the integer powers of geometric Frobenius in
$\pi_1(C_0)\to\Gal(k/\Fq)$. It has an exact degree sequence

$$
1\longrightarrow P\longrightarrow W(C_0)
\xrightarrow{\deg}\mathbf Z\longrightarrow0.
$$

A representation $\rho:W(C_0)\to\GL(V)$ on a $\Qlb$-vector space $V$ is
lisse if its restriction to $P$ is continuous, i.e. in every basis of
$V$ the matrix coefficients of $\rho|_P$ are continuous functions on $P$
for the $\ell$-adic topology of $\Qlb$. A lisse Weil $\Qlb$-sheaf is
equivalently a finite-dimensional lisse representation of $W(C_0)$; for
finite-dimensional $V$ this amounts to a finite coefficient field
$E/\Ql$ and an $E$-model whose restriction to $P$ is continuous and
preserves an $\mathcal O_E$-lattice. The quotient $\mathbf Z$ is
discrete. Choose a degree-one lift $\gamma$ and write $F=\rho(\gamma)$.
For a closed point $x$, the local Frobenius $F_x$ is the geometric
Frobenius at $x$: the image in $W(C_0)$ of the geometric Frobenius
element of a decomposition group $D_x\subset\pi_1(C_0)$ at $x$, i.e. of
the image of the geometric Frobenius of $\Gal(\overline{k(x)}/k(x))$
under $\pi_1(x)\to\pi_1(C_0)$ for a chosen path from a geometric point
over $x$ to the base point. It has degree $e_x$, and it is well defined
up to conjugacy in $W(C_0)$.
A constructible Weil sheaf is lisse of finite rank on each stratum of a
finite stratification into locally closed subschemes.
