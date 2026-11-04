+++
id = "proposition-composition-base-change-rf-shriek"
kind = "proposition"
title = "Composition and base change for $Rf_!$"
order = 511
lean = ["AlgebraicGeometry.Etale.nonempty_iso_rightDerivedLowerShriek_comp", "AlgebraicGeometry.Etale.rightDerivedLowerShriekPlusCompIso", "AlgebraicGeometry.Etale.rightDerivedLowerShriekPlusCompIso_assoc", "AlgebraicGeometry.Etale.isIso_derivedPlusFormalism_baseChange_and_shriekBaseChange"]
uses = ["definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "theorem-proper-base-change-classical-pro", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness"]
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
   it is compatible with composing cartesian squares.
