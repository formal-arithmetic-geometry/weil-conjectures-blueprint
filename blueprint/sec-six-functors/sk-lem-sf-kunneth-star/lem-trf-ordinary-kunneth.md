+++
id = "lem-trf-ordinary-kunneth"
kind = "lemma"
title = "Ordinary Kunneth for a general morphism"
order = 2218
uses = ["def-trf-coefficient-conventions", "def-weil-finite-tor-amplitude", "def-weil-scheme-morphism-properties", "fix-prop-projection-formula", "sbc-thm-smooth-base-change"]
+++
Use the finite coefficient ring $A=A_{E,n}$ of
[def-trf-coefficient-conventions]. Let $f:X\to Y$ be a morphism of
separated finite-type
schemes, let $Z$ be an auxiliary such scheme, and let $L\in D^b_{ctf}(X,A)$, $Q\in D^b_{ctf}(Z,A)$ in the
finite-Tor constructible
category. Then the canonical comparison

$$
Rf_*L\boxtimes_A^{\mathrm L} Q
\xrightarrow{\ \sim\ }
R(f\times\operatorname{id}_Z)_*\bigl(L\boxtimes_A^{\mathrm L} Q\bigr)
$$

is an isomorphism, natural in $L$ and $Q$.

## Proof

Consider the Cartesian square

$$
\begin{gathered}
X\times Z \xrightarrow{f\times\operatorname{id}_Z} Y\times Z,\\
p_X:X\times Z\to X,\qquad p_Y:Y\times Z\to Y,\qquad
p_Z:X\times Z\to Z,\qquad p'_Z:Y\times Z\to Z,
\end{gathered}
$$

with $p_Z=p'_Z\circ(f\times\operatorname{id}_Z)$. The base morphism
$p_Y$ is smooth (a projection), so the smooth base change
[sbc-thm-smooth-base-change] of the smooth-base-change chapter, applied to this square,
gives the first isomorphism below:

$$
R(f\times\operatorname{id}_Z)_*\bigl(p_X^*L\bigr)
\cong p_Y^*Rf_*L .
$$

Writing the external product as
$L\boxtimes_A^{\mathrm L}Q=p_X^*L\otimes_A^{\mathrm L}p_Z^*Q =p_X^*L\otimes_A^{\mathrm L}(f\times\operatorname{id}_Z)^*\bigl(p'_Z{}^*Q\bigr)$,
the projection formula [fix-prop-projection-formula] of the framework chapter
gives the second isomorphism:

$$
\begin{aligned}
R(f\times\operatorname{id}_Z)_*\bigl(L\boxtimes_A^{\mathrm L}Q\bigr)
&\cong
R(f\times\operatorname{id}_Z)_*\bigl(p_X^*L\bigr)
\otimes_A^{\mathrm L}p'_Z{}^*Q\\
&\cong p_Y^*Rf_*L\otimes_A^{\mathrm L}p'_Z{}^*Q
= Rf_*L\boxtimes_A^{\mathrm L}Q .
\end{aligned}
$$

The composite is the canonical comparison, since both isomorphisms are
natural in their variables; naturality in $L$ and $Q$ follows from the
functoriality of base change and of the projection formula.
(*Provenance:* the Stacks Project form of this input is Étale
Cohomology, Lemma 59.97.8,
[Tag `0F1N`](https://stacks.math.columbia.edu/tag/0F1N),
the canonical map
$p^{-1}E\otimes^L_{\mathbf Z/n\mathbf Z}(f')^{-1}Rg_*F\to Rh_*(h^{-1}p^{-1}E\otimes^L_{\mathbf Z/n\mathbf Z}e^{-1}F)$ being an
isomorphism for $\mathbf Z/n\mathbf Z$-coefficients on schemes of
finite type over a field, together with SGA 5, III, 1.1 and 1.6.4 for
the coefficient and site generality used here; the two-step proof above
replaces those citations.)
