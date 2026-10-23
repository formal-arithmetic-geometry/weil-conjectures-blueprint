+++
kind  = "proof"
of    = "lem-exc-closed-localization"
+++
By the slice identification in
[lem-weil-pbc-proetale-restriction-injectives], restriction along a weakly
etale map is evaluation on objects over it. For an object $T\to W$ of the
slice, both $(w^*g_*G)(T)$ and $(g'_*w'^*G)(T)$ are the value of $G$ on
$T\times_XZ=T\times_WW'$, the two descriptions of this fibre product being
identified by the cartesian square [def-weil-pbc-cartesian-square]. Thus both
functors are precomposition with two functors of sites that are isomorphic
via the canonical comparison of fibre products, and the base change map is
induced by this isomorphism; hence it is an isomorphism. Its mate under the
restriction adjunctions is computed sectionwise: the units restrict sections
to the slices and the counits evaluate them, and unwinding these formulas
gives exactly the isomorphism of direct images along the two composites
$g\circ w'$ and $w\circ g'$ of the square. Finally, inverse images are left
adjoint to direct images, and direct images compose strictly up to canonical
isomorphism; by uniqueness of adjoints $(g\circ w')^*\cong w'^*g^*$ and
$(w\circ g')^*\cong g'^*w^*$, and $g\circ w'=w\circ g'$ gives the
agreement of the two composites of inverse images.
