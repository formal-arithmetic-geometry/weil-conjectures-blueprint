+++
kind = "proof"
of = "pur9-lem-closed-unit"
uses = ["pur9-lem-closed-push-fully-faithful", "pur9-lem-open-immersion-lower-shriek", "pur9-lem-open-immersion-upper-shriek", "pur9-lem-proper-lower-shriek"]
+++
For a left adjoint $F$ with right adjoint $G$ and unit $\eta$, the map $\operatorname{Hom}(P,Q)\to\operatorname{Hom}(FP,FQ)\cong\operatorname{Hom}(P,GFQ)$ is postcomposition with $\eta_Q$; if $F$ is fully faithful it is bijective for all $P$, so $\eta_Q$ is an isomorphism by the Yoneda lemma. It therefore suffices that $Ri_{!,\mathcal O_E/\varpi^n}$ be fully faithful. If $i$ is not an open immersion, $Ri_{!,\mathcal O_E/\varpi^n}\cong Ri_{*,\mathcal O_E/\varpi^n}$ by Lemma [pur9-lem-proper-lower-shriek], fully faithful by Lemma [pur9-lem-closed-push-fully-faithful]. If $i$ is also an open immersion, $Ri_{!,\mathcal O_E/\varpi^n}\cong\mathrm D(i_{!,\mathcal O_E/\varpi^n})$ by Lemma [pur9-lem-open-immersion-lower-shriek], and the unit of Lemma “Finite-coefficient derived open-extension adjunction” (`pur713-lem-open-adjunction`), which is the standing unit by Lemma [pur9-lem-open-immersion-upper-shriek], is invertible.
