+++
kind  = "proof"
of    = "prop-nagata-affine-blowup-restrict"
uses = ["def-nagata-affine-blowup-chart-map", "def-nagata-affine-proj", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-rees-localization-map", "lemma-nagata-localization-ideal-pow", "lemma-nagata-rees-degree-one-element", "lemma-nagata-rees-generators-cover-proj", "lemma-nagata-rees-piece-membership", "prop-nagata-affine-blowup-chart", "prop-nagata-rees-localization"]
+++
Write $R=\mathcal R_A(I)$, $R'=\mathcal R_B(J)$ and
$b\colon\operatorname{Bl}_I(\operatorname{Spec}A)\to\operatorname{Spec}A$,
$b'\colon\operatorname{Bl}_J(\operatorname{Spec}B)\to\operatorname{Spec}B$
for the structure morphisms. Both are induced by the degree-zero maps, and
$\rho_\varphi$ is $\varphi$ in degree zero, so
$b\circ r_\varphi=\operatorname{Spec}(\varphi)\circ b'$. Since
$\operatorname{Spec}\varphi$ is an open immersion onto $D(s)$, it suffices
to show that $r_\varphi$ is an open immersion with image $b^{-1}(D(s))$:
an open immersion onto the preimage of an open subscheme, compatible with
the maps down, exhibits its source as the fibre product.

By [lemma-nagata-rees-generators-cover-proj] the standard opens
$D_+(at)$, $a\in I$, cover $\operatorname{Bl}_I(\operatorname{Spec}A)$,
and by [prop-nagata-affine-blowup-chart] each is the image of the chart
$\chi_{at}$ from $\operatorname{Spec}R_{(at),0}$, over
$\operatorname{Spec}A$. The preimage of $D_+(at)$ under $r_\varphi$ is
$D_+(\varphi(a)t)$, and there $r_\varphi$ is $\operatorname{Spec}$ of the
induced map $R_{(at),0}\to R'_{(\varphi(a)t),0}$. By
[prop-nagata-rees-localization] this map is a localization away from the
image of $s$, so its $\operatorname{Spec}$ is an open immersion onto the
basic open of $s$ in $\operatorname{Spec}R_{(at),0}$, which is the preimage
of $D(s)$ under the chart's map to $\operatorname{Spec}A$. Hence over each
$D_+(at)$ the morphism $r_\varphi$ is an open immersion onto
$b^{-1}(D(s))\cap D_+(at)$. Being an open immersion is local on the
target, so $r_\varphi$ is an open immersion, and its image is the union of
these pieces, namely $b^{-1}(D(s))$.
