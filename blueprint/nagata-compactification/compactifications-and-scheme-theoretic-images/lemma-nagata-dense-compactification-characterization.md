+++
id = "lemma-nagata-dense-compactification-characterization"
kind = "lemma"
title = "Characterization of scheme-theoretic density"
order = 143
lean = ["AlgebraicGeometry.isSchemeTheoreticallyDominant_iff_isIso_imageι"]
uses = ["def-nagata-dense-compactification", "def-nagata-scheme-theoretic-image", "lemma-nagata-scheme-image-ideal-qc"]
+++
For an open immersion $j$ (no quasi-compactness is needed), the density
condition in
[def-nagata-dense-compactification] is equivalent to the assertion that
the image inclusion
$j_{\mathrm{im}}\colon\operatorname{SIm}(j)\to\overline X$ is an
isomorphism. Under the resulting identification
$\operatorname{SIm}(j)\cong\overline X$, the factor map
$j^{\mathrm{im}}$ identifies with the original open immersion $j$; in
general, $j^{\mathrm{im}}$ is not an isomorphism.

## Proof

The kernel of $\mathcal O_{\overline X}\to j_*\mathcal O_X$ is the ideal
defining $\operatorname{SIm}(j)$ by
[def-nagata-scheme-theoretic-image]. It is zero exactly when the
closed immersion $\operatorname{SIm}(j)\hookrightarrow\overline X$ is an
isomorphism, by
`Scheme.isIso_subschemeι_iff_eq_bot`. Finally,
`Scheme.Hom.toImage_imageι` identifies the composite of the factor
map with this inclusion with $j$. This transports $j^{\mathrm{im}}$ to
$j$ when the inclusion is inverted; it does not make the factor map an
isomorphism.
