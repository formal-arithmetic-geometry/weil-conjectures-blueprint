+++
kind = "proof"
of = "lemma-extension-separably-closed-ground-field"
order = 365
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finite-morphisms", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "definition-tate-module", "definition-relative-picard-functor", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-sheaves-finite-support-finite-morphisms", "lemma-normalization-constant-sheaf", "lemma-removing-finitely-many-points", "lemma-reduction-unipotent-local-system"]
+++
A purely inseparable extension does not change the étale topos, which
allows us to replace $k$ and $k'$ by their algebraic closures and then
apply $(C_7)$.

By the classical
comparison we may compute on the étale site. Choose compatible
algebraic closures $\bar k\subseteq\bar k'$. Since $\bar k/k$ and
$\bar k'/k'$ are purely inseparable, $C_{\bar k}\to C$ and
$C_{\bar k'}\to C_{k'}$ are universal homeomorphisms, and hence they induce
equivalences of small étale topoi [Stacks, [03SI](https://stacks.math.columbia.edu/tag/03SI)]. This reduces the
claim to the pullback from $C_{\bar k}$ to $C_{\bar k'}$, which is an
isomorphism by $(C_7)$ of Theorem [theorem-cohomology-curves]. Since all these maps are
pullback maps, the comparison square commutes [Stacks, [0A5E](https://stacks.math.columbia.edu/tag/0A5E)].
