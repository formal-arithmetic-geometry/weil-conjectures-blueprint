+++
id = "sk-p-real-integral"
kind = "proposition"
title = "Integral models"
order = 2935
uses = ["sec-algebraic-groups-lie-algebras", "sk-d-real-weil", "sk-i-real-sheaves"]
lean = ["AlgebraicGeometry.WeilGroup.IsLisse.exists_lattice"]
tags = ["sketch"]
+++
Keep the notation of [sk-i-real-sheaves], and let $U_0\subseteq C_0$ be a
nonempty open subscheme with base change $U$ and geometric fundamental group
$\pi_1(U)$, acting through the restriction map $W(U_0)\to W(C_0)$ of Weil
groups. An $\mathcal O_E$-lattice in a $\Qlb$-vector space $V$ means a free
$\mathcal O_E$-submodule of $V$ of rank $\dim_{\Qlb}V$ that spans $V$ over
$\Qlb$.

Let $(V,\rho)$ be a lisse Weil sheaf on $C_0$, i.e. a lisse representation
of $W(C_0)$ on a finite-dimensional $\Qlb$-vector space $V$. Then there are
a finite extension $E/\Ql$ inside $\Qlb$ and an $\mathcal O_E$-lattice
$L\subset V$ with

$$
\rho(\pi_1(U))L\subseteq L,
$$

such that the image of $\pi_1(U)$ in $\operatorname{Aut}(L/\mathfrak m_E^nL)$ is
finite for every $n$.
