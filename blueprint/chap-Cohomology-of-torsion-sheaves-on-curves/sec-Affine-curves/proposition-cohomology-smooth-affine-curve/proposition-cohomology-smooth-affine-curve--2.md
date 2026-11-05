+++
id = "proposition-cohomology-smooth-affine-curve--2"
kind = "proposition"
title = "Kummer computation on a smooth affine curve"
order = 1582003
aliases = ["bp-r493-2"]
lean = ["AlgebraicGeometry.IsConnectedCurve.sheafH_constantZMod_of_isAffine"]
+++
Let $U$ be a smooth affine connected curve over an algebraically closed
field $k$, and let $n\geq1$ be invertible in $k$. Choose a primitive
$n$th root of unity to identify $\mu_n$ with the constant sheaf $\mathbf Z/n$.
Then

$$
H^0(U,\mathbf Z/n)\simeq\mathbf Z/n,
\qquad H^q(U,\mathbf Z/n)=0\quad(q>1).
$$

There exist homomorphisms giving a short exact sequence

$$
0\longrightarrow
\mathcal O(U)^\times/(\mathcal O(U)^\times)^n
\longrightarrow H^1(U,\mathbf Z/n)
\longrightarrow\operatorname{Pic}(U)[n]\longrightarrow0,
$$

and both outer groups are finite. Here the Picard group is identified
with $H^1(U,\mathbf G_m)$. Under the chosen identification of coefficients,
the degree zero calculation gives $H^0(U,\mu_n)\simeq\mu_n(k)$.
