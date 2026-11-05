+++
kind = "proof"
of = "lemma-triviality-fibres--1"
order = 1478003
uses = ["lemma-schematic-closure-uniqueness--1", "lemma-uniqueness-maps-dense-open--1", "theorem-chow-s-lemma-projective-form--2"]
+++
The proof uses only that $P_t$ is proper and integral with
$H^0(P_t,\mathcal O_{P_t})=\kappa(t)$, which holds by [Stacks, [0BUG](https://stacks.math.columbia.edu/tag/0BUG)]
because $P$ is proper and geometrically integral.

For (1), a trivial sheaf and its inverse both have the nonzero section
$1$, so only the converse needs an argument. On $\mathbf P^1$, for
instance, $\mathcal O(d)$ and $\mathcal O(-d)$ both have nonzero
sections only when $d=0$. Let $s$ and $s'$ be nonzero
sections of $\mathcal L_t$ and $\mathcal L_t^{-1}$. Since $P_t$ is
integral, the product $ss'$ is a nonzero element of
$H^0(P_t,\mathcal O)=\kappa(t)$, hence a unit. Since $ss'$ would
vanish wherever $s$ does, the section $s$ vanishes nowhere, and it
trivializes $\mathcal L_t$.

*Source:* the proof of Lemma [lemma-triviality-fibres].
