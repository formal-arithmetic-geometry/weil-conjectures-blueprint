+++
kind = "proof"
of = "pur9-cs-lem-bc"
uses = ["pur713-lem-monoidal-pullback", "pur9-cs-input-bc-phi", "pur9-cs-input-constructible-closure", "pur9-cs-lem-tensor-formula"]
+++
By Input [pur9-cs-input-bc-phi], $b_{v,K}\circ Lu^*_{\mathcal O_E/\varpi^n}(\varphi_{f,K})=\varphi_{f',Lv^*_{\mathcal O_E/\varpi^n}K}\circ\beta'_K$. The maps $\varphi_{f,K}$ and $\varphi_{f',Lv^*_{\mathcal O_E/\varpi^n}K}$ are isomorphisms by Lemma [pur9-cs-lem-tensor-formula] (note $Lv^*_{\mathcal O_E/\varpi^n}K\in D^b_{ctf}(Y'_{\Proet},\mathcal O_E/\varpi^n)$ by Input [pur9-cs-input-constructible-closure]), and $\beta'_K$ is an isomorphism because its factors are those of Lemmas [pur713-lem-monoidal-pullback], “The finite-coefficient inverse-image composition comparison is invertible” (`pur713-lem-pull-composition`) and [pur9-cs-lem-bc-dualizing]. Hence $b_{v,K}$ is an isomorphism.
