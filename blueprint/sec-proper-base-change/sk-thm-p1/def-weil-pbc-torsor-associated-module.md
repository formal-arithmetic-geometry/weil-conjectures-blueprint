+++
id = "def-weil-pbc-torsor-associated-module"
kind = "definition"
title = "Associated module functor of equivariant locally constant sections"
uses = ["def-sbc-normal-dominant-galois", "def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-scheme-conventions"]
lean = ["AlgebraicGeometry.Scheme.GaloisCover.associatedModuleFunctor"]
source = "literature/stacks-project/etale-cohomology.tex, Tags 0DV5 (3), 0DV6 and 0A3R, proof identifying the restricted representation; sites.tex Tags 04TR and 04TS (gluing sheaves and mapping property), with module operations as in 0DV5 (3)"
+++
Let $V$ be a scheme [def-weil-pbc-scheme-conventions], $\ell\in\mathbb N$, $P$ a finite group and $c:Y\to V$ a finite etale $\operatorname{ULift}(P)$-torsor [def-sbc-normal-dominant-galois]. Put $k=\mathbb Z/\ell\mathbb Z$ and $\widetilde k=\operatorname{ULift}(k)$. For a $k$-representation $N$ of $P$ and an etale object $W\to V$ [def-weil-pbc-etale-site], take the submodule of locally constant functions $s:W\times_V Y\to N$ satisfying $s(g y)=\rho_N(g)s(y)$. Restriction is precomposition with the induced map of fibre products, and intertwiners act pointwise. The associated module functor $T_c$ restricts these presheaves along $\widetilde k\to k$ and sheafifies `CategoryTheory.presheafToSheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/Sheafification.lean)), giving sheaves of $\widetilde k$-modules [def-weil-pbc-etale-sheaves].
