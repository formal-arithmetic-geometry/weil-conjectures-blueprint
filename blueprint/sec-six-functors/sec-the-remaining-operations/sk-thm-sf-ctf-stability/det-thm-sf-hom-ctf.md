+++
id = "det-thm-sf-hom-ctf"
kind = "theorem"
title = "Internal Hom with finite Tor amplitude"
order = 2813
uses = ["det-def-sf-admissible", "sk-prop-sf-open-closed-triangle", "det-prop-sf-biduality-general", "sk-prop-sf-existence", "det-prop-sf-finiteness", "det-prop-sf-fullcd-etale-origin", "sk-prop-sf-rf-shriek-preservation"]
lean = ["AlgebraicGeometry.Etale.boundedConstructible_derivedHom", "AlgebraicGeometry.Etale.torAmplitudeIn_derivedHom", "AlgebraicGeometry.Etale.torAmplitudeIn_derivedHom_of_isDualizable"]
+++
Let $A=A_{E,n}$, let $X$ be a finite-type $k$-scheme with $\dim X\le m$, and
let $K,M$ be bounded constructible $A$-complexes on $X_{\Et}$ with finite Tor
amplitude in $[a,b]$ and in $[c,d]$. Then
$\RHom_A(K,M)$ is bounded constructible with finite Tor amplitude in
$[c-b-2m,d-a+2m]$. If $K$ is site-perfect, that is, dualizable (locally on
$X_{\Et}$ a bounded complex of finite projective $A$-modules in degrees
$[a,b]$), the sharper interval $[c-b,d-a]$ holds.
