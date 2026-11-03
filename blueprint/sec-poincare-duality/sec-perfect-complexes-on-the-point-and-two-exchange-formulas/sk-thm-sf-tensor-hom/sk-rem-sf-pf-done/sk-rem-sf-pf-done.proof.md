+++
kind  = "proof"
of    = "sk-rem-sf-pf-done"
uses = ["sk-thm-sf-pf-adic", "sk-thm-sf-pf-field", "sk-thm-sf-pf-proetale", "sk-prop-sf-pf-coherence"]
+++
The obligations of the interface are discharged one coefficient ring at a
time. At the finite stages $A_{E,n}$ the projection formula is
[det-thm-sf-pf-finite], and it is compatible with finite reduction by
[det-prop-sf-pf-reduction]. At the derived-complete stage $\mathcal O_E$ it is
[sk-thm-sf-pf-adic], obtained from the finite stages by that compatibility.
At $E$ and $\Qlb$ it is [sk-thm-sf-pf-field]. On the pro-étale realization it
is [sk-thm-sf-pf-proetale]. The naturality, unit, associativity and
compactification-independence clauses are [sk-prop-sf-pf-coherence]. None of
these proofs uses a duality statement.
