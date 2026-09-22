+++
id = "def-weil-pbc-chow-scheme-theoretic-closure"
kind = "definition"
title = "Scheme-theoretic closure and dense opens"
order = 1084
lean = ["AlgebraicGeometry.Scheme.Hom.schemeTheoreticImage", "AlgebraicGeometry.IsSchemeTheoreticallyDominant"]
+++
For a morphism $u:W\to X$ of schemes, the *scheme-theoretic image* of $u$ is
the largest closed subscheme $X'$ of $X$ through which $u$ factors, i.e. the
closed subscheme defined by $\ker(\mathcal O_X\to u_*\mathcal O_W)$. A
subscheme $W\subseteq X$ is *scheme-theoretically dense* if its
scheme-theoretic image in $X$ is $X$ itself. The scheme-theoretic closure of a
locally closed subscheme is the scheme-theoretic image of its immersion.

Unresolved dependencies: def:weil-pbc-scheme-conventions
