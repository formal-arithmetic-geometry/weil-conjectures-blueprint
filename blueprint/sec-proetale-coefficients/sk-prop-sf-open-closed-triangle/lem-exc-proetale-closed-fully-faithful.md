+++
id = "lem-exc-proetale-closed-fully-faithful"
kind = "lemma"
title = "Full faithfulness of closed direct image"
lean = ["AlgebraicGeometry.ProEtale.isIso_upperStarLowerStarAdjunction_counit", "AlgebraicGeometry.ProEtale.fullyFaithfulLowerStar"]
order = 1092
uses = ["def-weil-pbc-proetale-operations", "def-weil-pbc-scheme-conventions", "lem-exc-closed-localization", "lem-exc-closed-site-adjunction"]
+++
Let $R$ be a ring and $i:Z\hookrightarrow X$ any closed immersion. On
pro-etale sheaves of $R$-modules the adjunction counit $i^*i_*G\to G$ is an
isomorphism for every $G$. Thus $i_*$ is fully faithful, without a
constructibility hypothesis.
