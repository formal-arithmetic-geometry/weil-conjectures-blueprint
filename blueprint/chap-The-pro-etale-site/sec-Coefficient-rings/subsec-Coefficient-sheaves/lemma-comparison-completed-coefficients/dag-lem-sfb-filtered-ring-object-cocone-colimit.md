+++
id = "dag-lem-sfb-filtered-ring-object-cocone-colimit"
kind = "dag-lemma"
title = "A ring-object cocone over a filtered diagram is a colimit when its underlying cocone is"
name_showing = false
order = 178503
tags = ["sheaf-dag"]
split_from = "lemma-comparison-completed-coefficients--2"
dag_id = "lem-sfb-filtered-ring-object-cocone-colimit"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["CategoryTheory.Mon.filtered_cocone_isColimit"]
+++
Let $(\mathcal C,\otimes,\mathbf 1)$ be a monoidal category `def-sfb-monoidal-category`, and let $I$ be a small filtered category: $I$ is nonempty, for any two objects $i,j$ there are arrows $i\to k$ and $j\to k$ to some object $k$, and for any two parallel arrows $u,v\colon i\to j$ there is an arrow $w\colon j\to k$ with $wu=wv$. Assume that for every object $Y$ of $\mathcal C$ both functors $Y\otimes-$ and $-\otimes Y$ preserve colimits of $I$-indexed diagrams `def-weil-pbc-category-colimit`.

Let $D\colon I\to\operatorname{Mon}(\mathcal C)$ be a diagram of ring objects of $\mathcal C$ and morphisms of ring objects `sk-def-sfb-ring-object`. Let $A$ be a ring object and let $c_i\colon D(i)\to A$ $(i\in I)$ be morphisms of ring objects with $c_j\circ D(u)=c_i$ for every arrow $u\colon i\to j$. Suppose that $(A,(c_i)_{i\in I})$ is a colimit in $\mathcal C$ of the underlying diagram $i\mapsto D(i)$. Then $(A,(c_i)_{i\in I})$ is a colimit of $D$ in the category of ring objects of $\mathcal C$. Explicitly: if $B$ is a ring object and $b_i\colon D(i)\to B$ are morphisms of ring objects with $b_j\circ D(u)=b_i$ for every $u\colon i\to j$, then the unique morphism $b\colon A\to B$ of $\mathcal C$ with $b\circ c_i=b_i$ for all $i$ is a morphism of ring objects.

If moreover $\mathcal C$ is braided and $A$ and all $D(i)$ are commutative ring objects, then $(A,(c_i)_{i\in I})$ is also a colimit of $D$ in the full subcategory of commutative ring objects.

(SHEAF DAG node `lem-sfb-filtered-ring-object-cocone-colimit`; machine-alignment layer.) Split from [lemma-comparison-completed-coefficients--2]. DAG kind: statement. Placed through `sk-prop-sfb-qlbar-colimit-x` (ancestor-1). DAG status: split. Lean names not on master: `CategoryTheory.CommMon.filtered_cocone_isColimit`. Statement dependencies not drawn: `def-sfb-monoidal-category`, `def-weil-pbc-category-colimit`.
