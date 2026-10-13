+++
kind = "proof"
of = "pur7710-lem-origin-cbc"
uses = ["pur713-lem-exchange-naturality-shriek", "pur7710-lem-etale-cbc"]
+++
Choose an isomorphism $K\cong L\nu^*_{X,\mathcal O_E/\varpi^n}L$ with $L\in D^+(X_{\Et},\mathcal O_E/\varpi^n)$ (Definition “The bounded-below étale-origin subcategory” (`pur456-def-etale-origin`, see [sk-prop-sf-comp-coherence])). By naturality of the exchange (Lemma [pur713-lem-exchange-naturality-shriek]) it suffices to treat $K=L\nu^*_{X,\mathcal O_E/\varpi^n}L$. In the equality of Input [pur7710-input-site-exchange], evaluated at $L$, the maps $\kappa_{f,\mathcal O_E/\varpi^n}$ and $\kappa_{c',\mathcal O_E/\varpi^n}$ are isomorphisms by Lemma “Invertibility of the candidate comparison” (`pur456-lem-candidate-site-iso`, see [sk-prop-sf-comp-coherence]), $\beta_g$ and $\beta_{g'}$ are isomorphisms by Definition “Inverse image across the two sites” (`pur7710-def-site-pullback-comparison`, see [sk-prop-sf-comp-coherence]), and the étale exchange is an isomorphism by Lemma [pur7710-lem-etale-cbc]. Hence the remaining factor, the pro-étale exchange at $K$, is an isomorphism. The last assertion follows from Definition [pur713-def-shriek-exchange-chosen].
