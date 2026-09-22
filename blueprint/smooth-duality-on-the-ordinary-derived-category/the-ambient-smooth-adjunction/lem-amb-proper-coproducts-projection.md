+++
id = "lem-amb-proper-coproducts-projection"
kind = "lemma"
title = "The proper projection formula on the ambient category"
order = 5606
lean = ["AlgebraicGeometry.Etale.IsProper.projection_formula"]
uses = ["lem-amb-proper-coproducts"]
+++
Let $r:V\to T$ be a proper morphism of finite type between Noetherian
schemes. For all complexes $L$ on $V$ and $K$ on $T$, the canonical derived
tensor projection map is an isomorphism in the ordinary derived category:
$$
K\otimes_A^LRr_*L\longrightarrow Rr_*(r^*K\otimes_A^LL).
$$

## Proof

Test the projection map at a geometric point $\bar t$. It becomes the
constant-coefficient map
$$
K_{\bar t}\otimes_A^LR\Gamma(V_{\bar t},L|_{V_{\bar t}})
\longrightarrow R\Gamma(V_{\bar t},\underline{K_{\bar t}}\otimes_A^LL|_{V_{\bar t}}).
$$

Both sides, as functors of $K_{\bar t}\in D(A)$, are exact and preserve
coproducts. This follows on the right from the coproduct result
[lem-amb-proper-coproducts] applied over the geometric point. The comparison
is the identity for $K_{\bar t}=A$. The shifts of $A$ generate $D(A)$ under
coproducts and cones: free resolutions and their truncations give the usual
explicit construction. Hence the map is an isomorphism for every
$K_{\bar t}$, and conservativity of geometric stalks proves the assertion on
$T$.

Unresolved dependencies: def:weil-pbc-derived-categories, def:weil-pbc-direct-image, def:weil-derived-tensor, def:weil-pbc-inverse-image, def:weil-scheme-morphism-properties, def:weil-pbc-projection-formula-map, lem:weil-pbc-geometric-stalk-conservative
