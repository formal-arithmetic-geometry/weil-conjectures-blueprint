+++
id = "proposition-weights-under-usual-operations--17"
kind = "proposition"
title = "Weights after Tate twisting"
order = 1070018
aliases = ["bp-r329-17"]
lean = ["FrobeniusModule.IsPureOfWeight.tateTwist"]
uses = ["definition-weights"]
+++
The general pure- and mixed-sheaf Tate-weight assertions are bypassed
as standalone lemmas by the Lean route. Its weight calculation is the
following statement for Frobenius modules. Let $E$ be a field with an
embedding $\iota:E\hookrightarrow\mathbf C$, let $Q$ be a positive
integer, and let $M$ be a finite-dimensional $E$-vector space with an
automorphism. If $M$ is pure of weight $w$ relative to $Q$, then the
Tate twist $M(r)$, whose Frobenius is multiplied by $Q^{-r}$, is pure
of weight $w-2r$ for every $r\in\mathbf Z$.
