+++
kind = "proof"
of = "lem-weil-pbc-etale-limit-canonical-cohomology-diagram"
uses = ["lem-weil-pbc-cohomology-pullback-functorial"]
+++
Define H_i as the degree-n cohomology of F_i and each transition as cohomology pullback followed by H.map(phi_f). The identity transition of F and the identity pullback clause give H.map_id. For composition, rewrite phi_(f≫g), use naturality of pullback in coefficients to interchange the map of phi_f and pullback along g, then apply the composition clause of cohomologyPullbackFunctorial. This gives H.map_comp. ([lem-weil-pbc-cohomology-pullback-functorial]).

Take B.pt=H^n(L.pt) and its ith leg to be cohomology pullback along f_i followed by H.map((eG_i).inv≫L_i). For naturality along f:i->j, interchange phi_f with pullback along f_j; the cone equation identifies f_j composed with D(f^op) with f_i. The cohomology pullback composition clause introduces exactly the upperStarComp in hG. Rewrite G.map f by hG in the cocone equation L.w f and cancel the inverse-image object isomorphisms. Applying H.map to the resulting coefficient equality proves naturality of the legs. Take all eH and eB to be identity isomorphisms. ([lem-weil-pbc-cohomology-pullback-functorial]).
