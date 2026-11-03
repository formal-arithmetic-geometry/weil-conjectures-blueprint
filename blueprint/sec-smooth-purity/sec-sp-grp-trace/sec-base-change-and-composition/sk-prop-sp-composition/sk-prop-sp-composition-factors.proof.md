+++
kind = "proof"
of = "det-sp-composition-factors"
+++
(1) Choose coordinates for $g$, $Y\supset V\to\mathbf A^e_Z$ étale, and
coordinates for $f$ over $V$, $X\supset U\to\mathbf A^d_V$ étale; then
$U\to\mathbf A^d_V\to\mathbf A^{d+e}_Z$ is a chart for $g\circ f$. By
[det-sp-orientation-charts], on these charts each diagonal orientation is the
affine-space orientation, i.e. adjoint to iterated integration along affine
lines. Both orientations of $g\circ f$ (the direct one and the composite one)
are adjoint to integration along the $d$ coordinates of $f$ followed by the $e$
coordinates of $g$: the integration on $\mathbf A^{d+e}$ is defined recursively
by exactly this composite, and the composite law of
[prop-pur-affine-space-composition-law] shows that regrouping the coordinates
introduces no sign. So the two orientations agree on each chart. After removing
the common twist and shift, both are maps of locally constant rank-one sheaves
(tower sheaves for towers, where equality is tested levelwise); local agreement
implies equality.

(2) Transpose both maps under the composite adjunction $R(g\circ f)_!\dashv f^!g^!$
of [det-sp-composition-comparisons]. The transpose of the iterated tensor map
applies the projection formula for $f$ and the counit for $f$, then the
projection formula for $g$ and the counit for $g$. The transpose of the tensor
map for $g\circ f$ applies the projection formula for $g\circ f$ and its counit.
The projection formula for $g\circ f$ is the composite of those for $f$ and $g$
(associativity of tensor products and the composition isomorphism for
$R(-)_!$), and the counit of the composite adjunction is the composite of the
two counits. Hence the transposes agree, and so do the maps.

The final identity follows by writing each $\gamma$ as inverse orientation
followed by tensor map, and inserting (1) and (2), together with naturality of
the tensor map for $f$ with respect to $\gamma_g(K)$.
