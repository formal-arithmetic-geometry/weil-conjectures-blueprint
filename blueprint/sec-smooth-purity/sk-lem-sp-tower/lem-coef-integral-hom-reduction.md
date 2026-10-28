+++
id = "lem-coef-integral-hom-reduction"
kind = "lemma"
title = "Integral internal Hom and reduction"
order = 2975
uses = ["det-def-sfb-pulled-back-coefficients", "det-def-sfb-derived-tensor-hom", "def-pe-derived-complete"]
+++
Let $E/\Ql$ be finite with uniformizer $\pi=\pi_E$, let
$R_X=\mathcal O_{E,X}=p_X^*\underline{\mathcal O}_E$ and
$A_n=(\mathcal O_E/\pi^n)_X$ be the pulled-back coefficient sheaves
([det-def-sfb-pulled-back-coefficients]), and write
$K_n=K\otimes^L_RA_n$. For arbitrary complexes $K,L$ in
$D(X_{\mathrm{proét}},\mathcal O_E)$,
the canonical evaluation-defined comparison is an isomorphism

$$
R\mathcal Hom_R(K,L)\otimes_R^L A_n
\xrightarrow{\sim}R\mathcal Hom_{A_n}(K_n,L_n).
$$

It preserves evaluation and its transposes. If $L$ is derived
complete ([def-pe-derived-complete]), then $R\mathcal Hom_R(K,L)$ is
derived complete.
No site-perfectness assumption on $K$ is imposed.
