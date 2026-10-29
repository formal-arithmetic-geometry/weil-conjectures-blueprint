+++
id = "prose-A2-01"
kind = "hidden"
title = "Overview of abelian varieties and the cube"
order = 457
+++
In this appendix all group schemes are of finite type over a field $k$
of arbitrary characteristic. For an abelian variety $A$ of dimension $g$ and an integer $n$
invertible in $k$, we show that $A[n]$ is finite étale of rank
$n^{2g}$, that the Tate module $T_\ell A$ is free of rank $2g$, and that over a finite
field Frobenius has no nonzero fixed vector on $T_\ell A$. Applied to
the Jacobian of a curve, which is constructed in
Appendix “Picard schemes and Jacobians”, the first two facts compute the cohomology of
a curve with coefficients $\mu_n$ in Appendix “Cohomology of curves”, and the
third proves that Frobenius has no fixed class in degree one
(Proposition [sk-prop-wrp-h1-no-fixed]) in the weight argument for rank-one
sheaves. Everything rests on the isomorphism
$[n]^*\mathcal N\simeq\mathcal N^{\otimes n^2}$ for a symmetric ample
invertible sheaf $\mathcal N$, a consequence of the theorem of the cube.
It forces $[n]$ to have finite fibres, and a comparison of degrees
shows that it has degree $n^{2g}$.

The theorem of the cube says that an invertible sheaf on a product of
three varieties is trivial as soon as it is trivial on three slices
through a point. It is the source of the formula for
$[n]^*\mathcal N$ below, and through it of everything in this appendix.
We prove it over a field $k$, following [Stacks, Tag 0BEZ](https://stacks.math.columbia.edu/tag/0BEZ). The proof has two steps: the set of points of the third
factor over which the sheaf is trivial is closed, by semicontinuity, and
it is open, by a computation of $H^0$ and $H^1$ near such a point.
