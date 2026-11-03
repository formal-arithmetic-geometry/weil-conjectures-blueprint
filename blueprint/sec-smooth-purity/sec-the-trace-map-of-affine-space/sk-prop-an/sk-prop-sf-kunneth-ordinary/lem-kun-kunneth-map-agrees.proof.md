+++
kind  = "proof"
of    = "lem-kun-kunneth-map-agrees"
+++
We verify (a); the proof of (b) is identical, replacing
[lem-kun-0f0f] by [lem-kun-0f0g], [thm-weil-pbc-bounded-below]
by [lem-kun-0f0c], [lem-kun-0f0e] by
[lem-kun-0f12] and [lem-kun-leray-bdd] by
[lem-kun-leray-unbdd]. It suffices to compare adjoints under
$c^{-1}\dashv Rc_*$ (writing $c:X\times_kY\to\Spec(k)$). By
[def-kun-kunneth-map] the adjoint of $\kappa_{E,K}$ is
$(\varepsilon_f\otimes\varepsilon_g)\circ\mathrm{mon}$. Each arrow
in the definition of $\theta$ is the mate of an identification
built from the adjunction data of
[def-weil-pbc-inverse-image] and of
[def-kun-derived-tensor]: the first is the comparison
$\RGamma\circ R\operatorname{pr}_{2,*}\cong\RGamma$ (an instance of
the Leray composition [lem-kun-leray-bdd]); the second is the
projection formula map of [lem-kun-0f0f], which is by
definition the mate of the unit–monoidality composite of
[lem-kun-inverse-image-monoidal]; the third is
the inverse of the proper base change map of
[thm-weil-pbc-bounded-below], itself the mate of
$\varepsilon_f$ by [def-kun-unbounded-exchange]; the fourth is
the map of [lem-kun-0f0e], whose mate is
$\mathrm{id}\otimes\eta_g$ for the unit $\eta_g$ of
[def-weil-pbc-inverse-image] (using
[lem-kun-tensor-unit] and [lem-kun-pullback-constant] for
the constant objects); the fifth is the symmetry
[lem-kun-tensor-sym], whose mate is again the symmetry.
Applying $c^{-1}$ to $\theta\circ\kappa_{E,K}$ therefore yields the
composite of the corresponding mates, and an elementary cancellation
of each unit against the adjacent counit – all compatibilities being
instances of the pasting law
[lem-weil-pbc-exchange-identity-pasting] and of the naturality of
[lem-kun-unbounded-exchange-natural] – leaves exactly
$(\varepsilon_f\otimes\varepsilon_g)\circ\mathrm{mon}$, the adjoint
of $\mathrm{id}$. Since the adjunction bijection is injective,
$\theta\circ\kappa_{E,K}=\mathrm{id}$, and as $\theta$ is an
isomorphism so is $\kappa_{E,K}$.
