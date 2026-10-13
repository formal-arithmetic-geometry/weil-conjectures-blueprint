+++
kind = "proof"
of = "pur9-lem-closed-push-fully-faithful"
uses = ["pur9-lem-closed-push-levelwise"]
+++
By Lemma [pur9-lem-closed-push-levelwise], the counit $\varepsilon_A:Li^*_{\mathcal O_E/\varpi^n}Ri_{*,\mathcal O_E/\varpi^n}A\to A$ of $Li^*_{\mathcal O_E/\varpi^n}\dashv Ri_{*,\mathcal O_E/\varpi^n}$ is induced termwise by the sheaf counit, which is an isomorphism by Input [pur9-input-closed-immersion]; so $\varepsilon$ is an isomorphism. The map $\operatorname{Hom}(A,B)\to\operatorname{Hom}(Ri_{*,\mathcal O_E/\varpi^n}A,Ri_{*,\mathcal O_E/\varpi^n}B)\cong\operatorname{Hom}(Li^*_{\mathcal O_E/\varpi^n}Ri_{*,\mathcal O_E/\varpi^n}A,B)$, composed with the adjunction bijection, sends $\phi$ to $\varepsilon_B\circ Li^*_{\mathcal O_E/\varpi^n}Ri_{*,\mathcal O_E/\varpi^n}\phi=\phi\circ\varepsilon_A$, by naturality of $\varepsilon$. Precomposition with the isomorphism $\varepsilon_A$ is bijective, hence so is the action of $Ri_{*,\mathcal O_E/\varpi^n}$ on morphisms.
