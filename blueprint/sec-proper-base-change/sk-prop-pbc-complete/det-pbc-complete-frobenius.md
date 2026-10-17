+++
id = "det-pbc-complete-frobenius"
kind = "lemma"
title = "Frobenius equivariance of the completed exchange map"
order = 1403
uses = ["det-pbc-complete-exchange-map", "det-pbc-complete-tower-calculus", "lemma-weil-pbc-completed-pullback-reduction", "prop-weil-pbc-direct-image-limits", "lem-weil-derived-direct-image-composition", "sk-lem-pbc-exchange-pasting"]
+++
In the cartesian square of [det-pbc-complete-exchange-map], let
$\operatorname{Fr}_X,\operatorname{Fr}_Y,\operatorname{Fr}_{X'},\operatorname{Fr}_{Y'}$ be
automorphisms of the four schemes (for instance the geometric Frobenius
automorphisms of a square defined over $k_0$) such that

$$
p\operatorname{Fr}_X=\operatorname{Fr}_Yp,\qquad
g\operatorname{Fr}_{Y'}=\operatorname{Fr}_Yg,\qquad
g'\operatorname{Fr}_{X'}=\operatorname{Fr}_Xg',\qquad
p'\operatorname{Fr}_{X'}=\operatorname{Fr}_{Y'}p',
$$

and put $\Phi_Z=\operatorname{Fr}_Z^*$ on $D(Z_{\mathrm{proét}},\mathcal O_E)$.

1. There are canonical isomorphisms
   $\Phi_{Y'}g^*_{\mathrm{comp}}Rp_*\simeq g^*_{\mathrm{comp}}Rp_*\Phi_X$ and
   $\Phi_{Y'}Rp'_*g'^*_{\mathrm{comp}}\simeq Rp'_*g'^*_{\mathrm{comp}}\Phi_X$, under which
   $\Phi_{Y'}(\operatorname{Ex}^{\mathrm{comp}}_K)=\operatorname{Ex}^{\mathrm{comp}}_{\Phi_XK}$
   for every $K\in D(X_{\mathrm{proét}},\mathcal O_E)$.
2. Let $\theta\colon\Phi_XK\xrightarrow{\sim}K$ be a Weil structure on $K$, and let
   $\theta_S$ on $S=g^*_{\mathrm{comp}}Rp_*K$ and $\theta_T$ on
   $T=Rp'_*g'^*_{\mathrm{comp}}K$ be the induced Weil structures, i.e. the
   isomorphisms of (1) followed by $g^*_{\mathrm{comp}}Rp_*\theta$, resp.
   $Rp'_*g'^*_{\mathrm{comp}}\theta$. Then
   $$
   \operatorname{Ex}^{\mathrm{comp}}_K\circ\theta_S
   =\theta_T\circ\Phi_{Y'}\bigl(\operatorname{Ex}^{\mathrm{comp}}_K\bigr)
   \colon\Phi_{Y'}S\longrightarrow T,
   $$
   so $\operatorname{Ex}^{\mathrm{comp}}_K$ is a morphism of Weil complexes. Under the
   hypotheses of [det-pbc-complete-exchange-iso] it is an isomorphism of Weil
   complexes.
