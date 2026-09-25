+++
id = "prop-sf-direct-image-ctf-proper"
kind = "theorem"
title = "Direct image in the proper case"
order = 2337
tags = ["latex:proposition"]
uses = ["def-compact-support-direct-image-detailed", "def-weil-finite-tor-amplitude", "def-weil-finite-torsion-constructibility", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "open-sf-preservation-gaps"]
+++
Fix the global finite-field datum, a prime $\ell\ne p$, $n\geq1$, put
$A=A_{E,n}$, and let $f:X\to Y$ be a
proper finite-type morphism
of finite-type $k$-schemes. Then the compact-support direct image and the
ordinary direct image agree, $Rf_!=Rf_*$ on
$D(X_{\mathrm{proet}},A)$, and $Rf_*$ carries $D^b_{ctf}(X,A)$ into
$D^b_{ctf}(Y,A)$; explicitly, the cell for $Rf_*$ on the finite-Tor
categories is clause (iv) of the finite-Tor preservation summary transported across
this identification.

## Proof

For proper $f$ the compact-support direct image of
[def-compact-support-direct-image-detailed] is the ordinary direct image,
$Rf_!=Rf_*$. Clause (iv) of the finite-Tor preservation summary asserts that
$Rf_!$ carries $D^b_{ctf}(X,A)$ into $D^b_{ctf}(Y,A)$; transported
across the identification this is the assertion for $Rf_*$, and the
statement about the finite-Tor categories follows. No general non-proper
form of this cell is asserted by this proposition; what is proved for a
general $f$, and what remains missing, is recorded in
[open-sf-preservation-gaps].
