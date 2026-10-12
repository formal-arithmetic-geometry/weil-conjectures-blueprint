+++
kind  = "proof"
of    = "lem-fin-finite-reflects-constructibility"
+++
At a geometric point $\bar z$, with induced point $\bar s$ of $S$,
the counit has stalk

$$
(p^*p_*F)_{\bar z}
=\prod_{\bar z'\in |Z_{\bar s}|}F_{\bar z'}
\longrightarrow F_{\bar z},
$$

the projection of [lemma-weil-pbc-finite-stalk-formula].
It is surjective for modules, hence the counit is surjective by
[lemma-weil-pbc-geometric-stalk-conservative].
Pulling back a finite partition and its etale trivializations proves
that $p^*p_*F$ is constructible, by
[def-weil-pbc-constructible-complexes].
Its kernel is constructible by
[lem-weil-pbc-constructible-subobjects-noetherian].
Now take its cokernel using [thm-constructible-serre].
No surjectivity of $p$ onto $S$ is required.
