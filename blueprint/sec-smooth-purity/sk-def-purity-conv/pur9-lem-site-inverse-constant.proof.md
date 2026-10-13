+++
kind = "proof"
of = "pur9-lem-site-inverse-constant"
+++
$L\nu^*$ is the levelwise functor of the exact $\nu^*$, so it suffices to treat sheaves. For $G\in\mathsf{Sh}(W_{\Proet},\mathsf{Mod}_{\mathcal O_E/\varpi^n})$, Input “The site comparison is a morphism of sites” (`pur456-input-site-morphism`, see [sk-prop-sf-comp-coherence]) and the adjunction between constant sheaves and global sections on each site give natural bijections
$\operatorname{Hom}(\nu^*M_W,G)\cong\operatorname{Hom}(M_W,\nu_*G)\cong\operatorname{Hom}_{\mathcal O_E/\varpi^n}(M,(\nu_*G)(W))=\operatorname{Hom}_{\mathcal O_E/\varpi^n}(M,G(W))\cong\operatorname{Hom}(M_W,G)$,
the equality being Definition “Site-comparison direct image of sheaves” (`pur456-def-site-restriction`, see [sk-prop-sf-comp-coherence]) ($\nu_*$ is restriction along the inclusion of sites, and $W$ is the final object of both). The Yoneda lemma gives the isomorphism.
