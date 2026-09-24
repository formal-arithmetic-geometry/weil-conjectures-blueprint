+++
id = "lem-weil-pbc-finite-proper"
kind = "lemma"
title = "Finite morphisms are proper"
order = 1175
uses = ["def-weil-pbc-scheme-conventions"]
+++
A finite [def-weil-pbc-scheme-conventions] morphism is proper.

## Proof

A finite morphism is affine, hence separated, since the diagonal of an affine
morphism is a closed immersion in the sense of
[def-weil-pbc-scheme-conventions]; it is of finite type because an
$A$-algebra that is a finite $A$-module is finitely generated as an
$A$-algebra. It is universally closed: a finite ring map has going-up, hence
a finite morphism is closed, and finite morphisms are stable under base
change, so every base change of a finite morphism is closed. These are
exactly the defining properties of properness in
[def-weil-pbc-scheme-conventions].
