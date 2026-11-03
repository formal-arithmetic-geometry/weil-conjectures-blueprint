+++
id = "lem-exc-proetale-closed-essential-image"
kind = "lemma"
title = "The essential image of closed direct image"
lean = ["AlgebraicGeometry.ProEtale.isIso_adicUpperStarLowerStarAdjunction_unit_app_of_isCompl", "AlgebraicGeometry.ProEtale.adicLowerStar_essImage_iff_of_isCompl", "AlgebraicGeometry.ProEtale.isIso_upperStarLowerStarAdjunction_unit_app_of_isCompl", "AlgebraicGeometry.ProEtale.lowerStar_essImage_iff_of_isCompl"]
order = 1350
uses = ["def-weil-pbc-proetale-operations", "def-weil-pbc-scheme-conventions", "lem-exc-closed-localization", "lem-exc-open-closed-detection", "lem-exc-proetale-closed-fully-faithful", "det-prop-sfb-module-pullback-exact-main"]
+++
For a closed immersion $i:Z\hookrightarrow X$ with quasi-compact open
complement $j$, a pro-etale module sheaf $F$ lies in the image of $i_*$ if
and only if $j^*F=0$. For such a sheaf the canonical unit $F\to i_*i^*F$ is
an isomorphism.
