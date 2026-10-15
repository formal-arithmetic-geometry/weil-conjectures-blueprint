+++
id = "pur9-def-etale-compact-projection"
kind = "definition"
title = "Étale compact-support projection map"
order = 2002
uses = ["pur7710-def-etale-projection", "pur9-def-etale-unbounded-candidate", "sk-thm-sf-comp-composition", "sk-thm-sf-pf-finite"]
+++
Under Input “Unbounded étale derived inverse-image adjunction” (`pur713-input-etale-unbounded-adjunction`), for $K\in D(X_{\Et},\mathcal O_E/\varpi^n)$ and $L\in D(Y_{\Et},\mathcal O_E/\varpi^n)$, let

$$
\operatorname{PF}^{\Et}_{f,K,L}:Rf^{\mathrm{un}}_{!,\Et,\mathcal O_E/\varpi^n}K\otimes^L_{\mathcal O_E/\varpi^n}L\longrightarrow Rf^{\mathrm{un}}_{!,\Et,\mathcal O_E/\varpi^n}\bigl(K\otimes^L_{\mathcal O_E/\varpi^n}Lf^*_{\Et,\mathcal O_E/\varpi^n}L\bigr)
$$

be the composite of $P_{p,\Et,\mathcal O_E/\varpi^n,\mathrm D(j_{!,\Et,\mathcal O_E/\varpi^n})K,L}$ of Definition [pur7710-def-etale-projection], of $Rp_{*,\Et,\mathcal O_E/\varpi^n}$ applied to $(\sigma^{\Et}_{j,K,Lp^*_{\Et,\mathcal O_E/\varpi^n}L})^{-1}$ (Lemma “\'{E}tale open-extension projection isomorphism” (`pur9-lem-etale-open-projection`, in [sk-thm-sf-pf-finite])), and of the composition comparison $Lj^*_{\Et,\mathcal O_E/\varpi^n}Lp^*_{\Et,\mathcal O_E/\varpi^n}\cong Lf^*_{\Et,\mathcal O_E/\varpi^n}$ of Definition “Finite-coefficient étale derived inverse image” (`pur456-pbc-pullback-derived`, in [sk-thm-sf-comp-composition]), all at the coefficient $\mathcal O_E/\varpi^n$, with $Rf^{\mathrm{un}}_{!,\Et,\mathcal O_E/\varpi^n}$ of Definition [pur9-def-etale-unbounded-candidate].
