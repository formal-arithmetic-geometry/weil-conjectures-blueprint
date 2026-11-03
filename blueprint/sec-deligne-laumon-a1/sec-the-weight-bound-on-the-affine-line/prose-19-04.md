+++
id = "prose-19-04"
kind = "hidden"
title = "The weight bound on the affine line"
order = 750
+++
Corollary [sk-c-dl-a1-hc1] bounds $H^1_c$ for one irreducible
sheaf with no geometric constituent of the form $\mathcal L_{\psi(ax)}$.
To pass to an arbitrary pure sheaf through a
composition series, we need $j_*$ to be exact on sequences of pure
sheaves of the same weight (Proposition [sk-p-dl-a1-exact]). This
follows from Proposition [sk-p-real-semi] and a local
duality at the boundary points, which we prove first.

The obstruction to exactness is the connecting map
$j_*F_2\to R^1j_*F_1$ at the points of $C\setminus U$. Its source has
weights at most $w$, and local duality identifies $R^1j_*F_1$ at such a
point with the dual of the invariants of $F_1^\vee$, twisted by $(-1)$,
which has weights at least $w+2$. A Frobenius-equivariant map between
spaces with disjoint weights is zero. The Kummer extension
$0\to \overline{\mathbf Q}_\ell(1)\to F\to \overline{\mathbf Q}_\ell\to0$ of the section opening shows that the
hypothesis of equal weights is needed: there $F_1=\overline{\mathbf Q}_\ell(1)$ has weight
$-2$ and $F_2=\overline{\mathbf Q}_\ell$ weight $0$, so at the origin both the stalk of
$j_*\overline{\mathbf Q}_\ell$ and that of $R^1j_*\overline{\mathbf Q}_\ell(1)$ have weight $0$, and the
connecting map is indeed nonzero. With exactness in hand, the bound for
a pure sheaf unramified at infinity (Theorem [sk-thm-dl-a1-upper])
follows by induction along a composition series from the bound for
its irreducible factors, which are either geometrically constant, with
$H^1_c=0$, or covered by Corollary [sk-c-dl-a1-hc1].
