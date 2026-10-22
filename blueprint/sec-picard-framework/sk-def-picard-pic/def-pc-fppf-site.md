+++
id = "def-pc-fppf-site"
kind = "definition"
title = "The big fppf site"
lean = ["AlgebraicGeometry.Scheme.fppfPrecoverage", "AlgebraicGeometry.Scheme.fppfTopology", "CategoryTheory.GrothendieckTopology.over"]
order = 778
uses = ["def-pc-morphism-conventions", "def-pc-scheme"]
+++
Let $S$ be a scheme and $\mathit{Sch}_{fppf}$ a big fppf site containing
$S$. The
*big fppf site of $S$* is $(\mathit{Sch}/S)_{fppf}$, whose coverings
are the families $\{T_i\to T\}_{i\in I}$ of
flat morphisms locally of finite
presentation which are jointly surjective, i.e.
$T=\bigcup_i\operatorname{im}(T_i\to T)$; an *fppf covering* is such a family.
