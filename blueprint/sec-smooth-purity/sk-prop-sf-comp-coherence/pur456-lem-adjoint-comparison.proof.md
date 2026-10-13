+++
kind = "proof"
of = "pur456-lem-adjoint-comparison"
+++
For fixed $L$, the displayed condition says that the bijection

$$
\operatorname{Hom}(K,Rf^!_TL)\cong\operatorname{Hom}(Rf_{!,T}K,L)\xrightarrow{-\circ\theta_{d,T,K}}\operatorname{Hom}(R_{d,T}K,L)\cong\operatorname{Hom}(K,R^!_{d,T}L),
$$

built from the two adjunctions of Lemma [pur713-lem-shriek-adjunction-module] and the isomorphism $\theta_{d,T,K}$, is composition with $\theta^!_{d,T,L}$. This bijection is natural in $K$ because $\theta_{d,T}$ and the adjunction bijections are natural. By the Yoneda lemma it is composition with a unique morphism $Rf^!_TL\to R^!_{d,T}L$, namely its value on $\mathrm{id}_{Rf^!_TL}$, and this morphism is an isomorphism because the bijection is induced by an isomorphism of representing objects. That value is the $d$-adjoint of $\varepsilon_{f,L}\circ\theta_{d,T,Rf^!_TL}$, which by the description of the adjunction bijection through the unit $\eta_d$ is the displayed composite. Naturality in $L$ follows from naturality of the bijection in $L$.
