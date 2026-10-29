+++
id = "lem-fet-finite-limits"
kind = "theorem"
title = "Finite limits, coproducts and quotients of finite etale covers"
order = 1466
lean = ["AlgebraicGeometry.Scheme.FiniteEtale.toFiniteEtaleOver", "AlgebraicGeometry.Scheme.FiniteEtale.isInitialEmpty", "AlgebraicGeometry.Scheme.FiniteEtale.isColimitCoprodCofan", "AlgebraicGeometry.Scheme.FiniteEtale.hasColimitsOfShape_singleObj", "AlgebraicGeometry.Scheme.FiniteEtale.monoInducesIsoOnDirectSummand"]
uses = ["def-galois-categories", "def-weil-pbc-scheme-conventions"]
+++
Let $Y$ be a scheme. Then $\mathrm{F\acute Et}(Y)$ has finite limits,
computed as in $Y$-schemes; it has finite coproducts, the initial object
being the empty scheme and the coproduct of $P$ and $Q$ the disjoint
union $P\amalg Q$; it has quotients $P/G$ by finite groups $G$ acting on
$P$ over $Y$; and every monomorphism in $\mathrm{F\acute Et}(Y)$ is the
inclusion of a direct summand, i.e. of an open and closed subscheme.
