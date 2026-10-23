+++
id = "pur7710-def-etale-projection"
kind = "definition"
title = "The étale direct-image projection morphism"
order = 3092
uses = ["pur713-def-star-projection", "pur7710-def-unbounded-etale-push"]
+++
Under Input “Structure of inverse image on the small étale sites” (`pur713-input-etale-structure`), for a morphism $f:X\to Y$, $K\in D(X_{\Et},\mathcal O_E/\pi_E^n)$ and $M\in D(Y_{\Et},\mathcal O_E/\pi_E^n)$, the morphism

$$
P_{f,\Et,\mathcal O_E/\pi_E^n,K,M}:Rf_{*,\Et,\mathcal O_E/\pi_E^n}K
\otimes^L_{\mathcal O_E/\pi_E^n}M
\longrightarrow Rf_{*,\Et,\mathcal O_E/\pi_E^n}
(K\otimes^L_{\mathcal O_E/\pi_E^n}Lf^*_{\Et,\mathcal O_E/\pi_E^n}M)
$$

in $D(Y_{\Et},\mathcal O_E/\pi_E^n)$ is the morphism corresponding, under the adjunction of Lemma “The unbounded étale inverse-image adjunction” (`pur7710-lem-unbounded-etale-adjunction`), to the composite of the derived monoidal comparison

$$
Lf^*_{\Et,\mathcal O_E/\pi_E^n}\bigl(Rf_{*,\Et,\mathcal O_E/\pi_E^n}K\otimes^L_{\mathcal O_E/\pi_E^n}M\bigr)\cong Lf^*_{\Et,\mathcal O_E/\pi_E^n}Rf_{*,\Et,\mathcal O_E/\pi_E^n}K\otimes^L_{\mathcal O_E/\pi_E^n}Lf^*_{\Et,\mathcal O_E/\pi_E^n}M
$$

supplied by Input “Unbounded étale derived inverse-image adjunction” (`pur713-input-etale-unbounded-adjunction`) with the tensor of the counit at $K$ and the identity of $Lf^*_{\Et,\mathcal O_E/\pi_E^n}M$. This is the étale-site analogue of Definition [pur713-def-star-projection]; here $Rf_{*,\Et,\mathcal O_E/\pi_E^n}$ is the unbounded functor of Definition [pur7710-def-unbounded-etale-push].
