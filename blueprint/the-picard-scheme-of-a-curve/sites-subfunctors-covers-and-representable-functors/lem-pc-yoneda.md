+++
id = "lem-pc-yoneda"
kind = "lemma"
title = "Yoneda"
order = 4233
lean = ["CategoryTheory.yoneda", "CategoryTheory.Functor.IsRepresentedBy", "CategoryTheory.Representable"]
+++
Let $S$ be a scheme. For any functor
$F:(\mathit{Sch}/S)^{\mathrm{op}}\to\textit{Sets}$ and any scheme $X/S$,
the map
$$
\operatorname{Hom}_{\textit{fun}}(h_X,F)\;\longrightarrow\;F(X),\qquad
\tau\;\longmapsto\;\tau_X(\mathrm{id}_X)
$$
is a bijection, natural in both arguments (Categories, Lemma 4.3.5, [Tag
001P](https://stacks.math.columbia.edu/tag/001P)).

*The source marks this as already available in Mathlib.*

## Proof

Omitted; the source records this as a Mathlib item.
