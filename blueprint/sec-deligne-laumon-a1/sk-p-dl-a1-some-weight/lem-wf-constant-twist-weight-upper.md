+++
id = "lem-wf-constant-twist-weight-upper"
kind = "lemma"
title = "Shift of upper weight bounds under a constant twist"
order = 2970
uses = ["def-weil-punctual-weights", "def-wf-constant-weil-twist", "lem-tw-multiplicativity", "lem-wf-constant-twist-weight"]
+++
If $\mathcal F$ is lisse and punctually $\iota$-mixed of weights at
most $w$, and $2\log_q|\iota(b)|=c$, then the constant twist
$\mathcal F\otimes\mathcal B_b$ of [def-wf-constant-weil-twist]
is punctually $\iota$-mixed of weights at most $w+c$ in the sense of
[def-weil-punctual-weights].

## Proof

By the punctual mixedness of $\mathcal F$ in the sense of
[def-weil-punctual-weights] there are constructible
$\Qlb$-Weil subsheaves
$0=\mathcal F_0\subset\mathcal F_1\subset\cdots\subset\mathcal F_m =\mathcal F$ with each quotient
$\mathcal F_r/\mathcal F_{r-1}$ punctually $\iota$-pure of a weight
$w_r\leq w$. Tensoring by the constant twist
$\mathcal B_b$ of [def-wf-constant-weil-twist] is exact on the
coefficient category, so it carries this chain to a chain of
$\Qlb$-Weil subsheaves of $\mathcal F\otimes\mathcal B_b$ with
quotients $(\mathcal F_r/\mathcal F_{r-1})\otimes\mathcal B_b$; by
[lem-wf-constant-twist-weight] each of those quotients is
punctually $\iota$-pure of weight $w_r+c$, the sum of the weight
$w_r$ of the quotient and the weight $c$ of the twist by
[lem-tw-multiplicativity], and $w_r+c\leq w+c$. Such a chain is
exactly a punctual mixedness of weights at most $w+c$ in the sense of
[def-weil-punctual-weights].
