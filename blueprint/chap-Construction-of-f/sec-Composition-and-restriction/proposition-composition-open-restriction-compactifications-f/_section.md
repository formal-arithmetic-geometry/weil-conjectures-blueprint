+++
id = "proposition-composition-open-restriction-compactifications-f"
kind = "proposition"
title = "Composition, open restriction and compactifications for $f^!$"
order = 530
lean = ["AlgebraicGeometry.Etale.existsUnique_rightDerivedUpperShriekOfCompactificationIso", "AlgebraicGeometry.ProEtale.exists_rightDerivedUpperShriekAdjunction_comp_eq", "AlgebraicGeometry.Etale.rightDerivedUpperShriekIdIso", "AlgebraicGeometry.Etale.rightDerivedUpperShriekOfCompactification"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "proposition-comparison-morphism-inverse-image", "theorem-bounded-below-cohomology-comparison", "proposition-comparison-immersions", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "theorem-proper-base-change-classical-pro", "proposition-construction-independence-rf-shriek", "proposition-forgetting-supports-composition", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "definition-relative-picard-functor", "lemma-finite-direct-images", "lemma-finite-morphisms-cohomology"]
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
