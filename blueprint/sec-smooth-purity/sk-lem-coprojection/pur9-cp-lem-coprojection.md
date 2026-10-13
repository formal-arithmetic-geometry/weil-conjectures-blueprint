+++
id = "pur9-cp-lem-coprojection"
kind = "lemma"
title = "Co-projection for a closed immersion"
order = 2346
tags = ["latex:bplemma"]
uses = ["pur713-input-proper-adjoint", "pur9-cs-def-invertible", "pur9-cs-input-constructible-closure", "pur9-def-shriek-notation", "pur9-input-preservation", "pur9-lem-proet-projection-formula"]
+++
Assume Inputs [pur713-input-proper-adjoint], [pur9-input-preservation] and [pur9-cs-input-constructible-closure] and the hypotheses of Lemma [pur9-lem-proet-projection-formula]. Let $i:Z\hookrightarrow X$ be a closed immersion, $K\in D^b_{ctf}(X_{\Proet},\mathcal O_E/\varpi^n)$, and $(L,L',e)$ an invertible object (Definition [pur9-cs-def-invertible]) with $L,L'\in D^b_{ctf}(X_{\Proet},\mathcal O_E/\varpi^n)$. There is a unique isomorphism

$$
\chi_{i,K,L}:Ri^!_{\mathcal O_E/\varpi^n}(K\otimes^L_{\mathcal O_E/\varpi^n}L)\xrightarrow{\sim}Ri^!_{\mathcal O_E/\varpi^n}K\otimes^L_{\mathcal O_E/\varpi^n}Li^*_{\mathcal O_E/\varpi^n}L
$$

in $D(Z_{\Proet},\mathcal O_E/\varpi^n)$ such that, for every $A\in D^b_c(Z_{\Proet},\mathcal O_E/\varpi^n)$, composition with $\chi_{i,K,L}$ is the composite of the natural bijections

$$
\begin{aligned}
\operatorname{Hom}(A,Ri^!_{\mathcal O_E/\varpi^n}(K\otimes L))&\cong\operatorname{Hom}(Ri_{!,\mathcal O_E/\varpi^n}A,K\otimes L)\cong\operatorname{Hom}(Ri_{!,\mathcal O_E/\varpi^n}A\otimes L',K)\\
&\cong\operatorname{Hom}(Ri_{!,\mathcal O_E/\varpi^n}(A\otimes Li^*_{\mathcal O_E/\varpi^n}L'),K)\cong\operatorname{Hom}(A\otimes Li^*_{\mathcal O_E/\varpi^n}L',Ri^!_{\mathcal O_E/\varpi^n}K)\cong\operatorname{Hom}(A,Ri^!_{\mathcal O_E/\varpi^n}K\otimes Li^*_{\mathcal O_E/\varpi^n}L),
\end{aligned}
$$

all functors at the coefficient $\mathcal O_E/\varpi^n$ and standing as in Definition [pur9-def-shriek-notation].
