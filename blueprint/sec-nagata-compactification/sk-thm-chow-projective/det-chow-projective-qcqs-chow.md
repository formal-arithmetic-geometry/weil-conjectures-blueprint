+++
id = "det-chow-projective-qcqs-chow"
kind = "theorem"
title = "Chow's lemma over a qcqs base"
lean = ["AlgebraicGeometry.exists_chow_finite_type"]
order = 440
uses = ["thm-chow-lemma", "prop-nagata-finite-type-closed-in-fp", "prop-nagata-noetherian-inverse-system", "lemma-nagata-separated-eventually"]
+++
Let $S$ be quasi-compact and quasi-separated and let $f:X\to S$ be separated
and of finite type. Then there are a finite set $N$, a scheme $\widetilde X$,
a proper surjective morphism $\pi:\widetilde X\to X$ and an immersion
$i_S:\widetilde X\to\mathbf P^N_S$ such that $q_S\circ i_S=f\circ\pi$, where
$q_S:\mathbf P^N_S\to S$ is the projection.
