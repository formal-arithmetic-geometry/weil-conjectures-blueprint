+++
id = "proposition-topos-functoriality--2"
kind = "proposition"
title = "The topos and its functoriality (2)"
name_showing = false
order = 39003
aliases = ["bp-r006-2"]
lean = ["AlgebraicGeometry.ProEtale.lowerStar", "AlgebraicGeometry.ProEtale.preservesHomology_upperStar", "AlgebraicGeometry.ProEtale.setPullback", "AlgebraicGeometry.ProEtale.setPullbackAdjunction", "AlgebraicGeometry.ProEtale.upperStar"]
+++
Let $f:X\to Y$ be a morphism of schemes in a universe $u$, and take
sheaves of sets in universe $u+1$. Base change
$b_f:V\mapsto V\times_YX$ preserves finite limits and covering families
on the small pro-étale sites. It induces a geometric morphism

$$
f_{\mathrm{pro}\acute{e}t}:\Sh(X_{\mathrm{pro}\acute{e}t})\longrightarrow\Sh(Y_{\mathrm{pro}\acute{e}t}),
\qquad f^{-1}\dashv f_*.
$$

Here $f_*$ is restriction along $b_f$, so that
$(f_*\mathcal F)(V)=\mathcal F(V\times_YX)$, and $f^{-1}$ is left Kan extension along
$b_f^{\mathrm{op}}$ followed by sheafification. The functor
$f^{-1}:\Sh(Y_{\mathrm{pro}\acute{e}t})\to\Sh(X_{\mathrm{pro}\acute{e}t})$
preserves finite limits and all colimits. The same construction for
abelian sheaves in universe $u+1$ agrees with $f^{-1}$ on underlying
sheaves of sets and is exact.
