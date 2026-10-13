+++
id = "sk-d-pairing"
kind = "definition"
title = "The supported pairing recipe"
order = 2652
uses = ["sk-d-corr", "sk-d-integral", "sk-d-six", "sk-thm-sf-kunneth-verdier"]
lean = ["AlgebraicGeometry.ProEtale.GeometricOperations.supportedPairing"]
tags = ["sketch"]
+++
Let $s$ be the spectrum of a field, $X,Y$ quasi-compact and compactifiable over
$s$, $K\in D^b_{ctf}(X,A)$ and $L\in D^b_{ctf}(Y,A)$.
For an opposite pair, use the inverse
Künneth–Verdier maps to obtain

$$
\widetilde u:Rc_!A_C\to P=L\boxt D_XK,
\qquad \widetilde v:R\bar d_!A_D\to Q=K\boxt D_YL
$$

on $Z=Y\times X$. If $e:E(C,D)\to Z$, the projection formula and $!$-base change
give $Re_!A_E\simeq Rc_!A_C\otimes R\bar d_!A_D$.
Compose with $\widetilde u\otimes\widetilde v$, the exchange of the middle factors
and the monoidality of the pullbacks, then the two Verdier
evaluations $L\otimes D_YL\to\omega_Y$, $K\otimes D_XK\to\omega_X$, and the exterior
product map $\omega_Y\boxt\omega_X\to\omega_Z$ (the exceptional adjoint of the trace
$Ra_{X!}\omega_X\simeq Ra_{X!}a_X^!A\to A$ after the projection formula and
$!$-base change).
Its exceptional adjoint is the Borel–Moore section
$\langle u,v\rangle_{\mathrm{LV}}:A_E\to\omega_E$.
