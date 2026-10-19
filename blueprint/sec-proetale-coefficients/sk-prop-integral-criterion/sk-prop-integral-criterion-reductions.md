+++
id = "det-prop-integral-criterion-reductions"
kind = "lemma"
title = "Constructibility of all reductions from the first one"
uses = ["sk-def-pe-derived-completion"]
+++
Let $X$ be Noetherian, $E/\mathbf Q_\ell$ finite and $K\in D(X_{\mathrm{proét}},\cO_E)$ derived
$\pi_E$-complete. Write $K_n=K\otimes^{\mathbf L}_{\cO_{E,X}}(\cO_E/\pi_E^n)_X$. The
following are equivalent:

1. $K_1\in\Dbc(X,\cO_E/\pi_E)$;
2. $K_n\in\Dbc(X,\cO_E/\pi_E^n)$ for every $n\ge1$, and the cohomology of the $K_n$ lies in
   one interval $[r,s]$ independent of $n$.

Combined with [sk-prop-integral-criterion], a derived $\pi_E$-complete $K$ lies in
$\Dbc(X,\cO_E)$ if and only if (2) holds.
