+++
id = "pur7710-def-kunneth-map"
kind = "definition"
title = "The ordinary Künneth morphism at finite level"
order = 1994
uses = ["pur7710-def-exterior-product", "sk-thm-sf-comp-composition"]
+++
For $X,Y,Z,K,L$ as in Definition [pur7710-def-exterior-product], let

$$
\operatorname{Kun}_{\mathcal O_E/\varpi^n,K,L}:
R\Gamma_{X,\Et,\mathcal O_E/\varpi^n}K\otimes^L_{\mathcal O_E/\varpi^n}R\Gamma_{Y,\Et,\mathcal O_E/\varpi^n}L
\longrightarrow R\Gamma_{Z,\Et,\mathcal O_E/\varpi^n}(K\boxtimes^L_{\mathcal O_E/\varpi^n}L)
$$

be the morphism corresponding, under $c_{Z,\mathcal O_E/\varpi^n}\dashv R\Gamma_{Z,\Et,\mathcal O_E/\varpi^n}$ (Lemma “Constant complexes and derived sections are adjoint” (`pur7710-lem-constant-adjunction`)), to the composite

$$
\begin{aligned}
&c_{Z,\mathcal O_E/\varpi^n}\bigl(R\Gamma_{X,\Et,\mathcal O_E/\varpi^n}K\otimes^L_{\mathcal O_E/\varpi^n}R\Gamma_{Y,\Et,\mathcal O_E/\varpi^n}L\bigr)\\
&\quad\cong Lp^*_{X,\Et,\mathcal O_E/\varpi^n}c_{X,\mathcal O_E/\varpi^n}R\Gamma_{X,\Et,\mathcal O_E/\varpi^n}K\otimes^L_{\mathcal O_E/\varpi^n}Lp^*_{Y,\Et,\mathcal O_E/\varpi^n}c_{Y,\mathcal O_E/\varpi^n}R\Gamma_{Y,\Et,\mathcal O_E/\varpi^n}L\\
&\quad\xrightarrow{Lp^*_{X,\Et,\mathcal O_E/\varpi^n}\varepsilon_K\otimes Lp^*_{Y,\Et,\mathcal O_E/\varpi^n}\varepsilon_L}Lp^*_{X,\Et,\mathcal O_E/\varpi^n}K\otimes^L_{\mathcal O_E/\varpi^n}Lp^*_{Y,\Et,\mathcal O_E/\varpi^n}L,
\end{aligned}
$$

in $D(Z_{\Et},\mathcal O_E/\varpi^n)$. The first isomorphism is Lemma “Monoidality of constant complexes” (`pur7710-lem-constant-monoidal`) together with the identifications $Lp^*_{X,\Et,\mathcal O_E/\varpi^n}c_{X,\mathcal O_E/\varpi^n}\cong c_{Z,\mathcal O_E/\varpi^n}$, $Lp^*_{Y,\Et,\mathcal O_E/\varpi^n}c_{Y,\mathcal O_E/\varpi^n}\cong c_{Z,\mathcal O_E/\varpi^n}$, induced by the composition isomorphisms of inverse image (Lemma “Composition of étale inverse images” (`pur456-pbc-pullback-composition`, in [sk-thm-sf-comp-composition])) applied to the constant-sheaf functors, which are inverse images along the structure morphisms to $\operatorname{Spec}k$ followed by global constant modules; $\varepsilon$ is the counit of Lemma “Constant complexes and derived sections are adjoint” (`pur7710-lem-constant-adjunction`). It is natural in $K$ and $L$.
