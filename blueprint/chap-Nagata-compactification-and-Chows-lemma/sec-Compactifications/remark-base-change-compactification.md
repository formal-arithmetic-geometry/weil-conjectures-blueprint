+++
id = "remark-base-change-compactification"
kind = "remark"
title = "Base change of a compactification"
order = 1413
lean = ["AlgebraicGeometry.Compactification.baseChange", "AlgebraicGeometry.Compactification.isSchemeTheoreticallyDominant_i_baseChange", "AlgebraicGeometry.Scheme.Hom.ker_pullback_snd"]
uses = ["lemma-passing-schematic-closure"]
+++
For every $S'\to S$, the base change of a compactification is an open
immersion followed by a proper morphism, which suffices to define
the direct image with compact support of $X\times_SS'\to S'$. When the
base-changed ambient scheme is Noetherian, as for schemes of finite
type over $k$, Lemma [lemma-passing-schematic-closure] shows that
this direct image agrees with the one defined by the schematic closure.

Schematic density
and schematic closure commute with flat base change, but density can
be lost under an arbitrary base change. In that case the schematic
closure of $X\times_SS'$ in $\overline X\times_SS'$ is a dense
compactification, and a base-changed common refinement can be replaced
by its closure in the same way. The comparisons in the main text are
made on a further common refinement, where they are canonical by
uniqueness.
