+++
id = "det-pe-wcb-projective"
kind = "lemma"
title = "Representables of w-contractible affines are projective"
lean = ["AlgebraicGeometry.Scheme.ProEt.isWeaklyContractible_of_iso"]
order = 963
uses = ["det-pe-wcb-clopen-partition", "det-pe-topos-functoriality-site"]
+++
Let $U=\operatorname{Spec}D$ with $D$ w-contractible be an object of $X_{\mathrm{proét}}$.

1. Every epimorphism of sheaves of sets $F\to h_U$ has a section.
2. $h_U$ is projective in $\Sh(X_{\mathrm{proét}})$: for every epimorphism $F\to G$, the map
   $F(U)\to G(U)$ is surjective.
