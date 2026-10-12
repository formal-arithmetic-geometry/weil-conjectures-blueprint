+++
kind  = "proof"
of    = "prop-sfb-module-derived-open-adjunction"
uses = ["def-sfb-module-derived-pushpull-adjunction"]
+++
Derive the adjunction $j_!\dashv j^*$ of [def-sfb-module-open-lower-shriek-adjunction]
as in [def-sfb-module-derived-pushpull-adjunction]: the exact functor $j_!$ preserves
quasi-isomorphisms between K-flat complexes, so the general derivation of adjunctions
gives $L(j_!)\dashv R(j^*)$. For an exact functor the total left (resp. right) derived
functor is the levelwise functor ([sk-def-sfb-derived-categories]): $L(j_!)\cong
D(j_!)$ and $R(j^*)\cong D(j^*)$. Transporting the adjunction along these isomorphisms
gives $D(j_!)\dashv D(j^*)$.
