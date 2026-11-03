+++
kind = "proof"
of = "lem-weil-pbc-etale-cech-sectionwise-short-exact"
uses = ["def-sp-left-exact-additive"]
+++
Write $V_a=V_{a_0}\times_U\cdots\times_UV_{a_p}$ for a tuple $a=(a_0,\dots,a_p)\in T^{p+1}$. Fix $p\ge0$. Evaluating an abelian sheaf at all the objects $V_a$ is a functor $Q$ from abelian sheaves on $X_{\Et}$ to families of abelian groups indexed by the set $T^{p+1}$. It is additive and preserves finite limits, because kernels of abelian sheaves are computed sectionwise [def-sp-left-exact-additive]. Applying $Q$ to the exact sequence $0\to F_1\to F_2\xrightarrow{g}F_3$ therefore gives, for every $a$, an exact sequence $0\to F_1(V_a)\to F_2(V_a)\to F_3(V_a)$, and the last map is surjective by hypothesis. So for every $a$ the sequence $0\to F_1(V_a)\to F_2(V_a)\to F_3(V_a)\to0$ is short exact.

Arbitrary products of abelian groups preserve short exact sequences (products are exact in the category of abelian groups). Taking the product over $a\in T^{p+1}$ gives a short exact sequence
$$0\to\prod_aF_1(V_a)\to\prod_aF_2(V_a)\to\prod_aF_3(V_a)\to0,$$
which is the degree-$p$ part of the sequence of Čech complexes: the degree-$p$ Čech cochains of $F_k$ are $\prod_aF_k(V_a)$, and the maps induced by $F_1\to F_2\to F_3$ act componentwise. This works for every index set $T$, including the empty one.

A sequence of cochain complexes which is short exact in every degree is a short exact sequence of complexes, which proves the claim.
