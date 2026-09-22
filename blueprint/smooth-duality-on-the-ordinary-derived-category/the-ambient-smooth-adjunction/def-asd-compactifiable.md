+++
id = "def-asd-compactifiable"
kind = "definition"
title = "Compactifiable morphism"
order = 5602
lean = ["AlgebraicGeometry.IsCompactifiable"]
uses = ["thm-nagata-compactification"]
+++
A separated finite-type morphism $f:X\to S$ is *compactifiable* if it admits
a factorization $f=rj$ with $j:X\hookrightarrow\overline X$ an open
immersion and $r:\overline X\to S$ proper; such a factorization is a
*compactification* of $f$.

Every morphism occurring in this chapter is compactifiable: for a separated
finite-type morphism of finite-type schemes over a field, a compactification
exists by Nagata's theorem [thm-nagata-compactification].

Unresolved dependencies: def:weil-scheme-morphism-properties, def:weil-compactifications-refinements
