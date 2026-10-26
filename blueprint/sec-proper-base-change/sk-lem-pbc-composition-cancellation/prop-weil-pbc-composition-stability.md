+++
id = "prop-weil-pbc-composition-stability"
kind = "theorem"
title = "Composition stability"
lean = ["AlgebraicGeometry.Etale.HasTorsionBaseChange.comp", "AlgebraicGeometry.Etale.HasInjectiveAcyclicity.comp"]
order = 1928
uses = ["def-weil-pbc-scheme-conventions", "lemma-weil-pbc-cancellation"]
tags = ["latex:proposition"]
+++
Let $\Lambda$ be a commutative ring which is torsion as an abelian group, and
use the notions of torsion base change and injective acyclicity over $\Lambda$
of [lemma-weil-pbc-cancellation]. Let $X\xrightarrow{f}Y\xrightarrow{h}Z$ be
morphisms of schemes.

1. If $f$ and $h$ have torsion base change over $\Lambda$, then so does $hf$.
2. If $f$ and $h$ are proper and have injective acyclicity over $\Lambda$, then
   so does $hf$.
