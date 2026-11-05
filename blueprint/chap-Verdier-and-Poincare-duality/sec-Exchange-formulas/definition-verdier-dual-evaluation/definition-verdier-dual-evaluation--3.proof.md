+++
kind = "proof"
of = "definition-verdier-dual-evaluation--3"
order = 827005
uses = ["prose-03-02"]
+++
Represent $M$ by a K-injective complex $I$, and represent the given
distinguished triangle, up to isomorphism, by the image of a degreewise
split short exact sequence of complexes
$P'\to P\to P''$. Internal Hom into $I$ reverses this sequence and
preserves its degreewise splitting. The reversed sequence therefore gives
a distinguished triangle after passage to the derived category.

The comparison from the image of the internal Hom complex to derived
internal Hom is an isomorphism because $I$ is K-injective, and is natural
in the first variable (`DerivedCategory.qhInternalHomToIhom` and
`DerivedCategory.qhInternalHomToIhom_naturality`). Transporting the triangle
along these comparisons and the chosen isomorphisms gives the required
connecting morphism. This is
`DerivedCategory.exists_distinguished_ihom_pre`, specialized to étale
sheaves by `AlgebraicGeometry.Etale.exists_distTriang_derivedHom_left`.
Taking $M=\omega_X$ gives the assertion about Verdier duals.
