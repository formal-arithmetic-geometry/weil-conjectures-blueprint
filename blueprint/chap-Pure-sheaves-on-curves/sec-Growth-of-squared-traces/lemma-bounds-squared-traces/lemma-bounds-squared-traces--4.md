+++
id = "lemma-bounds-squared-traces--4"
kind = "lemma"
title = "Bounds for squared traces (4)"
name_showing = false
order = 1202005
aliases = ["bp-r371-4"]
lean = ["AlgebraicGeometry.WeilSheaf.l2Weight_le_of_traceEnergy_le"]
uses = ["definition-growth-squared-traces"]
+++
The conclusion for arbitrary complexes with finite support is bypassed
by Lean; the general estimate used for Weil sheaves is the following.

Let $F$ be a Weil sheaf on a $k_0$-scheme $X_0$, and let $C,B\in\mathbf R$.
If

$$
S_n(F)\le Cq^{nB}\qquad(n\ge1),
$$

then $\nu(F)\le B-1$. In particular, a bound $S_n(F)\le Cq^{na}$
gives $\nu(F)\le a-1$.
