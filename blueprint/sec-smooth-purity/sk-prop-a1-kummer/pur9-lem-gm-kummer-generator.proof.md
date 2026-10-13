+++
kind = "proof"
of = "pur9-lem-gm-kummer-generator"
uses = ["pur9-input-stalk-formula", "pur9-lem-a1-acyclic", "pur9-lem-curve-gm-kummer", "pur9-lem-fibre-reduction", "pur9-lem-kummer-base-change"]
+++
As in Lemma [pur9-lem-a1-acyclic], check on geometric stalks of underlying abelian sheaves. By Input [pur9-input-stalk-formula], the stalk map at $\bar y$ is $\mathcal O_E/\varpi^n\to H^1(\mathbf G_{m,S'},P(1))$, $1\mapsto\kappa(t)|_{\mathbf G_{m,S'}}$. Lemma [pur9-lem-fibre-reduction] identifies the target with $H^1(\mathbf G_{m,k},P(1))$, carrying the class to $\kappa(t)$ on $\mathbf G_{m,k}$ by Lemma [pur9-lem-kummer-base-change]. With $P(1)=\mu_{\ell^n}(k)\otimes_{\mathbf Z/\ell^n}\mathcal O_E/\varpi^n$, Lemma [pur9-lem-curve-gm-kummer] for $M=\mathcal O_E/\varpi^n$ shows the map is bijective.
