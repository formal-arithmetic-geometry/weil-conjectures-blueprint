+++
id = "lemma-weil-pbc-etale-proetale-functor"
kind = "lemma"
title = "The etale/pro-etale assignment is a functor"
order = 1660
uses = ["def-weil-pbc-etale-proetale-inclusion"]
+++
The assignment $\iota_X$ preserves identity morphisms and composition.

## Proof

For an etale object $U\to X$, both $\iota_X(1_U)$ and
$1_{\iota_X(U)}$ have underlying scheme morphism $1_U$. For composable
$X$-morphisms $U\xrightarrow{h}V\xrightarrow{k}W$, both
$\iota_X(kh)$ and $\iota_X(k)\iota_X(h)$ have underlying scheme morphism
$kh$. Morphisms in either A2 over-category are determined by this underlying
map, which proves both equations.
