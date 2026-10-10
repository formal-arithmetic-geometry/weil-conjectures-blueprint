+++
id = "lem-weil-scalar-extension-exact-triangulated"
kind = "lemma"
title = "Scalar extension is an exact triangulated functor"
order = 1883
uses = ["def-weil-derived-complete-integral-detailed", "def-weil-derived-tensor", "def-weil-rationalization-karoubi", "lem-weil-scalar-extension-well-defined", "prop-weil-pbc-scalar-extension"]
+++
Let $E\subset L$ be a finite extension of $\Ql$ and let $Y$ be a scheme. The
scalar-extension functor

$$
 -\otimes_E L:D^b_c(Y,E)\longrightarrow D^b_c(Y,L)
$$

of [def-weil-rationalization-karoubi] is an exact triangulated functor: it
preserves shifts and carries distinguished triangles of $D^b_c(Y,E)$ to
distinguished triangles of $D^b_c(Y,L)$.
