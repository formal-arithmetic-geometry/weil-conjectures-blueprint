+++
id = "pur7710-def-kunneth-map"
kind = "definition"
title = "The ordinary Künneth morphism at finite level"
order = 3069
uses = ["pur7710-def-exterior-product", "sk-thm-sf-comp-composition"]
+++
For $X,Y,Z,K,L$ as in Definition [pur7710-def-exterior-product], let

$$
\operatorname{Kun}_{\mathcal O_E/\pi_E^n,K,L}:
R\Gamma_{X,\Et,\mathcal O_E/\pi_E^n}K\otimes^L_{\mathcal O_E/\pi_E^n}R\Gamma_{Y,\Et,\mathcal O_E/\pi_E^n}L
\longrightarrow R\Gamma_{Z,\Et,\mathcal O_E/\pi_E^n}(K\boxtimes^L_{\mathcal O_E/\pi_E^n}L)
$$

be the morphism corresponding, under $c_{Z,\mathcal O_E/\pi_E^n}\dashv R\Gamma_{Z,\Et,\mathcal O_E/\pi_E^n}$ (Lemma “Constant complexes and derived sections are adjoint” (`pur7710-lem-constant-adjunction`)), to the composite

$$
\begin{aligned}
&c_{Z,\mathcal O_E/\pi_E^n}\bigl(R\Gamma_{X,\Et,\mathcal O_E/\pi_E^n}K\otimes^L_{\mathcal O_E/\pi_E^n}R\Gamma_{Y,\Et,\mathcal O_E/\pi_E^n}L\bigr)\\
&\quad\cong Lp^*_{X,\Et,\mathcal O_E/\pi_E^n}c_{X,\mathcal O_E/\pi_E^n}R\Gamma_{X,\Et,\mathcal O_E/\pi_E^n}K\otimes^L_{\mathcal O_E/\pi_E^n}Lp^*_{Y,\Et,\mathcal O_E/\pi_E^n}c_{Y,\mathcal O_E/\pi_E^n}R\Gamma_{Y,\Et,\mathcal O_E/\pi_E^n}L\\
&\quad\xrightarrow{Lp^*_{X,\Et,\mathcal O_E/\pi_E^n}\varepsilon_K\otimes Lp^*_{Y,\Et,\mathcal O_E/\pi_E^n}\varepsilon_L}Lp^*_{X,\Et,\mathcal O_E/\pi_E^n}K\otimes^L_{\mathcal O_E/\pi_E^n}Lp^*_{Y,\Et,\mathcal O_E/\pi_E^n}L,
\end{aligned}
$$

in $D(Z_{\Et},\mathcal O_E/\pi_E^n)$. The first isomorphism is Lemma “Monoidality of constant complexes” (`pur7710-lem-constant-monoidal`) together with the identifications $Lp^*_{X,\Et,\mathcal O_E/\pi_E^n}c_{X,\mathcal O_E/\pi_E^n}\cong c_{Z,\mathcal O_E/\pi_E^n}$, $Lp^*_{Y,\Et,\mathcal O_E/\pi_E^n}c_{Y,\mathcal O_E/\pi_E^n}\cong c_{Z,\mathcal O_E/\pi_E^n}$, induced by the composition isomorphisms of inverse image (Lemma “Composition of étale inverse images” (`pur456-pbc-pullback-composition`, in [sk-thm-sf-comp-composition])) applied to the constant-sheaf functors, which are inverse images along the structure morphisms to $\operatorname{Spec}k$ followed by global constant modules; $\varepsilon$ is the counit of Lemma “Constant complexes and derived sections are adjoint” (`pur7710-lem-constant-adjunction`). It is natural in $K$ and $L$.
