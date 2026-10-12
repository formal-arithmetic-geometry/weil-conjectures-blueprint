+++
id = "lem-weil-pbc-left-adjoint-preserves-colimits"
kind = "lemma"
title = "Left adjoints preserve colimits"
order = 1057
uses = ["def-weil-pbc-category-colimit"]
lean = ["CategoryTheory.Adjunction.leftAdjoint_preservesColimits"]
tags = ["mathlib", "stacks-0038"]
+++
Let $L:\mathcal C\to\mathcal D$ and $R:\mathcal D\to\mathcal C$ be functors with an adjunction $L\dashv R$, i.e. bijections $\operatorname{Hom}_{\mathcal D}(LX,Y)\cong\operatorname{Hom}_{\mathcal C}(X,RY)$ natural in $X\in\mathcal C$ and $Y\in\mathcal D$. Let $I$ be a small category and $M:I\to\mathcal C$ a diagram having a colimit $(\varinjlim_IM,(\iota_i)_i)$ in $\mathcal C$ [def-weil-pbc-category-colimit]. Then $(L(\varinjlim_IM),(L\iota_i)_i)$ is a colimit of $L\circ M$ in $\mathcal D$. In particular, when $L\circ M$ has a chosen colimit, the canonical morphism $\varinjlim_I(L\circ M)\to L(\varinjlim_IM)$ induced by the $L\iota_i$ is an isomorphism.
