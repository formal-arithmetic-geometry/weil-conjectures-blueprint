+++
id = "cor-pur-general-admissibility-datum"
kind = "theorem"
title = "Preservation for a general separated finite-type morphism"
order = 2868
tags = ["latex:corollary"]
uses = ["def-pur-conventions", "def-weil-ambient-exceptional-adjoint", "def-weil-exceptional-adjoint-admissibility", "def-weil-exceptional-inverse-image", "def-weil-scheme-morphism-properties", "lem-exc-open-complement-known", "thm-pur-general-admissibility", "thm-sf-ambient-adjoint-class"]
+++
In the purity conventions of this chapter
([def-pur-conventions] fixed setting), let $f:X\to Y$ be a
separated finite-type
morphism. The ambient exceptional right adjoint datum of
[def-weil-ambient-exceptional-adjoint] is not assumed: on the bounded
constructible and finite-Tor coefficients of the two clauses below, the right
adjoint of $Rf_!$ is the finite-stage exceptional inverse image $Rf^!$ of
[def-weil-exceptional-inverse-image], the adjoint relative to the
bounded-below objects of étale origin of [thm-sf-ambient-adjoint-class]. Then
$Rf^!$ satisfies the analogues of the two preservation clauses of
[def-weil-exceptional-adjoint-admissibility]: with the affine charts
$U\subseteq f^{-1}(V)$ and the integers $d_U$ of
[thm-pur-general-admissibility], put
$D=\max_Ud_U$ and $c_U=2\,(d_U+\dim Y)$. Then $Rf^!$ carries
$D_c^{[a,b]}(Y,A)$ into $D_c^{[a-2D,b-2D+c]}(X,A)$ for
$c=\max_U\bigl(c_U+1+2(D-d_U)\bigr)$, and it carries finite Tor
amplitude in $[a,b]$ to finite Tor amplitude in $[a-2D,b-2D+c]$.
