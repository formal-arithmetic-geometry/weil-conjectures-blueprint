+++
id = "dag-def-weil-signed-mapping-cocone-functor"
kind = "dag-definition"
title = "Functorial mapping cocones and their specified signed shift comparisons"
name_showing = false
order = 210507
tags = ["sheaf-dag"]
split_from = "lemma-reduction-derived-nakayama--2"
dag_id = "def-weil-signed-mapping-cocone-functor"
dag_kind = "definition"
dag_status = "split"
serial = false
dag_lean = ["CategoryTheory.SignedCoconeShift.coconeMap", "CategoryTheory.SignedCoconeShift.coconeFunctor", "CategoryTheory.SignedCoconeShift.signedCoconeShiftIso", "CategoryTheory.SignedCoconeShift.coconeFunctorShiftIso", "CategoryTheory.SignedCoconeShift.coconeFunctorShiftNatIso"]
+++
Let $\mathcal A$ be an abelian category `def-sp-abelian`, with integer cochain complexes, mapping cones and shifts as in `def-weil-abstract-derived-category`. For chain maps $\varphi:K\to L$, $\psi:K^\prime\to L^\prime$ and a commuting square $(a,b)$ with $b\varphi=\psi a$, define the mapping-cocone map $\operatorname{Cone}(\varphi)[-1]\to\operatorname{Cone}(\psi)[-1]$ by shifting the diagonal mapping-cone map induced by $(a,b)$. For any category $S$, functors $F,G:S\to\operatorname{CochainComplex}(\mathcal A,\mathbb Z)$ and natural transformation $\tau:F\to G$, define the functor $C_\tau(X)=\operatorname{Cone}(\tau_X)[-1]$ on maps by this construction for $(F(f),G(f))$. For every chain map $\varphi$ and integer $m$, specify the signed comparison $\operatorname{Cone}(\varphi[m])[-1]\cong(\operatorname{Cone}(\varphi)[-1])[m]$ as $(-1)^m$ times the inverse standard cone-shift comparison shifted by $[-1]$, followed by the canonical interchange of shifts. If $S$ has integer shifts, $F,G$ have coherent shift comparisons and $\tau$ commutes with them, define $C_\tau(X[m])\cong C_\tau(X)[m]$ by the mapping-cocone isomorphism of the square of these comparisons, followed by that signed comparison. These specified component isomorphisms define the natural isomorphism $C_\tau\circ[m]\cong[m]\circ C_\tau$ (shift first on the left, shift last on the right). This definition specifies the data; the zero and successive-shift coherence laws are separate assertions.

(SHEAF DAG node `def-weil-signed-mapping-cocone-functor`; machine-alignment layer.) Split from [lemma-reduction-derived-nakayama--2]. DAG kind: definition. Placed through `det-pe-derived-nakayama-first-reduction` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-sp-abelian`, `def-weil-abstract-derived-category`.
