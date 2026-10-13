+++
id = "pur9-lem-push-projection-reduction"
kind = "lemma"
title = "Direct-image projection map and finite reduction"
order = 2224
tags = ["latex:bplemma"]
uses = ["pur713-def-star-projection", "pur9-input-reduction-monoidal"]
+++
Under Input [pur9-input-reduction-monoidal], for $p:\overline X\to Y$, $M\in D(\overline X_{\Proet},\mathcal O_E/\varpi^n)$ and $L\in D(Y_{\Proet},\mathcal O_E/\varpi^n)$,

$$
\begin{aligned}
&Rp_{*,\mathcal O_E/\varpi^m}(1\otimes r^*_{p,L})\circ Rp_{*,\mathcal O_E/\varpi^m}(r^\otimes)\circ r_{*,p,M\otimes^L_{\mathcal O_E/\varpi^n}Lp^*_{\mathcal O_E/\varpi^n}L}\circ\mathrm{red}_{n,m}(P_{p,M,L,\mathcal O_E/\varpi^n})\\
&\quad=P_{p,\mathrm{red}_{n,m}M,\mathrm{red}_{n,m}L,\mathcal O_E/\varpi^m}\circ(r_{*,p,M}\otimes1)\circ r^\otimes_{Rp_{*,\mathcal O_E/\varpi^n}M,L}
\end{aligned}
$$

as maps $\mathrm{red}_{n,m}(Rp_{*,\mathcal O_E/\varpi^n}M\otimes^L_{\mathcal O_E/\varpi^n}L)\to Rp_{*,\mathcal O_E/\varpi^m}(\mathrm{red}_{n,m}M\otimes^L_{\mathcal O_E/\varpi^m}Lp^*_{\mathcal O_E/\varpi^m}\mathrm{red}_{n,m}L)$ in $D(Y_{\Proet},\mathcal O_E/\varpi^m)$, with $P$ the finite-coefficient maps of Definition [pur713-def-star-projection] at levels $n$ and $m$.
