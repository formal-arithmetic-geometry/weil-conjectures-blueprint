+++
kind = "proof"
of = "lemma-connected-components-images-homomorphisms--3"
order = 1720007
uses = ["proposition-cartier-s-theorem--2"]
+++
The matrix form of the dimension formula in
[proposition-cartier-s-theorem--2], proved as
`AlgebraicGeometry.GeneralLinearGroup.finrank_lieSubalgebra`, gives
$$
\dim\operatorname{Lie}(V(I))=\dim k[\GL_n]/I,
\qquad
\dim\operatorname{Lie}(V(J))=\dim k[\GL_n]/J.
$$
It identifies the matrix Lie algebra with the dual of the
cotangent space at the identity and uses
`HopfAlgebra.finrank_cotangent_eq_ringKrullDim` for the quotient
Hopf algebra. Equality of the Lie algebras therefore gives equality
of the two Krull dimensions.

The ring $k[\GL_n]$ is of finite type over $k$, so its dimension
is finite. Since $I$ is prime and $I\subseteq J$, equality of
the quotient dimensions forces $J=I$, by
`Matrix.GeneralLinearGroup.eq_of_le_of_ringKrullDim_eq`.
