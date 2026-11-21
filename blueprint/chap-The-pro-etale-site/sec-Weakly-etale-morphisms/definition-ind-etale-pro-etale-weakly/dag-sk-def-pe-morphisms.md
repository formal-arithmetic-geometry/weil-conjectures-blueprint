+++
id = "dag-sk-def-pe-morphisms"
kind = "dag-definition"
title = "Ind-étale, pro-étale and weakly étale morphisms"
name_showing = false
order = 27502
tags = ["sheaf-dag"]
split_from = "definition-ind-etale-pro-etale-weakly--1"
dag_id = "sk-def-pe-morphisms"
dag_kind = "definition"
dag_status = "split"
serial = false
dag_lean = ["Algebra.IndEtale", "RingHom.IndEtale", "AlgebraicGeometry.proAffineEtale_Spec_iff", "RingHom.WeaklyEtale", "AlgebraicGeometry.proAffineEtale"]
+++
Let $R$ and $B$ be commutative rings. A ring map $R\to B$ is *ind-étale* if, as an $R$-algebra, $B$ is a filtered colimit of finitely presented étale $R$-algebras, with the convention of [dag-def-weil-pbc-ind-etale-algebra]. All indexing categories are small; filtered includes nonemptiness, as in `def-weil-pbc-category-colimit`.

For $X=\operatorname{Spec}R$ `def-weil-affine-spectrum`, the morphism $\operatorname{Spec}B\to X$ associated to an ind-étale $R$-algebra $B$ is called *affine pro-étale*. A presentation $B=\varinjlim_\alpha B_\alpha$ gives its affine inverse-limit presentation $\operatorname{Spec}B=\varprojlim_\alpha\operatorname{Spec}B_\alpha$, with the canonical maps, as in [dag-def-weil-pbc-ind-etale-algebra].

For an arbitrary scheme $X$, a *pro-étale affine over $X$* is an $X$-scheme $u:U\to X$ admitting a small nonempty cofiltered presentation $U=\varprojlim_{i\in I}U_i$ over $X$, where every $U_i$ is an affine scheme and $U_i\to X$ is étale `def-weil-etale-morphism`. Here cofiltered means that $I^{\mathrm{op}}$ is filtered `def-weil-pbc-category-colimit`. The transition maps are $X$-morphisms. The limit over $X$ means compatible $X$-morphisms $p_i:U\to U_i$ such that every compatible family of $X$-morphisms $T\to U_i$ factors through exactly one $X$-morphism $T\to U$. The word affine refers to the schemes $U_i$ themselves, not merely to the morphisms $U_i\to X$.

A scheme morphism $u:U\to X$ is *weakly étale* if $u$ and its diagonal $\Delta_u:U\to U\times_XU$ are flat `def-weil-weakly-etale-morphism`. A ring map $R\to B$ is weakly étale when both $R\to B$ and the multiplication map $B\otimes_RB\to B$, $b\otimes b'\mapsto bb'$, are flat, as in [dag-def-weil-pbc-ind-etale-algebra].

(SHEAF DAG node `sk-def-pe-morphisms`; machine-alignment layer.) Split from [definition-ind-etale-pro-etale-weakly--1]. DAG kind: definition. DAG status: split. Lean names not on master: `AlgebraicGeometry.WeaklyEtale`, `Algebra.WeaklyEtale`. Statement dependencies not drawn: `def-weil-affine-spectrum`, `def-weil-etale-morphism`, `def-weil-pbc-category-colimit`, `def-weil-weakly-etale-morphism`.
