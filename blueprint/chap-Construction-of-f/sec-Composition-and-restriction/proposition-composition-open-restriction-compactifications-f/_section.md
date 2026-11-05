+++
id = "proposition-composition-open-restriction-compactifications-f"
kind = "proposition"
title = "Composition, open restriction and compactifications for $f^!$"
order = 530
lean = ["AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_comp", "AlgebraicGeometry.ProEtale.exists_rightDerivedUpperShriekAdjunction_comp_eq", "AlgebraicGeometry.Etale.rightDerivedUpperShriekIsoOfIsOpenImmersion", "AlgebraicGeometry.Etale.existsUnique_rightDerivedUpperShriekOfCompactificationIso"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "theorem-bounded-below-cohomology-comparison", "theorem-comparison-direct-images", "proposition-comparison-immersions", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "theorem-proper-base-change-classical-pro", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "definition-tate-module", "definition-relative-picard-functor", "corollary-serre-duality-field-extension", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic"]
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
