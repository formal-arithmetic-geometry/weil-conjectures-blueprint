+++
id = "det-lem-int-ext-bound"
kind = "lemma"
title = "Uniform vanishing of Ext between integral constructible sheaves"
order = 2478
uses = ["det-lem-int-ext-formula", "sk-def-cd", "sk-lem-int-integral-heart", "sk-prop-integral-criterion"]
+++
Let $a=i\circ u:S\hookrightarrow X$ and $L$ be as in
[det-lem-int-ext-formula], and let $j$ be the open immersion complementary to
$i$. Then

$$
\Ext^q_X(a_!L,N)=0\qquad\text{for }q>\operatorname{cd}_\ell(j)+\operatorname{cd}_\ell(S)+3
\text{ and all }N\in\Cons(X,\mathcal O_E).
$$

Consequently every $C\in\Cons(X,\mathcal O_E)$ has an integer $d_C$ with
$\Ext^q(C,N)=0$ for $q>d_C$ and all $N\in\Cons(X,\mathcal O_E)$.
