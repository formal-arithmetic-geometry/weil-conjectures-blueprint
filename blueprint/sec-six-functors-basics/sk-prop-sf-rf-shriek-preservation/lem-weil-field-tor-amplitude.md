+++
id = "lem-weil-field-tor-amplitude"
kind = "lemma"
title = "Finite Tor amplitude at field coefficients"
order = 2404
uses = ["def-weil-finite-tor-amplitude", "sk-def-sfb-constructible", "sk-def-sfb-bounded-constructible", "sk-lem-coefficient-heart", "sk-cor-coefficient-heart-ii"]
+++
Let $\Lambda\in\{E,\Qlb\}$, regarded as a condensed ring, let $Y$ be a
standing scheme, and let $K\in\Dbc(Y,\Lambda)$ be an object of the condensed
bounded constructible category ([sk-def-sfb-bounded-constructible]). Then $K$
has finite Tor amplitude ([sk-def-sfb-constructible],
[def-weil-finite-tor-amplitude]): there are integers $a\leq b$ such that

$$
 \mathcal H^r\bigl(K\otimes^{\mathbf L}_{\Lambda_Y}M\bigr)=0
 \qquad(r\in\mathbf Z\setminus[a,b])
$$

for every sheaf $M$ of $\Lambda_Y$-modules placed in degree zero. Thus
$\Dctf(Y,\Lambda)=\Dbc(Y,\Lambda)$.
