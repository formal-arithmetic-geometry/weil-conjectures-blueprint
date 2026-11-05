+++
kind = "proof"
of = "proposition-comparison-etale-derived-category--5"
order = 474010
uses = ["proposition-comparison-morphism-inverse-image", "proposition-topos-functoriality"]
+++
The restriction $\nu_*$ commutes with direct images along $g$: both composites
restrict sections along the same base-change functor on étale objects. Taking
left adjoints gives the isomorphism on sheaves
`AlgebraicGeometry.ProEtale.comparisonUpperStarCompUpperStarIso`.
All the inverse-image functors are exact. Apply this isomorphism termwise to
complexes and pass to the derived categories, using
`CategoryTheory.Functor.mapDerivedCategoryNatIso` and the comparison for
composition `CategoryTheory.Functor.mapDerivedCategoryCompIso`.
