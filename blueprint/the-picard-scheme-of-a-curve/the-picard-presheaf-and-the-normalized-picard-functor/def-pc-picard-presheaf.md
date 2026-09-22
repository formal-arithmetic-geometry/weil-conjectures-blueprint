+++
id = "def-pc-picard-presheaf"
kind = "definition"
title = "The Picard presheaf"
order = 4235
lean = ["AlgebraicGeometry.picardPresheaf"]
uses = ["def-pc-base-change", "rem-pc-sc-modules", "lem-pc-pic-presheaf-functorial"]
+++
Let $f:X\to S$ be a morphism of schemes. The *Picard presheaf* is
$$
(\mathit{Sch}/S)^{\mathrm{op}}\longrightarrow\textit{Sets},\qquad
T\longmapsto\operatorname{Pic}(X_T),
$$
with $\operatorname{Pic}$ the Picard group of the curve-calculation chapter
(in the generality of [rem-pc-sc-modules]) and $X_T$ of
[def-pc-base-change]. That this is indeed a functor — the pullback maps
compose correctly — is [lem-pc-pic-presheaf-functorial].

*Import note.* The source's sentence breaks off at a semicolon and the
definition then closes; it is completed with the cross-reference the
pointer remark [rem-ptr-pc-picard-presheaf-6] supplies, and nothing else is
added.

Unresolved dependencies: def:sc-picard-group
