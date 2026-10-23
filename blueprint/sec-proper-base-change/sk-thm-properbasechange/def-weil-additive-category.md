+++
id = "def-weil-additive-category"
kind = "definition"
title = "Additive category"
uses = ["def-weil-preadditive-category"]
lean = ["CategoryTheory.Limits.HasFiniteBiproducts"]
order = 1992
tags = ["mathlib"]
+++
An *additive category* is a preadditive category $\mathcal A$ [def-weil-preadditive-category] that has a zero object and in which every two objects $A,B$ have a direct sum (biproduct) $A\oplus B$, i.e. an object with morphisms $i_A:A\to A\oplus B$, $i_B:B\to A\oplus B$, $p_A:A\oplus B\to A$, $p_B:A\oplus B\to B$ satisfying $p_Ai_A=\mathrm{id}_A$, $p_Bi_B=\mathrm{id}_B$, $p_Ai_B=0$, $p_Bi_A=0$ and $i_Ap_A+i_Bp_B=\mathrm{id}_{A\oplus B}$; equivalently, $\mathcal A$ has all finite biproducts.
