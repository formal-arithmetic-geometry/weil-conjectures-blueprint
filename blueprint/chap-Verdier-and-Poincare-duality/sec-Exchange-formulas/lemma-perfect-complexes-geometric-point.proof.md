+++
kind = "proof"
of = "lemma-perfect-complexes-geometric-point"
order = 826
uses = ["definition-w-local-w-strictly-local", "lemma-extremally-disconnected-covers", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "lemma-comparison-completed-coefficients", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "proposition-integral-constructibility-criterion", "lemma-descent-finite-coefficient-field", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-base-change-complete-integral", "proposition-comparison-etale-derived-category", "proposition-forgetting-supports-composition", "theorem-results-from-etale-theory", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "proposition-sp-unique-adjoint", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "definition-relative-picard-functor", "theorem-riemann-roch-coherent-serre-duality", "lemma-coherent-base-change-invertible-sheaves", "theorem-picard-scheme-jacobian-over-separably", "corollary-torsion-jacobian-field-extension", "lemma-finite-direct-images", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-finite-morphisms-cohomology"]
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
