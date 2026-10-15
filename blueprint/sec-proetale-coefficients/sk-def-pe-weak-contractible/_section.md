+++
id = "sk-def-pe-weak-contractible"
kind = "definition"
title = "Weak contractibility"
order = 713
uses = ["sk-def-pe-site", "sk-def-sfb-finite-pushforward-pullback"]
tags = ["sketch"]
+++
An object $W$ of $X_{\mathrm{proét}}$ is *weakly contractible* if every epimorphism of
sheaves of sets $F\to h_W$ admits a section, where $h_W$ is the representable sheaf
associated to $W$. Equivalently, $h_W$ is projective in $\Sh(X_{\mathrm{proét}})$, or every
epimorphism $F\to G$ induces a surjection $F(W)\to G(W)$.

For the equivalence, pull an epimorphism $F\to G$ back along a section $h_W\to G$; the
resulting epimorphism onto $h_W$ splits. Conversely, surjectivity on sections lifts
$\mathrm{id}_{h_W}$ along any epimorphism onto $h_W$. This is the categorical definition of
Bhatt–Scholze, §3.2. The splitting condition concerns a cover as a whole: a disconnected
$W$ need not lift into a single member of a covering family.
