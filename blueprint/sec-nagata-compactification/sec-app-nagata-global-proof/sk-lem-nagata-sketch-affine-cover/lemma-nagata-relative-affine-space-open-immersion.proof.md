+++
kind  = "proof"
of    = "lemma-nagata-relative-affine-space-open-immersion"
+++
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
