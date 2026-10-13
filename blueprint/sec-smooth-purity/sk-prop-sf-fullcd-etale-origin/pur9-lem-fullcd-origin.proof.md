+++
kind = "proof"
of = "pur9-lem-fullcd-origin"
uses = ["pur7710-lem-proper-interval"]
+++
A geometric fibre of $p'$ over a geometric point $\bar y'$ of $Y'$ is the base change of the geometric fibre of $p$ over the image of $\bar y'$ to a larger algebraically closed field, so it has dimension at most $e$. The morphism $p'$ is proper. Lemma [pur7710-lem-proper-interval], applied to $p'$, shows that $Rp'_{*,\Et,\mathcal O_E/\varpi^n}M$ has cohomology only in degrees $[0,2e]$. Since $p'$ is quasi-compact and quasi-separated and $M\in D^+(\overline X'_{\Et},\mathcal O_E/\varpi^n)$, Input “The qcqs direct-image comparison theorem” (`pur7710-input-qcqs-comparison`, see [sk-prop-sf-comp-coherence]) makes the map $\lambda_{p',M}$ of Definition “The canonical direct-image comparison” (`pur7710-def-direct-image-comparison`, see [sk-prop-sf-comp-coherence]) an isomorphism
$L\nu^*_{Y',\mathcal O_E/\varpi^n}Rp'_{*,\Et,\mathcal O_E/\varpi^n}M\cong Rp'_{*,\mathcal O_E/\varpi^n}L\nu^*_{\overline X',\mathcal O_E/\varpi^n}M$.
The functor $L\nu^*_{Y',\mathcal O_E/\varpi^n}$ is the levelwise functor of an exact functor (Definition “The derived site inverse image” (`pur456-def-site-inverse-derived`, see [sk-prop-sf-comp-coherence])), so it commutes with cohomology sheaves and the vanishing transports.
