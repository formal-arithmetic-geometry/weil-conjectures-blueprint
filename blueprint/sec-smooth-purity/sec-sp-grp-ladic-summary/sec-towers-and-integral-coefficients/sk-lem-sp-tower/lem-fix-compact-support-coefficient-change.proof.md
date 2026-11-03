+++
kind  = "proof"
of    = "lem-fix-compact-support-coefficient-change"
+++
Use the compactification description of
[def-compact-support-direct-image-detailed] and the derived tensor of
[def-weil-derived-pullback-tensor-hom]. For a bounded finite-free
complex $P$ of constant $A$-modules, the comparison with $P$
is an isomorphism: it is the identity for $P=A$, and finite sums,
shifts and cones preserve this assertion. Its compatibility with the
projection transformation of [def-exchange-projection] follows by
transposing the two maps: both apply the same counit to the first
factor and retain the coefficient factors in their original order.

Choose a bounded-above resolution $P\to B$ by finite free
$A$-modules. This resolution need not have finite length. If
$K$ has Tor amplitude $[a,b]$, the error made by replacing $P$
by its truncation by terms in degrees $\geq-t$ has cohomology in
degrees $\leq b-t$, up to a fixed shift independent of $t$.
Compact-support base change [thm-cbc-finite-torsion] identifies
each geometric stalk of the comparison with compactly supported
cohomology of a geometric fiber. On that fiber, the uniform
cohomological-dimension bound of
[thm-sc-finite-type-torsion-cd], applied after a compactification,
shows that the error after $R\Gamma_c$ vanishes in every fixed
degree once $t$ is large. On the tensor side the same assertion
follows from boundedness above of $R\Gamma_c(K)$.
The finite-free comparison therefore proves the required isomorphism
in every degree. Stalk conservativity
[lemma-weil-pbc-geometric-stalk-conservative] proves it on the
etale site, and the compact-support site comparison of
[thm-cbc-finite-level-proetale] transports the construction to the
specified pro-etale realizations. All compatibility identities hold
before passage to a resolution, because they are associativity and
counit identities for the specified tensor map. They survive both
truncation and coefficient change. In particular no flatness of
$A\to B$ is used.
