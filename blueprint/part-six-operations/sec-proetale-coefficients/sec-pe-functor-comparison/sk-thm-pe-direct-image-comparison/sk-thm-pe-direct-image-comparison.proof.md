+++
kind = "proof"
of = "sk-thm-pe-direct-image-comparison"
uses = ["lem-weil-pbc-comparison-pullback", "prop-weil-pbc-comparison-direct-image", "lemma-weil-pbc-etale-cohomology-continuity", "sk-cor-pe-classical-derived"]
+++
Evaluated on a pro-étale affine
$V=\varprojlim_iV_i$ over $Y$, the map becomes the continuity map of
étale cohomology for the affine limit $X\times_YV=\varprojlim_iX\times_YV_i$.
Since the map is defined from the adjunctions $g^*\dashv Rg_*$ on the two
sites, it is compatible with their units and counits. For a composite
$X\to Y\to Z$, the map for the composite is the composite of the two
maps, because the isomorphisms $g^*\nu^*\simeq\nu^*g^*$ are compatible
with composition and the adjoint of a composite is the composite of the
adjoints. To show that it is an
isomorphism, we work over an affine open of $Y$ and evaluate on the
covering basis $V=\varprojlim_iV_i$, with $V_i$ affine and étale
over $Y$. By (2.6) and
Theorem [sk-prop-sf-comparison], for a sheaf $F$ the map in
degree $q$ is the continuity map

$$
\varinjlim_i H^q_{\acute{e}t}(X\times_YV_i,F)
\longrightarrow
H^q_{\acute{e}t}(X\times_YV,F).
$$

Since $g$ is quasi-compact and quasi-separated, so are its base
changes, and the map is an isomorphism by continuity of étale
cohomology under affine limits [Stacks, Tag 03Q6](https://stacks.math.columbia.edu/tag/03Q6). Using bounded-below
resolutions, or the convergent hypercohomology spectral sequences, we
pass from sheaves to $K$; see [Stacks, Tag 09A6](https://stacks.math.columbia.edu/tag/09A6). The assertion on
classical complexes follows because, by
Corollary [sk-cor-pe-classical-derived], every bounded-below classical
complex is of the form $\nu_X^*K$.
