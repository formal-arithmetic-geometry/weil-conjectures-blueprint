+++
id = "lemma-class-diagonal-projective-line"
kind = "lemma"
title = "The class of the diagonal of $\\mathbf P^1_S$"
order = 551
lean = ["AlgebraicGeometry.Etale.projectiveLineTrace_diagonal", "AlgebraicGeometry.Etale.projectiveLineTrace_diagonal_swap", "AlgebraicGeometry.Etale.ordinaryFiniteP1_diagonal_integral", "AlgebraicGeometry.Etale.projectiveLine_diagonal_ker_isInvertible"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "lemma-cohomology-modules-underlying-abelian", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "theorem-proper-base-change-classical-pro", "proposition-construction-independence-rf-shriek", "proposition-composition-base-change-rf-shriek", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "definition-exceptional-base-change-finite", "lemma-cohomology-projective-line-trace", "theorem-smooth-base-change-classical-torsion", "theorem-smooth-base-change-classical-torsion-2", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "definition-relative-picard-functor", "lemma-finite-direct-images", "lemma-finite-morphisms-cohomology"]
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
