+++
kind  = "proof"
of    = "fix-lem-exchanges"
+++
Step 1: construction. By [def-exchange-projection],
$\operatorname{Ex}_*$ is the adjoint of the composite of the
canonical identification $Lf'^*Lg^*\cong Lg'^*Lf^*$ of the
cartesian square ([def-weil-pbc-cartesian-square]) with the
counit of $Lf^*\dashv Rf_*$ of [def-weil-derived-direct-image],
and $\operatorname{Ex}_!$ is represented by $\operatorname{Ex}_*$
for a proper compactification $\bar f$, followed by the
extension-by-zero identification
$L\bar g'^*j_!\cong j'_!Lg'^*$ of [def-exchange-projection]; at
a finite coefficient level the latter is the map of
[def-cbc-exchange-map], whose definition is the same composite.
Step 2: naturality. Each ingredient of these composites is a natural
transformation: the identification of the cartesian square is natural
in the square and the coefficient ring
([def-weil-pbc-cartesian-square]), the counit is natural by
[def-weil-derived-pullback-tensor-hom] and
[def-weil-derived-direct-image], and the extension-by-zero
identification is natural by [def-cbc-exchange-map] at finite
levels and by [det-def-sfb-open-base-change] on the condensed categories at
$\mathcal O_E,E,\Qlb$, where $\operatorname{Ex}_!$ is the morphism of
[det-def-sfb-shriek-base-change-morphism], an isomorphism by
[thm-cbc-complete-proetale] and [det-thm-sfb-shriek-base-change].
Step 3: identity and pasting. The identity and pasting equations
for $\operatorname{Ex}_*$ are the mate versions of the identity
and pasting laws of the identification of the cartesian square,
recorded in [lem-weil-pbc-exchange-identity-pasting] (finite
etale coefficients) and in
[sbc-lem-identity-and-base-change-composition] (derived level,
for successive base changes); the identity and horizontal and
vertical pasting for $\operatorname{Ex}_!$ are the corresponding
properties of its two ingredients, stated in
[thm-cbc-finite-torsion], together with
[lem-weil-pbc-exchange-identity-pasting] for the proper factor.
Step 4: smooth base
change. For smooth $g$, $\operatorname{Ex}_*$ is the derived
exchange morphism of [sbc-def-base-change-map] read on the same
square, and it is an isomorphism by
[sbc-thm-bounded-below-derived-smooth-base-change] at finite levels and by
[sk-thm-sbc-coefficients] at $\mathcal O_E$, $E$ and $\Qlb$ (condensed
$\Dbc$). Step 5: independence. The comparison
isomorphisms of [prop-compactification-coherence-detailed] identify the
two compactification candidates of $\operatorname{Ex}_!$ and are
compatible with the composition law of
[thm-sf-comp-composition] (the proper-composition
isomorphism and the extension-by-zero identification), so
$\operatorname{Ex}_!$ does not depend on the compactification.
