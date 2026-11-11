+++
id = "lemma-cohomology-projective-line-trace"
kind = "lemma"
title = "Cohomology of the projective line and the trace"
order = 546
lean = ["AlgebraicGeometry.Etale.isIso_projectiveLineDecompositionMap", "AlgebraicGeometry.Etale.projectiveLineDecompositionMap_baseChange", "AlgebraicGeometry.Etale.projectiveLineTrace", "AlgebraicGeometry.Etale.projectiveLineTrace_baseChange"]
uses = ["lemma-stability", "proposition-comparison-morphism-inverse-image", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "lemma-class-diagonal-projective-line", "proposition-six-operations-change-coefficients", "lemma-schematic-closure-uniqueness", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "lemma-rigidification-along-section", "lemma-twisting-h-0-1-h", "corollary-degree-jacobian"]
+++
Let $\Lambda$ be a finite commutative $\ell$-primary ring, let $S$ be a
Noetherian scheme on which $\ell$ is invertible, and let
$p:\mathbf P^1_S\to S$ be the projection. The unit
$\Lambda_S\to Rp_*\Lambda_{\mathbf P^1_S}$ and the class
$c_1(\mathcal O_{\mathbf P^1_S}(1))$ define an isomorphism

$$
\sigma_S:\Lambda_S\oplus\Lambda_S(-1)[-2]
\ \xrightarrow{\ \sim\ }\ Rp_*\Lambda_{\mathbf P^1_S}
\quad\text{in }D^+(S_{\acute{e}t},\Lambda),
\tag{6.4}
$$

compatible with base change in the sense that for $g:S'\to S$ with $S'$
Noetherian, the base change map $g^*Rp_*\Lambda\to Rp'_*\Lambda$ carries $g^*\sigma_S$ to $\sigma_{S'}$. Let

$$
\operatorname{Tr}_p:Rp_*\Lambda_{\mathbf P^1_S}(1)[2]\longrightarrow\Lambda_S
\tag{6.5}
$$

be the morphism given by the projection
onto the summand $\Lambda_S$ of the twist of $\sigma_S$.
Then $\operatorname{Tr}_p$ is compatible with every Noetherian base
change.
