+++
kind = "proof"
of = "sk-prop-sp-composition"
uses = ["sk-prop-an", "sk-prop-sp-orientation", "sk-prop-sp-tower-geometric"]
+++
As for base change, we compare orientations and the maps (10.9), first
over any finite admissible ring and then for towers.
Applying $R\varprojlim$ gives the integral identity, and inverting $\ell$
and descending to a finite extension of $\Ql$ give the identities
for coefficient fields.

*Orientation, finite coefficients.* Choose an open $W\subset Y$ with
an étale $Z$-map $W\to\mathbf A^e_Z$, and an open $U\subset f^{-1}(W)$
with an étale $W$-map $U\to\mathbf A^d_W$. The composite
$U\to\mathbf A^d_W\to\mathbf A^d_{\mathbf A^e_Z}=\mathbf A^{d+e}_Z$ is
étale, and we order the coordinates of $\mathbf A^{d+e}_Z$ with the $e$
coordinates of $g$ first and the $d$ coordinates of $f$ last. Over this
chart, both orientations are adjoint to iterated integration along affine
lines, in the same order: first the $d$ coordinates of $f$, then the $e$
coordinates of $g$. Since the recursive construction preceding
(10.7) integrates the last coordinate first, the
integration on $\mathbf A^{d+e}_Z$ is exactly this composite, and the
diagonal orientation agrees with this composite on charts. Thus the
two orientations agree locally. After removing the common twist and
shift, they are maps of locally constant sheaves of rank one, so local
agreement implies equality.

*The maps (10.9), finite coefficients.* We transpose both maps
under the composite adjunction. The transpose of the iterated map
applies the projection formula for $f$ and the counit for $f$, then the
projection formula for $g$ and the counit for $g$. The transpose of the
map for $g\circ f$ applies the projection formula for $g\circ f$
and its counit. The two isomorphisms given by the projection formula agree by
associativity of tensor products, and the counit of the composite
adjunction is the composite of the two counits. Therefore the transposes
agree, and with them the two maps.

*Towers.* The same two arguments apply in the category of towers, with its maps
$\gamma_{f,\bullet}$ and its composite adjunction. Since the orientations are maps of
sheaves of towers of rank one, we may test their equality at each level. The maps
(10.9) are compared by the same transposition.
