+++
kind  = "proof"
of    = "thm-fin-proper-case"
+++
Constructibility follows from
[thm-fin-proper-constructibility-complete], applied to the given
proper morphism and constructible coefficient sheaf.
For every geometric point $\bar s$, proper base change
[cor-weil-pbc-geometric-fiber-finite] identifies

$$
(R^qf_*F)_{\bar s}=H^q(X_{\bar s},F|_{X_{\bar s}}).
$$

The right side is zero above twice the specified fibre-dimension
bound by [fin4-lem-fibrewise-cohomological-dimension].
Geometric stalk conservativity
[lemma-weil-pbc-geometric-stalk-conservative] proves the sheaf vanishing.
Each fibre group is finite because constructible sheaves have finite
stalks by [def-weil-pbc-constructible-complexes].
The constructibility proof uses finite resolutions and proper
modifications; the sharp bound is obtained separately from this
geometric-fibre calculation.
