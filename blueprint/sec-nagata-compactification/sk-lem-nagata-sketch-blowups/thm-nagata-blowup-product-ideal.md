+++
id = "thm-nagata-blowup-product-ideal"
kind = "theorem"
title = "[stacks-project]"
order = 244
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.exists_blowup_mul_iso"]
uses = ["def-nagata-blowup-product-comparison", "def-nagata-extended-ideal", "def-nagata-global-blowup", "lemma-nagata-effective-cartier-is-invertible", "prop-nagata-global-blowup-cover-independent"]
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
