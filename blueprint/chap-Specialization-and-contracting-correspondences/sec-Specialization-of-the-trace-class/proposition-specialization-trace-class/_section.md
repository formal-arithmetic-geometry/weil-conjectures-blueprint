+++
id = "proposition-specialization-trace-class"
kind = "proposition"
title = "Specialization of the trace class"
order = 1689
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.TraceSpecialization.sp", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.TraceSpecialization.sp_traceClass"]
uses = ["proposition-etale-implications", "lemma-stability", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "theorem-comparison-direct-images", "lemma-comparison-direct-images-compatibilities", "proposition-locally-constant-sheaves-finite-presentation", "theorem-comparison-constructible-sheaves", "proposition-pro-etale-site-separably-closed", "definition-tate-twists", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "lemma-reduction-derived-nakayama", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "definition-exceptional-base-change-finite", "proposition-adjunction-projective-line", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "definition-change-of-coefficients-maps", "lemma-change-coefficients-compact-support", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "proposition-isomorphisms-reduce-finite-coefficients", "lemma-degree-zero-calculation", "lemma-reduction-field", "lemma-reduction-curve-over-normal-base", "proposition-base-change-larger-algebraically-closed", "lemma-change-coefficients", "lemma-kunneth-field-coefficients", "definition-exceptional-base-change-map", "theorem-smooth-purity-all-admissible-coefficients", "definition-relative-dualizing-complex", "theorem-sp-qbar", "definition-verdier-dual-evaluation", "lemma-internal-adjunction-two-exchange-formulas", "theorem-verdier-biduality", "definition-correspondence", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
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
