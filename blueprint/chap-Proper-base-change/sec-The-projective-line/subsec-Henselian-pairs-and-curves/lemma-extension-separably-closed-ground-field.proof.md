+++
kind = "proof"
of = "lemma-extension-separably-closed-ground-field"
order = 365
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finite-morphisms", "theorem-smooth-base-change-classical-torsion", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "proposition-cohomology-smooth-affine-curve", "proposition-p-torsion-smooth-proper-curve", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology", "lemma-sheaves-finite-support-finite-morphisms", "lemma-normalization-constant-sheaf", "lemma-removing-finitely-many-points", "lemma-reduction-unipotent-local-system"]
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
