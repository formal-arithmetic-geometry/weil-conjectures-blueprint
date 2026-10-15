+++
kind = "proof"
of = "sk-prop-sp-composition"
uses = ["sk-prop-an", "sk-prop-sp-orientation", "sk-prop-sp-tower-geometric"]
+++
As for base change, we compare orientations and tensor maps, first over any
finite admissible ring and then for towers. $R\varprojlim$ gives the integral
identity, and inversion of $\ell$ and descent to a finite extension of $\Ql$
give the field identities.

*Orientation, finite coefficients.* Choose coordinates for $g$, and coordinates
for $f$ over such a chart. Over the resulting tower of affine-space
projections, both orientations are adjoint to iterated integration along affine
lines, in the same order: first the $d$ coordinates of $f$, then the $e$
coordinates of $g$. The integration on $\mathbf A^{d+e}$ is defined by exactly
this composite (the recursive construction of affine-space integration in
[sk-prop-an]), and the diagonal orientation agrees with this normalization on
charts ([sk-prop-sp-orientation]), so the two orientations agree locally. After
removing the common twist and shift they are maps of locally constant rank-one
sheaves, so local agreement implies equality.

*Tensor maps, finite coefficients.* Transpose both tensor maps under the
composite adjunction between $\Dctf(X,\Lambda)$ and $\Dctf(Z,\Lambda)$. The
transpose of the iterated tensor map applies the projection formula for $f$ and
the counit for $f$, then the projection formula for $g$ and the counit for $g$.
The transpose of the tensor map for $g\circ f$ applies the projection formula
for $g\circ f$ and its counit. The two projection-formula isomorphisms agree by
associativity of tensor products, and the counit of the composite adjunction is
the composite of the two counits. Hence the transposes, and with them the
tensor maps, agree.

*Towers.* In the tower category $\Dctf(X_{\mathrm{proét}},\mathcal O_E/\ell^\bullet)$ of
[sk-prop-sp-tower-geometric], with its purity maps and its composite
adjunction, the two arguments apply as follows: the orientations are maps of
rank-one tower sheaves, whose equality can be tested at each level, and the
tensor maps are compared by the same transposition.
