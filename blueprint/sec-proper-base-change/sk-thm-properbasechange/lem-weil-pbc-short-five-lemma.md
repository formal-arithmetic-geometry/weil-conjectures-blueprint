+++
id = "lem-weil-pbc-short-five-lemma"
kind = "lemma"
title = "Short five lemma in an abelian category"
lean = ["CategoryTheory.ShortComplex.isIso₂_of_shortExact_of_isIso₁₃"]
order = 2000
tags = ["mathlib", "stacks-05QB"]
+++
Let $\mathcal A$ be an abelian category and consider a commutative diagram in $\mathcal A$

$$
\begin{array}{ccccccccc}
0&\to& X_1&\xrightarrow{i}& X_2&\xrightarrow{\pi}& X_3&\to&0\\
&&\downarrow{\scriptstyle\alpha}&&\downarrow{\scriptstyle\beta}&&\downarrow{\scriptstyle\gamma}&&\\
0&\to& Y_1&\xrightarrow{i'}& Y_2&\xrightarrow{\pi'}& Y_3&\to&0
\end{array}
$$

whose rows are short exact sequences ($i$, $i'$ monomorphisms, $\pi$, $\pi'$ epimorphisms, exact in the middle). If $\alpha$ and $\gamma$ are isomorphisms, then $\beta$ is an isomorphism.
