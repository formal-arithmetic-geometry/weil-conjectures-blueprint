+++
kind = "proof"
of = "theorem-picard-scheme-jacobian-over-separably--2"
order = 1549007
uses = ["theorem-picard-scheme-jacobian-over-separably--1", "theorem-hilbert-schemes-points-smooth-curve", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension"]
+++
First consider a scheme representing $\operatorname{Pic}^g_{C/k}$.
By [theorem-picard-scheme-jacobian-over-separably--1], it is an open
subscheme of the smooth separated Picard scheme, so it is smooth of
dimension $g$ and separated.

The universal divisor gives an Abel map
$\operatorname{Hilb}^g_{C/k}\to\operatorname{Pic}^g_{C/k}$.
To lift a point of the target, pass to an algebraic closure of its
residue field. Over this field the Picard class has an invertible
sheaf representative. Riemann–Roch gives a nonzero section of any
invertible sheaf of degree $g$. Its zero divisor has degree $g$ and
maps to the given class. This proves surjectivity, as formalized in
`AlgebraicGeometry.exists_surjective_of_representableBy_picardFunctorDegree_genus`.

The Hilbert scheme is proper and geometrically integral by
[theorem-hilbert-schemes-points-smooth-curve]. Its surjective image
is universally closed; together with separatedness and local finite
type this proves properness of $\operatorname{Pic}^g_{C/k}$. The
same map gives geometric irreducibility, and smoothness gives
geometric reducedness, hence geometric integrality.

Choose $P_0\in C(k)$. Tensoring with invertible sheaves
$\mathcal O_C(nP_0)$ identifies the degree components. Lean uses
`AlgebraicGeometry.nonempty_iso_of_representableBy` and
`AlgebraicGeometry.exists_iso_representableBy_picardFunctorDegree_genus`
to transport the three properties from degree $g$ to every degree $d$.
