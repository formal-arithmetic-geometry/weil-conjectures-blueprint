+++
id = "det-def-sfb-dc-lower-shriek-compatibility"
kind = "lemma"
title = "The lower shriek on $D_{\\mathrm{cons}}$ agrees with the ambient one"
order = 2585
uses = ["det-def-sfb-dc-lower-shriek-definition", "def-sfb-module-derived-lower-shriek-compactification", "def-sfb-dc-open-lower-shriek", "def-sfb-dc-lower-star"]
+++
In the situation of [det-def-sfb-dc-lower-shriek-definition], write
$\iota_X\colon D_{\mathrm{cons}}(X,\Lambda)\hookrightarrow D(\Mod_{\Lambda_X})$ for the fully faithful
inclusions, and let $Rf_!^c=R(p_*)\circ D(i_!)\colon D(\Mod_{\Lambda_X})\to D(\Mod_{\Lambda_Y})$ be
the ambient derived lower shriek attached to $c$
([def-sfb-module-derived-lower-shriek-compactification]). Then there is a natural isomorphism
$$
\iota_Y\circ Rf_!^c\ \cong\ R(p_*)\circ D(i_!)\circ\iota_X
$$
of functors $D_{\mathrm{cons}}(X,\Lambda)\to D(\Mod_{\Lambda_Y})$, namely the pasting of the
isomorphisms $\iota_Z\circ i_!\cong D(i_!)\circ\iota_X$ and $\iota_Y\circ Rp_*\cong R(p_*)\circ\iota_Z$
expressing that the restricted functors commute with the inclusions. In particular, for
$c=c_f$, the derived lower shriek $Rf_!$ on $D_{\mathrm{cons}}$ is the restriction of the ambient
$Rf_!$ of the chosen compactification.
