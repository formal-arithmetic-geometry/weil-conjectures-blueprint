+++
kind  = "proof"
of    = "fix-prop-coherence"
+++
The identity and pasting equations are [fix-lem-exchanges].
The projection diamonds and associativity are
[fix-prop-projection-formula]; taking adjoint mates gives the
corresponding equations for [fix-cor-verdier-exchange].
The maps used here are tensor reassociation, evaluation, and adjunction
units and counits, whose coefficient comparisons are proved in
[lem-fix-operation-reduction]. The general Hom comparisons
[thm-coef-finite-hom], [lem-coef-integral-hom-reduction], [lem-coef-integral-finite-extension]
are defined by the same evaluation maps. The exceptional comparisons
[lem-coef-finite-exceptional] and those of [sk-prop-scalar-six] for the
adjoint of [sk-thm-existence]
preserve units and counits, so their mates satisfy the same equations.
Their Weil structures are [lem-fix-weil-operations], with
general duality equivariance given by [cor-coef-verdier-weil-equivariance]. The geometric orientation is supplied
separately by [thm-pur-finite-reduction-of-purity] and
[prop-pur-weil-equivariance-compatibilities]; composing it with
evaluation gives the pairing comparison [thm-pod-finite-reduction].
Thus coherence is inherited from the individual maps on the stated
domains, without an additional preservation or biduality assertion.
