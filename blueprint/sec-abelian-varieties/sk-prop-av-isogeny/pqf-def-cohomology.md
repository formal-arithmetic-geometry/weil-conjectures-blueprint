+++
id = "pqf-def-cohomology"
kind = "definition"
title = "Sheaf cohomology and higher direct images"
lean = ["AlgebraicGeometry.Scheme.Modules.globalSectionsFunctor", "AlgebraicGeometry.Scheme.Modules.higherDirectImage", "CategoryTheory.ShortComplex.ShortExact.exists_rightDerived_δ_exact"]
order = 508
+++
Let $X$ be a scheme. The cohomology functors $\mathrm H^p(X,-)$ are
the right derived functors of the global sections functor $\Gamma(X,-)$
on $\mathcal O_X$-modules; a short exact sequence of $\mathcal O_X$-modules gives a long exact cohomology sequence. For a morphism
$f:X\to S$, the higher direct images $R^pf_*\mathcal F$ are the right
derived functors of $f_*$.
