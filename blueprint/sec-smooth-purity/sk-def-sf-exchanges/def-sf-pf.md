+++
id = "def-sf-pf"
kind = "definition"
title = "Coefficient dual, Verdier dual, and the projection formula"
order = 1806
uses = ["def-exchange-projection", "def-sf-datum", "def-weil-derived-pullback-tensor-hom"]
+++
In the setting of [def-sf-datum], let $a_X:X\to\operatorname{Spec}k$ be
the structure morphism of a separated finite-type $k$-scheme and put
$\omega_X=Ra_X^!\Lambda$. For $K\in D^b_{ctf}(X,\Lambda)$ the
*Verdier dual* and the *coefficient dual* are

$$
\mathbb D_XK=R\mathcal H om_X(K,\omega_X),\qquad
K^\vee=R\mathcal H om_X(K,\Lambda_X),
$$

and for a separated finite-type $f:X\to Y$ the *projection
transformation* is

$$
\operatorname{PF}_{f,K,L}:Rf_!K\otimes^L_\Lambda L\longrightarrow
Rf_!\bigl(K\otimes^L_\Lambda Lf^*L\bigr)
$$

of [def-exchange-projection].
