+++
kind = "proof"
of = "lem-weil-pbc-finite-etale-graph-clopen"
+++
For $a$ with $q\circ a=p$, the graph $s_a=(a,\mathrm{id}_U):U\to P$ is a section of the projection $r$, which is finite etale as a base change of $q$. The section $s_a$ is etale by cancellation (both $r\circ s_a=\mathrm{id}$ and $r$ are etale), a monomorphism because it has a retraction, hence an open immersion; and it is a closed immersion because $r$ is separated. So its image $W_a$ is open and closed. The open immersion $s_a$ identifies $U$ with the open subscheme $W_a$, and the inverse of this identification is $r|_{W_a}$, which is therefore an isomorphism.

Conversely, given such a clopen $W$, compose the inverse of $r|_W$ with the inclusion $W\to P$ and the first projection $P\to V$ to get $a_W:U\to V$; the pullback identities give $q\circ a_W=p$, and the graph of $a_W$ is the inverse of $r|_W$ followed by the inclusion, whose image is $W$.

The two constructions are inverse. If $W_a=W_b$, the open immersions $s_a$ and $s_b$ have the same image, so $s_b=s_a\circ\theta$ for an isomorphism $\theta$ of $U$; composing with $r$ gives $\theta=\mathrm{id}_U$, so $s_a=s_b$ and $a=b$. Surjectivity was shown above. Empty $U$ or $V$ is allowed.
