+++
id = "lem-wf-zero-dimensional-matrix-group-finite"
kind = "lemma"
title = "Zero-dimensional closed matrix groups are finite"
order = 4032
uses = ["def-wf-algebraic-components", "lem-wf-matrix-group-components"]
+++
Let $G\subseteq\operatorname{GL}(V)$ be a closed reduced matrix group
over $k=\overline{\mathbf Q}_\ell$. If $G^\circ=1$, then
$G(k)$ is finite and $G\to\operatorname{Spec}k$ is a finite
morphism.

## Proof

By [lem-wf-matrix-group-components], the components are the
pairwise disjoint cosets $gG^\circ$. If $G^\circ=1$, every
component is one point, and there are only finitely many components.
Thus $G$ is a zero-dimensional finite-type affine $k$-scheme.
Its coordinate ring is a finitely generated $k$-algebra of Krull
dimension zero, hence is Artinian; it is therefore finite-dimensional
over $k$ (apply Zariski's lemma to its finitely many maximal
quotients). This is exactly the assertion that $G\to\operatorname{Spec} k$ is finite, and in particular $G(k)$ is finite.
