+++
id = "sk-lem-sp-field-extension"
kind = "lemma"
title = "Compatibility with finite extensions of $E$"
order = 3014
uses = ["sk-prop-sp-rational", "sk-lem-sp-reduction", "sk-prop-sp-integral-adjunction"]
tags = ["sketch"]
+++
Let $f:X\to Y$ be smooth of pure relative dimension $d$, and let $E\subset F$ be
finite extensions of $\Ql$. For $M\in\Dbc(X,E)$ and $K\in\Dbc(Y,E)$ there are
natural isomorphisms, in $\Dbc(Y,F)$ and $\Dbc(X,F)$ respectively,

$$
\begin{aligned}
(Rf_{!,E}M)\otimes^{\mathbf L}_{E_Y}F_Y
&\simeq Rf_{!,F}(M\otimes^{\mathbf L}_{E_X}F_X),\\
(f_E^*K(d)[2d])\otimes^{\mathbf L}_{E_X}F_X
&\simeq f_F^*(K\otimes^{\mathbf L}_{E_Y}F_Y)(d)[2d],
\end{aligned}
$$

which carry the unit and counit of [sk-prop-sp-rational] for $E$ to those for
$F$. For a further extension $F\subset L$, the comparison for $E\subset L$ is
the composite of those for $E\subset F$ and $F\subset L$.
