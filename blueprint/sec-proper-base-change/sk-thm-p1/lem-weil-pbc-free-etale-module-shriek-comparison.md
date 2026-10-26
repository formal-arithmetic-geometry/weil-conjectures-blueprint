+++
id = "lem-weil-pbc-free-etale-module-shriek-comparison"
kind = "lemma"
title = "Free representable module sheaves are etale extensions by zero"
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-etale-sum-extension"]
lean = ["AlgebraicGeometry.Scheme.free_etale_module_shriek_comparison"]
order = 1796
+++
Let $X$ be a scheme and $W$ an object of its small etale site [def-weil-pbc-etale-site]. Let $\Lambda$ be a commutative ring and consider sheaves of $\Lambda$-modules on the small etale site [def-weil-pbc-etale-sheaves]. Write $P_W$ for the sheafification of the presheaf $V\mapsto\Lambda^{(\operatorname{Hom}_X(V,W))}$, with restriction induced by precomposition. There is an isomorphism $P_W\cong j_{W!}\underline{\Lambda}_{W}$, where $j_{W!}$ is etale extension by zero [def-weil-pbc-etale-sum-extension] and $\underline{\Lambda}_W$ is the constant rank-one module sheaf. No quasi-compactness, affineness, separatedness, or finiteness of $\Lambda$ is assumed.
