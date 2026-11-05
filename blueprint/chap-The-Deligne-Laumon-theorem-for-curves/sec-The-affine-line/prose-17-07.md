+++
id = "prose-17-07"
kind = "hidden"
title = "The affine line (1)"
order = 1293
+++
To pass from irreducible sheaves to arbitrary ones we show that $j_*$
is exact on sequences of pure sheaves of one weight. The reason is
a gap in weights. Let $0\to F_1\to F\to F_2\to0$ be an exact sequence of lisse sheaves on
a dense open $U$ of a curve $C$. Applying $j_*$ gives an exact sequence
$0\to j_*F_1\to j_*F\to j_*F_2\to R^1j_*F_1$, and $R^1j_*F_1$ is
supported on $C\setminus U$. Now suppose that $F_1$ and $F_2$ are pure of
weight $w$. Then, by Proposition [proposition-weights-j-boundary-points],
the source of the last map has weights at most $w$ at a point of
$C\setminus U$. On the other hand, by local duality, which we prove first, the stalk of
$R^1j_*F_1$ at such a point is the dual of the invariants of
$F_1^\vee$, twisted by $(-1)$, and this space has weights at least
$w+2$. Since a Frobenius-equivariant map between spaces with disjoint weights
is zero, $j_*$ is exact on such sequences
(Proposition [proposition-exactness-fixed-pure-weight]).

The hypothesis of equal weights is needed. In the Kummer extension
$0\to\overline{\mathbf Q}_\ell(1)\to F\to\overline{\mathbf Q}_\ell\to0$ of the chapter opening, $F_1=\overline{\mathbf Q}_\ell(1)$
has weight $-2$ and $F_2=\overline{\mathbf Q}_\ell$ has weight $0$, so at the origin the
stalks of $j_*\overline{\mathbf Q}_\ell$ and of $R^1j_*\overline{\mathbf Q}_\ell(1)$ both have weight $0$, and
the connecting map is indeed nonzero.

Exactness lets us extend Corollary [corollary-h-1-c-stalk-fourier]
from one irreducible sheaf with no geometric constituent of the form
$\mathcal L_{\psi(ax)}$ to a pure sheaf unramified at infinity
(Theorem [theorem-weight-bound-affine-line]) by induction along a
composition series. Each factor of the series is either geometrically
constant, and then $H^1_c=0$, or it satisfies the hypotheses of the corollary.
