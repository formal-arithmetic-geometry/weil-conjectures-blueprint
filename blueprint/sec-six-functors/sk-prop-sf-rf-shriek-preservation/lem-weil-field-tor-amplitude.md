+++
id = "lem-weil-field-tor-amplitude"
kind = "lemma"
title = "Finite Tor amplitude at field coefficients"
order = 2364
uses = ["def-weil-algebraically-closed-coefficients", "def-weil-derived-tensor", "def-weil-finite-tor-amplitude", "def-weil-rationalization-karoubi"]
+++
Let $F$ be a field, let $Y$ be a scheme, and let $K$ be a bounded
constructible complex at a field coefficient stage: an object of the
rationalized category $D^b_c(Y,E)$ of [def-weil-rationalization-karoubi] with
$F=E$, or an object of the common-stage category $D^b_c(Y,\Qlb)$ of
[def-weil-algebraically-closed-coefficients] with $F=\Qlb$. Then $K$ has
finite Tor amplitude in the sense of [def-weil-finite-tor-amplitude]: there
are integers $a\leq b$ such that

$$
 \mathcal H^r\bigl(K\otimes^L_FM\bigr)=0
 \qquad(r\in\mathbf Z\setminus[a,b])
$$

for every sheaf $M$ of $F$-modules placed in degree zero, the derived tensor
product being that of [def-weil-derived-tensor].
