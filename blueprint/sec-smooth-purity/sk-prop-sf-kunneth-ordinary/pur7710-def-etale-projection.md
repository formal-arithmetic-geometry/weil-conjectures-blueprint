+++
id = "pur7710-def-etale-projection"
kind = "definition"
title = "The étale direct-image projection morphism"
order = 2026
tags = ["latex:bpdefinition"]
uses = ["pur713-def-star-projection", "pur7710-def-unbounded-etale-push", "pur7710-lem-unbounded-etale-adjunction"]
+++
Under Input “Structure of inverse image on the small étale sites” (`pur713-input-etale-structure`), for a morphism $f:X\to Y$, $K\in D(X_{\Et},\mathcal O_E/\varpi^n)$ and $M\in D(Y_{\Et},\mathcal O_E/\varpi^n)$, the morphism

$$
P_{f,\Et,\mathcal O_E/\varpi^n,K,M}:Rf_{*,\Et,\mathcal O_E/\varpi^n}K
\otimes^L_{\mathcal O_E/\varpi^n}M
\longrightarrow Rf_{*,\Et,\mathcal O_E/\varpi^n}
(K\otimes^L_{\mathcal O_E/\varpi^n}Lf^*_{\Et,\mathcal O_E/\varpi^n}M)
$$

in $D(Y_{\Et},\mathcal O_E/\varpi^n)$ is the morphism corresponding, under the adjunction of Lemma [pur7710-lem-unbounded-etale-adjunction], to the composite of the derived monoidal comparison

$$
Lf^*_{\Et,\mathcal O_E/\varpi^n}\bigl(Rf_{*,\Et,\mathcal O_E/\varpi^n}K\otimes^L_{\mathcal O_E/\varpi^n}M\bigr)\cong Lf^*_{\Et,\mathcal O_E/\varpi^n}Rf_{*,\Et,\mathcal O_E/\varpi^n}K\otimes^L_{\mathcal O_E/\varpi^n}Lf^*_{\Et,\mathcal O_E/\varpi^n}M
$$

supplied by Input “Unbounded étale derived inverse-image adjunction” (`pur713-input-etale-unbounded-adjunction`) with the tensor of the counit at $K$ and the identity of $Lf^*_{\Et,\mathcal O_E/\varpi^n}M$. This is the étale-site analogue of Definition [pur713-def-star-projection]; here $Rf_{*,\Et,\mathcal O_E/\varpi^n}$ is the unbounded functor of Definition [pur7710-def-unbounded-etale-push].
