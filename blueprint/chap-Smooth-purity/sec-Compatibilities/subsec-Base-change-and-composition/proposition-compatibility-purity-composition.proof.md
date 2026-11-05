+++
kind = "proof"
of = "proposition-compatibility-purity-composition"
order = 801
uses = ["definition-trace-map"]
+++
As for base change, we compare orientations and the maps $\mu_{f,K}$, first
over any finite admissible ring and then for towers. The orientations are
compared on a chart adapted to both $f$ and $g$, where each is iterated
integration along affine lines, with the coordinates ordered so that the
two iterated integrals are the same. Applying $R\varprojlim$ then gives the
integral identity, and inverting $\ell$ and descending to a finite extension of
$\mathbf Q_\ell$ give the identities for coefficient fields.

*Orientation, finite coefficients.* Both orientations are maps of
rank one locally constant sheaves after removing twist and shift, so it
suffices to compare them on a cover of $X$ by charts, and we choose charts
adapted to both morphisms. That is, choose an open $W\subset Y$ with
an étale $Z$-map $W\to\mathbf A^e_Z$, and an open $U\subset f^{-1}(W)$
with an étale $W$-map $U\to\mathbf A^d_W$. Then the composite
$U\to\mathbf A^d_W\to\mathbf A^d_{\mathbf A^e_Z}=\mathbf A^{d+e}_Z$ is
étale, and we order the coordinates of $\mathbf A^{d+e}_Z$ with the $e$
coordinates of $g$ first and the $d$ coordinates of $f$ last. Over this
chart, both orientations are adjoint to iterated integration along affine
lines, in the same order: first the $d$ coordinates of $f$, then the $e$
coordinates of $g$. Since the recursive construction preceding
(9.11) integrates the last coordinate first, the
integration on $\mathbf A^{d+e}_Z$ is exactly this composite. Each diagonal
orientation agrees on a chart with the integration in its coordinates, so the two
orientations agree on the cover.

*The maps $\mu_{f,K}$, finite coefficients.* The two maps
agree because their transposes under the composite adjunction do. Indeed, the
transpose of the iterated map applies the projection formula and the
counit for $f$, then the projection formula and the counit for $g$, whereas the
transpose of the map for $g\circ f$ applies the projection formula for
$g\circ f$ and its counit. The two isomorphisms given by the projection
formula agree by associativity of tensor products, and the counit of the
composite adjunction is the composite of the two counits.

*Towers.* The same two arguments apply in the category of towers, with its maps
$\gamma_{f,\bullet}$ and its composite adjunction. Since the orientations are maps of
sheaves of towers of rank one, we may test their equality at each level, while the maps
(9.4) are compared by the same transposition.
