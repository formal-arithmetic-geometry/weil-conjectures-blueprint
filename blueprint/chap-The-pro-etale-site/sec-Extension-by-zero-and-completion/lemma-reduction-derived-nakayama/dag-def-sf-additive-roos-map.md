+++
id = "dag-def-sf-additive-roos-map"
kind = "dag-definition"
title = "Canonical additive-functor map of strict Roos complexes"
name_showing = false
order = 210505
tags = ["sheaf-dag"]
split_from = "lemma-reduction-derived-nakayama--2"
dag_id = "def-sf-additive-roos-map"
dag_kind = "definition"
dag_status = "split"
serial = false
dag_lean = ["WeilConjectures.scalarRoosBoundary", "WeilConjectures.scalarRoosMap_existsUnique", "WeilConjectures.scalarRoosMap"]
uses = ["dag-def-sf-strict-roos-functor"]
+++
Let $\mathcal A,\mathcal B$ be abelian categories `def-sp-abelian` with countable products `def-weil-category-product`, let $F:\mathcal A\to\mathcal B$ be additive, and let $C:\mathbf N^{op}\to\operatorname{CochainComplex}(\mathcal A,\mathbf Z)$ be a strict tower `def-weil-inverse-system`. Use the strict Roos construction [dag-def-sf-strict-roos-functor]. Define $b_C=1-s_C$ `def-weil-tower-transition-endomorphism` and the map $\kappa_{F,C}:F(\operatorname{Roos}(C))\to\operatorname{Roos}(F C)$ as the unique chain map with both prescribed product coordinates: its unshifted coordinate followed by the $n$th projection is $F(\operatorname{fst}\,;\operatorname{pr}_n)$; in degree $i$, its shifted coordinate followed by the $n$th degree $i-1$ projection is $F(\operatorname{snd}^i\,;\operatorname{pr}_n^{i-1})$. Here $F$ is applied termwise to complexes. Thus both coordinates use the canonical product comparison, without an arbitrary completion of a triangle. No exactness or product-preservation assumption is part of this definition.

(SHEAF DAG node `def-sf-additive-roos-map`; machine-alignment layer.) Split from [lemma-reduction-derived-nakayama--2]. DAG kind: definition. Placed through `det-pe-derived-nakayama-first-reduction` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-sp-abelian`, `def-weil-category-product`, `def-weil-inverse-system`, `def-weil-pbc-additive-functor`, `def-weil-tower-transition-endomorphism`.
