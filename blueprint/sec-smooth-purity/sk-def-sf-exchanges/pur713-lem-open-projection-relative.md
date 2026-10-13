+++
id = "pur713-lem-open-projection-relative"
kind = "lemma"
title = "Relative open-extension projection formula"
order = 1870
tags = ["latex:bplemma"]
uses = ["pur713-lem-module-pull-monoidal", "pur713-lem-open-adjunction-underived"]
+++
Under the inputs of Lemma [pur713-lem-open-adjunction-underived], for an open immersion $j:U\hookrightarrow X$, $T\in\{\mathcal O_E,E,\overline{\mathbf Q}_\ell\}$, an $\mathcal R_{X,T}$-module $N$ and an $\mathcal R_{U,T}$-module $M$, the map

$$
\pi^T_{j,N,M}:j_{!,T}(j^*_TN\otimes_{\mathcal R_{U,T}}M)\longrightarrow N\otimes_{\mathcal R_{X,T}}j_{!,T}M,
$$

defined as the adjoint under Lemma [pur713-lem-open-adjunction-underived] of $1\otimes\mathrm{unit}$ followed by the monoidal comparison $j^*_TN\otimes j^*_Tj_{!,T}M\cong j^*_T(N\otimes j_{!,T}M)$ of Lemma [pur713-lem-module-pull-monoidal], is a natural isomorphism.
