+++
id = "sk-d-real-monodromy"
kind = "section"
title = "Arithmetic monodromy and a central representative"
order = 2793
uses = ["sk-d-real-setup", "sk-d-real-weil"]
+++
*Definition (sketch).*

An affine algebraic group over an algebraically closed field $K$ of
characteristic zero is a reduced closed subgroup of $\GL_n$; its equations
are polynomials in matrix entries and inverse determinant. A rational
representation is a regular group homomorphism into a general linear group.
An irreducible representation is nonzero and has no proper nonzero
invariant subspace. A representation is semisimple if it is a finite direct sum of irreducible
representations, with the zero representation allowed as an empty sum.
Write $G^\circ$ for the connected component of $1$ and $Z(G)$ for the
subgroup commuting with every element of $G$.
Dimension means the Krull dimension of the coordinate ring.
For the Weil representation
$\rho:W(C_0)\to\GL(V)$ over the coefficient field
$K=\Qlb$, put

$$
P=\pi_1(C),\qquad
H=\overline{\rho(P)}^{\mathrm{Zar}},\qquad
G=\overline{\rho(W(C_0))}^{\mathrm{Zar}},\qquad F=\rho(\gamma),
$$

where $\gamma$ has degree one. A positive central Frobenius representative
is a pair $(N,z)$ with $N\ge1$ an integer and
$z\in Z(G)\cap HF^N$; here $HF^N=\{hF^N:h\in H\}$ is an ordinary matrix coset.
def:monodromy; def:algebraic-representation; def:central-frobenius-representative

Uses: [sk-d-real-setup], [sk-d-real-weil]
