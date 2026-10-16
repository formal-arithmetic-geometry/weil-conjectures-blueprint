+++
id = "lem-weil-geometric-generic-exchange"
kind = "lemma"
title = "Geometric generic restriction and the boundary operations"
lean = ["AlgebraicGeometry.Etale.isIso_derivedBaseChangeMap_app_of_isOpenImmersion_of_generic", "AlgebraicGeometry.Etale.isIso_derivedHomUpperStarComparison_rightDerivedLowerStar_of_generic", "AlgebraicGeometry.Etale.isIso_derivedHomUpperStarComparison_rightDerivedLowerStar_of_isClosedImmersion", "AlgebraicGeometry.Etale.isIso_derivedHomUpperStarComparison_of_generic", "AlgebraicGeometry.Etale.derivedHomUpperStarComparison", "AlgebraicGeometry.Etale.derivedHomUpperStarComparison_ev", "AlgebraicGeometry.Etale.isIso_rightDerivedUpperShriekBaseChangeMap_app_of_isIso", "AlgebraicGeometry.Etale.isIso_rightDerivedUpperShriekBaseChangeMap_app_of_generic"]
order = 2470
uses = ["def-weil-open-closed-recollement", "def-weil-site-perfect-complex", "lem-exc-closed-amplitude", "lem-exc-closed-support-triangle", "lem-weil-bounded-finite-tor-perfect", "lem-weil-pbc-derived-cohomology-continuity", "lem-weil-stratum-ambient-hom", "sbc-thm-bounded-below-derived-smooth-base-change", "thm-dg-finite-type-constructibility", "thm-weil-pbc-universal-homeomorphism-invariance"]
+++
Let $B$ be a smooth integral curve over $k$, let
$\bar\eta=\operatorname{Spec}\overline{k(B)}$, and let $g$
denote geometric generic pullback on a finite-type $B$-scheme.
For a separated finite-type $B$-morphism $h:T\to X$, a closed
immersion $i:Z\hookrightarrow X$, and bounded constructible
complexes in the expressions below, the natural comparisons are
isomorphisms:

$$
g_X^*Rh_*L\cong Rh_{\bar\eta,*}g_T^*L,
\qquad
g_Z^*Ri^!M\cong Ri_{\bar\eta}^!g_X^*M.
$$

For $K\in D^b_{ctf}(X_{\Et},A)$ and
$M\in D^b_c(X_{\Et},A)$, one also has

$$
g_X^*R\mathcal Hom_A(K,M)
\cong R\mathcal Hom_A(g_X^*K,g_X^*M).
$$

The comparisons preserve evaluation and tensor adjunction.
