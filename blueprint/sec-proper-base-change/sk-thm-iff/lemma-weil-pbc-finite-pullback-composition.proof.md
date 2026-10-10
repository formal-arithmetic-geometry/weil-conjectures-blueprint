+++
kind  = "proof"
of    = "lemma-weil-pbc-finite-pullback-composition"
+++
Both maps send a section to the image of the same presheaf section under the
composite inverse-image functor: the composition isomorphism
$(uv)^{-1}\cong v^{-1}u^{-1}$ carries the unit of $(uv)^{-1}\dashv(uv)_*$ to the
composite of the units of $u^{-1}\dashv u_*$ and $v^{-1}\dashv v_*$. Naturality of
sheafification and the associativity isomorphism
$T\times_TT'\times_{T'}T''=T''$ make the two maps equal; the identity case
[lemma-weil-pbc-finite-pullback-identity] is the degenerate instance in which
one of the morphisms is an identity.
