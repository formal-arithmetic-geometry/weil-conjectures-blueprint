+++
kind = "proof"
of = "proposition-compatibility-purity-composition--1"
order = 801003
+++
*Orientation, finite coefficients.* Both orientations are maps of
rank one locally constant sheaves after removing twist and shift, so it
suffices to compare them on a cover of $X$ by charts. We choose charts
adapted to both morphisms. Choose an open $W\subset Y$ with
an étale $Z$-map $W\to\mathbf A^e_Z$, and an open $U\subset f^{-1}(W)$
with an étale $W$-map $U\to\mathbf A^d_W$. The composite
$U\to\mathbf A^d_W\to\mathbf A^d_{\mathbf A^e_Z}=\mathbf A^{d+e}_Z$ is
étale, and we order the coordinates of $\mathbf A^{d+e}_Z$ with the $e$
coordinates of $g$ first and the $d$ coordinates of $f$ last. Over this
chart, both orientations are adjoint to iterated integration along affine
lines, in the same order: first the $d$ coordinates of $f$, then the $e$
coordinates of $g$. Since the recursive construction preceding
(9.11) integrates the last coordinate first, the
integration on $\mathbf A^{d+e}_Z$ is exactly this composite. The diagonal
orientation agrees with this composite on charts. Hence the two
orientations agree on the cover.

*The maps (9.4), finite coefficients.* The two maps
agree because their transposes under the composite adjunction do. The
transpose of the iterated map applies the projection formula and the
counit for $f$, then the projection formula and the counit for $g$. The
transpose of the map for $g\circ f$ applies the projection formula for
$g\circ f$ and its counit. The two isomorphisms given by the projection
formula agree by associativity of tensor products. And the counit of the
composite adjunction is the composite of the two counits.

*Source:* the proof of Proposition [proposition-compatibility-purity-composition].
