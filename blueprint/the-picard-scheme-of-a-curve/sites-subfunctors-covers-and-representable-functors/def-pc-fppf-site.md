+++
id = "def-pc-fppf-site"
kind = "definition"
title = "The big fppf site"
order = 4227
lean = ["AlgebraicGeometry.Scheme.fppfSite"]
uses = ["def-pc-scheme", "def-pc-morphism-conventions"]
+++
Let $S$ be a scheme and $\mathit{Sch}_{fppf}$ a big fppf site containing
$S$ (Topologies, Definition 34.7.8, [Tag
021S](https://stacks.math.columbia.edu/tag/021S)). The *big fppf site of
$S$* is $(\mathit{Sch}/S)_{fppf}$, whose coverings are the families
$\{T_i\to T\}_{i\in I}$ of flat morphisms [def-pc-morphism-conventions]
locally of finite presentation; an *fppf covering* is such a family.

That Zariski coverings are fppf coverings is
[lem-pc-zariski-coverings-are-fppf], as [rem-ptr-pc-fppf-site-5] records.
