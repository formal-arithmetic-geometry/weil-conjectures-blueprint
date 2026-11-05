+++
id = "theorem-purity-real-sheaves-curves--1"
kind = "theorem"
title = "Purity of real sheaves on curves (1)"
name_showing = false
order = 1169001
aliases = ["bp-r359-1"]
lean = ["AlgebraicGeometry.WeilGroup.isPunctuallyPure_of_isConstituent_of_isReal", "AlgebraicGeometry.WeilSheaf.IsReal.exists_isPunctuallyPureOfWeight_cokernel_detWeight"]
+++
Let $C_0$ be a smooth geometrically connected curve over $\mathbf F_q$,
and let $\mathcal G$ be an $\iota$-real lisse Weil sheaf on $C_0$.
Suppose that $\mathcal G_1\subseteq\mathcal G_2\subseteq\mathcal G$
are lisse Weil subsheaves and that
$\mathcal V=\mathcal G_2/\mathcal G_1$ is irreducible lisse.
Then $\mathcal V$ is punctually $\iota$-pure of weight
$\gamma=\operatorname{dw}_\iota(\mathcal V)$. At every closed point $x$,

$$
\operatorname{rank}(\mathcal V)\gamma
=\frac{2\log\bigl|\iota\det(\operatorname{Frob}_x\mid\mathcal V_{\bar x})\bigr|}{\log q_x}.
$$

Equivalently, if $\rho$ is an $\iota$-real lisse representation of
$W(C_0)$ and $\sigma$ is an irreducible constituent of $\rho$ of
determinant weight $\gamma$, then $\sigma$ is punctually
$\iota$-pure of weight $\gamma$.
