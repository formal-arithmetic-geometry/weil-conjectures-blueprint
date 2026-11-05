+++
kind = "proof"
of = "theorem-trace-formula-euler-product--1"
order = 1036007
uses = ["definition-weil-structure"]
+++
The two geometric points are related by an isomorphism of their sources
and a power of geometric Frobenius. Transport of global sections along
this square, followed by the iterated Weil isomorphism, gives a linear
isomorphism of stalks. Compatibility with iteration shows that it
intertwines the two Frobenius operators. For $m=0$, both operators are
the identity. This is
`AlgebraicGeometry.WeilSheaf.nonempty_equiv_stalkAt`.

Apply the result degree by degree to $\mathcal H^j(K)$. Characteristic
polynomials are invariant under conjugation, so every factor of
$\Delta_x(T)$, and hence the local alternating determinant, is unchanged.
