+++
kind = "proof"
of = "sk-thm-pe-direct-image-comparison"
uses = ["lem-weil-pbc-comparison-pullback", "prop-weil-pbc-comparison-direct-image", "det-pe-direct-image-comparison-classical", "lemma-weil-pbc-etale-cohomology-continuity"]
+++
The isomorphism $g_{\Proet}^*\nu_Y^*\simeq\nu_X^*g_{\Et}^*$ is
[lem-weil-pbc-comparison-pullback]. The map of the theorem is adjoint to the
composite of $g_{\Proet}^*\nu_Y^*\simeq\nu_X^*g_{\Et}^*$ with the counit of the
adjunction $g_{\Et}^*\dashv Rg_{\Et,*}$ between $D^+(Y_{\Et},\Lambda)$ and
$D^+(X_{\Et},\Lambda)$; built from these adjunctions, it is compatible with
their units and counits. To show it is an isomorphism, work over an affine open
of $Y$ and evaluate on the covering basis $V=\varprojlim_iV_i$, with $V_i$ affine
and étale over $Y$. For a sheaf $F$ the map in degree $q$ is the continuity map

$$
\varinjlim_iH^q_{\Et}(X\times_YV_i,F)\longrightarrow H^q_{\Et}(X\times_YV,F).
$$

Since $g$ is quasi-compact and quasi-separated, so are its base changes, and the
map is an isomorphism by Stacks Project, Tag 03Q6
([lemma-weil-pbc-etale-cohomology-continuity]). Bounded-below resolutions, or
the convergent hypercohomology spectral sequences, extend this from sheaves to
$K$. This is the proof of Stacks Project, Tag 09A6, carried out in
[prop-weil-pbc-comparison-direct-image]. The statement about classical
complexes is [det-pe-direct-image-comparison-classical].
