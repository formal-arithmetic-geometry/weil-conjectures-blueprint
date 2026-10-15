+++
id = "det-base-field-cd-cochains"
kind = "lemma"
title = "Continuous cochains compute Galois cohomology"
uses = ["def-exc-continuous-cohomology"]
+++
Let $G$ be a profinite group and let $\mathcal C_G$ be the abelian category of
discrete $G$-modules (abelian groups with a $G$-action whose stabilizers are
open). Let $C^\bullet(G,M)$ be the complex of continuous inhomogeneous cochains
$G^s\to M$ with the usual differential.

1. $M\mapsto H^s(C^\bullet(G,M))$ is a universal $\delta$-functor on
   $\mathcal C_G$ with $H^0=M^G$; hence it is the right derived functor of
   $M\mapsto M^G$, i.e. $H^s(G,M)$ as in [def-exc-continuous-cohomology].
2. If $M=\bigcup_\alpha M_\alpha$ is a directed union of submodules, then
   $H^s(G,M)=\varinjlim_\alpha H^s(G,M_\alpha)$.
3. If $G=\varprojlim_NG/N$ over open normal subgroups $N$ acting trivially on $M$,
   then $C^\bullet(G,M)=\varinjlim_NC^\bullet(G/N,M)$ along inflation, and
   $H^s(G,M)=\varinjlim_NH^s(G/N,M)$.
