+++
id = "theorem-existence-exceptional-inverse-image"
kind = "theorem"
title = "Existence of the exceptional inverse image"
order = 521
lean = ["AlgebraicGeometry.ProEtale.exists_rightAdjoint_rightDerivedLowerShriekLocalizing", "AlgebraicGeometry.ProEtale.CondensedRing.exists_rightAdjoint_rightDerivedLowerShriekLocalizing_continuousMapRingObj", "AlgebraicGeometry.ProEtale.CondensedRing.exists_rightAdjoint_rightDerivedLowerShriekLocalizing_padicIntegersRingObj", "AlgebraicGeometry.ProEtale.CondensedRing.exists_rightAdjoint_rightDerivedLowerShriekLocalizing_padicAlgClRingObj", "AlgebraicGeometry.ProEtale.rightDerivedUpperShriekLocalizing", "AlgebraicGeometry.ProEtale.rightDerivedUpperShriekLocalizingAdjunction"]
uses = ["definition-localizing-subcategory", "proposition-construction-independence-rf-shriek", "definition-compactification-refinement"]
+++
Let $\Lambda\in\{A,\mathbf Z_\ell,\mathcal O_E,\mathbf Q_\ell,E,\overline{\mathbf Q}_\ell\}$ be any admissible
coefficient ring. For every separated morphism of finite type $f:X\to Y$,
the coproduct-preserving functor
$Rf_!:\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))\to\Loc(D^b_{\mathrm{ctf}}(Y,\Lambda))$ has an exact
right adjoint

$$
f^!:\Loc(D^b_{\mathrm{ctf}}(Y,\Lambda))\longrightarrow\Loc(D^b_{\mathrm{ctf}}(X,\Lambda)),
\qquad
\Hom(Rf_!M,N)\simeq\Hom(M,f^!N),
$$

for $M\in\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$ and $N\in\Loc(D^b_{\mathrm{ctf}}(Y,\Lambda))$.
It is unique up to unique isomorphism compatible with the adjunction,
and it preserves arbitrary direct sums.
