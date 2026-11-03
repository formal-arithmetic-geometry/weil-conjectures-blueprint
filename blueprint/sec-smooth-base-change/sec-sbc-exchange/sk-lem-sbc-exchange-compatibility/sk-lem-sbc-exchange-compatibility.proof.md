+++
kind = "proof"
of = "sk-lem-sbc-exchange-compatibility"
uses = ["sk-thm-pe-direct-image-comparison", "sk-lem-pbc-exchange-pasting"]
+++
By definition, the base change map is the adjoint transpose of a counit preceded
by the composition isomorphism for inverse images. Since the counit for a
composite adjunction is the composite of the two counits, taking
adjoint transposes proves pasting, in either order of composing the
two directions of a rectangle. The assertion about identity squares
follows from the triangle identities; see also Lemma [sk-lem-pbc-exchange-pasting].
The comparisons of sites of Theorem [sk-thm-pe-direct-image-comparison]
identify the composition maps for inverse images and the units and counits,
and hence also the base change maps constructed from them. The same argument with
Proposition [sk-prop-scalar-six] proves the coefficient assertion.
