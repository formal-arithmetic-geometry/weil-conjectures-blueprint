+++
id = "geo-ba43-dense-refinement-uniqueness"
kind = "remark"
title = "Exact unresolved interface"
order = 947
tags = ["latex:openproblem"]
+++
**Owner.**`GEO-BA43-DENSE-REFINEMENT-UNIQUENESS` **Status.**`OPEN`; **reduction status.**`LEAF`; **class.**`GEO`.
**Exact output required.**Two refinement maps agreeing on the schematically dense source open agree globally when the target is separated.

**Formalization note.** Formalized as `AlgebraicGeometry.Compactification.Refinement.ext_of_isSchemeTheoreticallyDominant` (`WeilConjectures/Compactification/RefinementUniqueness.lean`). Two refinements of a compactification $d$ by a compactification $c$ whose open immersion `c.i` is scheme-theoretically dominant are equal; both automatically agree on the source open, and separatedness of the target is supplied by properness of `d.g`. The full required output is delivered, so the owner is discharged.

*Constructed by:* GEO-BA43-DENSE-REFINEMENT-UNIQUENESS
