+++
id = "corollary-contracting-local-terms-point"
kind = "corollary"
title = "Contracting local terms at a point"
order = 1715
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.localTerm_traceClass_eq_integral_of_isContractingAt", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.localTerm_traceClass_ofGraph_eq_trace_of_isContractingAt"]
uses = ["proposition-etale-implications", "lemma-stability", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "theorem-comparison-direct-images", "lemma-comparison-direct-images-compatibilities", "proposition-locally-constant-sheaves-finite-presentation", "theorem-comparison-constructible-sheaves", "proposition-pro-etale-site-separably-closed", "definition-tate-twists", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "lemma-reduction-derived-nakayama", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "definition-exceptional-base-change-finite", "proposition-adjunction-projective-line", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "definition-change-of-coefficients-maps", "lemma-change-coefficients-compact-support", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "proposition-isomorphisms-reduce-finite-coefficients", "lemma-degree-zero-calculation", "lemma-reduction-field", "lemma-reduction-curve-over-normal-base", "proposition-base-change-larger-algebraically-closed", "lemma-change-coefficients", "lemma-kunneth-field-coefficients", "definition-exceptional-base-change-map", "theorem-smooth-purity-all-admissible-coefficients", "definition-relative-dualizing-complex", "theorem-sp-qbar", "definition-verdier-dual-evaluation", "lemma-internal-adjunction-two-exchange-formulas", "theorem-verdier-biduality", "definition-correspondence", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
Let $y\in X(k)$, and suppose that $c_1^{-1}(y)$ is a single reduced point
$z$, with $c_2(z)=y$. Suppose that $F_0=\{z\}$ is an isolated reduced
component of $\Fix(c)$, open and closed, and that on a neighbourhood of $F_0$
the ideal $I_y$ satisfies

$$
c_2^{-1}(I_y)\mathcal O_C\subset c_1^{-1}(I_y)\mathcal O_C,
\qquad
\bigl(c_2^{-1}(I_y)\mathcal O_C\bigr)^n
\subset\bigl(c_1^{-1}(I_y)\mathcal O_C\bigr)^{n+1}
\quad\text{for some }n\geq1.
$$

Then for every $K\in D^b_{\mathrm{ctf}}(X,A)$ and every morphism
$u:c_2^*K\to c_1^!K$, the local term at $F_0$ is the categorical
trace of the restriction $u_Z$ to $Z=\{y\}$ of $u$ restricted to
that neighbourhood, defined in (E.21). In particular, for
$c=(\operatorname{id}_X,h)$,

$$
\operatorname{LT}_y(u)
=\operatorname{tr}_A(u_{\bar y}\mid K_{\bar y}).
$$
