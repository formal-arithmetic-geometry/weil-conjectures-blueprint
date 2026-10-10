+++
id = "def-nagata-blowup-product-comparison"
kind = "definition"
title = "Comparison maps for the product-ideal blow-up"
order = 122
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.exists_blowup_mul_iso"]
uses = ["def-nagata-effective-cartier-ideal", "def-nagata-extended-ideal", "def-nagata-global-blowup", "def-nagata-invertible-ideal", "lemma-nagata-cartier-total-transform-blowup", "lemma-nagata-effective-cartier-is-invertible", "lemma-nagata-ideal-invertible-product-factor", "lemma-nagata-invertible-ideal-mul", "lemma-nagata-invertible-product-factor", "prop-nagata-global-blowup-cover-independent", "thm-nagata-blowup-principalizes-center", "thm-nagata-blowup-universal-property"]
+++
Let $X$ be a scheme and let $\mathcal I,\mathcal J$ be quasi-coherent
ideals on $X$. Let $X_{\mathcal I,\mathcal J}$ be the
scheme obtained by first blowing up $\mathcal I$ and then the extended
ideal $\mathcal J\mathcal O_{\operatorname{Bl}_{\mathcal I}(X)}$ from
[def-nagata-extended-ideal].
On $X_{\mathcal I,\mathcal J}$ the total transform of the first exceptional
ideal is invertible ([lemma-nagata-cartier-total-transform-blowup]) and
the second exceptional ideal is invertible
([thm-nagata-blowup-principalizes-center]), so their product, which is
the extension of $\mathcal I\mathcal J$, is invertible
([lemma-nagata-invertible-ideal-mul]). Define

$$
\Phi_{\mathcal I,\mathcal J}\colon
X_{\mathcal I,\mathcal J}
\longrightarrow\operatorname{Bl}_{\mathcal I\mathcal J}(X)
$$

to be the universal lift ([thm-nagata-blowup-universal-property]) for
this product. On $\operatorname{Bl}_{\mathcal I\mathcal J}(X)$ the
extension of $\mathcal I\mathcal J$ is invertible, so the extensions of both
factors are invertible ([lemma-nagata-invertible-product-factor]).
Define

$$
\Psi_{\mathcal I,\mathcal J}\colon
\operatorname{Bl}_{\mathcal I\mathcal J}(X)
\longrightarrow X_{\mathcal I,\mathcal J}
$$

as the universal lift for $\mathcal I$, followed by the universal lift for
the extended $\mathcal J$.
