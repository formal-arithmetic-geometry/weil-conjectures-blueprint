+++
kind  = "proof"
of    = "lem-sfb-finite-extension-by-zero-fully-faithful"
uses = ["def-sfb-finite-extension-by-zero-adjunction", "def-sfb-finite-lower-star"]
+++
By the proof of [def-sfb-finite-extension-by-zero-adjunction] there is an adjoint triple
$j_!\dashv j^*\dashv j_*$. The counit $j^*j_*\to\mathrm{id}$ is an isomorphism: since $j$
is a monomorphism, $T\times_XU\cong T$ for every $T$ over $U$, so the unit of the site-level
adjunction between localization and base change is an isomorphism, and
$(j^*j_*G)(T)=G(T\times_XU)\cong G(T)$ ([def-sfb-finite-lower-star]). In an adjoint triple
the counit of the right adjunction is invertible if and only if the unit of the left
adjunction is. So $\mathrm{id}\to j^*j_!$ is an isomorphism, which means that $j_!$ is fully
faithful.
