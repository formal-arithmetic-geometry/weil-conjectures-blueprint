+++
kind = "proof"
of = "lemma-perfect-complexes-geometric-point"
order = 825
uses = ["proposition-comparison-morphism-inverse-image", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "corollary-open-direct-image-over-field", "proposition-sp-unique-adjoint", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "remark-base-change-compactification", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
Once $D^b_{\mathrm{ctf}}(s,\Lambda)$ is identified with
$\operatorname{Perf}(\Lambda)$, the other assertions follow, because the direct images
and the stalks of $K$ are objects of $D^b_{\mathrm{ctf}}(s,\Lambda)$.

By the comparisons of Section [sec-Continuous-cohomology], taking global
sections identifies $D^b_{\mathrm{ctf}}(s,\Lambda)$ with the full subcategory of
$D(\Lambda)$ of complexes with bounded finitely generated cohomology and
finite Tor dimension, and we show that these complexes are perfect
separately for the three kinds of coefficients.
A constructible complex with finite coefficients has
bounded finite cohomology and finite Tor amplitude, so it is perfect:
take a bounded-above resolution by finite free modules and
truncate it below the Tor bound. Then the last syzygy that remains is finitely
presented and flat, hence projective, so the truncated resolution is a
bounded complex of finite projective modules. With integral coefficients, by contrast, the
constructible complexes on the point are those with bounded finitely
generated $\mathcal O_E$-cohomology, and since a discrete valuation ring has
global dimension one, these complexes are perfect. Finally, with field
coefficients, bounded complexes with finite-dimensional cohomology are perfect.

By Proposition [proposition-six-operations-dctf], the two
direct images of $a_X$ lie in $D^b_{\mathrm{ctf}}(s,\Lambda)$ and are
therefore perfect. If we represent such a
complex by a bounded complex of finite projective modules, its termwise
dual is again of this form, and the double evaluation map is termwise
an isomorphism. The stalk $K_{\bar x}$ is the complex of global sections of
$\bar x^*K\in D^b_{\mathrm{ctf}}(s,\Lambda)$ (Proposition [proposition-six-operations-dctf]), so it
is perfect as well.
