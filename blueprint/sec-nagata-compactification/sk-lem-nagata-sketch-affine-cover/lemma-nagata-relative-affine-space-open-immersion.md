+++
id = "lemma-nagata-relative-affine-space-open-immersion"
kind = "lemma"
title = "The standard affine chart in relative projective space"
order = 310
lean = ["AlgebraicGeometry.AffineSpace.isOpenImmersion_toRelativeProjectiveSpace"]
uses = ["def-nagata-affine-proj", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-projective-space-base-change", "def-nagata-relative-affine-space", "def-nagata-relative-projective-space", "lemma-nagata-relative-affine-space-charts", "lemma-nagata-relative-proj-exists"]
+++
For every index set $n$ and every scheme $S$, the morphism
$\mathbb A^n_S\to\mathbf P(\{0\}\sqcup n;S)$ over $S$ induced by
$T_i\mapsto T_i/T_0$ (the standard chart at the extra homogeneous
coordinate $T_0$) is an open immersion.

## Proof

First take $S=\operatorname{Spec}\mathbf Z$. The standard open
$D_+(T_0)\subseteq\mathbf P^{\{0\}\sqcup n}_{\mathbf Z}$ is
$\operatorname{Spec}$ of the degree-zero homogeneous localization
$\mathbf Z[T_0,T_i:i\in n]_{(T_0),0}$ ([def-nagata-affine-proj]), and
dehomogenization $T_i/T_0\mapsto T_i$ identifies this ring with the
polynomial ring $\mathbf Z[T_i:i\in n]$. Hence the morphism
$\operatorname{Spec}\mathbf Z[T_i:i\in n]\to\mathbf P^{\{0\}\sqcup n}_{\mathbf Z}$
induced by $T_i\mapsto T_i/T_0$ is an open immersion onto $D_+(T_0)$.

For general $S$, both $\mathbb A^n_S=S\times\operatorname{Spec}\mathbf Z[T_i:i\in n]$
([def-nagata-relative-affine-space]) and
$\mathbf P(\{0\}\sqcup n;S)=S\times\mathbf P^{\{0\}\sqcup n}_{\mathbf Z}$
([def-nagata-projective-space-base-change]) are base changes along
$S\to\operatorname{Spec}\mathbf Z$, and the morphism of the statement is
the base change of the integral chart. Open immersions are stable under
base change, so it is an open immersion; it is a morphism over $S$ because
both sides map to $S$ by the first projection.
