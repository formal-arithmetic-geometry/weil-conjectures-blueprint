+++
id = "prop-sf-localization-all-stages"
kind = "theorem"
title = "The closed-support triangle for every admissible coefficient ring"
lean = ["AlgebraicGeometry.WeilComplex.upperStarDerivedLowerStarAdjunction", "AlgebraicGeometry.WeilComplex.subsingleton_hom_shift", "AlgebraicGeometry.WeilComplex.closedUpperShriek", "AlgebraicGeometry.WeilComplex.closedUpperShriekAdjunction", "AlgebraicGeometry.WeilComplex.existsUnique_distTriang_closedSupportTriangle", "AlgebraicGeometry.WeilComplex.exists_triangleHom_closedSupportTriangle", "AlgebraicGeometry.WeilComplex.closedSupportTriangle_hom_ext", "AlgebraicGeometry.WeilComplex.isZero_closedUpperShriek_obj", "AlgebraicGeometry.WeilComplex.isIso_closedUpperShriekAdjunction_unit", "AlgebraicGeometry.WeilComplex.exists_iso_mapTriangle_closedSupportTriangle", "AlgebraicGeometry.WeilComplex.nonempty_forget_closedUpperShriek_obj_iso", "AlgebraicGeometry.WeilComplex.exists_closedUpperShriek_comp_forget_iso", "CategoryTheory.Pretriangulated.Recollement.isIso_mateEquiv", "CategoryTheory.Pretriangulated.Recollement.rightAdjointIso", "CategoryTheory.Pretriangulated.Recollement.isoAlgebraAdjunction", "CategoryTheory.Pretriangulated.Recollement.isIso_mateEquiv_symm", "CategoryTheory.Pretriangulated.Recollement.leftAdjointIso", "CategoryTheory.Pretriangulated.Recollement.map_mor\u2083_comp_str", "CategoryTheory.Pretriangulated.Recollement.mapTriangleIso", "AlgebraicGeometry.ProEtale.boundedConstructibleAdic_rightDerivedFunctor_adicLowerStar_obj", "AlgebraicGeometry.ProEtale.subsingleton_hom_shift_boundedConstructibleAdic", "AlgebraicGeometry.ProEtale.boundedConstructibleAdicClosedUpperShriekAdjunction", "AlgebraicGeometry.ProEtale.existsUnique_distTriang_boundedConstructibleAdicClosedSupportTriangle", "AlgebraicGeometry.ProEtale.exists_triangleHom_boundedConstructibleAdicClosedSupportTriangle", "AlgebraicGeometry.ProEtale.boundedConstructibleAdicClosedSupportTriangle_hom_ext", "AlgebraicGeometry.ProEtale.isZero_boundedConstructibleAdicClosedUpperShriek_obj", "AlgebraicGeometry.ProEtale.isIso_boundedConstructibleAdicClosedUpperShriekAdjunction_unit", "AlgebraicGeometry.ProEtale.boundedConstructible_rightDerivedFunctor_lowerStar_of_isOpenImmersion", "AlgebraicGeometry.ProEtale.boundedConstructible_rightDerivedFunctor_lowerStar_obj_closedUpperShriek", "AlgebraicGeometry.ProEtale.boundedConstructible_closedUpperShriek_rightDerivedFunctor_obj", "AlgebraicGeometry.ProEtale.boundedConstructible_closedSupportTriangle_obj", "AlgebraicGeometry.ProEtale.boundedConstructibleClosedUpperShriekAdjunction", "AlgebraicGeometry.ProEtale.isIso_boundedConstructibleClosedUpperShriekAdjunction_unit_app", "AlgebraicGeometry.ProEtale.isZero_boundedConstructibleClosedUpperShriek_obj", "AlgebraicGeometry.ProEtale.nonempty_iso_closedUpperShriek_rightDerivedFunctor_obj_rightDerivedUpperShriek_obj", "AlgebraicGeometry.ProEtale.torAmplitudeIn_rightDerivedFunctor_lowerStar_of_isClosedImmersion", "AlgebraicGeometry.ProEtale.torAmplitudeIn_rightDerivedFunctor_lowerStar_of_isOpenImmersion", "AlgebraicGeometry.ProEtale.constructibleFiniteTor_rightDerivedFunctor_lowerStar_of_isOpenImmersion", "AlgebraicGeometry.ProEtale.boundedConstructible_and_torAmplitudeIn_rightDerivedLowerStar_of_isClosedImmersion", "AlgebraicGeometry.ProEtale.constructibleFiniteTor_rightDerivedFunctor_lowerStar_of_isClosedImmersion", "AlgebraicGeometry.ProEtale.boundedConstructible_and_torAmplitudeIn_leftDerivedFunctor_upperStar_obj", "AlgebraicGeometry.ProEtale.torAmplitudeIn_rightDerivedFunctor_lowerStar_obj_closedUpperShriek", "AlgebraicGeometry.ProEtale.torAmplitudeIn_closedUpperShriek_rightDerivedFunctor_obj", "AlgebraicGeometry.ProEtale.constructibleFiniteTor_closedUpperShriek_rightDerivedFunctor_obj", "AlgebraicGeometry.ProEtale.constructibleFiniteTor_closedSupportTriangle_obj", "AlgebraicGeometry.ProEtale.finiteTorClosedUpperShriekAdjunction", "AlgebraicGeometry.ProEtale.isIso_finiteTorClosedUpperShriekAdjunction_unit_app", "AlgebraicGeometry.ProEtale.isZero_finiteTorClosedUpperShriek_obj"]
order = 3217
tags = ["latex:proposition"]
uses = ["def-sf-setting", "lem-integral-ctf-equals-bc", "det-def-sfb-bounded-constructible", "det-def-sf-operations", "sk-thm-existence", "sk-thm-sf-ctf-stability", "sk-prop-scalar-six", "def-sc-etale-torsion-cd", "def-weil-derived-direct-image", "def-weil-derived-pullback-tensor-hom", "def-weil-exceptional-inverse-image", "def-weil-finite-tor-amplitude", "def-weil-pbc-proetale-operations", "def-weil-weil-sheaf-complex", "lem-exc-proetale-closed-essential-image", "lem-exc-proetale-closed-exact", "lem-exc-proetale-closed-support", "lem-exc-proetale-support-triangle", "lem-exc-residue-tor-test", "lem-sf-etale-direct-image-vanishing", "lem-sf-proetale-constructible-origin", "lem-sf-proetale-residue-tor-test", "prop-sf-closed-immersion-unit", "prop-sf-closed-unit-all-stages", "prop-sf-open-closed-triangle-all-stages", "prop-weil-pbc-comparison-direct-image", "lem-sfb-finite-upper-star-unit", "thm-constructible-serre", "thm-fin-open-immersion", "thm-sc-finite-type-torsion-cd", "thm-sp-truncation-e2", "thm-weil-pbc-site-comparison"]
+++
Let $X$ be a separated finite-type $k$-scheme, let $i:Z\hookrightarrow X$ be
a closed immersion and $j:U\hookrightarrow X$ the complementary open
immersion. Let $\Lambda$ be one of the coefficient rings
$A_{E,n},\mathcal O_E,E,\Qlb$, regarded as condensed rings, with the
categories $D^b_c(-,\Lambda)\subseteq D(-_{\mathrm{proét}},\Lambda)$ of
[def-sf-setting], the pullbacks of [def-weil-derived-pullback-tensor-hom]
and the direct images $i_*$, $Rj_*$ of $\Lambda$-modules
([def-weil-derived-direct-image], [det-def-sf-operations]).

