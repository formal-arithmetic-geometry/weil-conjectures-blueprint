+++
id = "lemma-class-diagonal-projective-line"
kind = "lemma"
title = "The class of the diagonal of $\\mathbf P^1_S$"
order = 551
lean = ["AlgebraicGeometry.Etale.projectiveLineTrace_diagonal", "AlgebraicGeometry.Etale.projectiveLineTrace_diagonal_swap"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "proposition-forgetting-supports-composition", "definition-exceptional-base-change-finite", "theorem-smooth-base-change-classical-torsion", "lemma-kunneth-one-identity-factor", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
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
