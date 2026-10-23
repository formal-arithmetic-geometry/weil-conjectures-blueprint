+++
id = "lem-weil-pbc-module-restriction-tensor-comparison"
kind = "lemma"
title = "Restriction of a sheaf tensor product to an open immersion"
uses = ["def-pc-scheme", "def-pur-sheaf-tensor-product"]
lean = ["AlgebraicGeometry.Scheme.Modules.exists_restriction_tensor_comparison"]
order = 1894
+++
Let $j:Y\to X$ be an open immersion of schemes [def-pc-scheme], and let $F,G$ be $\mathcal O_X$-modules. Write $F|_Y$ for the restriction of $F$ along $j$ (the $\mathcal O_Y$-module $V\mapsto F(j(V))$) and $\otimes$ for the tensor product of [def-pur-sheaf-tensor-product]. There exists an isomorphism $(F\otimes G)|_Y\cong F|_Y\otimes G|_Y$ whose inverse, on every open $V\subseteq Y$, takes the pure tensor of restricted sections $s,t$ to the section corresponding to the pure tensor of their images in $F(j(V)),G(j(V))$ under the canonical restriction-section isomorphisms.
