+++
id = "pur713-def-shriek-projection"
kind = "definition"
title = "Compact-support projection transformation, finite coefficients"
order = 3057
uses = ["pur713-def-star-projection", "sk-def-sf-exchanges", "det-def-sf-operations"]
+++
Assume Inputs “Fixed-coefficient inverse image preserves K-flat complexes” (`pur713-input-kflat-fixed`) and “Open-extension projection formula for sheaves of $\mathcal O_E/\pi_E^n$-modules” (`pur713-input-open-projection-finite`, in [det-def-sf-operations]). For $f$ with chosen compactification $c_f=(j,p)$, $K\in D(X_{\Proet},\mathcal O_E/\pi_E^n)$ and $L\in D(Y_{\Proet},\mathcal O_E/\pi_E^n)$, define

$$
\operatorname{PF}_{f,K,L,\mathcal O_E/\pi_E^n}:
Rf_{!,\mathcal O_E/\pi_E^n}K\otimes^L_{\mathcal O_E/\pi_E^n}L
\longrightarrow Rf_{!,\mathcal O_E/\pi_E^n}\bigl(K\otimes^L_{\mathcal O_E/\pi_E^n}Lf^*_{\mathcal O_E/\pi_E^n}L\bigr)
$$

in $D(Y_{\Proet},\mathcal O_E/\pi_E^n)$ as the composite

$$
\begin{aligned}
Rp_{*,\mathcal O_E/\pi_E^n}\mathrm D(j_{!,\mathcal O_E/\pi_E^n})K\otimes^L_{\mathcal O_E/\pi_E^n}L
&\xrightarrow{P_{p,\mathrm D(j_{!,\mathcal O_E/\pi_E^n})K,L,\mathcal O_E/\pi_E^n}}
Rp_{*,\mathcal O_E/\pi_E^n}\bigl(\mathrm D(j_{!,\mathcal O_E/\pi_E^n})K\otimes^L_{\mathcal O_E/\pi_E^n}Lp^*_{\mathcal O_E/\pi_E^n}L\bigr)\\
&\xrightarrow{Rp_{*,\mathcal O_E/\pi_E^n}(\sigma^{-1}_{j,K,Lp^*_{\mathcal O_E/\pi_E^n}L,\mathcal O_E/\pi_E^n})}
Rp_{*,\mathcal O_E/\pi_E^n}\mathrm D(j_{!,\mathcal O_E/\pi_E^n})
\bigl(K\otimes^L_{\mathcal O_E/\pi_E^n}\mathrm D(j^*_{\mathcal O_E/\pi_E^n})Lp^*_{\mathcal O_E/\pi_E^n}L\bigr)\\
&\xrightarrow{\sim} Rf_{!,\mathcal O_E/\pi_E^n}\bigl(K\otimes^L_{\mathcal O_E/\pi_E^n}Lf^*_{\mathcal O_E/\pi_E^n}L\bigr).
\end{aligned}
$$

Here $P$ is Definition [pur713-def-star-projection], $\sigma^{-1}$ is the inverse of the isomorphism of Lemma “Finite-coefficient open-extension projection isomorphism” (`pur713-lem-open-projection`, in [sk-def-sf-exchanges]), and the final arrow is induced by $\mathrm D(j^*_{\mathcal O_E/\pi_E^n})Lp^*_{\mathcal O_E/\pi_E^n}\cong Lj^*_{\mathcal O_E/\pi_E^n}Lp^*_{\mathcal O_E/\pi_E^n}\xrightarrow{\mu_{p,j,\mathcal O_E/\pi_E^n}}Lf^*_{\mathcal O_E/\pi_E^n}$, from Lemma “The finite-coefficient derived inverse image is levelwise” (`pur713-lem-finite-pull-levelwise`) and Definition “Composition comparison for finite-coefficient derived inverse image” (`pur713-def-pull-composition`). The direction of $\sigma^{-1}$ is part of the definition; no inverse of the proper projection transformation is used. The same composite with an arbitrary compactification $d=(j,p)$ of $f$ in place of $c_f$ defines $\operatorname{PF}_{d,K,L,\mathcal O_E/\pi_E^n}:R_dK\otimes^L_{\mathcal O_E/\pi_E^n}L\to R_d(K\otimes^L_{\mathcal O_E/\pi_E^n}Lf^*_{\mathcal O_E/\pi_E^n}L)$; thus $\operatorname{PF}_f=\operatorname{PF}_{c_f}$.
