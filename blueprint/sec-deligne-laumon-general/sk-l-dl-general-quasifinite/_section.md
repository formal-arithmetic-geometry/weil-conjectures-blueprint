+++
id = "sk-l-dl-general-quasifinite"
kind = "lemma"
title = "Finite and quasi-finite direct images"
order = 4053
lean = ["AlgebraicGeometry.isZero_higherLowerShriek_of_quasiFinite", "AlgebraicGeometry.WeilSheaf.IsMixedOfWeightsAtMost.higherLowerShriek_zero_of_quasiFinite", "AlgebraicGeometry.WeilSheaf.HasWeightsAtMost.higherLowerShriek_zero_of_quasiFinite"]
uses = ["sk-d-real-weights", "sk-lem-pbc-finite", "sk-thm-sf-comp-composition"]
tags = ["sketch"]
+++
Let $g:Z_0\to Y_0$ be separated and quasi-finite. Then $Rg_!$ is
exact on sheaves and carries mixed sheaves of weights at most $w$ to
mixed sheaves of weights at most $w$. It also carries
$D_{\leq w}(Z_0)$ into $D_{\leq w}(Y_0)$.
For a finite map, direct image carries a pure sheaf of weight $w$
to a pure sheaf of weight $w$.

*Complement.* Here $g$ is a separated, quasi-finite morphism of finite
type of $k_0$-schemes, with $Y_0$ quasi-separated of finite type over
$k_0$; thus $R^ig_!F=0$ for every Weil sheaf $F$ and every $i>0$. If
every local Frobenius eigenvalue of $F$ has weight at most $w$ (a
punctual bound at most $w$ in the sense of [sk-d-real-weights]), then
the same holds for $g_!F=R^0g_!F$.
