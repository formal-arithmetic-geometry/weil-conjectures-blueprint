+++
id = "def-weil-pbc-etale-residue-triples"
kind = "definition"
title = "The category of étale algebras with a prime and a residue-field embedding"
uses = ["def-pc-scheme"]
lean = ["AlgebraicGeometry.Scheme.EtaleResidueTriple"]
+++
Let $A$ be a commutative ring, let $p\in\operatorname{Spec}A$ `AlgebraicGeometry.Spec` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Scheme.lean)), let $K$ be a field, and let $\chi:\kappa(p)\to K$ be a field homomorphism `AlgebraicGeometry.Scheme.residueField` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/ResidueField.lean)). An etale residue triple is $(B,\alpha,q,\phi)$, where $\alpha:A\to B$ has etale spectrum map `AlgebraicGeometry.Etale` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/Etale.lean)), $q\in\operatorname{Spec}B$ maps to $p$, and $\phi:\kappa(q)\to K$ is compatible with $\chi$ over $\kappa(p)$. Its associated map $\psi:B\to K$ is $B\to\kappa(q)\xrightarrow{\phi}K$. The category has as morphisms $A$-ring maps $\beta:B\to B\prime$ with $\psi\prime\circ\beta=\psi$, equivalently $\beta^{-1}(q\prime)=q$ and $\phi\prime\circ\kappa(\beta)=\phi$. The forgetful ring diagram sends a triple to $B$ and a morphism to $\beta$. Residue fields here are those of the affine schemes [def-pc-scheme].
