+++
id = "lem-a1-lisse-middle-extension"
kind = "lemma"
title = "Recovery from a dense lisse open"
lean = ["AlgebraicGeometry.ProEtale.nonempty_adicLowerStar_unit_iso_geometricFiberMap", "AlgebraicGeometry.WeilSheaf.IsLisse.isIso_upperStarLowerStarAdjunction_unit_app", "AlgebraicGeometry.WeilSheaf.IsLisse.nonempty_iso_directImage_upperStar", "AlgebraicGeometry.Scheme.isIso_sheafFiber_map_unit_upperStarLowerStarAdjunction", "AlgebraicGeometry.WeilSheaf.exists_lowerStar_iso_directImage_of_isFinite", "AlgebraicGeometry.ProEtale.IsAdicLisseSheaf.isIso_adicUpperStarLowerStarAdjunction_unit_app"]
order = 2989
uses = ["def-wf-middle-extension", "lem-wf-boundary-stalk-invariants", "sk-lem-coefficient-heart", "sk-thm-sf-ctf-stability"]
+++
If $\mathcal F$ is lisse on a smooth curve $C_0$ and
$j:U_0\hookrightarrow C_0$ is dense, then the adjunction map

$$
\mathcal F\xrightarrow{\sim}j_*j^*\mathcal F
$$

is an isomorphism.
