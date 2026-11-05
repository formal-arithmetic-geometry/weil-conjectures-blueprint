+++
id = "proposition-properties-trace--1"
kind = "proposition"
title = "Additivity"
order = 895002
aliases = ["bp-r270-1"]
lean = ["CategoryTheory.MonoidalCategory.trace_add"]
uses = ["definition-categorical-trace"]
+++
Let $\mathcal C$ be a preadditive braided monoidal category whose tensor
product is additive in each variable, and let $P$ have a right dual.
For endomorphisms $v,w:P\to P$,

$$
\operatorname{tr}(v+w\mid P)
=\operatorname{tr}(v\mid P)+\operatorname{tr}(w\mid P)
\quad\text{in }\End(\mathbf 1).
$$
