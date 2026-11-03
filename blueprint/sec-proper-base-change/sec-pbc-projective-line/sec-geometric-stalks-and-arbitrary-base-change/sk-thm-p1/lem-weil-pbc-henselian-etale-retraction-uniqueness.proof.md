+++
kind = "proof"
of = "lem-weil-pbc-henselian-etale-retraction-uniqueness"
uses = ["lem-weil-pbc-root-lifting-etale-retraction"]
+++
Since $S$ is henselian, simple roots modulo $\mathfrak m$ of monic polynomials over $S$ lift to roots in $S$. Let $x=\mathfrak q'\in\operatorname{Spec}B$ and $y=\mathfrak m\in\operatorname{Spec}S$ its image. The scheme residue fields at $x$ and $y$ are $\kappa(\mathfrak q')$ and $\kappa$, compatibly with $B\to\kappa(\mathfrak q')$ and $S\to\kappa$, so the residue-field map of $\operatorname{Spec}B\to\operatorname{Spec}S$ at $x$ is the given map $\kappa\to\kappa(\mathfrak q')$. The composite $S\to\kappa\to\kappa(\mathfrak q')$ is surjective, so this residue-field map is surjective, and it is injective because it is a homomorphism of fields.

Apply the root-lifting retraction lemma to the $S$-algebra $B$ with this root-lifting property and this residue-field bijection. Both given algebra maps have maximal-ideal preimage $\mathfrak q'$, so its uniqueness clause identifies each with the unique retraction, and hence $\sigma=\tau$. ([lem-weil-pbc-root-lifting-etale-retraction]).
