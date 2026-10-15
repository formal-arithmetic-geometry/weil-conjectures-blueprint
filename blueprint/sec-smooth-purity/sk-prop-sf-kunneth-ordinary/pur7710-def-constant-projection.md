+++
id = "pur7710-def-constant-projection"
kind = "definition"
title = "The constant-tensor comparison"
order = 1991
+++
For a scheme $W$, $K\in D(W_{\Et},\mathcal O_E/\varpi^n)$ and $M\in D(\mathsf{Mod}_{\mathcal O_E/\varpi^n})$, define

$$
P_{W,\mathcal O_E/\varpi^n,K,M}:
R\Gamma_{W,\Et,\mathcal O_E/\varpi^n}K\otimes^L_{\mathcal O_E/\varpi^n}M
\longrightarrow R\Gamma_{W,\Et,\mathcal O_E/\varpi^n}
(K\otimes^L_{\mathcal O_E/\varpi^n}c_{W,\mathcal O_E/\varpi^n}M)
$$

as the morphism corresponding, under the adjunction of Lemma “Constant complexes and derived sections are adjoint” (`pur7710-lem-constant-adjunction`), to the composite

$$
\begin{aligned}
c_{W,\mathcal O_E/\varpi^n}\bigl(R\Gamma_{W,\Et,\mathcal O_E/\varpi^n}K\otimes^L_{\mathcal O_E/\varpi^n}M\bigr)
&\cong c_{W,\mathcal O_E/\varpi^n}R\Gamma_{W,\Et,\mathcal O_E/\varpi^n}K\otimes^L_{\mathcal O_E/\varpi^n}c_{W,\mathcal O_E/\varpi^n}M\\
&\xrightarrow{\varepsilon_K\otimes1}K\otimes^L_{\mathcal O_E/\varpi^n}c_{W,\mathcal O_E/\varpi^n}M,
\end{aligned}
$$

in $D(W_{\Et},\mathcal O_E/\varpi^n)$, where the first map is Lemma “Monoidality of constant complexes” (`pur7710-lem-constant-monoidal`), and $\varepsilon$ is the counit of Lemma “Constant complexes and derived sections are adjoint” (`pur7710-lem-constant-adjunction`). It is a natural morphism in $D(\mathsf{Mod}_{\mathcal O_E/\varpi^n})$.
