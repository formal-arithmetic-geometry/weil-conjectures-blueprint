+++
id = "proposition-composition-open-restriction-compactifications-f"
kind = "proposition"
title = "Composition, open restriction and compactifications for $f^!$"
order = 530
lean = ["AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_comp", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperShriekComp_padicAlgCl", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperShriekComp_padicAlgCl_assoc", "AlgebraicGeometry.Etale.rightDerivedUpperShriekIdIso", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperShriekId", "AlgebraicGeometry.Etale.rightDerivedUpperShriekIsoOfIsOpenImmersion", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperShriekIsoUpperStar_padicIntegers", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperShriekIsoUpperStar_padicAlgCl", "AlgebraicGeometry.Etale.isIso_rightDerivedUpperShriekBaseChangeMap_of_isOpenImmersion", "AlgebraicGeometry.Etale.rightDerivedUpperShriekOfCompactification", "AlgebraicGeometry.ProEtale.CondensedRing.ContinuousMapRingObj.boundedConstructibleUpperShriekOfCompactification", "AlgebraicGeometry.ProEtale.CondensedRing.PadicIntegersRingObj.boundedConstructibleUpperShriekOfCompactification", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperShriekOfCompactification"]
uses = ["theorem-existence-exceptional-inverse-image", "definition-localizing-subcategory", "definition-compactification-refinement"]
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
