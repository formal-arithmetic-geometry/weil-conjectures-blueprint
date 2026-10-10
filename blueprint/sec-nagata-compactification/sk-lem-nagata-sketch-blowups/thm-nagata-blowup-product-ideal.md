+++
id = "thm-nagata-blowup-product-ideal"
kind = "theorem"
title = "[stacks-project]"
order = 123
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.exists_blowup_mul_iso"]
uses = ["def-nagata-blowup-product-comparison", "def-nagata-effective-cartier-ideal", "def-nagata-extended-ideal", "def-nagata-global-blowup", "def-nagata-invertible-ideal", "lemma-nagata-cartier-total-transform-blowup", "lemma-nagata-effective-cartier-is-invertible", "lemma-nagata-ideal-invertible-product-factor", "lemma-nagata-invertible-ideal-mul", "lemma-nagata-invertible-product-factor", "prop-nagata-global-blowup-cover-independent", "thm-nagata-blowup-principalizes-center", "thm-nagata-blowup-universal-property"]
+++
Let $X$ be a scheme and let $\mathcal I,\mathcal J$ be quasi-coherent
ideals on $X$. Then there is an isomorphism

$$
\operatorname{Bl}_{\mathcal I\mathcal J}(X)\cong X_{\mathcal I,\mathcal J}
=\operatorname{Bl}_{\mathcal J\mathcal O_{\operatorname{Bl}_{\mathcal I}(X)}}\bigl(\operatorname{Bl}_{\mathcal I}(X)\bigr)
$$

over $X$, given by the mutually inverse maps $\Psi_{\mathcal I,\mathcal J}$
and $\Phi_{\mathcal I,\mathcal J}$. Thus the iterated blow-up is identified
with the blow-up of $\mathcal I\mathcal J$.
