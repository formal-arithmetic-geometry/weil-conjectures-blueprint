+++
id = "example-running-example-duality--1"
kind = "example"
title = "The running example: duality (1)"
name_showing = false
order = 889001
aliases = ["bp-r268-1"]
+++
Let $C_0\colon y^2=x^3-x$ over $\mathbf F_3$ be the elliptic curve of
the introduction, and $C=C_0\times_{\mathbf F_3}k$. Since $C$ has genus
one, $H^1(C,\mathbf Q_\ell)$ is a plane. Indeed, by the Kummer sequence
$H^1(C,\mu_{\ell^n})=J[\ell^n](k)\simeq(\mathbf Z/\ell^n)^{2g}$ with $2g=2$
(Proposition [proposition-smooth-proper-curves-torsion-prime] and Corollary [corollary-torsion-jacobian-field-extension]).
Since $k$ is algebraically closed, $\mu_{\ell^n}\simeq\mathbf Z/\ell^n$, and passing to the limit
and inverting $\ell$ gives $\dim H^1(C,\mathbf Q_\ell)=2$.
For $d=1$ the middle pairing on $H^1$ is alternating and perfect, with values
in $\mathbf Q_\ell(-1)$ (Corollary [corollary-cup-product-pairing]). By
Theorem [theorem-poincare-duality-frobenius] it satisfies
$\langle Fx,Fy\rangle=3\langle x,y\rangle$. On a plane an alternating
form is unique up to a scalar, so $\langle Fx,Fy\rangle=\det(F)\langle
x,y\rangle$.
