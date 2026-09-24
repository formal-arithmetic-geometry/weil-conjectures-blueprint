+++
id = "prop-weil-pbc-p1-strict-henselian-comparison"
kind = "theorem"
title = "Strictly henselian $\\mathbf P^1$ comparison"
order = 1619
tags = ["latex:proposition"]
uses = ["def-weil-pbc-strict-henselian-setup", "lemma-weil-pbc-etale-degree-zero", "lemma-weil-pbc-p1-injective-acyclic"]
+++
For every torsion sheaf $F$ on $X$, restriction induces isomorphisms

$$
H^q(X,F)\xrightarrow{\sim}H^q(X_0,F_0)\qquad(q\geq0).
$$

## Proof

Choose an injective resolution $F\to I^\bullet$. Exactness of inverse
image along the closed immersion gives an exact complex $F_0\to I_0^\bullet$.
The preceding lemma makes each $I_0^r$ acyclic, so Leray's acyclicity lemma
identifies $R\Gamma(X_0,F_0)$ with $\Gamma(X_0,I_0^\bullet)$. Degree-zero
restriction identifies this complex with $\Gamma(X,I^\bullet)$ term by term.
Taking cohomology gives the displayed isomorphisms, and naturality follows
from the naturality of the restriction map and of injective resolutions. The
source locators are Tags `0A0C` and `0A3S`.
