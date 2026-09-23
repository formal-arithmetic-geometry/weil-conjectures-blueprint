+++
id = "geo-ba43-pairwise-common-refinement"
kind = "remark"
title = "Exact unresolved interface"
order = 1837
tags = ["latex:openproblem"]
+++
**Owner.**`GEO-BA43-PAIRWISE-COMMON-REFINEMENT` **Status.**`OPEN`; **reduction status.**`LEAF`; **class.**`GEO`.
**Exact output required.**Construct a typed common dense refinement with finitely presented proper structure map.

**Formalization note.** Partially formalized as `AlgebraicGeometry.Compactification.exists_common_refinement_isSchemeTheoreticallyDominant`, with the density-free version `AlgebraicGeometry.Compactification.exists_common_refinement` (both in `WeilConjectures/Compactification/CommonRefinement.lean`). Delivered: for a quasi-compact $f$, any two compactifications of $f$ are refined by a common one — the schematic closure of the graph in the fibre product — in which the source open is scheme-theoretically dense. Not delivered: the structure morphism of that common refinement is proper but is not shown to be finitely presented, so the owner stays open on that half. Finite presentation of the constructed models is tracked separately.

**Open obligation:** GEO-BA43-PAIRWISE-COMMON-REFINEMENT
