+++
kind = "proof"
of = "lemma-extension-separably-closed-ground-field"
order = 365
uses = ["lemma-stability", "proposition-comparison-morphism-inverse-image", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "proposition-cohomology-p-1-over-henselian", "lemma-degree-zero-calculation", "lemma-reduction-field", "lemma-reduction-curve-over-normal-base", "proposition-base-change-larger-algebraically-closed", "lemma-schematic-closure-uniqueness", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian", "proposition-p-torsion-smooth-proper-curve", "lemma-normalization-constant-sheaf", "lemma-removing-finitely-many-points", "lemma-reduction-unipotent-local-system"]
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
