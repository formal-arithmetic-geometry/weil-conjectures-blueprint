+++
id = "pur7710-def-constant-projection"
kind = "definition"
title = "The constant-tensor comparison"
order = 3084
+++
For a scheme $W$, $K\in D(W_{\Et},\mathcal O_E/\pi_E^n)$ and $M\in D(\mathsf{Mod}_{\mathcal O_E/\pi_E^n})$, define

$$
P_{W,\mathcal O_E/\pi_E^n,K,M}:
R\Gamma_{W,\Et,\mathcal O_E/\pi_E^n}K\otimes^L_{\mathcal O_E/\pi_E^n}M
\longrightarrow R\Gamma_{W,\Et,\mathcal O_E/\pi_E^n}
(K\otimes^L_{\mathcal O_E/\pi_E^n}c_{W,\mathcal O_E/\pi_E^n}M)
$$

as the morphism corresponding, under the adjunction of Lemma “Constant complexes and derived sections are adjoint” (`pur7710-lem-constant-adjunction`), to the composite

$$
\begin{aligned}
c_{W,\mathcal O_E/\pi_E^n}\bigl(R\Gamma_{W,\Et,\mathcal O_E/\pi_E^n}K\otimes^L_{\mathcal O_E/\pi_E^n}M\bigr)
&\cong c_{W,\mathcal O_E/\pi_E^n}R\Gamma_{W,\Et,\mathcal O_E/\pi_E^n}K\otimes^L_{\mathcal O_E/\pi_E^n}c_{W,\mathcal O_E/\pi_E^n}M\\
&\xrightarrow{\varepsilon_K\otimes1}K\otimes^L_{\mathcal O_E/\pi_E^n}c_{W,\mathcal O_E/\pi_E^n}M,
\end{aligned}
$$

in $D(W_{\Et},\mathcal O_E/\pi_E^n)$, where the first map is Lemma “Monoidality of constant complexes” (`pur7710-lem-constant-monoidal`), and $\varepsilon$ is the counit of Lemma “Constant complexes and derived sections are adjoint” (`pur7710-lem-constant-adjunction`). It is a natural morphism in $D(\mathsf{Mod}_{\mathcal O_E/\pi_E^n})$.
