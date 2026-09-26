+++
id = "sk-d-real-weil"
kind = "section"
title = "Weil sheaves and their representations"
order = 2577
uses = ["sk-d-real-setup"]
lean = ["AlgebraicGeometry.WeilGroup", "AlgebraicGeometry.WeilGroup.IsLisse"]
+++
*Definition (sketch).*

Choose a geometric base point on the curve $C$.
Let $P=\pi_1(C)$ be its profinite etale fundamental group, defined by
the fiber functor on finite etale covers. The Weil group $W(C_0)$ is the
inverse image of the integer powers of geometric Frobenius in
$\pi_1(C_0)\to\Gal(k/\Fq)$. It has an exact degree sequence

$$
1\longrightarrow P\longrightarrow W(C_0)
\xrightarrow{\deg}\mathbf Z\longrightarrow0.
$$

A lisse Weil $\Qlb$-sheaf is equivalently a finite-dimensional
representation $\rho:W(C_0)\to\GL(V)$ admitting a finite coefficient
field $E/\Ql$ and an $E$-model whose restriction to $P$ is continuous
and preserves an $\mathcal O_E$-lattice. The quotient $\mathbf Z$ is
discrete. Choose a degree-one lift $\gamma$ and write $F=\rho(\gamma)$.
Local $F_x$ acts through a conjugacy class of degree $e_x$.
A constructible Weil sheaf is lisse of finite rank on each stratum of a
finite stratification into locally closed subschemes.

Uses: [sk-d-real-setup]
