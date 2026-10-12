+++
id = "lem-weil-pbc-commshift-nattrans-triangle-morphism"
kind = "lemma"
title = "A shift-compatible natural transformation gives morphisms of the image triangles"
uses = ["def-weil-pbc-triangles-with-shift"]
lean = ["branch", "declarations", "note"]
tags = ["stacks-0144"]
+++
Let $\mathcal D,\mathcal D'$ be additive categories with shift functors $[1 ]$ [def-weil-pbc-triangles-with-shift], let $F_1,F_2:\mathcal D\to\mathcal D'$ be functors with natural isomorphisms $\varphi_X:F_1(X[1 ])\xrightarrow{\sim}F_1(X)[1 ]$ and $\psi_X:F_2(X[1 ])\xrightarrow{\sim}F_2(X)[1 ]$, and let $\tau:F_1\to F_2$ be a natural transformation compatible with the shift: $\psi_X\circ\tau_{X[1 ]}=\tau_X[1 ]\circ\varphi_X$ for every object $X$. For a triangle $T=(X,Y,Z,u,v,w)$ of $\mathcal D$ ($w:Z\to X[1 ]$) let $F_1T=(F_1X,F_1Y,F_1Z,F_1u,F_1v,\varphi_X\circ F_1w)$ and $F_2T=(F_2X,F_2Y,F_2Z,F_2u,F_2v,\psi_X\circ F_2w)$ be its image triangles. Then $(\tau_X,\tau_Y,\tau_Z)$ is a morphism of triangles $F_1T\to F_2T$ [def-weil-pbc-triangles-with-shift], natural in $T$.
