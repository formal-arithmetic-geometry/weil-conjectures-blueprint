+++
kind = "proof"
of = "pur9-lem-localization-triangle"
uses = ["pur9-lem-closed-push-fully-faithful", "pur9-lem-open-counit", "pur9-lem-open-restriction-closed", "pur9-lem-supported-objects"]
+++
Complete $\varepsilon^!_L$ to a distinguished triangle $Ri_{*,\mathcal O_E/\varpi^n}Ri^!_{\mathcal O_E/\varpi^n}L\to L\xrightarrow{w}C\to Ri_{*,\mathcal O_E/\varpi^n}Ri^!_{\mathcal O_E/\varpi^n}L[1]$.

*Step 1: $\operatorname{Hom}(Ri_{*,\mathcal O_E/\varpi^n}A,C[n])=0$ for all $A\in D(Z_{\Proet},\mathcal O_E/\varpi^n)$ and $n$.* Postcomposition with $\varepsilon^!_L$ is the map $\operatorname{Hom}(Ri_{*,\mathcal O_E/\varpi^n}A,Ri_{*,\mathcal O_E/\varpi^n}Ri^!_{\mathcal O_E/\varpi^n}L)\to\operatorname{Hom}(Ri_{*,\mathcal O_E/\varpi^n}A,L)$; composed with the bijection $\operatorname{Hom}(A,Ri^!_{\mathcal O_E/\varpi^n}L)\to\operatorname{Hom}(Ri_{*,\mathcal O_E/\varpi^n}A,Ri_{*,\mathcal O_E/\varpi^n}Ri^!_{\mathcal O_E/\varpi^n}L)$ of Lemma [pur9-lem-closed-push-fully-faithful], it is the adjunction bijection. Hence it is bijective for all shifts of $A$, and the long exact sequence of $\operatorname{Hom}(Ri_{*,\mathcal O_E/\varpi^n}A,-)$ gives the claim.

*Step 2: $Lj^*_{\mathcal O_E/\varpi^n}w$ is an isomorphism.* $Lj^*_{\mathcal O_E/\varpi^n}$ is exact and $Lj^*_{\mathcal O_E/\varpi^n}Ri_{*,\mathcal O_E/\varpi^n}Ri^!_{\mathcal O_E/\varpi^n}L=0$ by Lemma [pur9-lem-open-restriction-closed].

*Step 3: $\eta^j_C:C\to Rj_{*,\mathcal O_E/\varpi^n}Lj^*_{\mathcal O_E/\varpi^n}C$ is an isomorphism.* Complete it to a triangle $C\to Rj_{*,\mathcal O_E/\varpi^n}Lj^*_{\mathcal O_E/\varpi^n}C\to N\to C[1]$. Applying $Lj^*_{\mathcal O_E/\varpi^n}$ and using Lemma [pur9-lem-open-counit] together with the triangle identity, $Lj^*_{\mathcal O_E/\varpi^n}\eta^j_C$ is an isomorphism, so $Lj^*_{\mathcal O_E/\varpi^n}N=0$, and $N\cong Ri_{*,\mathcal O_E/\varpi^n}Li^*_{\mathcal O_E/\varpi^n}N$ by Lemma [pur9-lem-supported-objects]. The map $N\to C[1]$ vanishes by Step 1, so the triangle splits and $N$ is a direct summand of $Rj_{*,\mathcal O_E/\varpi^n}Lj^*_{\mathcal O_E/\varpi^n}C$; the inclusion $N\to Rj_{*,\mathcal O_E/\varpi^n}Lj^*_{\mathcal O_E/\varpi^n}C$ vanishes by Lemma [pur9-lem-open-restriction-closed], hence $N=0$.

*Step 4.* The isomorphism $\psi=(Rj_{*,\mathcal O_E/\varpi^n}Lj^*_{\mathcal O_E/\varpi^n}w)^{-1}\circ\eta^j_C:C\to Rj_{*,\mathcal O_E/\varpi^n}Lj^*_{\mathcal O_E/\varpi^n}L$ (Steps 2, 3) satisfies $\psi\circ w=\eta^j_L$, by naturality of $\eta^j$. Replacing $C$ by $Rj_{*,\mathcal O_E/\varpi^n}Lj^*_{\mathcal O_E/\varpi^n}L$ along $\psi$ gives a distinguished triangle with the stated first two maps; $\partial_L$ is the transported third map.
