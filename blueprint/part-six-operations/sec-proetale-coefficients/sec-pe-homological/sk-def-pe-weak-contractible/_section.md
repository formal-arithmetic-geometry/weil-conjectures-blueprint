+++
id = "sk-def-pe-weak-contractible"
kind = "definition"
title = "Weak contractibility"
order = 53
lean = ["CategoryTheory.GrothendieckTopology.IsWeaklyContractible"]
uses = ["sk-def-pe-site", "sk-def-sfb-finite-pushforward-pullback"]
tags = ["sketch"]
+++
An object $W$ of $X_{\mathrm{pro}\acute{e}t}$ is *weakly contractible* if every
epimorphism of sheaves of sets $F\to h_W$ admits a section, where $h_W$
is the representable sheaf associated to $W$. Equivalently, $h_W$ is
projective in $\Sh(X_{\mathrm{pro}\acute{e}t})$, or every epimorphism $F\to G$ induces a
surjection $F(W)\to G(W)$.
