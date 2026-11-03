+++
kind  = "proof"
of    = "cor-nagata-blowup-product-common-refinement"
uses = ["def-nagata-invertible-ideal", "lemma-nagata-cartier-total-transform-blowup", "lemma-nagata-ideal-invertible-product-factor", "lemma-nagata-invertible-ideal-mul", "thm-nagata-blowup-principalizes-center", "thm-nagata-blowup-universal-property", "thm-nagata-global-blowup-complement"]
+++
The maps are composites over $X$ by definition: $d_{\mathcal I}$ is
$\Psi_{\mathcal I,\mathcal J}$ followed by the first blow-up projection,
and $\Psi_{\mathcal I,\mathcal J}$ is a composite of universal lifts, each
of which lies over the previous base. If $V(\mathcal I)$ and
$V(\mathcal J)$ miss $U$, then so does
$V(\mathcal I\mathcal J)=V(\mathcal I)\cup V(\mathcal J)$, so all three
blow-up maps are isomorphisms over $U$ by the complement theorem. Since
$b_{X,\mathcal I}\circ d_{\mathcal I}=b_{X,\mathcal I\mathcal J}$, the
restriction of $d_{\mathcal I}$ over $U$ is a composite of isomorphisms,
and likewise for $d_{\mathcal J}$.
