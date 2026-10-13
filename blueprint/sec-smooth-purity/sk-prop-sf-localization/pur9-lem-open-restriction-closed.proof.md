+++
kind = "proof"
of = "pur9-lem-open-restriction-closed"
uses = ["pur9-lem-closed-push-levelwise"]
+++
By Lemmas “The finite-coefficient derived inverse image is levelwise” (`pur713-lem-finite-pull-levelwise`) and [pur9-lem-closed-push-levelwise] it suffices to treat a sheaf $G$ on $Z_{\Proet}$. By Input “Inverse image along a weakly étale morphism” (`pur713-input-fixed-weakly-etale`), $j^*$ is restriction along the localization functor, so for $W\in U_{\Proet}$, $(j^*i_*G)(W)=G(W\times_XZ)$ by Definition “Fixed-coefficient direct image” (`pur713-def-sheaf-push`); as $W\to X$ factors through $U$, $W\times_XZ$ is empty, and a sheaf of modules has zero sections on the empty object. The second assertion follows from the adjunction $Lj^*_{\mathcal O_E/\varpi^n}\dashv Rj_{*,\mathcal O_E/\varpi^n}$ of Lemma “Finite-coefficient derived inverse-image adjunction” (`pur713-lem-star-adjunction`).
