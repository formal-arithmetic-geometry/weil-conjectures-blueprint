+++
id = "pur713-def-shriek-projection"
kind = "definition"
title = "Compact-support projection transformation, finite coefficients"
order = 1982
uses = ["pur713-def-star-projection", "sk-def-sf-exchanges", "sk-def-sf-operations"]
+++
Assume Inputs “Fixed-coefficient inverse image preserves K-flat complexes” (`pur713-input-kflat-fixed`) and “Open-extension projection formula for sheaves of $\mathcal O_E/\varpi^n$-modules” (`pur713-input-open-projection-finite`, in [sk-def-sf-operations]). For $f$ with chosen compactification $c_f=(j,p)$, $K\in D(X_{\Proet},\mathcal O_E/\varpi^n)$ and $L\in D(Y_{\Proet},\mathcal O_E/\varpi^n)$, define

$$
\operatorname{PF}_{f,K,L,\mathcal O_E/\varpi^n}:
Rf_{!,\mathcal O_E/\varpi^n}K\otimes^L_{\mathcal O_E/\varpi^n}L
\longrightarrow Rf_{!,\mathcal O_E/\varpi^n}\bigl(K\otimes^L_{\mathcal O_E/\varpi^n}Lf^*_{\mathcal O_E/\varpi^n}L\bigr)
$$

in $D(Y_{\Proet},\mathcal O_E/\varpi^n)$ as the composite

$$
\begin{aligned}
Rp_{*,\mathcal O_E/\varpi^n}\mathrm D(j_{!,\mathcal O_E/\varpi^n})K\otimes^L_{\mathcal O_E/\varpi^n}L
&\xrightarrow{P_{p,\mathrm D(j_{!,\mathcal O_E/\varpi^n})K,L,\mathcal O_E/\varpi^n}}
Rp_{*,\mathcal O_E/\varpi^n}\bigl(\mathrm D(j_{!,\mathcal O_E/\varpi^n})K\otimes^L_{\mathcal O_E/\varpi^n}Lp^*_{\mathcal O_E/\varpi^n}L\bigr)\\
&\xrightarrow{Rp_{*,\mathcal O_E/\varpi^n}(\sigma^{-1}_{j,K,Lp^*_{\mathcal O_E/\varpi^n}L,\mathcal O_E/\varpi^n})}
Rp_{*,\mathcal O_E/\varpi^n}\mathrm D(j_{!,\mathcal O_E/\varpi^n})
\bigl(K\otimes^L_{\mathcal O_E/\varpi^n}\mathrm D(j^*_{\mathcal O_E/\varpi^n})Lp^*_{\mathcal O_E/\varpi^n}L\bigr)\\
&\xrightarrow{\sim} Rf_{!,\mathcal O_E/\varpi^n}\bigl(K\otimes^L_{\mathcal O_E/\varpi^n}Lf^*_{\mathcal O_E/\varpi^n}L\bigr).
\end{aligned}
$$

Here $P$ is Definition [pur713-def-star-projection], $\sigma^{-1}$ is the inverse of the isomorphism of Lemma “Finite-coefficient open-extension projection isomorphism” (`pur713-lem-open-projection`, in [sk-def-sf-exchanges]), and the final arrow is induced by $\mathrm D(j^*_{\mathcal O_E/\varpi^n})Lp^*_{\mathcal O_E/\varpi^n}\cong Lj^*_{\mathcal O_E/\varpi^n}Lp^*_{\mathcal O_E/\varpi^n}\xrightarrow{\mu_{p,j,\mathcal O_E/\varpi^n}}Lf^*_{\mathcal O_E/\varpi^n}$, from Lemma “The finite-coefficient derived inverse image is levelwise” (`pur713-lem-finite-pull-levelwise`) and Definition “Composition comparison for finite-coefficient derived inverse image” (`pur713-def-pull-composition`). The direction of $\sigma^{-1}$ is part of the definition; no inverse of the proper projection transformation is used. The same composite with an arbitrary compactification $d=(j,p)$ of $f$ in place of $c_f$ defines $\operatorname{PF}_{d,K,L,\mathcal O_E/\varpi^n}:R_dK\otimes^L_{\mathcal O_E/\varpi^n}L\to R_d(K\otimes^L_{\mathcal O_E/\varpi^n}Lf^*_{\mathcal O_E/\varpi^n}L)$; thus $\operatorname{PF}_f=\operatorname{PF}_{c_f}$.
