+++
kind  = "proof"
of    = "prop-nagata-global-blowup-cover-independent"
+++
By [def-nagata-global-blowup-glue-data], for affine opens $W\subseteq V$
the square formed by the transition map
$\mathsf B_W(\mathcal I)\to\mathsf B_V(\mathcal I)$, the structure
morphisms and the inclusion $W\subseteq V$ is cartesian. Hence every
transition map is an open immersion (a base change of the open immersion
$W\to V$) whose image is the preimage of $W$ in $\mathsf B_V(\mathcal I)$.

**Gluing.** Glue the schemes $\mathsf B_V(\mathcal I)$ along these open
immersions. For two affine opens $V,V'$, the preimages of $V\cap V'$ in
$\mathsf B_V(\mathcal I)$ and in $\mathsf B_{V'}(\mathcal I)$ are both
covered by the images of $\mathsf B_W(\mathcal I)$, $W\subseteq V\cap V'$
affine, and they are identified with each other through these common
pieces. Since the index set is a poset and the diagram is a functor, all
identifications are composites of transition maps; they agree on overlaps
(again covered by affine $W$), and the cocycle condition holds
automatically. The result is the colimit $\operatorname{Bl}_{\mathcal I}(X)$
of [def-nagata-global-blowup], and the colimit maps
$\iota_V\colon\mathsf B_V(\mathcal I)\to\operatorname{Bl}_{\mathcal I}(X)$
are open immersions with $\iota_W=\iota_V\circ(\text{transition})$ for
$W\subseteq V$.

**The morphism $b_{X,\mathcal I}$ and (1).** The composites
$\mathsf B_V(\mathcal I)\to V\subseteq X$ are compatible with the
transition maps by [def-nagata-global-blowup-glue-data], so they induce a
morphism $b_{X,\mathcal I}$ out of the colimit with
$b_{X,\mathcal I}\circ\iota_V$ equal to the structure morphism followed by
$V\subseteq X$. This is (1).

**(2).** By (1), the image of $\iota_V$ lies in $b_{X,\mathcal I}^{-1}(V)$.
Conversely, a point of $b_{X,\mathcal I}^{-1}(V)$ lies in the image of
some $\iota_{V'}$, hence, by (1) for $V'$, in $\iota_{V'}$ of the preimage
of $V\cap V'$ in $\mathsf B_{V'}(\mathcal I)$. Choose an affine
$W\subseteq V\cap V'$ around the image point in $X$. The preimage of $W$
in $\mathsf B_{V'}(\mathcal I)$ is the image of $\mathsf B_W(\mathcal I)$,
so the point lies in the image of $\iota_W=\iota_V\circ(\text{transition})$,
hence in the image of $\iota_V$.

**(3).** By (2), $\iota_V$ is an open immersion onto
$b_{X,\mathcal I}^{-1}(V)$, hence an isomorphism
$\mathsf B_V(\mathcal I)\cong b_{X,\mathcal I}^{-1}(V)$, and by (1) it is
compatible with the morphisms to $V$. This says exactly that the square is
cartesian.
