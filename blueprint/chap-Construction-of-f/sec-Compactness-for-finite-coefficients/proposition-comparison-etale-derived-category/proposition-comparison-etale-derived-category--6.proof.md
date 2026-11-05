+++
kind = "proof"
of = "proposition-comparison-etale-derived-category--6"
order = 474011
uses = ["proposition-comparison-immersions"]
+++
Restriction to $U$ commutes with $\nu_*$, since both composites are restriction
of sections. The left adjoints therefore commute, giving (2.10) of
[proposition-comparison-immersions], namely
`AlgebraicGeometry.ProEtale.openImmersionLowerShriekComparisonUpperStarIso`.
The functors $j_!$ and $\nu^*$ are exact. Apply this isomorphism termwise and
pass to the derived categories, using
`CategoryTheory.Functor.mapDerivedCategoryNatIso` and
`CategoryTheory.Functor.mapDerivedCategoryCompIso`.