1. $Rj_*$ carries $D^b_c(U,\Lambda)$ into $D^b_c(X,\Lambda)$.
2. $i_*:D^b_c(Z,\Lambda)\to D^b_c(X,\Lambda)$ has a right adjoint $Ri^!$;
   it is the exceptional inverse image of
   [def-weil-exceptional-inverse-image] at $\Lambda=A_{E,n}$, and of
   [sk-thm-existence] in general. At $\mathcal O_E$ its reductions are
   $(Ri^!K)\otimes^{\mathbf L}_{\mathcal O_E}A_{E,m}\cong Ri_m^!K_m$.
3. For $K\in D^b_c(X,\Lambda)$ the closed exceptional counit and the open
   unit extend to a distinguished triangle
   $$
   i_*Ri^!K\longrightarrow K\longrightarrow Rj_*j^*K
   \longrightarrow i_*Ri^!K[1],
   $$
   with $\operatorname{Hom}(i_*Ri^!K[m],Rj_*j^*K)=0$ for all $m$, so the
   third arrow is unique and the triangle is functorial in $K$.
4. $Ri^!Rj_*G=0$ for $G\in D^b_c(U,\Lambda)$, and the unit
   $Q\to Ri^!i_*Q$ is an isomorphism for $Q\in D^b_c(Z,\Lambda)$.

The same holds on the finite-Tor subcategories $D^b_{ctf}(-,\Lambda)$ of
[def-sf-setting] and [def-weil-finite-tor-amplitude]. Let $d=\dim U$ and assume
$c=\operatorname{cd}_{\rm tor}(k)$ ([def-sc-etale-torsion-cd]) is finite
($c=0$ for $k$ algebraically closed).

- (1') $Rj_*$ carries $D^b_{ctf}(U,\Lambda)$ into $D^b_{ctf}(X,\Lambda)$;
   at $\Lambda=A_{E,n}$ Tor amplitude in $[a,b]$ goes to Tor amplitude in
   $[a,b+2d+c]$, and at $\mathcal O_E$ the same holds for the uniform
   interval of the reductions.
- (2') $Ri^!$ carries $D^b_{ctf}(X,\Lambda)$ into $D^b_{ctf}(Z,\Lambda)$,
   with Tor amplitude $[a,b]$ going to $[a,b+2d+c+1]$ (at $A_{E,n}$, and
   uniformly in the reductions at $\mathcal O_E$).
- (3') $i_*$, $i^*$ and $j^*$ preserve $D^b_{ctf}$ and Tor amplitude
   intervals; hence for $K\in D^b_{ctf}(X,\Lambda)$ all three vertices of
   the triangle of (3) lie in $D^b_{ctf}$.
- (4') For $G\in D^b_{ctf}(U,\Lambda)$ and $Q\in D^b_{ctf}(Z,\Lambda)$,
   $Ri^!Rj_*G=0$ and $Q\xrightarrow{\sim}Ri^!i_*Q$ inside $D^b_{ctf}$.

At $E$ and $\Qlb$ these are (1)–(4), since there $D^b_{ctf}=D^b_c$ ([lem-integral-ctf-equals-bc]).

If $X,Z,U$ come from $k_0$-schemes and $\Lambda\in\{E,\Qlb\}$, then $Ri^!$
carries Weil structures ([sk-def-sf-weil-complexes], [def-weil-weil-sheaf-complex]) for which the
adjunction is equivariant, and for Weil complexes the three arrows of the
triangle and the unit are Weil-equivariant.
