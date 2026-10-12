+++
id = "lem-trf-ordinary-kunneth"
kind = "lemma"
title = "Ordinary Kunneth for a general morphism"
order = 2558
uses = ["def-trf-coefficient-conventions", "def-weil-finite-tor-amplitude", "def-weil-scheme-morphism-properties", "lem-kun-0f1j", "lem-kun-0f1n", "lem-sf-flat-model"]
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
