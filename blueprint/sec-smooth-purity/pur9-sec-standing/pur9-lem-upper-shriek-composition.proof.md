+++
kind = "proof"
of = "pur9-lem-upper-shriek-composition"
uses = ["pur9-def-shriek-notation"]
+++
For $K\in D(X_{\Proet},\mathcal O_E/\varpi^n)$, consider the composite bijection

$$
\begin{aligned}
\operatorname{Hom}\bigl(K,R(gf)^!_{\mathcal O_E/\varpi^n}L\bigr)&\cong\operatorname{Hom}\bigl(R(gf)_{!,\mathcal O_E/\varpi^n}K,L\bigr)
\xrightarrow{-\circ\alpha_{g,f,K}}\operatorname{Hom}\bigl(Rg_{!,\mathcal O_E/\varpi^n}Rf_{!,\mathcal O_E/\varpi^n}K,L\bigr)\\
&\cong\operatorname{Hom}\bigl(K,Rf^!_{\mathcal O_E/\varpi^n}Rg^!_{\mathcal O_E/\varpi^n}L\bigr),
\end{aligned}
$$

Hom sets in $D(X_{\Proet},\mathcal O_E/\varpi^n)$ and $D(S_{\Proet},\mathcal O_E/\varpi^n)$: the outer bijections are the standing adjunctions of Definition [pur9-def-shriek-notation] for $gf$, and for $g$ followed by $f$; the middle one is a bijection because $\alpha_{g,f,K}$ is an isomorphism (Input [pur9-input-ambient-composition]). The composite is natural in $K$ and $L$, since $\alpha_{g,f}$ and the adjunction bijections are. Evaluated at $K=R(gf)^!_{\mathcal O_E/\varpi^n}L$ on the identity it gives the image of $\varepsilon_{gf,L}\circ\alpha_{g,f}$ under the composite adjunction, which is $c_{g,f,L}$ of Definition [pur9-def-upper-shriek-composition]. By the Yoneda lemma, a natural bijection $\operatorname{Hom}(-,A)\cong\operatorname{Hom}(-,B)$ is composition with a unique isomorphism $A\to B$, and this isomorphism is the image of $\mathrm{id}_A$; hence $c_{g,f,L}$ is an isomorphism, natural in $L$.
