+++
id = "cor-exc-closed-preservation-datum"
kind = "theorem"
title = "Preservation for a closed immersion"
order = 2156
tags = ["latex:corollary"]
uses = ["def-exc-open-complement-bound", "def-weil-finite-tor-amplitude", "def-weil-pbc-constructible-complexes", "def-weil-pbc-derived-categories", "def-weil-pbc-scheme-conventions", "lem-exc-closed-ambient", "lem-exc-closed-amplitude", "lem-exc-open-complement-known", "prop-exc-closed-tor"]
+++
Let $k$ be the algebraic closure of a finite field, let $T$ be a
finite-type $k$-scheme of dimension at most $d$, let
$i:Z\hookrightarrow T$ be a
closed immersion with
quasi-compact open complement $j$, and let $A$ be a finite ring
annihilated by a power of a prime $\ell\neq\operatorname{char}(k)$.
Then, in the
ordinary derived categories,

$$
Ri^!D^{[a,b]}(T_{{\mathrm{et}}},A)\subseteq D^{[a,b+2d+1]}(Z_{{\mathrm{et}}},A)
$$

with constructible
cohomology on both sides, and $Ri^!$ carries complexes of
finite Tor amplitude in
$[a,b]$ to complexes of finite Tor amplitude in $[a,b+2d+1]$.

## Proof

The pair $(Z,T)$ satisfies the open-complement condition of
[lem-exc-open-complement-known] with $c=2d$. The ambient right
adjoint $Ri^!$ exists by [lem-exc-closed-ambient], and the two
preservation assertions are then [lem-exc-closed-amplitude] and
[prop-exc-closed-tor] under that condition.
