+++
kind  = "proof"
of    = "lem-weil-extension-by-zero-exact"
+++
In the presheaf construction of [def-weil-extension-by-zero], kernels are
computed objectwise: on an object over $U$ this is the kernel of the
corresponding section map, and on other objects it is zero. Sheafification of
module presheaves is exact, so $j_!$ preserves kernels on the module sheaves
of [def-weil-finite-torsion-constructibility]. For an epimorphism $M\to N$, a
section of $P_N(V)$ is either zero or a section of $N(V)$ with $V$ over $U$.
In the latter case it lifts on a covering of $V$ in $U_{\mathrm{proet}}$.
This is also a covering in the ambient site of
[def-weil-pbc-proetale-site]. Thus $P_M\to P_N$ is locally
surjective; after sheafification it is an epimorphism. Preservation of
kernels and epimorphisms proves exactness.
