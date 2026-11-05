+++
kind = "proof"
of = "theorem-smooth-purity-all-admissible-coefficients--1"
order = 730003
uses = ["proposition-relative-dualizing-complex"]
+++
Put $W=X\times_Y X$ and let $\Delta:X\to W$ be the diagonal, a closed section of the first projection. Smooth base change identifies its section invariant $\Delta^*\omega_{p_1}$ with $\omega_f$. Étale coordinate frames along $\Delta$ give the Thom isomorphism for this section invariant. Composing the inverse of the first identification with the second gives
$\omega_f\simeq A_X(d)[2d]$, as in Proposition [proposition-relative-dualizing-complex].

These are the two steps `AlgebraicGeometry.Etale.nonempty_iso_sectionInvariant_diagonal` and `AlgebraicGeometry.Etale.nonempty_iso_sectionInvariant_twistShift_of_section`. The latter glues the classes of coordinate frames directly.
