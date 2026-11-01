+++
id = "rem-sf-axiom-verification"
kind = "remark"
title = "What verifies each axiom"
order = 3550
uses = ["cor-cbc-proper-coincidence", "def-compact-support-direct-image-detailed", "def-sf-datum", "def-weil-exceptional-adjoint-admissibility", "fix-lem-exchanges", "fix-prop-adjunctions", "fix-prop-projection-formula", "lem-sf-reduction-compatibility", "prop-compactification-coherence-detailed", "lem-sf-verdier-biduality-equivalence"]
+++
The formal axioms of [def-sf-datum] are supplied operation by
operation. Adjunction (A1) is [fix-prop-adjunctions], with the
explicit exceptional-adjoint hypothesis of
[def-weil-exceptional-adjoint-admissibility]. Base change (A2)
is the independent base-change theorems collected in
[fix-lem-exchanges] and [cor-cbc-proper-coincidence]. Projection (A3), on its unbounded finite-coefficient étale domain, is the
finite projection formula [`hasProjectionFormula_of_finite`](https://github.com/formal-arithmetic-geometry/weil-conjectures/blob/b04b998e53abc72b9702488ed2540905b21d614c/WeilConjectures/SixFunctors/Etale/Derived/ProjectionFormula.lean#L287-L311); the bounded condensed
[fix-prop-projection-formula] does not cover that domain. Composition and proper coincidence
(A4) are [def-compact-support-direct-image-detailed],
[prop-compactification-coherence-detailed] and
[cor-cbc-proper-coincidence].

Compatibility with change of coefficients is not a clause of the
datum. The finite-reduction compatibilities of derived pullback and of
compact-support direct image are [lem-sf-reduction-compatibility].
Biduality (A6) is the separate geometric theorem
[lem-sf-verdier-biduality-equivalence], for $k$ algebraically closed and
the exponent of $\Lambda$ invertible in $k$. The aggregate package
collects these results only after their individual proofs.
