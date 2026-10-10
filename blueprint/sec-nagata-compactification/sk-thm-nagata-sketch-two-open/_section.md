+++
id = "sk-thm-nagata-sketch-two-open"
kind = "theorem"
title = "Two-open compactification"
order = 284
uses = ["sk-lem-nagata-sketch-common", "sk-lem-nagata-sketch-dense-valuative", "sk-prop-nagata-sketch-key-disjointness"]
lean = ["AlgebraicGeometry.HasCompactification.of_two_open_cover"]
tags = ["sketch"]
+++
Let $S$ be a Noetherian scheme and let $U\to S$ be a separated
morphism which is locally of finite type and quasi-compact. Let
$U_1,U_2\subseteq U$ be open subschemes with $U_1\cup U_2=U$ and
$U_1\cap U_2$ dense in $U$, such that both composites $U_i\hookrightarrow U\to S$
are compactifiable.
Then $U\to S$ is compactifiable.
