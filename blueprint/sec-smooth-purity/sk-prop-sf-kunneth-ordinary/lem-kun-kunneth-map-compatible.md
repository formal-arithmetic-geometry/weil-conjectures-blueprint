+++
id = "lem-kun-kunneth-map-compatible"
kind = "lemma"
title = "Compatibility of the Kunneth map with the cartesian identifications"
order = 1785
uses = ["def-kun-kunneth-map", "def-weil-pbc-cartesian-square"]
+++
Let $f:X\to S$ and $g:Y\to S$ be morphisms of schemes and let
$\square=(f,f',g,g',\alpha)$ be the corresponding cartesian square
with its chosen identification, as in
[def-weil-pbc-cartesian-square]. Then the Kunneth maps
$\kappa_{E,K}$ of [def-kun-kunneth-map] are compatible with the
identifications $\theta_\square$ of
[def-weil-pbc-cartesian-square]: replacing the chosen
identification $\alpha$ of the square, or pasting the square with
another one, changes $\kappa_{E,K}$ only by the corresponding
canonical identifications $\theta_\square$ of the inverse-image
functors.

## Proof

The composite displayed in [def-kun-kunneth-map] is built from the
canonical identification $c^{-1}\cong p^{-1}f^{-1}\cong q^{-1}g^{-1}$
and from $\varepsilon_f$, $\varepsilon_g$, which do not depend on
the chosen identification $\alpha$; and the identification
$\theta_\square$ of [def-weil-pbc-cartesian-square] is
compatible with identities and with pasted squares. Since the mate of
a composite is formed from the fixed adjunction $c^{-1}\dashv Rc_*$,
the resulting map is changed only by the corresponding identifications
$\theta_\square$.
