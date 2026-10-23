+++
id = "lem-weil-pbc-coimage-mono"
kind = "lemma"
title = "In an abelian category the map from the coimage A/Ker f to the target of f is a monomorphism"
uses = ["def-sp-abelian"]
lean = ["CategoryTheory.Abelian.factorThruCoimage"]
order = 1999
tags = ["mathlib", "stacks-0109"]
+++
Let $\mathcal A$ be an abelian category [def-sp-abelian] and $f:A\to B$ a morphism of $\mathcal A$, with kernel $\ker f\hookrightarrow A$ and coimage $\mathrm{Coim}(f)=A/\ker f=\mathrm{coker}(\ker f\to A)$, $\pi:A\to A/\ker f$ the projection. Since $f$ vanishes on $\ker f$, $f=\bar f\circ\pi$ for a unique $\bar f:A/\ker f\to B$; then $\bar f$ is a monomorphism.
