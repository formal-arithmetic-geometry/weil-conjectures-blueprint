+++
kind  = "proof"
of    = "sk-def-sfb-dc-restricted-functors"
uses = ["sk-def-sfb-constructible", "sk-def-sfb-module-pushforward-pullback", "sk-prop-sfb-module-pullback-exact"]
+++
The preservation statements are [lem-sfb-dc-upper-star-preserves],
[lem-sfb-dc-lower-star-preserves], [lem-sfb-dc-open-lower-shriek-preserves],
[lem-sfb-dc-tensor-preserves] and [lem-sfb-dc-hom-preserves]. The restricted functors are
[def-sfb-dc-upper-star], [def-sfb-dc-lower-star], [def-sfb-dc-open-lower-shriek],
[def-sfb-dc-tensor] and [def-sfb-dc-hom].

Two general facts are used. If an ambient functor $F$ carries the full subcategory $\mathcal C$ into
the full subcategory $\mathcal C'$, then $F\circ\iota_{\mathcal C}$ factors uniquely through
$\iota_{\mathcal C'}$. If the two functors of an ambient adjunction $L\dashv R$ both restrict, then
the Hom-bijections restrict too, since Hom-sets in a full subcategory are the ambient ones. So the
adjunction restricts. In the same way, a natural isomorphism between composites of restricted
functors is the preimage, under the fully faithful inclusion, of the ambient one. This gives the
adjunctions [def-sfb-dc-upper-lower-adjunction], [def-sfb-dc-open-lower-shriek-adjunction] and
[def-sfb-dc-tensor-hom-adjunction], and the composition isomorphism [def-sfb-dc-upper-star-comp].
