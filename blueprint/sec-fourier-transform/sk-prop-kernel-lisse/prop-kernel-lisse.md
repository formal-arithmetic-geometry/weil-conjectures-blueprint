+++
id = "prop-kernel-lisse"
kind = "theorem"
title = "P1: the kernel is a lisse rank-one character sheaf"
order = 2938
uses = ["def-fd-kernel", "def-weil-finite-tor-amplitude", "lem-fd-as-lisse"]
tags = ["latex:proposition"]
+++
The Fourier kernel $\mathcal K_\psi$ of [def-fd-kernel] is lisse of rank one on
$V_0\times_{S_0}V_0^\vee$ and of finite Tor amplitude
([def-weil-finite-tor-amplitude]), and

$$
\mathcal K_\psi\otimes\mathcal K_{\psi'}\cong\mathcal K_{\psi\psi'},
\qquad
\mathcal K_\psi^{-1}\cong\mathcal K_{\psi^{-1}} .
$$

(Blueprint def:fd-kernel with lem:fd-as-lisse; the
purity of the kernel is a weight-theoretic statement and is not used here.)

## Proof

$\mathcal K_\psi$ is the inverse image along the pairing $b$ of the
Artin–Schreier sheaf of the linear function $b(x,\xi)$; inverse images of
lisse rank-one sheaves are lisse of rank one, so [lem-fd-as-lisse]
applies verbatim, the value of the character being additive in the defining
function. Lissity of rank one gives finite Tor amplitude, which is what the
definition of the transform needs.

Uses: [def-fd-kernel], [def-weil-finite-tor-amplitude], [lem-fd-as-lisse]
