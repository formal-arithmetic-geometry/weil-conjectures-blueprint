+++
id = "lem-fin-extension-by-zero"
kind = "lemma"
title = "Extension by zero preserves constructibility"
order = 1482
lean = ["AlgebraicGeometry.Scheme.IsConstructibleSheaf.openImmersionLowerShriek_of_quasiCompact", "AlgebraicGeometry.Scheme.IsConstructibleSheaf.openImmersionLowerShriek"]
uses = ["def-constructible-constructible", "def-weil-pbc-extension-by-zero", "def-weil-pbc-scheme-conventions"]
+++
Let $\Lambda$ be a commutative ring, let $X$ be a scheme, let $j:U\hookrightarrow X$ be a quasi-compact open immersion, and let $F$ be a constructible sheaf of $\Lambda$-modules on $U_{\mathrm{et}}$ [def-constructible-constructible]. Then $j_!F$ of [def-weil-pbc-extension-by-zero] is constructible on $X_{\mathrm{et}}$. (The quasi-compactness of $j$ is automatic when $X$ is locally Noetherian.)
