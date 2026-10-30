+++
id = "lem-wf-compact-character-logarithm"
kind = "lemma"
title = "A multiplicative curve character produces an invariant additive character"
lean = ["AlgebraicGeometry.WeilGroup.exists_smallLog_pow_hom", "PadicAlgCl.exists_smallLog_pow_hom"]
order = 4017
uses = ["def-wf-weil-group", "lem-wf-deep-principal-unit-log", "lem-wf-weil-group-exact-sequence"]
+++
Let $U_0/k_0$ be as in
[def-wf-weil-group], put
$\Pi=\pi_1(U_0\times_{k_0}\overline{k}_0,\bar u)$, and let
$\chi:W(U_0,\bar u)\to E^\times$
be continuous, where $E/\mathbf Q_\ell$ is finite. Choose
$s\in W(U_0,\bar u)$ with $\deg(s)=1$. There are integers
$N,r\geq1$ for which

$$
\lambda:\Pi\longrightarrow E,
\qquad
\lambda(g)=\log(\chi(g)^N),
$$

is a continuous additive character and satisfies

$$
\lambda(sgs^{-1})=\lambda(g)=\lambda(s^{-1}gs)
\qquad(g\in\Pi).
$$
