+++
kind  = "proof"
of    = "lem-exc-proetale-closed-fully-faithful"
+++
The assertion is local on affine opens of $X$, by the unit and counit
compatibility of [lem-exc-closed-localization]. On one such open the
presheaf formula of [lem-exc-closed-inverse-image-formula] gives
$$
 P_{i_*G}(V)=(i_*G)(v(V))=G(u(v(V)))=G(V),
$$
using [lem-exc-closed-lift-reduction] for the last equality. This presheaf
is already the sheaf $G$. Its sheafification and its map to $G$ are
therefore the identity. The adjunction calculation in that formula
identifies this map with the counit of the pro-etale operations. These
affine identifications agree on overlaps, since they are counits, and glue.
An adjunction has fully faithful right adjoint precisely when its counit is
an isomorphism, giving the assertion.
