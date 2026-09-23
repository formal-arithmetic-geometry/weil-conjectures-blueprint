+++
id = "def-weil-pbc-completed-base-change-map"
kind = "definition"
title = "Completed base-change map"
order = 1778
uses = ["def-weil-pbc-completed-pullback"]
+++
Let $K$ be derived complete and let every $K_n$ have a displayed witness
$\epsilon_X^{-1}L_n\simeq K_n$ with
$L_n\in D_c^+(X_{\mathrm{et}},\Lambda/I^n)$. Define

$$
\operatorname{Ex}^{\mathrm{comp}}_{\square,K}:
Lg^*_{\mathrm{comp}}Rf_*K\longrightarrow
Rf'_*L(g')^*_{\mathrm{comp}}K
$$

to be the ordered composite

$$
\begin{aligned}
Lg^*_{\mathrm{comp}}Rf_*K
&\xrightarrow{\sim}R\varprojlim_n Lg^*Rf_*K_n\\
&\xrightarrow{R\varprojlim_n\operatorname{Ex}_{\square,K_n}}
R\varprojlim_nRf'_*L(g')^*K_n\\
&\xrightarrow{\sim}Rf'_*R\varprojlim_nL(g')^*K_n
=Rf'_*L(g')^*_{\mathrm{comp}}K.
\end{aligned}
$$

In the notation above, the first two arrows are $H$ followed by $V'$.
The first isomorphism uses reconstruction and the perfect projection formula;
the second displayed isomorphism is the inverse of direct-image/limit
commutation. This definition fills the map-construction omission in Tag
`09C9`.
