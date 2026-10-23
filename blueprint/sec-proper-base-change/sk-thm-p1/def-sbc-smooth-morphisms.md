+++
id = "def-sbc-smooth-morphisms"
kind = "definition"
title = "Smooth morphisms"
order = 1590
lean = ["AlgebraicGeometry.Smooth", "Algebra.Smooth", "Algebra.FormallySmooth", "AlgebraicGeometry.SmoothOfRelativeDimension", "Algebra.IsStandardSmoothOfRelativeDimension", "AlgebraicGeometry.Etale", "AlgebraicGeometry.Etale.iff_smoothOfRelativeDimension_zero", "AlgebraicGeometry.smooth_iff_flat_and_smooth_fiber", "AlgebraicGeometry.Smooth.exists_smoothOfRelativeDimension_resLE", "AlgebraicGeometry.Smooth.isLocallyConstant_topologicalKrullDimAt_asFiber", "AlgebraicGeometry.topologicalKrullDimAt_eq_of_smoothOfRelativeDimension"]
uses = ["def-weil-pbc-scheme-conventions"]
+++
An algebra $A$ over a commutative ring $R$ is *smooth* if it is of finite presentation and *formally smooth*:
$\Omega_{A/R}$ is a projective $A$-module and $H_1(L_{A/R})=0$; equivalently, for every $R$-algebra $B$ and every
nilpotent ideal $I\subseteq B$, every $R$-algebra map $A\to B/I$ lifts to an $R$-algebra map $A\to B$. A morphism of
schemes $f:X\to Y$ is *smooth* if for all affine opens $U\subseteq Y$ and $V\subseteq f^{-1}(U)$ the ring map
$\mathcal O_Y(U)\to\mathcal O_X(V)$ is smooth.

The morphism $f$ is *smooth of relative dimension $n$* if every $x\in X$ has affine open neighbourhoods $V\ni x$ and
$U\supseteq f(V)$ such that $\mathcal O_X(V)$ is standard smooth of relative dimension $n$ over $\mathcal O_Y(U)$:
$\mathcal O_X(V)\cong\mathcal O_Y(U)[x_1,\dots,x_{n+c}]/(f_1,\dots,f_c)$ with the determinant of
$(\partial f_i/\partial x_{n+j})_{1\le i,j\le c}$ invertible in the quotient. The morphism $f$ is *étale* if for all
affine opens $U\subseteq Y$ and $V\subseteq f^{-1}(U)$ the ring map $\mathcal O_Y(U)\to\mathcal O_X(V)$ is étale.

Étale morphisms are exactly the morphisms smooth of relative dimension zero. A morphism locally of finite
presentation is smooth if and only if it is flat and all its fibres $X_y\to\operatorname{Spec}\kappa(y)$ are
smooth. If $f$ is smooth, every point has an open neighbourhood on which $f$ is smooth of some relative dimension
$d$; a scheme smooth of relative dimension $n$ over a field has dimension $n$ at every point, and the function
$x\mapsto\dim_x X_{f(x)}$ is locally constant on $X$.
