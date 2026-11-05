+++
id = "lemma-class-diagonal-projective-line"
kind = "lemma"
title = "The class of the diagonal of $\\mathbf P^1_S$"
order = 551
lean = ["AlgebraicGeometry.Etale.projectiveLineTrace_diagonal", "AlgebraicGeometry.Etale.projectiveLineTrace_diagonal_swap", "AlgebraicGeometry.Etale.ordinaryFiniteP1_diagonal_integral", "AlgebraicGeometry.Etale.projectiveLine_diagonal_ker_isInvertible"]
uses = ["lemma-stability", "proposition-comparison-morphism-inverse-image", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "definition-exceptional-base-change-finite", "lemma-degree-zero-calculation", "lemma-reduction-field", "lemma-reduction-curve-over-normal-base", "proposition-base-change-larger-algebraically-closed", "lemma-kunneth-field-coefficients", "lemma-schematic-closure-uniqueness", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
Let $S$ be of finite type over $k$, and let $p_i$ and
$\operatorname{Tr}_{p_i}$ be as above. The diagonal $\Delta$ is a relative
effective Cartier divisor in $\mathbf P^1_S\times_S\mathbf P^1_S$ over $S$,
and it remains one after every base change $S'\to S$. Let

$$
\delta:\Delta_*A_{\mathbf P^1_S}\longrightarrow
A_{\mathbf P^1_S\times_S\mathbf P^1_S}(1)[2]
$$

be its cycle class (Lemma [lemma-cycle-class-cartier-divisor]). Then for
$i=1,2$ the composite

$$
s_i:A_{\mathbf P^1_S}=Rp_{i*}\Delta_*A_{\mathbf P^1_S}
\xrightarrow{Rp_{i*}\delta}
Rp_{i*}A_{\mathbf P^1_S\times_S\mathbf P^1_S}(1)[2]
\xrightarrow{\operatorname{Tr}_{p_i}}A_{\mathbf P^1_S}
\tag{6.6}
$$

is the identity.
