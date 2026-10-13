+++
kind = "proof"
of = "pur9-lem-orientation-concentration"
uses = ["pur9-lem-a1-acyclic-proet", "pur9-lem-gm-degree-zero-proet", "pur9-lem-gm-kummer-generator-proet", "pur9-lem-gm-vanishing-proet", "pur9-lem-orientation-triangle"]
+++
Take cohomology sheaves of the triangle of Lemma [pur9-lem-orientation-triangle], with $j^*_{\mathcal O_E/\varpi^n}L_1=(\mathcal O_E/\varpi^n)_{\mathbf G_{m,Y}}(1)$. By Lemma [pur9-lem-a1-acyclic-proet] the middle term has cohomology $(\mathcal O_E/\varpi^n)_Y(1)$ in degree $0$ only. By Lemmas [pur9-lem-gm-degree-zero-proet], [pur9-lem-gm-kummer-generator-proet] and [pur9-lem-gm-vanishing-proet] the third term has $\mathcal H^0\cong(\mathcal O_E/\varpi^n)_Y(1)$, $\mathcal H^1\cong(\mathcal O_E/\varpi^n)_Y$, and nothing else, and the degree-zero map between them is the restriction isomorphism of Lemma [pur9-lem-gm-degree-zero-proet]. The long exact sequence gives $\mathcal H^m(Rs^!_{\mathcal O_E/\varpi^n}L_1)=0$ for $m\neq2$.
