+++
kind = "proof"
of = "theorem-comparison-constructible-sheaves--3"
order = 149007
uses = ["theorem-comparison-constructible-sheaves--1", "proposition-comparison-morphism-inverse-image", "proposition-locally-constant-sheaves-finite-presentation", "proposition-comparison-immersions", "theorem-classical-sheaves-essential-image", "corollary-bounded-below-classical-complexes"]
+++
First, the canonical inverse image supplies a functor $D$ with the stated
compatibilities. It is a left adjoint, and comparison of its underlying
additive sheaf with exact inverse image shows that it preserves finite
limits. It is therefore exact, so termwise inverse image descends through
localization and commutes with every cohomology functor. This construction
works for an arbitrary scheme and a discrete commutative coefficient
ring, without the Noetherian or quasi-compactness assumptions.

For any $D$ as in the statement, its cohomology comparison and the module
constructibility test show that it preserves constructible cohomology.
Inverse image preserves zero objects, so it also preserves a finite
interval outside which cohomology vanishes. Thus $D$ restricts to the
bounded constructible full subcategories. Bounded classical comparison
[corollary-bounded-below-classical-complexes] gives full faithfulness on
these objects.

If $K\in\Dbc(X,\Lambda)$, every $H^q(K)$ is classical by
[theorem-comparison-constructible-sheaves--1]. Bounded classical descent
gives an étale derived object $M$ with $D(M)\simeq K$. Cohomology
comparison and reflection of constructibility under module inverse image
show that every $H^q(M)$ is constructible. Full faithfulness of module
inverse image reflects zero objects, so $H^q(M)$ vanishes outside the
same finite interval as $H^q(K)$. Hence $M$ is bounded constructible.
This proves essential surjectivity, and forming the equivalence from
the restricted $D$ gives the stated forward-functor identification.
