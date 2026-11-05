+++
kind = "proof"
of = "corollary-functional-equation--10"
order = 1044013
uses = ["corollary-functional-equation--7", "theorem-poincare-duality-frobenius", "corollary-point-counting-zeta-function"]
+++
Apply [corollary-functional-equation--7] with $F=F_i$, $G=F_{2d-i}$ and
$c=q^d$. Since $c\ne0$, the similitude condition and the perfect pairing make
$F_i$ injective. Finite dimensionality makes it invertible, so its determinant
is nonzero. This is `LinearMap.isUnit_det_of_similitude`.

Map the polynomial identity along $\iota$ and take root multisets. The
nonzero constant factors do not change the roots; substitution of $q^dT$
divides the roots of the characteristic polynomial of $F_i$ by $q^d$.
The roots of $P_i$ are the inverses of these characteristic roots, by
`Polynomial.roots_reverse_of_monic`. Thus the roots of $P_{2d-i}$ are the
images of the roots of $P_i$ under $z\mapsto(q^dz)^{-1}$. This is the argument
of `LinearMap.roots_map_charpolyRev_of_similitude`, applied degree by degree
in `TraceDatum.roots_map_charpolyRev_rev`. Replacing $\iota(P_i)$ by the
complex image of $Q_i$ proves the second assertion.

For the geometric application, the mainline proof constructs the trace datum
from the point counts in [corollary-point-counting-zeta-function]. For smooth,
proper, geometrically connected $X_0$, it takes
$V_i=H^i(X,\overline{\mathbf Q}_\ell)$ and obtains the perfect pairings and
their Frobenius similitudes from [theorem-poincare-duality-frobenius], in the
form `AlgebraicGeometry.WeilSheaf.poincareDuality`. The integer factors are
constructed separately; the second assertion transfers the root identity to
them. No calculation with $\chi$, $D$ or $\varepsilon$ enters this transfer.
