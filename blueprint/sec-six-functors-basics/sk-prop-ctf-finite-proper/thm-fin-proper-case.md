+++
id = "thm-fin-proper-case"
kind = "theorem"
title = "The proper case: direct images of proper morphisms"
lean = ["AlgebraicGeometry.Etale.isConstructibleSheaf_homology_rightDerivedLowerStar_of_isProper"]
order = 2380
uses = ["cor-weil-pbc-geometric-fiber-finite", "def-weil-pbc-constructible-complexes", "def-weil-pbc-direct-image", "def-weil-pbc-scheme-conventions", "fin4-lem-fibrewise-cohomological-dimension", "lemma-weil-pbc-geometric-stalk-conservative", "thm-fin-proper-constructibility-complete"]
+++
Let $f:X\to S$ be a proper
morphism with $S$ of finite type over $k$, all
geometric fibres of $f$
of dimension at most $d\in\mathbf Z_{\geq0}$, and let $F$ be a
constructible
$\Lambda$-sheaf on $X_{{\mathrm{et}}}$. Then $R^qf_*F$ of
[def-weil-pbc-direct-image] is constructible on $S_{{\mathrm{et}}}$
for every $q\geq0$, and $R^qf_*F=0$ for $q>2d$.
