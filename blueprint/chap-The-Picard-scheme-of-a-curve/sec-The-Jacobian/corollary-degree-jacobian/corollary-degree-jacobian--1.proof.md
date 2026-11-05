+++
kind = "proof"
of = "corollary-degree-jacobian--1"
order = 1552002
uses = []
+++
The degree of the trivial invertible sheaf is zero, and degree is additive
under tensor product by
`AlgebraicGeometry.Scheme.Modules.degree_tensorObj`. These identities
give the homomorphism `AlgebraicGeometry.Scheme.picDegreeHom`.

For a closed point $P$, its ideal sheaf $\mathcal I_P$ is invertible.
Since $k$ is algebraically closed, $P$ is a $k$-rational point and
$\dim_k\Gamma(P,\mathcal O_P)=1$. The formula for the degree of the
dual of an invertible ideal sheaf,
`AlgebraicGeometry.Scheme.IdealSheafData.IsInvertible.degree_dual_toModules_eq_one`,
therefore gives $\deg\mathcal O_C(P)=1$. This is
`AlgebraicGeometry.Scheme.picDegreeHom_ofClosedPoint`.

Properness makes $C$ quasi-compact, so nonemptiness gives a closed point
$P$. For every $d\in\mathbf Z$, the class
$[\mathcal O_C(P)]^d$ has degree $d$. Hence the degree is surjective.

Choose a class $g\in\operatorname{Pic}(C)$ of degree one and put
$\sigma(d)=g^d$. Then $\deg\sigma(d)=d$. Define

$$
e(L)=\bigl(\deg L,\,L\otimes\sigma(\deg L)^{-1}\bigr),
\qquad e^{-1}(d,M)=\sigma(d)\otimes M.
$$

The second component of $e(L)$ has degree zero. The two displayed maps
are inverse homomorphisms, and the first component of $e$ is the degree.
This is the construction in
`AlgebraicGeometry.Scheme.exists_mulEquiv_prod_ker_picDegreeHom`.
Taking $g=[\mathcal O_C(P)]$ gives the section
$d\mapsto[\mathcal O_C(dP)]$.
