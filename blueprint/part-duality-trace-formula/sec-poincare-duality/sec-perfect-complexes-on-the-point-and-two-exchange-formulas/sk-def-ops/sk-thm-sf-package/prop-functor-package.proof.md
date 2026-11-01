+++
kind  = "proof"
of    = "prop-functor-package"
+++
The finite-stage internal-Hom preservation recorded before the clauses
is [cor-weil-finite-constructible-hom]; its coefficient comparison
is [thm-coef-finite-hom]. For every admissible $\Lambda$, preservation of
$\Dctf$ by the operations is [sk-thm-sf-ctf-stability] and the existence of
the exceptional adjoint is [sk-thm-existence], and their coefficient comparisons are
[sk-prop-scalar-six].
Clause (1) is [det-prop-sfb-finite-extension-compatibility] together with
[det-def-sfb-coefficient-change] and the descent statement
[sk-thm-sfb-qlbar-two-colimit].
For (2), use [prop-compactification-coherence-detailed], the
reduction comparisons of [sk-prop-scalar-six] and the independently
proved [lem-fix-operation-reduction], [lem-fix-compact-support-coefficient-change].
The ordinary finite quotient comparison is [lem-coef-finite-direct-image].
Clause (3) follows from [thm-sf-comp-composition], [fix-lem-exchanges],
[cor-cbc-proper-coincidence], and the image of
[lem-cbc-open-closed-recollement] under the exact functor of
[lem-compact-support-direct-image-triangulated].
Clause (4) is [thm-weil-pbc-bounded-below],
[sbc-thm-bounded-below-derived-smooth-base-change] and
[thm-cbc-finite-torsion] at the finite stages, and
[sk-thm-sfb-proper-base-change], [sk-thm-sbc-coefficients] and
[det-prop-sf-cbc] for every admissible $\Lambda$.
Clause (5) is [fix-prop-projection-formula].
Clause (6) is [thm-pur-finite-coefficient-smooth-purity] at the finite
stages and [sk-thm-purity-transport] for every admissible $\Lambda$.
For (7), the exchange is the unconditional Brown/Yoneda proof of
[sk-thm-sf-tensor-hom], not the conditional ambient exchange result
[fix-cor-verdier-exchange];
[lem-weil-coefficient-frobenius] proves the required point duality,
and [thm-sf-dual-perfect] reduces the smooth site-perfect
case to local perfect-complex biduality. General finite-stage biduality is
[thm-fix-general-biduality]; its proof establishes constructible
preservation first and then uses geometric generic restriction and
dimension induction. Boundary exchange is its consequence
[cor-weil-boundary-duality-discharge].
For the other admissible rings, biduality is [sk-thm-pd-verdier-duality]:
the integral case by reduction modulo $\pi_E$ and derived Nakayama
([thm-coef-integral-verdier]), $E$ by integral models and $\Qlb$ by descent.
The exceptional adjunction and its coefficient comparisons are
[sk-thm-existence], [lem-coef-finite-exceptional] and [sk-prop-scalar-six].
Finally apply [fix-prop-coherence].
