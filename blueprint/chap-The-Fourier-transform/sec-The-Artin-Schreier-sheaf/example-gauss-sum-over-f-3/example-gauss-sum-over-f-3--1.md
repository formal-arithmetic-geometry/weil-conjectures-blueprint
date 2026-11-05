+++
id = "example-gauss-sum-over-f-3--1"
kind = "example"
title = "A Gauss sum over $\\mathbf F_3$ (1)"
name_showing = false
order = 1223001
aliases = ["bp-r376-1"]
+++
Take $q=3$, a primitive cube root of unity $\omega\in\overline{\mathbf Q}_\ell$ and
$\psi(x)=\omega^x$ on $\mathbf F_3$. Pull $\mathcal L_\psi$ back along
$h:\mathbf A^1\to\mathbf A^1$, $x\mapsto x^2$. By the lemma, the trace
of Frobenius on the stalk of $h^*\mathcal L_\psi$ at $x\in\mathbf F_3$ is
$\psi(x^2)$, so the trace formula gives

$$
\sum_r(-1)^r\operatorname{Tr}\bigl(F\mid H^r_c(\mathbf A^1_k,h^*\mathcal L_\psi)\bigr)=\sum_{x\in\mathbf F_3}\omega^{x^2}.
$$
