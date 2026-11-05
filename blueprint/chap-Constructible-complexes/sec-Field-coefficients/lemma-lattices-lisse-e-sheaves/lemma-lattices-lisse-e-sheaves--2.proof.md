+++
kind = "proof"
of = "lemma-lattices-lisse-e-sheaves--2"
order = 260002
uses = ["lemma-lattices-lisse-e-sheaves--1", "proposition-locally-constant-sheaves-finite-presentation", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-stability", "proposition-pro-etale-coverings", "lemma-inverse-image-coefficient-sheaves", "proposition-extension-zero-restriction-closed-subscheme"]
+++
Apply [lemma-lattices-lisse-e-sheaves--1] to obtain a locally constant,
locally inhabited sheaf $F$. The comparison with the étale site makes $F$
classical: it is the inverse image of an étale sheaf $G$. Local
inhabitedness says that the map from $F$ to the terminal sheaf is an
epimorphism. Full faithfulness of the comparison inverse image reflects
this epimorphism, so $G$ has sections on an étale covering. This is the
set-valued local-section conclusion used in
[proposition-locally-constant-sheaves-finite-presentation].

Choose the integral pairs supplied by these sections. The equivalence
between the slice over $Y_i$ and its small pro-étale site transports each
pair to a module $M_i$ on $Y_i$. The coefficient comparison is the identity
on continuous functions. This equivalence preserves finite local freeness
and commutes with extension of scalars, giving the required isomorphism.

For the second assertion, express $L$ as a module object in sheaves of
abelian groups with continuous coefficients. The equivalence with sheaves
of modules preserves local finite freeness and transports the specified
integral pairs and their scalar-extension isomorphisms. At every point of
$X$, choose a member of the étale covering containing a point above it,
then an affine open neighborhood of that point. Pull back the integral
module to this affine open, using
[lemma-inverse-image-coefficient-sheaves] and the composition isomorphism
for inverse image.

The images of these affine neighborhoods are open and cover $X$.
Topological noetherianity implies quasi-compactness, so finitely many
suffice. Their disjoint union $U$ is affine, hence quasi-compact and
quasi-separated, and the map $U\to X$ is étale and surjective. On $U$ take
the finite direct sum of the extensions by zero of the integral modules
on its components, as in
[proposition-extension-zero-restriction-closed-subscheme]. Restriction to
each component recovers its module, so the resulting module is locally
free of finite rank. Extension of scalars commutes with these extensions
by zero and their finite direct sum, giving the scalar-extension
isomorphism on $U$. No compatibility among the component lattices is
required, and the same construction includes the empty covering.
