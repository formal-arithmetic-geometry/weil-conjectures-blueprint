+++
kind = "proof"
of = "proposition-dctf-x-qbar-2-colimit--2"
order = 648003
uses = ["proposition-dctf-x-qbar-2-colimit--3", "lemma-extension-scalars-preserves-dctf"]
+++
In the ambient derived category of $\overline{\mathbf Q}_{\ell,X}$-modules,
let $P$ be the class of objects isomorphic to an extension of scalars
of an object of some $\Dbc(X,E)$. This class is closed under isomorphisms,
contains zero and is stable under shifts. To check closure under cones,
descend a morphism between two such objects to a common finite field by
[proposition-dctf-x-qbar-2-colimit--3](1). Take its cone there and extend
scalars. The scalar-extension functors are triangulated, so the resulting
cone is isomorphic to the original one. This is
`CategoryTheory.CategoryCocone.isTriangulated_exists_essImage`.

Every constructible $\overline{\mathbf Q}_{\ell,X}$-module has a constructible
model over a finite coefficient field, by
`AlgebraicGeometry.ProEtale.exists_constructible_finiteCoefficient_model`.
Its proof descends finite presentations on the strata and assembles the
models over a common finite field. Exactness of scalar extension then
puts each constructible module in degree zero in $P$.

Finally, a bounded constructible complex is obtained from its finitely
many nonzero cohomology sheaves by shifts and cones. Apply
`AlgebraicGeometry.ProEtale.prop_of_boundedConstructibleModule` to $P$.
The resulting isomorphism in the ambient derived category lifts to the
full subcategory of bounded constructible complexes.
