+++
id = "lem-weil-pbc-p1-field-dimension-one"
kind = "lemma"
title = "The projective line over a field has dimension at most one"
uses = ["def-nagata-projective-space-base-change"]
lean = ["AlgebraicGeometry.topologicalKrullDim_projectiveLine_le_one"]
source = "literature/stacks-project/topology.tex, Lemma Tag 0B7I (topology-lemma-dimension-supremum-local-dimensions), applied to the two standard affine opens $D_+(T_0),D_+(T_1)\\cong\\mathbf A^1_k=\\operatorname{Spec}k[x]$; with algebra.tex Lemma Tag 00OP (algebra-lemma-dim-affine-space), $\\dim k[x]=1$"
+++
Let $k$ be a field and let $\mathbf P^1_k=\mathbf P(\{0,1\};\operatorname{Spec}k)$ be the projective line over $k$ in the sense of [def-nagata-projective-space-base-change]. Then the underlying topological space of $\mathbf P^1_k$ has Krull dimension at most one: every chain $Z_0\subsetneq Z_1\subsetneq\dots\subsetneq Z_n$ of irreducible closed subsets of $\mathbf P^1_k$ has $n\le1$.
