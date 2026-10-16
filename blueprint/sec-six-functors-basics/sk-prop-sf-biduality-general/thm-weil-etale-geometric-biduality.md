+++
id = "thm-weil-etale-geometric-biduality"
kind = "theorem"
title = "Finite-stage etale Verdier biduality"
lean = ["AlgebraicGeometry.mem_of_dense_of_forall_specializes_eq", "AlgebraicGeometry.topologicalKrullDim_le_of_dense", "AlgebraicGeometry.exists_dense_compactification", "AlgebraicGeometry.exists_hom_affineLine_over_apply_eq_genericPoint", "AlgebraicGeometry.exists_isClosedImmersion_affineSpace_affineLine", "AlgebraicGeometry.geometricGenericFiber_properties", "AlgebraicGeometry.topologicalKrullDim_geometricGenericFiber_add_one_le", "AlgebraicGeometry.exists_comp_geometricGenericFiber_fst_eq_algClosurePoint", "AlgebraicGeometry.isZero_sheafFiber_algClosurePoint_of_isZero_sheafFiber_upperStar", "AlgebraicGeometry.isZero_sheafFiber_algClosurePoint_of_isZero_upperStar", "AlgebraicGeometry.Etale.isZero_of_isZero_rightDerivedLowerStar_of_isFinite", "Set.Finite.of_isClosed_constructibleTopology", "AlgebraicGeometry.isFinite_comp_of_finite_range", "AlgebraicGeometry.exists_opens_isFinite_closedComplement", "AlgebraicGeometry.Etale.finite_compl_stalkZeroLocus", "AlgebraicGeometry.Etale.exists_isFinite_isZero_upperStar_of_boundedConstructible", "AlgebraicGeometry.Etale.isZero_obj\u2083_of_isIso_rightDerivedLowerStar_map", "AlgebraicGeometry.Etale.BidualityInDim", "AlgebraicGeometry.Etale.isZero_sheafFiber_homology_of_not_mem_closedPoints", "AlgebraicGeometry.Etale.isIso_verdierDualDoubleDual_app_of_isProper", "AlgebraicGeometry.Etale.isIso_verdierDualDoubleDual_app_of_forall_isProper", "AlgebraicGeometry.Etale.bidualityInDim", "AlgebraicGeometry.Etale.isIso_verdierDualDoubleDual_app_of_isAlgClosed"]
order = 2472
uses = ["lem-fin-coordinate-generic-dimension", "lem-sf-etale-direct-image-vanishing", "lem-weil-coefficient-frobenius", "lem-weil-delta-proper-pushforward", "lem-weil-delta-restriction", "lem-weil-duality-pairing", "lem-weil-geometric-generic-duality", "lem-weil-verdier-preservation-strata", "thm-nagata-compactification", "thm-sf-direct-image-tor-amplitude", "thm-sp-truncation-e2"]
+++
For every separated finite-type $X/k$, the natural map

$$
\delta_K:K\longrightarrow D_XD_XK
\qquad(K\in D^b_{ctf}(X_{\Et},A))
$$

is an isomorphism. Consequently $D_X$ is an exact contravariant
anti-equivalence of $D^b_{ctf}(X_{\Et},A)$.
