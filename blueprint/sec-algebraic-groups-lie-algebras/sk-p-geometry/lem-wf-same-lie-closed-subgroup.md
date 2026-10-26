+++
id = "lem-wf-same-lie-closed-subgroup"
kind = "lemma"
title = "Smoothness, dimension and Lie algebras of matrix groups"
lean = ["AlgebraicGeometry.GeneralLinearGroup.eq_of_le_of_lieSubalgebra_eq", "AlgebraicGeometry.GeneralLinearGroup.dualUnit_mem_zeroLocus_identityComponent", "AlgebraicGeometry.GeneralLinearGroup.eq_of_le_of_bijective_lieAlgebraMap", "HopfAlgebra.finrank_cotangent_eq_ringKrullDim", "Matrix.GeneralLinearGroup.IsConnected.isPrime"]
order = 3689
uses = ["def-wf-algebraic-components", "def-wf-lie-algebra-derivation", "lem-ag-equal-dimension-subgroup", "lem-sc-translation-automorphism", "lem-wf-smooth-components-disjoint"]
+++
Let $K$ be a closed matrix group over $\overline{\mathbf Q}_\ell$.

1. If $K$ is connected, then $K$ is irreducible. Moreover, if $K$ is
   connected, $L\subseteq K$ is a closed algebraic subgroup and
   $\operatorname{Lie}(L)=\operatorname{Lie}(K)$, then $L=K$.
2. $K$ is smooth, and
   $\dim\operatorname{Lie}(K)=\dim K$.
3. The identity component $K^\circ$ of [def-wf-algebraic-components]
   is open (and closed) in $K$, and
   $\operatorname{Lie}(K^\circ)=\operatorname{Lie}(K)$.
4. The differential at $(1,1)$ of the multiplication
   $K\times K\to K$ is the map
   $\operatorname{Lie}(K)\oplus\operatorname{Lie}(K)\to\operatorname{Lie}(K)$,
   $(X,Y)\mapsto X+Y$.
