+++
id = "proposition-composition-base-change-rf-shriek"
kind = "proposition"
title = "Composition and base change for $Rf_!$"
order = 516
lean = ["AlgebraicGeometry.Etale.isIso_derivedPlusFormalism_baseChange_and_shriekBaseChange", "AlgebraicGeometry.Etale.rightDerivedLowerShriekPlusCompIso", "AlgebraicGeometry.Etale.rightDerivedLowerShriekPlusCompIso_assoc"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-pro-etale-site-separably-closed", "lemma-inverse-image-coefficient-sheaves", "lemma-constructible-sheaves", "lemma-integral-models", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "theorem-proper-base-change-classical-pro", "definition-localizing-subcategory", "lemma-inverse-image-tensor-product", "proposition-construction-independence-rf-shriek", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
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
