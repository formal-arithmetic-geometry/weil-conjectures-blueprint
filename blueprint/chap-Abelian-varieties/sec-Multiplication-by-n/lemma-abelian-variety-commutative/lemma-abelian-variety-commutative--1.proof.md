+++
kind = "proof"
of = "lemma-abelian-variety-commutative--1"
order = 1495003
uses = ["definition-abelian-variety"]
+++
Write $p:A\to\operatorname{Spec}k$ for the structure morphism and
$e:\operatorname{Spec}k\to A$ for the identity section. Since $p\circ e$
is the identity, properness and connectedness imply that $A$ is
geometrically connected, by
`AlgebraicGeometry.GeometricallyConnected.of_universallyClosed_of_section`.

After any field extension, $A$ is smooth, hence regular and locally
noetherian, and remains connected. It is therefore irreducible, as in
`AlgebraicGeometry.GeometricallyIrreducible.of_smooth_of_geometricallyConnected`.
Smoothness also gives geometric reducedness. Combining geometric
irreducibility and geometric reducedness proves geometric integrality.
