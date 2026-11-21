+++
id = "dag-lem-sfb-qlbar-point-abelian-colimit"
kind = "dag-lemma"
title = "The finite-subextension cocone is a colimit in condensed abelian groups"
name_showing = false
order = 178504
tags = ["sheaf-dag"]
split_from = "lemma-comparison-completed-coefficients--2"
dag_id = "lem-sfb-qlbar-point-abelian-colimit"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["Profinite.isColimitPadicAlgClRingObjCocone", "Profinite.padicSubfieldRingObjFunctor", "Profinite.padicAlgClRingObjCocone"]
+++
Fix a prime $\ell$ and an algebraic closure $\Qlb$ of $\mathbf Q_\ell$. Let $I$ be the poset of finite intermediate fields $\mathbf Q_\ell\subseteq E\subseteq\Qlb$, ordered by inclusion, as in `sk-def-sfb-qlbar-condensed`. Work in a universe containing $\Qlb$, so that $I$ is a small filtered category. Give $E$ the topology restricted from $\Qlb$ and write $\underline E(S)=C(S,E)$ for its condensed ring on profinite sets with the coherent topology `sk-def-sfb-condensed-ring`. Let $A=\underline{\Qlb}$ be the finite-subextension-valued condensed ring of `sk-def-sfb-qlbar-condensed`; thus
$$
A(S)=\{a\in C(S,\Qlb)\mid a(S)\subseteq E\text{ for some }E\in I\}.
$$
Consider the diagram $D:I\to\Sh(*_{\mathrm{pro\acute et}},\Ab)$ with $D(E)$ the underlying abelian sheaf of $\underline E$ and transition $D(E\subseteq F)=\iota_{E,F}$ of `def-sfb-qlbar-subextension-map`. Its cocone with vertex the underlying abelian sheaf of $A$ and legs $j_E:\underline E\to A$ of `def-sfb-qlbar-subextension-to-qlbar` is a colimit in $\Sh(*_{\mathrm{pro\acute et}},\Ab)$ `def-weil-pbc-category-colimit`. Explicitly, for any condensed abelian group $G$ and additive sheaf morphisms $a_E:\underline E\to G$ satisfying $a_F\circ\iota_{E,F}=a_E$ whenever $E\subseteq F$, there exists a unique additive sheaf morphism $a:A\to G$ satisfying $a\circ j_E=a_E$ for every $E\in I$.

(SHEAF DAG node `lem-sfb-qlbar-point-abelian-colimit`; machine-alignment layer.) Split from [lemma-comparison-completed-coefficients--2]. DAG kind: statement. Placed through `sk-prop-sfb-qlbar-colimit-x` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-pbc-category-colimit`.
