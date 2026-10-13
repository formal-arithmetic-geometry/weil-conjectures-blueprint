+++
id = "sk-d-tangent"
kind = "definition"
title = "Tangent spaces and rational actions"
order = 2824
uses = ["sk-d-geometry", "sk-d-lie"]
lean = ["AlgebraicGeometry.tangentGroup", "AlgebraicGeometry.GrpObj.Lie", "AlgebraicGeometry.GeneralLinearGroup.lieAlgebraEquivMatrix", "AlgebraicGeometry.GeneralLinearGroup.RationalHom", "AlgebraicGeometry.GeneralLinearGroup.RationalHom.differential"]
tags = ["sketch"]
+++
For an affine variety $X$ and a $k$-point $x$,
let $\mathfrak m_x$ be the maximal ideal of functions vanishing at $x$.
The tangent space is $T_xX=(\mathfrak m_x/\mathfrak m_x^2)^\vee$.
A regular map induces a linear map on these spaces, its differential.
For a group scheme $G$ over $k$ with unit section $e$ set
$\Lie(G)=\operatorname{Hom}_k(e^*\Omega^1_{G/k},k)=T_1G$, which is also the
tangent group $\ker(G(k[\varepsilon]/\varepsilon^2)\to G(k))$. For a matrix
group, equivalently,
$X\in\Lie(G)$ when $1+\varepsilon X\in G(k[\varepsilon]/\varepsilon^2)$.
Here $R$-points mean matrices satisfying the defining equations over
the commutative $k$-algebra $R$. The bracket is $XY-YX$; in particular
$\Lie(\GL_n)=\mathfrak{gl}_n(k)$ as Lie algebras.
A rational representation of a group scheme $G$ over $k$ on $M=k^m$ is a
homomorphism of group schemes $r:G\to\GL(M)=\GL_m$ over $k$;
its differential $dr:\Lie(G)\to\mathfrak{gl}_m(k)$ is a Lie representation.
The adjoint action is $\operatorname{Ad}(g)X=gXg^{-1}$, with differential
$\operatorname{ad}(Y)X=[Y,X]$.

A finite-type matrix group scheme is a closed subscheme of $\GL(V)$,
cut out by a finitely generated ideal, possibly nonradical, such that
the regular group operations restrict to it. Its coordinate algebra
therefore need not initially be reduced. At a closed point, smoothness
over $k$ means that the dimension of the tangent space equals the
Krull dimension of the local ring; such a local ring is called regular.
The local ring is the localization of the coordinate algebra at the
point's maximal ideal.
