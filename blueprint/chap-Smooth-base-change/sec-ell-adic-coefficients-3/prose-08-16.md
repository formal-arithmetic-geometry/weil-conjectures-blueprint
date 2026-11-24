+++
id = "prose-08-16"
kind = "hidden"
title = "$\\ell$-adic coefficients (1)"
order = 698
+++
For every admissible coefficient ring, [smooth base change](@theorem-smooth-base-change-all-admissible) takes the
following form. For finite rings it is a case of smooth base change for
torsion complexes (Theorem [theorem-smooth-base-change-classical-torsion-2]),
and we deduce the other rings by
Proposition [proposition-isomorphisms-reduce-finite-coefficients].

On the [pro-étale site](@definition-small-pro-etale-site) the [base change map](@definition-pro-etale-base-change-map)
for $\mathcal O_E$-coefficients is a single map of complexes, defined by
the same adjunction as for finite rings.
Lemma [lemma-change-coefficients] identifies its reduction modulo
$\pi_E$ with the [base change map](@definition-pro-etale-base-change-map) for $\mathcal O_E/\pi_E$, so [derived
Nakayama](@lemma-reduction-derived-nakayama) gives the integral case from the [torsion theorem](@theorem-smooth-base-change-classical-torsion-2). The
rational cases then follow by inverting $\ell$ and by descent to a finite
extension.
