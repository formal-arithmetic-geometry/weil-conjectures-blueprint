+++
id = "lem-amb-etale-compact-comparisons"
kind = "lemma"
title = "The etale compact-support comparisons"
lean = ["AlgebraicGeometry.Etale.etaleCompactSupport_refinementComparison_eq"]
order = 2565
uses = ["def-amb-etale-compact-support", "def-nagata-compactifiable", "def-weil-compactifications-refinements", "lem-weil-derived-direct-image-composition", "lem-weil-pbc-proper-open-comparison-composition", "lem-weil-pbc-proper-open-comparison-iso", "prop-weil-proet-finite-proper-base-change", "thm-nagata-compactification"]
+++
Let $A$ be a torsion commutative ring. The proper-refinement comparisons for
[def-amb-etale-compact-support] on the full derived categories
$D(-_{\rm et},A)$ are coherent isomorphisms. Thus they identify its candidates canonically.
These identifications provide the usual composition
isomorphism $Rg_!Rf_!\cong R(gf)_!$ for composable
compactifiable separated finite-type morphisms between
Noetherian schemes, on the same unbounded domains.
[Stacks 0F7B](https://stacks.math.columbia.edu/tag/0F7B) constructs the
comparison maps for an arbitrary ring; the torsion hypothesis is needed for
them to be isomorphisms
([Stacks 0F7I](https://stacks.math.columbia.edu/tag/0F7I),
[Stacks 0F7J](https://stacks.math.columbia.edu/tag/0F7J)).
