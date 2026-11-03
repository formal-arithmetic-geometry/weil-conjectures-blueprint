+++
kind  = "proof"
of    = "lemma-weil-pbc-five-lemma-transfer"
+++
Applying $g^{-1}Rf_*$ and $Rf'_*g'^{-1}$ to the distinguished triangle
$F_1\to F\to F_2\to F_1[1]$ defined by the short exact sequence produces two long
exact cohomology sequences (the functors are triangulated and $g^{-1}$ is
exact). Naturality of the derived exchange morphism, as in
[lemma-weil-pbc-derived-exchange-replacement], makes the maps $\Ex^q$ a morphism
between these sequences; compatibility with the connecting maps holds because
$\Ex_\square$ is a natural transformation of triangulated functors, or
concretely by the connecting-homomorphism construction from an injective
resolution of [def-weil-pbc-derived-exchange]. The terms adjacent to
$g^{-1}R^qf_*F$ are
$g^{-1}R^{q-1}f_*F_2\to g^{-1}R^qf_*F_1\to g^{-1}R^qf_*F\to g^{-1}R^qf_*F_2\to
g^{-1}R^{q+1}f_*F_1$, and similarly for the target; if the exchange maps at
$F_1$ and $F_2$ are isomorphisms in all degrees, the five lemma shows that
$\Ex^q_{\square,F}$ is an isomorphism.
