+++
id = "proposition-composition-base-change-rf-shriek"
kind = "proposition"
title = "Composition and base change for $Rf_!$"
order = 516
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekComp_padicAlgCl", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekComp_padicIntegers", "AlgebraicGeometry.Etale.nonempty_iso_rightDerivedLowerShriek_comp", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekComp_padicAlgCl_assoc", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekComp_padicAlgCl_id_left", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekComp_padicAlgCl_id_right", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleLowerShriekBaseChange_padicAlgCl", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleLowerShriekBaseChange", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleLowerShriekBaseChange_padicIntegers", "AlgebraicGeometry.Etale.isIso_rightDerivedLowerShriekBaseChangeMap", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekBaseChange_padicAlgCl_eq_baseChange", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekBaseChange_padicAlgCl_paste_horiz", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekBaseChange_padicAlgCl_paste_vert"]
uses = ["proposition-construction-independence-rf-shriek", "prose-05-31", "definition-constructible-sheaves", "definition-localizing-subcategory", "definition-derived-base-change-map", "definition-pro-etale-base-change-map", "definition-torsion-sheaves", "definition-compactification-refinement"]
+++
For every admissible $\Lambda$, the following statements hold on
$\Loc(D^b_{\mathrm{ctf}}(-,\Lambda))$ and restrict to $D^b_{\mathrm{ctf}}(-,\Lambda)$.

1. For separated morphisms of finite type $X\xrightarrow fY
  \xrightarrow gZ$ there is a canonical isomorphism
   $Rg_!\circ Rf_!\simeq R(gf)_!$. These isomorphisms are associative and
   compatible with the identity $R(\mathrm{id})_!=\mathrm{id}$.
2. Let $v:Y'\to Y$ be a morphism, $f':X'\to Y'$ the base change of $f$
   along $v$, and $u:X'\to X$ the projection. The base change map
   (5.8) is an isomorphism
   $v^*Rf_!\simeq Rf'_!u^*$. It does not depend on the compactification, and
   it is compatible with composing cartesian squares and with the
   composition isomorphisms of (1).
