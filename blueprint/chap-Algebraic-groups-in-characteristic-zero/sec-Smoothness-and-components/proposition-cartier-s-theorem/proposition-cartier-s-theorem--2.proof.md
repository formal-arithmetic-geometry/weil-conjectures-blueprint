+++
kind = "proof"
of = "proposition-cartier-s-theorem--2"
order = 1717002
uses = []
+++
Let $e:B\to k$ be the counit and $\mathfrak m=\ker e$. A linear form
on $\mathfrak m/\mathfrak m^2$ gives a matrix tangent vector by evaluating
the coordinate functions $x_{ij}-\delta_{ij}$. This map is injective,
and its image consists exactly of the matrices $X$ with
$1+\varepsilon X\in G(k[\varepsilon]/(\varepsilon^2))$. Since the
cotangent space is finite-dimensional, it and its dual have the same
dimension. These steps are
`AlgebraicGeometry.GeneralLinearGroup.finrank_cotangent_eq_finrank_range_dualCotangentToMatrixₗ`
and `AlgebraicGeometry.GeneralLinearGroup.range_dualCotangentToMatrixₗ`.

It remains to compute the dimension of $\mathfrak m/\mathfrak m^2$.
The comultiplication extends every tangent vector to an invariant
derivation. In characteristic zero, lifts of a basis of
$\mathfrak m/\mathfrak m^2$ are algebraically independent modulo the
prime ideal $\bigcap_{r\geq0}\mathfrak m^r$. This gives
$\dim_k(\mathfrak m/\mathfrak m^2)\leq\dim B$. For the reverse
inequality, pass to an algebraic closure and translate each closed
point to the identity. The Krull dimension is then bounded by the
height of the augmentation ideal, which is bounded by the number of
generators modulo its square. These are the two inequalities combined
in `HopfAlgebra.finrank_cotangent_eq_ringKrullDim`. Substituting the
matrix description of the tangent space gives the result.
