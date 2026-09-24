+++
id = "def-trf-admissibility"
kind = "definition"
title = "Exceptional-adjoint admissibility datum"
order = 3299
uses = ["def-trf-coefficient-conventions", "def-weil-exceptional-adjoint-admissibility", "def-weil-finite-field-fiber", "def-weil-scheme-morphism-properties"]
+++
Fix the global finite-field datum
and the coefficient
conventions, $A=A_{E,n}$, and let $f:X\to Y$ be a
separated finite-type
morphism of finite-type $k$-schemes. Say that $f$ is
*exceptionally admissible* when the
exceptional-adjoint
admissibility condition of the framework chapter holds at $A=A_{E,n}$ and at
every finite coefficient stage, so that the compact-support direct image
$Rf_!:D^b_{ctf}(X,A)\to D^b_{ctf}(Y,A)$ has a specified right adjoint
$Rf^!:D^b_{ctf}(Y,A)\to D^b_{ctf}(X,A)$, with unit
$\operatorname{id}\to Rf^!Rf_!$ and counit
$Rf_!Rf^!\to\operatorname{id}$ (i.e. the adjunction $Rf_!\dashv Rf^!$),
and the composition and base-change exchange isomorphisms used below.
This is an explicit hypothesis; no
assertion that every separated finite-type morphism is admissible is
made here. Its ingredients have different status, and the difference
matters for every statement that cites this definition. No part of the ambient datum and
no preservation clause is assumed any longer.

*Recorded in advance* from chapter *The trace formula* of the source.
