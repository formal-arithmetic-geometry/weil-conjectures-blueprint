+++
id = "sk-lem-integral-finite-levels"
kind = "lemma"
title = "Bounds for the finite reductions"
order = 1210
uses = ["sk-def-pe-derived-completion", "sk-thm-pe-constructible-comparison", "sk-cor-pe-finite-tor-comparison", "sk-prop-pe-milnor"]
tags = ["sketch"]
+++
Constructibility over $\cO_E$ is defined by local models, but in practice we know a complex
$K\in D(X_{\mathrm{proét}},\cO_E)$ through its reductions
$K_n=K\otimes^{\mathbf L}_{\cO_{E,X}}(\cO_E/\pi_E^n)_X$ of [sk-def-pe-derived-completion]. The
criterion below says that $K$ is constructible exactly when it is derived complete and $K_1$
is constructible. Write $\mathbf F_E=\cO_E/\pi_E$ for the residue field, so that
$K_1\in D(X_{\mathrm{proét}},\mathbf F_E)$.

To prove the criterion we must produce, on each stratum, one complex of finite free
$\cO_E$-modules that is locally a model for all the $K_n$ at once. Each $K_n$ separately is
easy to control: its bounds and its stratification are inherited from $K_1$ by dévissage along
the powers of $\pi_E$, and on a stratum it is locally isomorphic to a constant perfect complex.
The difficulty is that these local isomorphisms are chosen independently at each level, and
they have to be made compatible before we pass to the limit. On a weakly contractible cover
this is a Mittag–Leffler argument, and the uniform rate it needs comes from the fact that a
bounded complex of finite free modules over the discrete valuation ring $\cO_E$ has finitely
generated cohomology, whose torsion is killed by a fixed power of $\pi_E$. We use the étale
site only at the finite levels, through [sk-thm-pe-constructible-comparison].

Let $X$ be Noetherian and let $K\in D(X_{\mathrm{proét}},\cO_E)$ be derived complete with
$K_1\in\Dbc(X,\mathbf F_E)$. Choose $[a,b]$ containing the cohomology of $K_1$. Then every
$K_n$ lies in $\Dbc(X,\cO_E/\pi_E^n)$ and has Tor amplitude in $[a,b]$, and $K$ has cohomology
only in $[a,b]$. If the cohomology sheaves of $K_1$ are locally constant on a stratum, then so
are those of every $K_n$.
