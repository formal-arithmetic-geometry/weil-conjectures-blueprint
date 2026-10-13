+++
kind = "proof"
of = "pur713-lem-open-exchange"
+++
All functors involved are exact and levelwise (Lemmas “The finite-coefficient derived inverse image is levelwise” (`pur713-lem-finite-pull-levelwise`) and “Finite-coefficient derived open-extension adjunction” (`pur713-lem-open-adjunction`)), so it suffices to treat sheaves. On sheaves, $\bar g^*_{\mathcal O_E/\varpi^n}j_{!,\mathcal O_E/\varpi^n}$ and $j'_{!,\mathcal O_E/\varpi^n}g'^*_{\mathcal O_E/\varpi^n}$ are left adjoint to $j^*_{\mathcal O_E/\varpi^n}\bar g_{*,\mathcal O_E/\varpi^n}$ and $g'_{*,\mathcal O_E/\varpi^n}j'^*_{\mathcal O_E/\varpi^n}$ respectively (Inputs “Adjunction and exactness of fixed-coefficient images” (`pur713-input-fixed-adjunction`) and “Fixed-coefficient open-extension adjunction” (`pur713-input-open-fixed`)). By Input “Inverse image along a weakly étale morphism” (`pur713-input-fixed-weakly-etale`), $j^*$ and $j'^*$ are restrictions along localization, so by Definition “Fixed-coefficient direct image” (`pur713-def-sheaf-push`), for $G$ on $\overline X'_{\Proet}$ and $W\in X_{\Proet}$,

$$
(j^*\bar g_*G)(W)=G(W\times_{\overline X}\overline X'),\qquad
(g'_*j'^*G)(W)=G(W\times_XX'),
$$

and $W\times_{\overline X}\overline X'\cong W\times_XX'$ canonically over $\overline X'$, because $X'=X\times_{\overline X}\overline X'$. The right adjoints are therefore canonically isomorphic, and so are the left adjoints. The map $b'$ is, by construction, the mate of this isomorphism of right adjoints: the composition isomorphisms $\mu$ are the mates of the direct-image composition isomorphisms (Definition “Composition comparison for finite-coefficient derived inverse image” (`pur713-def-pull-composition`) and Input “Composition of fixed-coefficient images” (`pur713-input-fixed-composition`)), and the unit of the open adjunction is the unit used in forming mates. Hence $b'$ is an isomorphism.
