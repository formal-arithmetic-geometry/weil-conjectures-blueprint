+++
id = "lem-weil-pbc-cohomology-pullback-degree-zero-iso-factor"
kind = "lemma"
title = "Isomorphism of the degree-zero cycle factor"
uses = ["def-pc-scheme", "def-weil-pbc-etale-cohomology", "def-weil-pbc-kinjective-resolutions"]
lean = ["AlgebraicGeometry.Etale.isIso_degreeZeroCohomology_cycles_factor"]
source = "literature/stacks-project/derived.tex, Lemma Tag 05TD, proof of (3), with a nonnegative injective resolution (Tag 013K) and transport by a homotopy equivalence to the given K-injective resolution."
+++
Let $T$ be a scheme [def-pc-scheme], $G$ an abelian sheaf on its small étale site `CategoryTheory.Sheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/Sheaf.lean)), and $s:G[0]\to I^\bullet$ a quasi-isomorphism with $I^\bullet$ K-injective [def-weil-pbc-kinjective-resolutions]. Write $\Gamma(T,-)$ for global sections and $Z^0$ for the kernel of the degree-zero differential. If $z:\Gamma(T,G)\to Z^0(\Gamma(T,I^\bullet))$ satisfies $i\circ z=\Gamma(T,s^0)$, where $i$ is the inclusion of cycles, then $\pi\circ z:\Gamma(T,G)\to H^0(\Gamma(T,I^\bullet))$ is an isomorphism, where $\pi$ is the homology projection [def-weil-pbc-etale-cohomology].
