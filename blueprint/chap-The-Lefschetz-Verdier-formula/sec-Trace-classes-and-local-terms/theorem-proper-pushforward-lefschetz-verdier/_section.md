+++
id = "theorem-proper-pushforward-lefschetz-verdier"
kind = "theorem"
title = "Proper pushforward and Lefschetz–Verdier"
order = 926
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.trace_globalOperator_eq_sum_localTerm", "AlgebraicGeometry.ProEtale.CondensedRing.BorelMooreSection.integral_eq_sum_localTerm"]
uses = ["proposition-etale-implications", "lemma-stability", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "theorem-comparison-direct-images", "lemma-comparison-direct-images-compatibilities", "proposition-locally-constant-sheaves-finite-presentation", "theorem-comparison-constructible-sheaves", "proposition-pro-etale-site-separably-closed", "definition-tate-twists", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "lemma-reduction-derived-nakayama", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "definition-exceptional-base-change-finite", "proposition-adjunction-projective-line", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "definition-change-of-coefficients-maps", "lemma-change-coefficients-compact-support", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "proposition-isomorphisms-reduce-finite-coefficients", "lemma-degree-zero-calculation", "lemma-reduction-field", "lemma-reduction-curve-over-normal-base", "proposition-base-change-larger-algebraically-closed", "lemma-change-coefficients", "lemma-kunneth-field-coefficients", "definition-exceptional-base-change-map", "theorem-smooth-purity-all-admissible-coefficients", "definition-relative-dualizing-complex", "theorem-sp-qbar", "definition-verdier-dual-evaluation", "lemma-internal-adjunction-two-exchange-formulas", "theorem-verdier-biduality", "definition-correspondence", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
Let $f:X\to Y$ and $g:C\to C'$ be proper, and let
$c'=(c'_1,c'_2):C'\to Y\times Y$ satisfy $c'_ig=fc_i$. Set $K'=Rf_*K$, and
let $u'$ be the pushforward of $u$ to $(Y,K')$ of
Definition [definition-pushforward-correspondence]. With
the induced proper map $h:\Fix(c)\to \Fix(c')$ one has

$$
\operatorname{Tr}_{c'}(u')=h_*\operatorname{Tr}_c(u).
$$

If $X$ and $C$ are proper over $k$, this gives

$$
\operatorname{tr}_A(T_c(u)\mid R\Gamma(X,K))
=\int_{\Fix(c)}\operatorname{Tr}_c(u)
=\sum_B\operatorname{LT}_B(u),
$$

for any finite open-and-closed decomposition $\Fix(c)=\coprod B$.
