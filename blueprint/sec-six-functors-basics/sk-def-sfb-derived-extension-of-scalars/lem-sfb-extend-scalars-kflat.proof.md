+++
kind  = "proof"
of    = "lem-sfb-extend-scalars-kflat"
uses = ["sk-prop-sfb-module-category"]
+++
The cone $C$ of $s$ is acyclic and K-flat, and the cone of $\mathcal S\otimes_{\mathcal R}s$
is $\mathcal S\otimes_{\mathcal R}C$. Restriction of scalars is exact and faithful on
underlying objects [sk-def-sfb-change-of-scalars], so it detects acyclicity. Hence it
suffices to show that $\mathcal S\otimes_{\mathcal R}C$, with $\mathcal S$ regarded as an
$\mathcal R$-module through $\varphi$, is acyclic. Choose a K-flat resolution
$Q\to\mathcal S$ of $\mathcal S$ as an $\mathcal R$-module [sk-prop-sfb-module-category].
Since $C$ is K-flat, $Q\otimes_{\mathcal R}C\to\mathcal S\otimes_{\mathcal R}C$ is a
quasi-isomorphism. Since $Q$ is K-flat and $C$ is acyclic, i.e. $0\to C$ is a
quasi-isomorphism, $Q\otimes_{\mathcal R}C$ is acyclic. Hence
$\mathcal S\otimes_{\mathcal R}C$ is acyclic.
