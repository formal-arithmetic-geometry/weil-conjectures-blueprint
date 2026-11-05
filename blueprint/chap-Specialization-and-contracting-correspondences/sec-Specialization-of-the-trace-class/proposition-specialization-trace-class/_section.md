+++
id = "proposition-specialization-trace-class"
kind = "proposition"
title = "Specialization of the trace class"
order = 1684
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.TraceSpecialization.sp", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.TraceSpecialization.sp_traceClass"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "proposition-comparison-immersions", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "lemma-proper-direct-image-unbounded-complexes", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "proposition-dctf-x-qbar-2-colimit", "lemma-perfect-complexes-geometric-point", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "proposition-pullback-multiplication-n", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "corollary-serre-duality-field-extension", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
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
