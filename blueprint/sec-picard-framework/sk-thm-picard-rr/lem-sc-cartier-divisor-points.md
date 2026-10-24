+++
id = "lem-sc-cartier-divisor-points"
kind = "lemma"
title = "Effective Cartier divisors on a smooth curve"
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.IsInvertible.exists_eq_idealSheaf"]
order = 716
uses = ["def-nagata-invertible-ideal", "lem-sc-dim0-finite", "lem-sc-regular-dim1-dvr", "lem-sc-smooth-regular"]
+++
Let $k$ be a field, $C$ a Noetherian integral scheme which is smooth of
relative dimension $1$ over $k$, and $D\subseteq C$ an effective
Cartier divisor, with
ideal sheaf $\mathcal I_D\subseteq\mathcal O_C$. Then there are
closed points $P_1,\dots,P_r$ of $C$ and integers
$n_1,\dots,n_r\geq1$ such that

$$
\mathcal I_{D,P_i}=(t_{P_i}^{n_i})\subseteq\mathcal O_{C,P_i}
\quad(1\leq i\leq r),\qquad
\mathcal I_{D,P}=\mathcal O_{C,P}\quad(P\notin\{P_1,\dots,P_r\}),
$$

where $t_P$ denotes a uniformizer of the discrete valuation ring
$\mathcal O_{C,P}$; equivalently
$\mathcal I_D=\prod_i\mathcal I_{P_i}^{n_i}$ with $\mathcal I_P$ the ideal
sheaf of the closed point $P$. Thus every effective Cartier divisor on $C$
is a finite sum $\sum_Pn_P[P]$ of closed points with positive integer
multiplicities.
