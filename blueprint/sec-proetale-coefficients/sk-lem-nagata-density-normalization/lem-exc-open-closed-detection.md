+++
id = "lem-exc-open-closed-detection"
kind = "lemma"
title = "Detection by the open and the closed restriction"
lean = ["AlgebraicGeometry.ProEtaleWeilSheaf.isZero_of_isZero_upperStar_of_isCompl", "AlgebraicGeometry.ProEtale.AdicSheaf.isZero_of_isZero_adicUpperStar_of_isCompl", "AlgebraicGeometry.ProEtale.isZero_of_isZero_upperStar_of_isCompl"]
order = 1269
uses = ["def-weil-pbc-proetale-operations", "def-weil-pbc-scheme-conventions", "lem-exc-closed-cover-extension", "lem-exc-closed-inverse-image-formula", "lem-exc-closed-localization", "lem-exc-closed-site-adjunction", "lem-weil-pbc-ind-etale-basis"]
+++
Let $i:Z\hookrightarrow X$ be closed, with quasi-compact open complement
$j:U\hookrightarrow X$. If a pro-etale module sheaf $F$ has zero inverse
images $j^*F=0$ and $i^*F=0$, then $F=0$.
