+++
id = "lem-weil-scalar-extension-well-defined"
kind = "lemma"
title = "Well-definedness of scalar extension"
order = 1882
uses = ["def-weil-derived-complete-integral-detailed", "def-weil-derived-tensor", "def-weil-rationalization-karoubi", "prop-weil-pbc-rational-transport"]
+++
Let $E\subset L$ be a finite extension of $\Ql$, with rings of integers
$\mathcal O_E\subset\mathcal O_L$ and uniformizers $\varpi_E,\varpi_L$, and
let $Y$ be a scheme. For an object of the rationalized category $D^b_c(Y,E)$
of [def-weil-rationalization-karoubi] represented by an integral complex
$K\in D^b_c(Y,\mathcal O_E)$, the object

$$
 \bigl(K\otimes^L_{\mathcal O_E}\mathcal O_L\bigr)
 \otimes_{\mathcal O_L}L
$$

of $D^b_c(Y,L)$, formed with the derived tensor product
[def-weil-derived-tensor], levelwise modulo powers of the two uniformizers
and followed by rationalization, is independent of the chosen integral
representative $K$, up to canonical isomorphism.
