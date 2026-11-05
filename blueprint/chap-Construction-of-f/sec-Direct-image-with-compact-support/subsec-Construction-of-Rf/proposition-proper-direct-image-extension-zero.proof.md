+++
kind = "proof"
of = "proposition-proper-direct-image-extension-zero"
order = 503
uses = ["proposition-etale-implications", "proposition-pro-etale-coverings", "definition-w-local-w-strictly-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-milnor-sequence", "theorem-classical-sheaves-essential-image", "theorem-bounded-below-cohomology-comparison", "theorem-comparison-direct-images", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "lemma-inverse-image-coefficient-sheaves", "definition-lisse-sheaves", "proposition-inverting-ell", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "lemma-uniform-bound-proper-direct-image", "lemma-proper-direct-image-unbounded-complexes", "proposition-compactness-proper-direct-image", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "lemma-change-coefficients-direct-image", "proposition-dctf-x-qbar-2-colimit", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "remark-base-change-compactification", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
For each functor we need two facts: it preserves direct sums, and it
maps $D^b_{\mathrm{ctf}}$ into $D^b_{\mathrm{ctf}}$. The rest then follows from the definition of
the localizing categories, in the form recalled before the proposition.

For $Rp_*$ with $E$ and $\overline{\mathbf Q}_\ell$, Lemma [lemma-proper-direct-image-unbounded-complexes](3)
shows that $Rp_*$ preserves direct sums on
$\Dic(X,\Lambda)\supset\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$, and
Proposition [proposition-proper-direct-image-constructible-complexes] shows that $Rp_*$ preserves
$D^b_{\mathrm{ctf}}=\Dbc$. For finite $A$, these two facts are
Proposition [proposition-proper-direct-image-finite-coefficients] and
Corollary [corollary-proper-direct-image-finite-coefficients-localizing];
for $\mathcal O_E$, they are
Proposition [proposition-compactness-proper-direct-image] and Proposition [proposition-proper-direct-image-constructible-complexes]. In each case, the
objects
$K\in\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$ with
$Rp_*K\in\Loc(D^b_{\mathrm{ctf}}(Y,\Lambda))$ form a triangulated subcategory closed
under direct sums and containing $D^b_{\mathrm{ctf}}(X,\Lambda)$, and hence they form all of
$\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$.

Extension by zero is exact and left adjoint to $j^*$, so it preserves
direct sums. It preserves constructibility, since we may add the closed
complement as a stratum on which the sheaf is zero. For finite $A$ it also preserves finite Tor amplitude, as one checks on stalks, while for $\mathcal O_E$, $E$ and $\overline{\mathbf Q}_\ell$ we have $D^b_{\mathrm{ctf}}=\Dbc$, so constructibility
suffices; for $\mathcal O_E$ this is Lemma [lemma-inverse-image-tensor-product]. With this, the localizing-subcategory argument shows that $j_!$ restricts as stated.
