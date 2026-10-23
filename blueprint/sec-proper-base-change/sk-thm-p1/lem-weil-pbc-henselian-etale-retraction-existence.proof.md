+++
kind = "proof"
of = "lem-weil-pbc-henselian-etale-retraction-existence"
uses = ["lem-weil-pbc-root-lifting-etale-retraction"]
+++
Since $S$ is henselian, every monic polynomial over $S$ whose reduction modulo $\mathfrak m$ has a simple root in $\kappa$ has a root in $S$ lifting it (one of the standard equivalent characterizations of henselian local rings). This is exactly the root-lifting hypothesis of the root-lifting retraction lemma.

Let $x=\mathfrak q'\in\operatorname{Spec}B$ and $y=\mathfrak m\in\operatorname{Spec}S$ its image. The residue field of the scheme $\operatorname{Spec}B$ at $x$ is $\kappa(\mathfrak q')$, and that of $\operatorname{Spec}S$ at $y$ is $\kappa$, compatibly with the maps $B\to\kappa(\mathfrak q')$ and $S\to\kappa$, and the residue-field map of $\operatorname{Spec}\varphi$ at $x$ is the given map $\kappa\to\kappa(\mathfrak q')$. The composite $S\to\kappa\to\kappa(\mathfrak q')$ is surjective, as a surjection followed by a bijection; so the residue-field map of $\operatorname{Spec}B\to\operatorname{Spec}S$ at $x$ is surjective, and it is injective as a homomorphism of fields. Thus the residue-field hypothesis of that lemma holds.

Apply the root-lifting retraction lemma with this root-lifting property and this residue-field bijectivity. Forget the uniqueness part to obtain the requested algebra homomorphism with maximal-ideal preimage q'. ([lem-weil-pbc-root-lifting-etale-retraction]).
