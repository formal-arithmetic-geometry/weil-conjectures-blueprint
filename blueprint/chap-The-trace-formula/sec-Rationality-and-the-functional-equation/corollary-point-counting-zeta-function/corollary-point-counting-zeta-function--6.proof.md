+++
kind = "proof"
of = "corollary-point-counting-zeta-function--6"
order = 1039012
uses = ["corollary-point-counting-zeta-function--3", "corollary-point-counting-zeta-function--4"]
+++
For $d>0$, the factor $(1-T^d)^{-1}$ is the image of the integral
series whose coefficient of $T^n$ is $1$ if $d\mid n$ and $0$
otherwise. The images of integral power series form a subring of
$\mathbf Q[[T]]$. By [corollary-point-counting-zeta-function--4], each
coefficient of $Z(X_0,T)$ occurs in a finite product of these factors,
and is therefore integral. This is
`AlgebraicGeometry.Scheme.Hom.coeff_zetaSeries_mem_range`.
Choosing the integral coefficients gives $Z_{\mathbf Z}$.

The exponential in [corollary-point-counting-zeta-function--3] has
constant coefficient $1$, since its argument has constant coefficient
zero. Injectivity of $\mathbf Z\longrightarrow\mathbf Q$ then gives
$Z_{\mathbf Z}(0)=1$.
