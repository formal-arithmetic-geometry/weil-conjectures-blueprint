+++
kind = "proof"
of = "pur9-lem-tor-pullback"
uses = ["pur9-lem-flat-model"]
+++
By Lemma [pur9-lem-flat-model], $H$ is represented by a complex $P$ of flat sheaves in degrees $[u,v]$. Inverse image is exact and strong monoidal, and preserves flatness of sheaves: $f^*Q\otimes M$ has geometric stalk $Q_{f(\bar x)}\otimes M_{\bar x}$ (Lemma “Stalks of étale inverse image” (`pur456-pbc-pullback-stalk`, see [sk-thm-sf-comp-composition])), and the stalk of a flat sheaf is a flat module, since every module is the stalk of a constant sheaf and stalks are exact. Hence $f^*P$ is a complex of flat sheaves in degrees $[u,v]$, and Lemma [pur9-lem-flat-model] applies again.
