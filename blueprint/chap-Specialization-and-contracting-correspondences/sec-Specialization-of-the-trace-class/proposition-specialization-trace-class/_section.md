+++
id = "proposition-specialization-trace-class"
kind = "proposition"
title = "Specialization of the trace class"
order = 1689
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.TraceSpecialization.sp", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.TraceSpecialization.sp_traceClass_eq_traceClass"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "lemma-inverse-image-coefficient-sheaves", "lemma-constructible-sheaves", "lemma-integral-models", "lemma-inverse-image-tensor-product", "proposition-composition-base-change-rf-shriek", "theorem-f-shriek-ell-adic-coefficients", "proposition-six-operations-dctf", "proposition-sp-unique-adjoint", "definition-verdier-dual-evaluation", "definition-correspondence", "lemma-external-duality-trace-morphism", "definition-trace-morphism", "definition-trace-class-local-terms", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
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
