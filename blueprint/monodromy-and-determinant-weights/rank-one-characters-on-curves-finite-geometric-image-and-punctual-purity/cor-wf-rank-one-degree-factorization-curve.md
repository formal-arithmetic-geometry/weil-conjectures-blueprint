+++
id = "cor-wf-rank-one-degree-factorization-curve"
kind = "theorem"
title = "Finite-order part times a degree character"
order = 4085
tags = ["latex:corollary"]
uses = ["def-weil-pbc-scheme-conventions", "def-wf-weil-group", "lem-wf-weil-group-exact-sequence", "thm-wf-rank-one-finite-geometric-image-curve"]
+++
Let $U_0/\mathbf F_q$, $U$, $\Pi$, $\ell$, and $E$ satisfy the
hypotheses of the preceding theorem, and let
$\chi:\hyperref[def:wf-weil-group]{W(U_0,\bar u)}\to E^\times$ be a
continuous character. Choose $s$ with $\deg(s)=1$ and put
$c=\chi(s)$. Then there is a finite-order character
$\varepsilon:W(U_0,\bar u)\to E^\times$ such that

$$
\chi(w)=\varepsilon(w)c^{\deg(w)}
\qquad(w\in W(U_0,\bar u)).
$$

The scheme and Weil-group conventions are those of
[def-weil-pbc-scheme-conventions], [def-wf-weil-group].

## Proof

Using the degree homomorphism of [def-wf-weil-group], define

$$
\varepsilon(w):=\chi(w)c^{-\deg(w)}.
$$

This is a character because both factors are characters. If
$n=\deg(w)$, then $g=ws^{-n}$ has degree zero and hence lies in
$\Pi$, which is the kernel of $\deg$ by
[lem-wf-weil-group-exact-sequence]. Since $E^\times$ is abelian,

$$
\varepsilon(w)=\chi(ws^{-n})=\chi(g)\in\chi(\Pi).
$$

The latter group is finite by
[thm-wf-rank-one-finite-geometric-image-curve]. Thus the image of
$\varepsilon$ is finite, so $\varepsilon$ is of finite order, and the
displayed factorization follows from its definition.
