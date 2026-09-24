+++
id = "lem-trf-contracting-local-model"
kind = "lemma"
title = "Contracting local model at an isolated fixed point"
order = 3913
uses = ["def-trf-trace-class", "def-weil-pbc-strict-henselization-limit", "lem-trf-frobenius-formal-contraction", "lem-trf-local-term-locality"]
+++
Let $c$ be an admissible correspondence on $X$ with an isolated
fixed point $y\in\operatorname{Fix}(c)(k)$ at which the two legs of
$c$ agree modulo the square of the maximal ideal, as in
[lem-trf-frobenius-formal-contraction]. Then the trace class of
[def-trf-trace-class] restricted to the open-and-closed component
$\{y\}$ of the fixed scheme depends only on the formal neighbourhood
of $y$ and on the stalk $K_{\bar y}$; after base change to the
strict henselization
$\Spec(\mathcal O^{\mathrm{sh}}_{X,y})$ of
[def-weil-pbc-strict-henselization-limit] the correspondence is,
on that neighbourhood, the graph correspondence of an endomorphism
$g$ of the local scheme with $g(y)=y$ and vanishing differential
$dg_y=0$, and the coefficient map corresponds to an endomorphism
$u_{\bar y}$ of the stalk $K_{\bar y}$.

## Proof

The first assertion is [lem-trf-local-term-locality]. For the
second, the congruence of the two legs modulo $\mathfrak m_y^2$ shows
that $c_1$ is etale at $y$ (its differential is an isomorphism,
hence it is unramified and flat there), so on a neighbourhood of $y$
the composite $g=c_2c_1^{-1}$ is a well-defined endomorphism with
$g(y)=y$; the same congruence gives $dg_y=\mathrm{id}-\mathrm{id}=0$.
Base changing along the strict henselization, which is a filtered
colimit of pointed etale neighbourhoods
([def-weil-pbc-strict-henselization-limit]), replaces $c$ by its
graph and the coefficient map by an endomorphism of the stalk, the
trace class being computed there by the compatibility of the trace
construction with etale base change ([def-trf-trace-class]).
