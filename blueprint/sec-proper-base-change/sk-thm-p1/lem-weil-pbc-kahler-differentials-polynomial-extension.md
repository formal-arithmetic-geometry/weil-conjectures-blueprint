+++
id = "lem-weil-pbc-kahler-differentials-polynomial-extension"
kind = "lemma"
title = "Kähler differentials of a polynomial algebra over an algebra"
lean = ["KaehlerDifferential.exists_polynomial_extension_equiv"]
order = 1848
+++
Let $R\to A$ be a homomorphism of commutative rings, $e\ge0$ and $B=A[z_1,\dots,z_e]$ the polynomial ring, an $R$-algebra via $R\to A\to B$. Then the $B$-linear map $(B\otimes_A\Omega_{A/R})\oplus B^{e}\to\Omega_{B/R}$, $(b\otimes\mathrm d\alpha,(b_1,\dots,b_e))\mapsto b\,\mathrm d\alpha+\sum_jb_j\,\mathrm dz_j$, is an isomorphism. In particular, if $\Omega_{A/R}$ is a free $A$-module of rank $d$, then $\Omega_{B/R}$ is a free $B$-module of rank $d+e$.
