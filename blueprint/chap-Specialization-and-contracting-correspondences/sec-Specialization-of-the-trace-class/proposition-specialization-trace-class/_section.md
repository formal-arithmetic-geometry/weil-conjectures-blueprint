+++
id = "proposition-specialization-trace-class"
kind = "proposition"
title = "Specialization of the trace class"
order = 1684
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.TraceSpecialization.sp", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.TraceSpecialization.sp_traceClass"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "example-locally-constant-functions-w-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-milnor-sequence", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "proposition-integral-constructibility-criterion", "lemma-lattices-after-finite-stratification", "proposition-inverting-ell", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "theorem-comparison-over-henselian-pair-degree", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-direct-image-constructible-complexes", "lemma-inverse-image-tensor-product", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "proposition-adjunction-projective-line", "proposition-exceptional-inverse-image-smooth-morphism", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "lemma-change-coefficients-direct-image", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "theorem-smooth-base-change-classical-torsion", "lemma-kunneth-one-identity-factor", "definition-relative-dualizing-complex", "proposition-sp-unique-adjoint", "definition-correspondence", "definition-trace-morphism", "definition-trace-class-local-terms", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "remark-base-change-compactification", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
Let $c=(c_1,c_2):C\to X\times_SX$ be a correspondence of separated
schemes of finite type over the trait $S$, and let $F=\Fix(c)$ be its
fixed scheme, with $i=i_c:F\hookrightarrow C$ and $d:F\to X$.
For $K\in D^b_{\mathrm{ctf}}(X_\eta,A)$ and a morphism
$u:c_{2\eta}^*K\to c_{1\eta}^!K$, put $K'=\Psi_XK$ and
let $u_s$ be the composite

$$
u_s:c_{2s}^*K'\xrightarrow{\alpha_{c_2}}\Psi_Cc_{2\eta}^*K
\xrightarrow{\Psi_Cu}\Psi_Cc_{1\eta}^!K
\xrightarrow{\beta_{c_1}}c_{1s}^!K'.
$$

For a section $z:A_{F_\eta}\to\omega_{F_\eta}$ of the dualizing complex, its
specialization is

$$
\operatorname{sp}_F(z)=\theta_F \Psi_F(z)\sigma_F:
A_{F_s}\longrightarrow\omega_{F_s}.
$$

Then

$$
\operatorname{Tr}_{c_s}(u_s)
=\operatorname{sp}_F\bigl(\operatorname{Tr}_{c_\eta}(u)\bigr).
$$
