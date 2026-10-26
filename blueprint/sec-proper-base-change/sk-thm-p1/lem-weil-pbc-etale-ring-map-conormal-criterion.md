+++
id = "lem-weil-pbc-etale-ring-map-conormal-criterion"
kind = "lemma"
title = "Etale ring maps: the conormal map of a finite presentation is an isomorphism"
lean = ["Algebra.etale_ring_map_conormal_criterion"]
order = 1722
+++
Let $R\to S$ be a homomorphism of commutative rings, $n\ge0$, $P=R[x_1,\dots,x_n]$ the polynomial ring, and $\alpha:P\to S$ a surjective homomorphism of $R$-algebras whose kernel $J$ is a finitely generated ideal of $P$. The quotient $J/J^2$ is an $S=P/J$-module, and let $\bigoplus_{k=1}^nS\,\mathrm dx_k$ be the free $S$-module on symbols $\mathrm dx_1,\dots,\mathrm dx_n$. The map $\mathrm d:J/J^2\to\bigoplus_{k=1}^nS\,\mathrm dx_k$, $\mathrm d(g\bmod J^2)=\sum_{k=1}^n\alpha(\partial g/\partial x_k)\,\mathrm dx_k$ ($\partial/\partial x_k$ the formal partial derivatives of $P$ over $R$), is well defined and $S$-linear. Then the morphism $\operatorname{Spec}S\to\operatorname{Spec}R$ induced by $R\to S$ is etale if and only if $\mathrm d$ is bijective.
