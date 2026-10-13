+++
id = "pur7710-lem-finite-ring-kunneth"
kind = "lemma"
title = "Ordinary Künneth at every finite coefficient level"
order = 2022
tags = ["latex:bplemma"]
uses = ["pur7710-def-kunneth-map", "pur7710-input-prime-field-kunneth", "pur7710-lem-residue-sections"]
+++
Assume the inputs of Lemma [pur7710-lem-residue-sections] and Input [pur7710-input-prime-field-kunneth]. For all $k$-schemes $X,Y$ of finite type and all
$K\in D(X_{\Et},\mathcal O_E/\varpi^n)$, $L\in D(Y_{\Et},\mathcal O_E/\varpi^n)$, the map $\operatorname{Kun}_{\mathcal O_E/\varpi^n,K,L}$ of Definition [pur7710-def-kunneth-map],

$$
R\Gamma_{X,\Et,\mathcal O_E/\varpi^n}K\otimes^L_{\mathcal O_E/\varpi^n}R\Gamma_{Y,\Et,\mathcal O_E/\varpi^n}L
\longrightarrow R\Gamma_{X\times_kY,\Et,\mathcal O_E/\varpi^n}
(K\boxtimes^L_{\mathcal O_E/\varpi^n}L),
$$

is an isomorphism in $D(\mathsf{Mod}_{\mathcal O_E/\varpi^n})$. No boundedness, separatedness, or properness assumption is imposed on the factors.
