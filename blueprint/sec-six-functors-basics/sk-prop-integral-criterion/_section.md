+++
id = "sk-prop-integral-criterion"
kind = "proposition"
title = "The integral constructibility criterion"
order = 1551
uses = ["sk-def-sfb-constructible", "sk-prop-sfb-qlbar-colimit-x", "sk-def-pe-derived-completion"]
tags = ["sketch"]
+++
For $\Lambda=\cO_E$ torsion is allowed: locally on a stratum, a constructible
$\cO_{E,X}$-module is $P\otimes_{\cO_E}\cO_{E,X}$ for a finitely generated $\cO_E$-module $P$
([sk-def-sfb-constructible]); for example $\cO_{E,X}/\pi_E$ is constructible. In most proofs
it is more convenient to use the following criterion.

For $X$ Noetherian and $E/\mathbf Q_\ell$ finite, a complex
$K\in D(X_{\mathrm{proét}},\cO_E)$ lies in $\Dbc(X,\cO_E)$ if and only if it is derived
$\pi_E$-complete ([sk-def-pe-derived-completion]) and
$$
K\otimes^{\mathbf L}_{\cO_{E,X}}(\cO_E/\pi_E)_X
$$
belongs to $\Dbc(X,\cO_E/\pi_E)$ on $X_{\mathrm{proét}}$.
