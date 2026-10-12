+++
id = "def-sfb-finite-lower-shriek-to-lower-star"
kind = "definition"
title = "The comparison $f_!\\to f_*$"
order = 1605
uses = ["def-sfb-finite-extension-by-zero-adjunction", "def-sfb-finite-lower-shriek", "def-sfb-finite-lower-star-comp"]
lean = ["AlgebraicGeometry.ProEtale.lowerShriekToLowerStar"]
+++
Let $f\colon X\to Y$ admit a compactification, with chosen compactification
$(X\xrightarrow{i}\bar X\xrightarrow{g}Y)$ as in [def-sfb-finite-lower-shriek]. The
counit $i^*i_*\to\mathrm{id}$ of $i^*\dashv i_*$ is an isomorphism. Let
$i_!\to i_*$ be the composite

$$
i_!F\xrightarrow{\ \sim\ }i_!i^*i_*F\longrightarrow i_*F,
$$

of the inverse of this counit and the counit of $i_!\dashv i^*$
([def-sfb-finite-extension-by-zero-adjunction]). The *comparison* $\iota_f\colon f_!\to f_*$
is

$$
f_!=g_*i_!\longrightarrow g_*i_*\cong(g\circ i)_*=f_*,
$$

using the composition isomorphism of [def-sfb-finite-lower-star-comp].
