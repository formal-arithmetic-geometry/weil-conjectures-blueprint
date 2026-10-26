+++
id = "lem-weil-pbc-cohomology-pullback-degree-zero-iso-factor"
kind = "lemma"
title = "Isomorphism of the degree-zero cycle factor"
uses = ["def-pc-scheme", "def-weil-pbc-etale-cohomology", "def-sp-kinjective-bridge"]
lean = ["AlgebraicGeometry.Etale.isIso_degreeZeroCohomology_cycles_factor"]
order = 1675
+++
Let $T$ be a scheme [def-pc-scheme], $G$ an abelian sheaf on its small étale site, and $s:G[0]\to I^\bullet$ a quasi-isomorphism with $I^\bullet$ K-injective [def-sp-kinjective-bridge]. Write $\Gamma(T,-)$ for global sections and $Z^0$ for the kernel of the degree-zero differential. If $z:\Gamma(T,G)\to Z^0(\Gamma(T,I^\bullet))$ satisfies $i\circ z=\Gamma(T,s^0)$, where $i$ is the inclusion of cycles, then $\pi\circ z:\Gamma(T,G)\to H^0(\Gamma(T,I^\bullet))$ is an isomorphism, where $\pi$ is the homology projection [def-weil-pbc-etale-cohomology].
