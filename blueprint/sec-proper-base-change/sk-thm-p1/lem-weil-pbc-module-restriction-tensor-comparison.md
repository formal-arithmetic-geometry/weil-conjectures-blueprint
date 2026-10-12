+++
id = "lem-weil-pbc-module-restriction-tensor-comparison"
kind = "lemma"
title = "Restriction of a sheaf tensor product to an open immersion"
uses = ["def-pc-scheme", "def-pur-sheaf-tensor-product"]
lean = ["AlgebraicGeometry.Scheme.Modules.exists_restriction_tensor_comparison"]
source = "literature/stacks-project/modules.tex, Modules, Lemma 17.16.4 (Tag 01CD), pullback along an open immersion"
+++
Let $j:Y\to X$ be an open immersion of schemes [def-pc-scheme], and let $F,G$ be $\mathcal O_X$-modules `SheafOfModules` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Category/ModuleCat/Sheaf.lean)). Write restriction along $j$ as in `AlgebraicGeometry.Scheme.Modules.restrictFunctor, AlgebraicGeometry.Scheme.Modules.restrictAdjunction, AlgebraicGeometry.Scheme.Modules.instIsLeftAdjointRestrictFunctor, AlgebraicGeometry.Scheme.Modules.isQuasicoherent_restrictFunctor` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Modules/Sheaf.lean)) and tensor product as in [def-pur-sheaf-tensor-product]. There exists an isomorphism $(F\otimes G)|_Y\cong F|_Y\otimes G|_Y$ whose inverse, on every open $V\subseteq Y$, takes the pure tensor of restricted sections $s,t$ to the section corresponding to the pure tensor of their images in $F(j(V)),G(j(V))$ under the canonical restriction-section isomorphisms.
