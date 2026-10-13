+++
id = "pur713-def-shriek-projection-module"
kind = "definition"
title = "Compact-support projection transformation, module objects"
order = 1883
tags = ["latex:bpdefinition"]
uses = ["pur713-def-star-projection-module", "pur713-lem-open-projection-module", "pur713-lem-open-pull-levelwise", "pur713-lem-pull-composition-module"]
+++
Under the inputs of Definition [pur713-def-star-projection-module] and Lemma [pur713-lem-open-projection-module], for $f$ with chosen compactification $c_f=(j,p)$, $T\in\{\mathcal O_E,E,\overline{\mathbf Q}_\ell\}$, $K\in D(X_{\Proet},T)$ and $L\in D(Y_{\Proet},T)$, define

$$
\operatorname{PF}_{f,K,L,T}:
Rf_{!,T}K\otimes^L_{\mathcal R_{Y,T}}L
\longrightarrow Rf_{!,T}\bigl(K\otimes^L_{\mathcal R_{X,T}}Lf^*_TL\bigr)
$$

in $D(Y_{\Proet},T)$ as the composite

$$
\begin{aligned}
Rp_{*,T}\mathrm D(j_{!,T})K\otimes^L_{\mathcal R_{Y,T}}L
&\xrightarrow{P_{p,\mathrm D(j_{!,T})K,L,T}}
Rp_{*,T}\bigl(\mathrm D(j_{!,T})K\otimes^L_{\mathcal R_{\overline X,T}}Lp^*_TL\bigr)\\
&\xrightarrow{Rp_{*,T}(\sigma^{-1}_{j,K,Lp^*_TL,T})}
Rp_{*,T}\mathrm D(j_{!,T})
\bigl(K\otimes^L_{\mathcal R_{X,T}}\mathrm D(j^*_T)Lp^*_TL\bigr)\\
&\xrightarrow{\sim} Rf_{!,T}\bigl(K\otimes^L_{\mathcal R_{X,T}}Lf^*_TL\bigr),
\end{aligned}
$$

with $P$ of Definition [pur713-def-star-projection-module], $\sigma^{-1}$ the inverse of the isomorphism of Lemma [pur713-lem-open-projection-module], and the final arrow induced by $\mathrm D(j^*_T)Lp^*_T\cong Lj^*_TLp^*_T\xrightarrow{\mu_{p,j,T}}Lf^*_T$, from Lemmas [pur713-lem-open-pull-levelwise] and [pur713-lem-pull-composition-module]. With an arbitrary compactification $d$ in place of $c_f$, the same composite defines $\operatorname{PF}_{d,K,L,T}$, and $\operatorname{PF}_f=\operatorname{PF}_{c_f}$.
