+++
id = "lem-pd-morphisms-descend"
kind = "lemma"
title = "Morphisms, and hence the group law, descend"
lean = ["CategoryTheory.Over.DescentDatum.existsUnique_hom_of_isPullback"]
order = 871
uses = ["def-pc-base-change", "def-pd-descent-datum"]
+++
Let $X\to Y$ be a faithfully flat (flat and surjective) and quasi-compact
morphism of schemes and let $V\to X$, $W\to X$ be schemes
with descent data over $X/Y$ which are
effective, with descended schemes $V_0,W_0$ over $Y$. Then every morphism
$\psi:V\to W$ over $X$ which is compatible with the two descent data descends
to a unique morphism $\psi_0:V_0\to W_0$ over $Y$.
