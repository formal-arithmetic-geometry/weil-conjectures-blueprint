+++
id = "def-zl-localized-coordinates"
kind = "definition"
title = "Coordinates on a principal open of an affine base"
order = 3127
lean = ["AlgebraicGeometry.Scheme.Hom.toIteratedAffineLine"]
uses = ["def-sbc-affine-space", "def-weil-pbc-scheme-conventions"]
+++
Let $g:X\to S$ be a morphism of schemes, $d\geq0$, and
$t=(t_1,\ldots,t_d)\in\Gamma(X,\mathcal O_X)^d$. Write $\mathbf A^d_S$
for the $d$-fold relative affine line over $S$, defined by
$\mathbf A^0_S=S$ and $\mathbf A^d_S=\mathbf A^1_{\mathbf A^{d-1}_S}$,
with its projection to $S$ the composition of the $d$ affine-line
projections. Define the $S$-morphism

$$
\nu_t:X\longrightarrow\mathbf A^d_S
$$

recursively: for $d=0$, $\nu_t=g$; for $d\geq1$, $\nu_t$ is the
morphism to $\mathbf A^1_{\mathbf A^{d-1}_S}$ lying over
$\nu_{(t_2,\ldots,t_d)}:X\to\mathbf A^{d-1}_S$ whose coordinate on the
outermost affine line is $t_1$.

In the case of interest, $A$ is a domain, $B$ a finitely generated
commutative $A$-algebra, $0\neq s\in A$, $A_s=A[1/s]$,
$B_s=B\otimes_A A_s$, $X=\operatorname{Spec}B_s$ and
$S=D(s)=\operatorname{Spec}A_s$; then $\nu_t:\operatorname{Spec}B_s\to
\mathbf A^d_{D(s)}$ is given by the algebra homomorphism
$A_s[T_1,\ldots,T_d]\to B_s$, $T_i\mapsto t_i$. Here affine space has
the meaning of relative affine space; the map is finite precisely when
$B_s$ is a finitely generated module over that polynomial ring.
No finiteness is included in the choice of $t$.
