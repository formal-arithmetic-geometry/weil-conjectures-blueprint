+++
id = "def-sfb-projection-formula"
kind = "definition"
title = "Projection formula"
order = 1545
lean = ["CategoryTheory.Functor.ProjectionFormula"]
+++
Let $S\colon\mathcal D\to\mathcal C$ be a strong monoidal functor between monoidal
categories, with inverse structure maps $\delta_{L,L'}\colon S(L\otimes L')\to SL\otimes SL'$
and $\epsilon\colon S\mathbf 1\to\mathbf 1$. Let $P\colon\mathcal C\to\mathcal D$ be a
functor. A *projection formula* for $P$ relative to $S$ is a family of isomorphisms
$$
\pi_{L,M}\colon P(SL\otimes M)\xrightarrow{\ \sim\ }L\otimes PM
\qquad(L\in\mathcal D,\ M\in\mathcal C),
$$
natural in $L$ and in $M$, and compatible with the unit and the associativity
constraints:
$$
\lambda_{PM}\circ\pi_{\mathbf 1,M}=P\bigl(\lambda_M\circ(\epsilon\otimes M)\bigr),
$$
$$
\alpha_{L,L',PM}\circ\pi_{L\otimes L',M}
=(L\otimes\pi_{L',M})\circ\pi_{L,SL'\otimes M}\circ
P\bigl(\alpha_{SL,SL',M}\circ(\delta_{L,L'}\otimes M)\bigr).
$$
