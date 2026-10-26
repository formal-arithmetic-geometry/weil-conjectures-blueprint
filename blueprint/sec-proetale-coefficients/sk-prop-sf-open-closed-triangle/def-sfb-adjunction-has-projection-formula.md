+++
id = "def-sfb-adjunction-has-projection-formula"
kind = "definition"
title = "Adjunctions satisfying the projection formula"
order = 1070
lean = ["CategoryTheory.Adjunction.projectionFormulaMap", "CategoryTheory.Adjunction.HasProjectionFormula"]
+++
Let $P\dashv S$ be an adjunction, with $P\colon\mathcal C\to\mathcal D$ and
$S\colon\mathcal D\to\mathcal C$, unit $u$, and $S$ strong monoidal with structure maps
$\mu^S$. The *projection formula map*
$$
P(SL\otimes M)\to L\otimes PM\qquad(L\in\mathcal D,\ M\in\mathcal C)
$$
is the adjoint of
$SL\otimes M\xrightarrow{SL\otimes u_M}SL\otimes SPM\xrightarrow{\mu^S_{L,PM}}S(L\otimes PM)$.
The adjunction *satisfies the projection formula* if all projection formula maps are
isomorphisms.
