+++
kind  = "proof"
of    = "prop-exc-open-adjoint"
+++
The site over the open $U$ is the localization of the site of
[def-weil-pbc-proetale-site] at the subterminal sheaf represented by
$U$. Thus restriction $j^*$ is exact. For module sheaves $M,N$,
the extension-by-zero adjunction of
[lem-weil-extension-by-zero-adjunction] gives

$$
\operatorname{Hom}(j_!M,N)=\operatorname{Hom}(M,j^*N).
$$

Exactness of extension by zero is proved using presheaf kernels,
local lifting, and sheafification in
[lem-weil-extension-by-zero-exact]. Apply the two exact
functors degree by degree to complexes.
They preserve acyclic complexes. Their sheaf-level unit and counit are
chain maps, still satisfy both triangular identities, and descend through
localization at quasi-isomorphisms. Hence they define the asserted
adjunction, with inverse image as in
[def-weil-derived-pullback-tensor-hom].
