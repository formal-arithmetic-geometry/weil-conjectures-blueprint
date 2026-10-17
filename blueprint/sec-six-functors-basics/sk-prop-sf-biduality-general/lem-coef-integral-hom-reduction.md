+++
id = "lem-coef-integral-hom-reduction"
kind = "lemma"
title = "Integral internal Hom and reduction"
lean = ["AlgebraicGeometry.Etale.nonempty_iso_reductionModIdeal_derivedHom", "AlgebraicGeometry.Etale.derivedComplete_derivedHom"]
order = 2478
uses = ["sk-def-sfb-pulled-back-coefficients", "sk-def-sfb-derived-tensor-hom", "sk-def-pe-derived-completion"]
+++
Let $E/\Ql$ be finite with uniformizer $\pi=\pi_E$, let
$R_X=\mathcal O_{E,X}=p_X^*\underline{\mathcal O}_E$ and
$A_n=(\mathcal O_E/\pi^n)_X$ be the pulled-back coefficient sheaves
([sk-def-sfb-pulled-back-coefficients]), and write
$K_n=K\otimes^L_RA_n$. For arbitrary complexes $K,L$ in
$D(X_{\mathrm{proét}},\mathcal O_E)$,
the canonical evaluation-defined comparison is an isomorphism

$$
R\mathcal Hom_R(K,L)\otimes_R^L A_n
\xrightarrow{\sim}R\mathcal Hom_{A_n}(K_n,L_n).
$$

It preserves evaluation and its transposes. If $L$ is derived
complete ([sk-def-pe-derived-completion]), then $R\mathcal Hom_R(K,L)$ is
derived complete.
No site-perfectness assumption on $K$ is imposed.
