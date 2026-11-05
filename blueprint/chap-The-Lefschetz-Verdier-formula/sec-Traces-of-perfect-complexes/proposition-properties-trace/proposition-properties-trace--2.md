+++
id = "proposition-properties-trace--2"
kind = "proposition"
title = "Conjugacy invariance"
order = 895003
aliases = ["bp-r270-2"]
lean = ["CategoryTheory.MonoidalCategory.trace_eq_of_iso"]
uses = ["definition-categorical-trace"]
+++
Let $P,P'$ be objects with right duals in a braided monoidal category,
and let $e:P\xrightarrow{\sim}P'$ be an isomorphism. If endomorphisms
$v:P\to P$ and $v':P'\to P'$ satisfy $e\circ v=v'\circ e$, then

$$
\operatorname{tr}(v\mid P)=\operatorname{tr}(v'\mid P').
$$
