+++
id = "corollary-degree-jacobian--1"
kind = "corollary"
title = "Splitting the degree homomorphism"
name_showing = false
order = 1552001
aliases = ["bp-r484-1"]
lean = ["AlgebraicGeometry.Scheme.picDegreeHom", "AlgebraicGeometry.Scheme.picDegreeHom_ofClosedPoint", "AlgebraicGeometry.Scheme.surjective_picDegreeHom", "AlgebraicGeometry.Scheme.exists_mulEquiv_prod_ker_picDegreeHom"]
uses = []
+++
Let $C$ be a nonempty smooth proper curve over an algebraically closed
field $k$. The degree

$$
\deg[\mathcal L]=\chi(C,\mathcal L)-\chi(C,\mathcal O_C)
$$

defines a homomorphism $\operatorname{Pic}(C)\to\mathbf Z$. For every
closed point $P$ of $C$, the class of
$\mathcal O_C(P)=\mathcal I_P^\vee$ has degree one. The degree is
surjective, and there is a group isomorphism

$$
e:\operatorname{Pic}(C)\xrightarrow{\sim}
\mathbf Z\times\ker(\deg),
\qquad \operatorname{pr}_1\circ e=\deg.
$$

Thus the degree sequence splits without assuming that $C$ is connected.
