+++
kind  = "proof"
of    = "def-sfb-module-derived-pushpull-adjunction"
+++
This is the general derivation of adjunctions: let $F\dashv G$ be additive functors
between abelian categories, $F\colon\mathcal C\to\mathcal D$, where $F$ is left
derivable via K-flat resolutions and $G$ right derivable via K-injective resolutions
([sk-def-sfb-derived-categories]). The adjunction $F\dashv G$ induces an adjunction
$K(F)\dashv K(G)$ on homotopy categories of complexes. Composing the counit of $LF$,
$LF\circ Q\to Q\circ K(F)$, with the unit of $RG$, $Q\circ K(G)\to RG\circ Q$, and with
the unit and counit of $K(F)\dashv K(G)$ gives natural maps
$\mathrm{id}\to RG\circ LF$ and $LF\circ RG\to\mathrm{id}$ on the derived categories;
evaluating on K-flat resp. K-injective representatives, where the counit of $LF$ and
the unit of $RG$ are isomorphisms, shows the triangle identities. Apply this to
$f^*\dashv f_*$; the K-flat hypothesis on $f^*$ is
[lem-sfb-module-upper-star-kflat-quasi-iso].
