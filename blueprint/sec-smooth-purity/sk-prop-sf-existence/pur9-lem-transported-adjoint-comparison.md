+++
id = "pur9-lem-transported-adjoint-comparison"
kind = "lemma"
title = "Comparison of the exceptional functor with the transported functor"
order = 2147
tags = ["latex:bplemma"]
uses = ["pur713-input-proper-adjoint", "pur9-def-standing-choices", "pur9-input-etale-exceptional-adjoint"]
+++
Assume Inputs [pur713-input-proper-adjoint], “The bounded-below site-comparison theorem” (`pur7710-input-site-unit`, see [sk-prop-sf-comp-coherence]), “The qcqs direct-image comparison theorem” (`pur7710-input-qcqs-comparison`, see [sk-prop-sf-comp-coherence]) and [pur9-input-etale-exceptional-adjoint]. Let $f:X\to Y$ be as in Definition [pur9-def-standing-choices] and $L\in D^+(Y_{\Proet},\mathcal O_E/\varpi^n)$, and suppose that

1. $Rf^!_{\mathcal O_E/\varpi^n}L$ lies in $\mathscr E^+(X_{\Proet},\mathcal O_E/\varpi^n)$ (Definition “The bounded-below étale-origin subcategory” (`pur456-def-etale-origin`, see [sk-prop-sf-comp-coherence])), and
1. $f^{\times}R\nu_{Y,*,\mathcal O_E/\varpi^n}L$ lies in $D^+(X_{\Et},\mathcal O_E/\varpi^n)$.

Then there is a unique isomorphism $\phi_L:Rf^!_{\mathcal O_E/\varpi^n}L\to f^{\mathrm{tr}}L$ in $D(X_{\Proet},\mathcal O_E/\varpi^n)$ such that, for every $G\in D^+(X_{\Et},\mathcal O_E/\varpi^n)$, composition with $\phi_L$ is the composite bijection

$$
\begin{aligned}
\operatorname{Hom}\bigl(L\nu^*_{X,\mathcal O_E/\varpi^n}G,Rf^!_{\mathcal O_E/\varpi^n}L\bigr)
&\cong\operatorname{Hom}\bigl(Rf_{!,\mathcal O_E/\varpi^n}L\nu^*_{X,\mathcal O_E/\varpi^n}G,L\bigr)
\cong\operatorname{Hom}\bigl(L\nu^*_{Y,\mathcal O_E/\varpi^n}Rf_{!,\Et,\mathcal O_E/\varpi^n}G,L\bigr)\\
&\cong\operatorname{Hom}\bigl(Rf_{!,\Et,\mathcal O_E/\varpi^n}G,R\nu_{Y,*,\mathcal O_E/\varpi^n}L\bigr)
\cong\operatorname{Hom}\bigl(G,f^{\times}R\nu_{Y,*,\mathcal O_E/\varpi^n}L\bigr)\\
&\cong\operatorname{Hom}\bigl(L\nu^*_{X,\mathcal O_E/\varpi^n}G,f^{\mathrm{tr}}L\bigr),
\end{aligned}
$$

each Hom taken in $D(X_{\Proet},\mathcal O_E/\varpi^n)$, $D(Y_{\Proet},\mathcal O_E/\varpi^n)$, $D(Y_{\Et},\mathcal O_E/\varpi^n)$ or $D(X_{\Et},\mathcal O_E/\varpi^n)$ according to its objects.
