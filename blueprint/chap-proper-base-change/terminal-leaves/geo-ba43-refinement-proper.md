+++
id = "geo-ba43-refinement-proper"
kind = "remark"
title = "Exact unresolved interface"
order = 1835
tags = ["latex:openproblem"]
+++
**Owner.**`GEO-BA43-REFINEMENT-PROPER` **Status.**`OPEN`; **reduction status.**`LEAF`; **class.**`GEO`.
**Exact output required.**A refinement between the typed models is proper because its source is proper and its target separated over the base.

**Formalization note.** Formalized as `AlgebraicGeometry.Compactification.Refinement.isProper` (`WeilConjectures/Compactification/Refinement.lean`). It is an unconditional instance on the ambient morphism of a refinement of compactifications, proved exactly by the stated argument: the composite with the proper structure morphism of the target is proper, and the target is separated over the base. The full required output is delivered, so the owner is discharged.

*Constructed by:* GEO-BA43-REFINEMENT-PROPER
