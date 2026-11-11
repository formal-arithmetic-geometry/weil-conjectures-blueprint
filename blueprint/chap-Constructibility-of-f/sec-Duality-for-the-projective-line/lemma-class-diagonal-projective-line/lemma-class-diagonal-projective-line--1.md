+++
id = "lemma-class-diagonal-projective-line--1"
kind = "lemma"
title = "The class of the diagonal of $\\mathbf P^1_S$ (1)"
name_showing = false
order = 551001
aliases = ["bp-r166-1"]
lean = ["AlgebraicGeometry.Etale.projectiveLineTrace_diagonal", "AlgebraicGeometry.Etale.projectiveLineTrace_diagonal_swap", "AlgebraicGeometry.Etale.projectiveLine_diagonal_ker_isInvertible"]
uses = ["lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "definition-exceptional-base-change-finite", "lemma-cohomology-projective-line-trace", "definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "lemma-stability--6", "definition-small-pro-etale-site--1", "proposition-comparison-morphism-inverse-image--1", "definition-constructible-sheaves--5", "definition-constructible-sheaves--6", "definition-underived-base-change-map--1", "definition-derived-base-change-map--1", "lemma-identity-pasting--1", "lemma-identity-pasting--2", "definition-torsion-sheaves--1", "definition-torsion-sheaves--3", "lemma-acyclic-resolutions--1", "theorem-cohomology-curves--1", "theorem-cohomology-curves--2", "lemma-finiteness-small-etale-topoi--2", "proposition-proper-base-change-projective-line--1", "lemma-finite-morphisms--2", "theorem-proper-base-change-classical-pro--1", "theorem-proper-base-change-classical-pro--2", "proposition-construction-independence-rf-shriek--7", "proposition-composition-base-change-rf-shriek--4", "proposition-forgetting-supports-composition--3", "definition-exceptional-base-change-finite--2", "theorem-smooth-base-change-classical-torsion--1", "theorem-smooth-base-change-classical-torsion-2--1", "proposition-sp-unique-adjoint--1", "definition-compactification-refinement--1", "definition-compactification-refinement--3", "lemma-schematic-closure-uniqueness--1", "lemma-schematic-closure-uniqueness--2", "definition-relative-picard-functor--2", "lemma-finite-direct-images--2", "lemma-finite-morphisms-cohomology--2"]
+++
Let $S$ be of finite type over $k$ and let $\Lambda$ be a finite
commutative $\ell$-primary ring; we work on the étale sites, and $p_i$ and
$\operatorname{Tr}_{p_i}$ are as above. The diagonal $\Delta$ is a relative
effective Cartier divisor in $\mathbf P^1_S\times_S\mathbf P^1_S$ over $S$,
and it remains one after every base change $S'\to S$. Let

$$
\delta:\Delta_*\Lambda_{\mathbf P^1_S}\longrightarrow
\Lambda_{\mathbf P^1_S\times_S\mathbf P^1_S}(1)[2]
$$

be its cycle class (Lemma [lemma-cycle-class-cartier-divisor]). Then for
$i=1,2$ the composite

$$
s_i:\Lambda_{\mathbf P^1_S}=Rp_{i*}\Delta_*\Lambda_{\mathbf P^1_S}
\xrightarrow{Rp_{i*}\delta}
Rp_{i*}\Lambda_{\mathbf P^1_S\times_S\mathbf P^1_S}(1)[2]
\xrightarrow{\operatorname{Tr}_{p_i}}\Lambda_{\mathbf P^1_S}
\tag{6.6}
$$

is the identity.
