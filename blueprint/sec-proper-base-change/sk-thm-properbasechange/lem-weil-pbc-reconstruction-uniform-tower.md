+++
id = "lem-weil-pbc-reconstruction-uniform-tower"
kind = "lemma"
title = "Reconstruction of a uniform local tower"
order = 1299
uses = ["def-weil-pbc-adic-coefficient-datum", "def-weil-pbc-bounded-constructible-tower", "def-weil-pbc-derived-inverse-limit", "def-weil-pbc-intrinsic-completion", "lem-weil-pbc-finite-reduction-reconstruction", "prop-weil-pbc-koszul-reconstruction"]
+++
Let $M_\bullet$ be a uniformly bounded constructible adic tower in the sense
of [def-weil-pbc-bounded-constructible-tower] and put $M=\Rlim M_\bullet$.
For every local model in [def-weil-pbc-bounded-constructible-tower],
restriction of the derived-limit projections gives a functorial isomorphism

$$
 L_{\alpha j}\xrightarrow{\sim}M|_{U_{\alpha j}}.
$$

Consequently $M$ is derived $I$-complete, the canonical maps

$$
 M\otimes_A^LP_n\xrightarrow{\sim}M_n
$$

are isomorphisms compatible with normalization, and $M$ has no cohomology
outside $[d_0,d_1]$. No finiteness assertion about the groups of sections on
$U_{\alpha j}$ is required.
