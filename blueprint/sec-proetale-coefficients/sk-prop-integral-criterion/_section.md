+++
id = "sk-prop-integral-criterion"
kind = "proposition"
title = "The integral constructibility criterion"
order = 1277
uses = ["sk-def-sfb-constructible", "sk-def-pe-derived-completion", "sk-prop-integral-local-structure", "sk-prop-sf-open-closed-triangle"]
tags = ["sketch"]
+++
For $\Lambda=\cO_E$ torsion is allowed: locally on a stratum, a constructible
$\cO_{E,X}$-module is $P\otimes_{\cO_E}\cO_{E,X}$ for a finitely generated $\cO_E$-module $P$
([sk-def-sfb-constructible]); for example $\cO_{E,X}/\pi_E$ is constructible.

Let $X$ be Noetherian. The following conditions on $K\in D(X_{\mathrm{proét}},\cO_E)$ are
equivalent:

- **(1)** $K\in\Dbc(X,\cO_E)$ ([sk-def-sfb-constructible]);
- **(2)** $K$ is derived complete ([sk-def-pe-derived-completion]) and
  $K_1\in\Dbc(X,\mathbf F_E)$;
- **(3)** there is a finite stratification of $X$ such that on each stratum $S$, pro-étale
  locally, $K|_S\simeq\cO_{E,S}\otimes_{\cO_E}P^\bullet$ for a bounded complex $P^\bullet$ of
  finite free $\cO_E$-modules;
- **(4)** $K\in\Dctf(X,\cO_E)$.

In the classical adic setting, this description of the integral constructible category is
Bhatt–Scholze, Proposition 6.8.11, and \stacks{09C7}.
