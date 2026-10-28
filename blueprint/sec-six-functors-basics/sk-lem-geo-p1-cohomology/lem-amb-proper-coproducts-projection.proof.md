+++
kind  = "proof"
of    = "lem-amb-proper-coproducts-projection"
+++
Test the projection map of
[def-weil-pbc-projection-formula-map] at a geometric point
$\bar t$. It becomes the constant-coefficient map

$$
K_{\bar t}\otimes_A^LR\Gamma(V_{\bar t},L|_{V_{\bar t}})
\longrightarrow
R\Gamma(V_{\bar t},\underline{K_{\bar t}}\otimes_A^LL|_{V_{\bar t}}).
$$

Both sides, as functors of $K_{\bar t}\in D(A)$, are exact
and preserve coproducts. This follows on the right from the coproduct result
[lem-amb-proper-coproducts] applied over the geometric point. The comparison is the
identity for $K_{\bar t}=A$. The shifts of $A$ generate
$D(A)$ under coproducts and cones: free resolutions and their
truncations give the usual explicit construction. Hence the map
is an isomorphism for every $K_{\bar t}$. [lemma-weil-pbc-geometric-stalk-conservative] proves the assertion on $T$.
