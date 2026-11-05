+++
kind = "proof"
of = "proposition-isomorphisms-reduce-finite-coefficients--3"
order = 653007
uses = ["proposition-isomorphisms-reduce-finite-coefficients--2", "lemma-integral-models"]
+++
Under the shared hypotheses, [proposition-isomorphisms-reduce-finite-coefficients--2] applies to $\theta_{\mathcal O_E}(K_0)$: its reduction modulo $\ell$ is an isomorphism by compatibility and the finite-coefficient hypothesis. Invert $\ell$ on these integral generators and extend through cones and shifts by exactness, using Lemma [lemma-integral-models](4). This proves the retained informal assertion.

For the particular maps used by Lean, `AlgebraicGeometry.ProEtale.exists_boundedConstructibleExtendScalars_obj_iso` gives an integral model of each bounded constructible $E$-complex directly. The compatibility of the exceptional base-change map with extension of scalars is obtained by transporting its defining mate and cancelling the comparison isomorphisms. There is no separate theorem here for an arbitrary natural transformation $\theta$.
