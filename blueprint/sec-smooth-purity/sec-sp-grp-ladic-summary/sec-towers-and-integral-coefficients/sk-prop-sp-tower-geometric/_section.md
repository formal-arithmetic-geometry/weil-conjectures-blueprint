+++
id = "sk-prop-sp-tower-geometric"
kind = "proposition"
title = "The tower model of the smooth adjunction"
order = 469
uses = ["sk-def-sp-normalized-towers", "sk-lem-sp-tower-levels", "sk-lem-sp-tower-bound", "sk-lem-sp-reduction", "sk-prop-geo-p1-adjunction", "sk-lem-sp-finite-existence", "sk-prop-an", "sk-thm-dnc"]
tags = ["sketch"]
+++
There is an adjunction

$$
Rf_{!,\bullet}\dashv f_\bullet^!
\quad\text{between the constructible towers on }X\text{ and on }Y.
\tag{10.17}
$$

At level $n$ its unit and counit are those of the finite adjunction, so
$(f_\bullet^!C_\bullet)_n\simeq f^!_{\mathcal O_E/\ell^n}C_n$, and the reduction maps of
$f_\bullet^!C_\bullet$ are $f^!$ of those of $C_\bullet$ composed with the comparisons $c$
of Lemma [sk-lem-sp-reduction].
