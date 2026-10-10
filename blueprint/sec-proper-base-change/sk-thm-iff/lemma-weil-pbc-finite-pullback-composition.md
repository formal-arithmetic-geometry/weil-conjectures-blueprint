+++
id = "lemma-weil-pbc-finite-pullback-composition"
kind = "lemma"
title = "Finite pullback composition"
order = 1081
lean = ["AlgebraicGeometry.Etale.globalSectionsUpperStarMap_comp"]
uses = ["def-weil-pbc-finite-section-pullback", "lemma-weil-pbc-finite-pullback-identity"]
+++
Let $T''\xrightarrow{v}T'\xrightarrow{u}T$ be morphisms of schemes and $G$ an
etale sheaf on $T$ (with values in $\mathcal A$ as in
[def-weil-pbc-finite-section-pullback]). Then the pullback of global sections
along the composite, followed by the map on global sections induced by the
composition isomorphism $(uv)^{-1}G\cong v^{-1}u^{-1}G$, equals the composite
pullback:

$$
\Gamma(T,G)\xrightarrow{(uv)^\sharp}\Gamma(T'',(uv)^{-1}G)\cong
\Gamma(T'',v^{-1}u^{-1}G)
\quad=\quad
\Gamma(T,G)\xrightarrow{u^\sharp}\Gamma(T',u^{-1}G)\xrightarrow{v^\sharp}
\Gamma(T'',v^{-1}u^{-1}G).
$$

## Proof

Both maps send a section to the image of the same presheaf section under the
composite inverse-image functor: the composition isomorphism
$(uv)^{-1}\cong v^{-1}u^{-1}$ carries the unit of $(uv)^{-1}\dashv(uv)_*$ to the
composite of the units of $u^{-1}\dashv u_*$ and $v^{-1}\dashv v_*$. Naturality of
sheafification and the associativity isomorphism
$T\times_TT'\times_{T'}T''=T''$ make the two maps equal; the identity case
[lemma-weil-pbc-finite-pullback-identity] is the degenerate instance in which
one of the morphisms is an identity.
