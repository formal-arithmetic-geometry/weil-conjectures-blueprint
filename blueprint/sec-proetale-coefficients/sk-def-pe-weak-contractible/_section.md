+++
id = "sk-def-pe-weak-contractible"
kind = "definition"
title = "Weak contractibility"
order = 966
lean = ["CategoryTheory.GrothendieckTopology.IsWeaklyContractible"]
uses = ["sk-def-pe-site", "sk-def-sfb-finite-pushforward-pullback"]
tags = ["sketch"]
+++
An object $W$ of $X_{\mathrm{proét}}$ is *weakly contractible* if every epimorphism of
sheaves of sets $F\to h_W$ admits a section, where $h_W$ is the representable sheaf
associated to $W$. Equivalently, $h_W$ is projective in $\Sh(X_{\mathrm{proét}})$, or every
epimorphism $F\to G$ induces a surjection $F(W)\to G(W)$.

To see the equivalence, pull an epimorphism $F\to G$ back along a section $h_W\to G$. The
resulting epimorphism onto $h_W$ splits. Conversely, if every epimorphism is surjective on
sections, then $\mathrm{id}_{h_W}$ lifts along any epimorphism onto $h_W$. This is the
categorical definition of Bhatt–Scholze, §3.2. Note that the splitting condition concerns a
cover as a whole. For example, if $W$ is disconnected, then a lift of $\mathrm{id}_{h_W}$
along a covering family may use different members of the family on different clopen pieces
of $W$.
