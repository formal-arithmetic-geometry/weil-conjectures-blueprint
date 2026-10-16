+++
id = "lem-coef-integral-hom-reduction"
kind = "lemma"
title = "Integral internal Hom and reduction"
lean = ["AlgebraicGeometry.Etale.nonempty_iso_reductionModIdeal_derivedHom", "AlgebraicGeometry.Etale.derivedComplete_derivedHom"]
order = 2478
uses = ["def-weil-completed-integral-coefficients", "def-weil-derived-complete", "def-weil-derived-pullback-tensor-hom"]
+++
For arbitrary ambient complexes $K,L$ of $R_X$-modules,
the canonical evaluation-defined comparison is an isomorphism

$$
R\mathcal Hom_R(K,L)\otimes_R^L A_n
\xrightarrow{\sim}R\mathcal Hom_{A_n}(K_n,L_n).
$$

It preserves evaluation and its transposes. If $L$ is derived
complete, then $R\mathcal Hom_R(K,L)$ is derived complete.
No site-perfectness assumption on $K$ is imposed.
