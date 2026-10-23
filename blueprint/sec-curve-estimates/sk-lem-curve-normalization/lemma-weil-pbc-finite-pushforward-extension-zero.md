+++
id = "lemma-weil-pbc-finite-pushforward-extension-zero"
kind = "lemma"
title = "Finite pushforward and extension by zero"
lean = ["AlgebraicGeometry.Etale.isIso_finiteOpenComparison", "AlgebraicGeometry.Etale.isIso_finiteOpenComparison_app"]
order = 1506
uses = ["def-weil-pbc-finite-open-comparison"]
+++
Consider a Cartesian square as in [def-weil-pbc-finite-open-comparison],
with $j_X,j_Y$ open immersions and $\bar v$ finite, and coefficients in a
category $\mathcal A$ as there. Then for every $\mathcal A$-valued sheaf $G$
on $U_{\mathrm{et}}$ the morphism

$$
\beta_{\bar v,j_Y,G}:(j_Y)_!v_*G\xrightarrow{\sim}\bar v_*(j_X)_!G
$$

of [def-weil-pbc-finite-open-comparison] is an isomorphism. Hence the natural
transformation $\beta:(j_Y)_!v_*\to\bar v_*(j_X)_!$ is a natural isomorphism.
