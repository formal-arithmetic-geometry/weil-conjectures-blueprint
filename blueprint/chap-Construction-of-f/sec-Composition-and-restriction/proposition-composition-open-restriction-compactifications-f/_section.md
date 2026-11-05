+++
id = "proposition-composition-open-restriction-compactifications-f"
kind = "proposition"
title = "Composition, open restriction and compactifications for $f^!$"
order = 530
lean = ["AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_comp", "AlgebraicGeometry.ProEtale.exists_rightDerivedUpperShriekAdjunction_comp_eq", "AlgebraicGeometry.Etale.rightDerivedUpperShriekIsoOfIsOpenImmersion", "AlgebraicGeometry.Etale.existsUnique_rightDerivedUpperShriekOfCompactificationIso"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "proposition-comparison-morphism-inverse-image", "theorem-bounded-below-cohomology-comparison", "proposition-comparison-immersions", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "proposition-forgetting-supports-composition", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "remark-base-change-compactification", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
For every admissible $\Lambda$, the adjoints $f^!$ on
$\Loc(D^b_{\mathrm{ctf}}(-,\Lambda))$ have the following canonical compatibilities.

1. For composable $X\xrightarrow fY\xrightarrow gZ$ there are canonical
   isomorphisms $(gf)^!\simeq f^!g^!$, associative and
   compatible with the identity.
2. For an open immersion $j:U\to X$, $j^!\simeq j^*$.
3. Let $v:V\to Y$ be an open immersion, $X_V=f^{-1}(V)$ with inclusion
   $u:X_V\to X$, and $f_V:X_V\to V$ the restriction of $f$. Then
   $u^*f^!\simeq f_V^!v^*$.
4. If $f=p\circ j$ is a compactification, then $f^!\simeq j^*\circ p^!$
   on $\Loc(D^b_{\mathrm{ctf}}(Y,\Lambda))$.

In particular, $f^!$ can be computed locally on $X$ and on $Y$ for open
coverings.
