+++
id = "fin2-thm-smooth-proper-lisse-constructible"
kind = "theorem"
title = "Smooth proper families with locally constant coefficients"
order = 1678
uses = ["cor-weil-pbc-geometric-fiber-finite", "def-sbc-normal-dominant-galois", "def-sbc-smooth-morphisms", "def-weil-pbc-constructible-complexes", "def-weil-pbc-direct-image", "def-weil-pbc-scheme-conventions", "fin4-lem-fibrewise-cohomological-dimension", "lemma-weil-pbc-geometric-stalk-conservative", "sbc-def-coefficient-conventions", "thm-fin-proper-constructibility-complete"]
+++
Let $f:X\to S$ be a
smooth proper morphism with $S$ of
finite type over $k$ and
geometrically connected
geometric fibres of
dimension at most $r\in\mathbf Z_{\geq0}$, and let $M$ be a
lisse $\Lambda$-sheaf
on $X_{{\mathrm{et}}}$ (the ring $\Lambda$ of
[sbc-def-coefficient-conventions]). Then the higher direct
images $R^qf_*M$ of [def-weil-pbc-direct-image] are
constructible on
$S_{{\mathrm{et}}}$ for every $q\geq0$, and $R^qf_*M=0$ for $q>2r$.

## Proof

Constructibility follows from
[thm-fin-proper-constructibility-complete], applied to the given
proper morphism and constructible coefficient sheaf.
For every geometric point $\bar s$, proper base change
[cor-weil-pbc-geometric-fiber-finite] identifies

$$
(R^qf_*M)_{\bar s}=H^q(X_{\bar s},M|_{X_{\bar s}}).
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
