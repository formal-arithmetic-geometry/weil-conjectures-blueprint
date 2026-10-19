+++
id = "thm-sf-pf-adic"
kind = "theorem"
title = "Projection formula over $\\mathcal O_E$"
order = 2440
uses = ["def-sf-datum", "def-sf-pf", "sk-def-pe-derived-completion", "sk-prop-integral-criterion", "sk-lem-pe-derived-nakayama", "sk-lem-int-tensor", "sk-prop-scalar-six", "thm-sf-pf-finite"]
+++
In the setting of [def-sf-datum], regard $\mathcal O_E$ as a condensed ring and
let $K\in\Dbc(X,\mathcal O_E)$ and $L\in\Dbc(Y,\mathcal O_E)$ be objects of the
condensed integral categories, with reductions
$K_n=K\otimes^{\mathbf L}_{\mathcal O_{E,X}}(A_{E,n})_X$ and $L_n$
([sk-def-pe-derived-completion]). Then the projection transformation of
[def-sf-pf]

$$
\operatorname{PF}_{f,K,L}:Rf_!K\otimes^{\mathbf L}_{\mathcal O_{E,Y}}L
\longrightarrow Rf_!\bigl(K\otimes^{\mathbf L}_{\mathcal O_{E,X}}Lf^*L\bigr)
$$

is an isomorphism in $\Dbc(Y,\mathcal O_E)$, and its reduction modulo
$\pi_E^n$ is $\operatorname{PF}_{f,K_n,L_n}$ for every $n$. More generally, a
morphism between objects of $\Dbc(Y,\mathcal O_E)$ is an isomorphism as soon
as its reduction modulo $\pi_E$ is one.
