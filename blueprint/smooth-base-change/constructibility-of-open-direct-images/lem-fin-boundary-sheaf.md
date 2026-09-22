+++
id = "lem-fin-boundary-sheaf"
kind = "lemma"
title = "Boundary sheaf of an open immersion"
order = 5174
lean = ["AlgebraicGeometry.Etale.isConstructible_boundarySheaf"]
uses = ["sbc-def-coefficient-conventions", "thm-fin-open-degree-zero"]
+++
Let $X$ be of finite type over $k$, let $j:U\hookrightarrow X$ be an open
immersion, let $i:Z=X\setminus U\hookrightarrow X$ be its closed complement,
and let $F$ be a constructible $\Lambda$-sheaf on $U_{\Et}$. Then the
boundary sheaf $i^*j_*F$ is constructible on $Z_{\Et}$.

## Proof

By [thm-fin-open-degree-zero], the sheaf $j_*F$ is constructible. Pull back
its finite locally closed partition and the finite constant étale
trivializations on its parts to $Z$. The inverse image takes a constant
finite module to the same constant module and commutes with restriction. The
pulled-back partition therefore proves constructibility of $i^*j_*F$. No
surjectivity of restriction maps between punctured neighbourhoods is needed.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-constructible-complexes, def:weil-pbc-inverse-image
