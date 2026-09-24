+++
id = "lem-tw-dual-negation"
kind = "lemma"
title = "Weight of the linear dual"
order = 4060
uses = ["def-weil-punctual-weights", "def-weil-weil-sheaf-complex", "lem-tw-multiplicativity"]
+++
In the setting of [def-weil-punctual-weights], if a lisse
Weil sheaf $\mathcal F$ is
punctually $\iota$-pure of weight $w$, then its linear dual
$\mathcal F^\vee$ is punctually $\iota$-pure of weight $-w$.

## Proof

The Frobenius eigenvalues on the dual stalk at a closed point $y$ are
the inverses of the eigenvalues of $F_y$ on $\mathcal F_{\bar y}$
(the dual representation), so the complex moduli are
$q_y^{-w/2}$ by [lem-tw-multiplicativity], which is weight $-w$
in [def-weil-punctual-weights].
