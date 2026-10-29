+++
id = "def-wf-normalized-real-envelope"
kind = "definition"
title = "Normalized real envelope"
order = 4124
uses = ["def-weil-punctual-weights", "def-wf-constant-weil-twist"]
lean = ["AlgebraicGeometry.WeilSheaf.realEnvelope"]
+++
Let $\mathcal F$ be a Weil sheaf on a $k_0$-scheme and let
$b\in\Qlb^\times$. Put

$$
\mathcal F^0=\mathcal F\otimes\mathcal B_b,
$$

where $\mathcal B_b$ is the constant Weil twist of
[def-wf-constant-weil-twist], and

$$
\operatorname{Env}_\iota(\mathcal F;b)=\mathcal F^0\oplus
\bigl(\mathcal F^0\bigr)^\vee.
$$

This direct sum is the *normalized real envelope* associated with
$b$. It is intended for $\mathcal F$ lisse and punctually $\iota$-pure of
weight $w$ ([def-weil-punctual-weights]) and $|\iota(b)|=q^{-w/2}$. Such
a $b$ exists as soon as $\mathcal F\ne0$ on a nonempty scheme: choose a
closed point $x$, of degree $d$, with nonzero stalk, a Frobenius
eigenvalue $\alpha$ at $x$, and a $d$th root $b\in\Qlb$ of
$\alpha^{-1}$; purity gives $|\iota(b)|=|\iota(\alpha)|^{-1/d}=q^{-w/2}$.
Only the field embedding $\iota$ enters this choice.
