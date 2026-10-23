+++
kind = "proof"
of = "lem-weil-pbc-modulecat-upperstar-free-yoneda"
uses = ["def-weil-pbc-inverse-image"]
+++
Let $F$ be a sheaf of $\Lambda$-modules on $Y_{\Et}$. The adjunction $g^{-1}\dashv g_*$ [def-weil-pbc-inverse-image], followed by the free-module Yoneda isomorphism $\operatorname{Hom}(\Lambda[W],G)\cong G(W)$ (a map out of $\Lambda[W]$ is determined by the image of the section $\mathrm{id}_W$), identifies $\operatorname{Hom}(g^{-1}\Lambda[W],F)$ with $\operatorname{Hom}(\Lambda[W],g_*F)\cong(g_*F)(W)$. By the definition of the direct image this is $F(W\times_XY)$, which by the free-module Yoneda isomorphism again is $\operatorname{Hom}(\Lambda[W\times_XY],F)$. Each of these bijections is natural in $F$, so by the Yoneda lemma they are induced by an isomorphism $g^{-1}\Lambda[W]\cong\Lambda[W\times_XY]$.
