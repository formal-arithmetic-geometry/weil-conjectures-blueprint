+++
id = "theorem-contracting-correspondences-local-terms"
kind = "theorem"
title = "Contracting correspondences and local terms"
order = 1711
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.restrict_traceClass_eq_pushforward_of_isContractingAt"]
uses = ["proposition-etale-implications", "lemma-stability", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "theorem-comparison-direct-images", "lemma-comparison-direct-images-compatibilities", "proposition-locally-constant-sheaves-finite-presentation", "theorem-comparison-constructible-sheaves", "proposition-pro-etale-site-separably-closed", "definition-tate-twists", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "lemma-reduction-derived-nakayama", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "definition-exceptional-base-change-finite", "proposition-adjunction-projective-line", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "definition-change-of-coefficients-maps", "lemma-change-coefficients-compact-support", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "proposition-isomorphisms-reduce-finite-coefficients", "lemma-degree-zero-calculation", "lemma-reduction-field", "lemma-reduction-curve-over-normal-base", "proposition-base-change-larger-algebraically-closed", "lemma-change-coefficients", "lemma-kunneth-field-coefficients", "definition-exceptional-base-change-map", "theorem-smooth-purity-all-admissible-coefficients", "definition-relative-dualizing-complex", "theorem-sp-qbar", "definition-verdier-dual-evaluation", "lemma-internal-adjunction-two-exchange-formulas", "theorem-verdier-biduality", "definition-correspondence", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
Let $c=(c_1,c_2):C\to X\times X$ be a correspondence, and let
$Z\hookrightarrow X$ have ideal $I$. Let $F_0$ be a connected component
of $\Fix(c)$ that is open and closed and whose image meets $Z$. Choose
an open neighbourhood $W\subset C$ of $F_0$ on which

$$
I_2=c_2^{-1}(I)\mathcal O_W\subset
I_1=c_1^{-1}(I)\mathcal O_W,
\qquad I_2^n\subset I_1^{n+1}\quad\text{for some }n\geq1.
$$

Let $K\in D^b_{\mathrm{ctf}}(X,A)$, let $u:c_2^*K\to c_1^!K$ be a cohomological
correspondence, and let $u_Z$ be the restriction
(E.21) to $Z$ of $u|_W$, for the
correspondence $c|_W$, with $c_Z:C_Z=(W\cap c_1^{-1}Z)_{\mathrm{red}}\to
Z_{\mathrm{red}}\times Z_{\mathrm{red}}$. Then $h_{F_0}$ is an
isomorphism after reduction, and

$$
\operatorname{Tr}_c(u)|_{F_0}
=(h_{F_0})_*\bigl(\operatorname{Tr}_{c_Z}(u_Z)|_{F_{0,Z}}\bigr),
$$

where $(h_{F_0})_*:H^0(F_{0,Z},\omega_{F_{0,Z}})\to H^0(F_0,\omega_{F_0})$
is the induced isomorphism. In particular, if $F_0$ is proper, then
$\operatorname{LT}_{F_0}(u)=\operatorname{LT}_{F_{0,Z}}(u_Z)$.
