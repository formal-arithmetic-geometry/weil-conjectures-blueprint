+++
id = "rem-sf-axiom-verification"
kind = "remark"
title = "What verifies each axiom"
order = 3706
uses = ["cor-cbc-proper-coincidence", "cor-sf-finite-level-comparison-two-cases", "def-compact-support-direct-image-detailed", "def-sf-datum", "def-weil-exceptional-adjoint-admissibility", "fix-lem-exchanges", "fix-prop-adjunctions", "fix-prop-projection-formula", "lem-fix-operation-reduction", "lem-sf-finite-level-comparison", "prop-compactification-coherence-detailed", "thm-fix-general-biduality"]
+++
The formal axioms of [def-sf-datum] are supplied operation by
operation. Adjunction (A1) is [fix-prop-adjunctions], with the
explicit exceptional-adjoint hypothesis of
[def-weil-exceptional-adjoint-admissibility]. Base change (A2)
is the independent base-change theorems collected in
[fix-lem-exchanges]. Projection (A3) is the proved
[fix-prop-projection-formula]. Composition and proper coincidence
(A4) are [def-compact-support-direct-image-detailed],
[prop-compactification-coherence-detailed] and
[cor-cbc-proper-coincidence].

For (A5), [lem-fix-operation-reduction] supplies the elementary
coefficient comparisons on its stated domains. The additional
constructible-tower comparisons are
[lem-sf-finite-level-comparison] with its explicit hypotheses,
which [cor-sf-finite-level-comparison-two-cases] verifies in the
specified cases. The exceptional comparisons remain subject to the
coefficient compatibility in admissibility. Biduality (A6) is the
separate geometric theorem [thm-fix-general-biduality], on its
actual hypotheses and coefficient domains. The aggregate package
collects these results only after their individual proofs.
