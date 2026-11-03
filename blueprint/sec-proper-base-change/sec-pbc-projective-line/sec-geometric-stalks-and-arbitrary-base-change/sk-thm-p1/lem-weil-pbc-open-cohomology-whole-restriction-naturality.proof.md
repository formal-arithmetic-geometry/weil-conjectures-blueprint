+++
kind = "proof"
of = "lem-weil-pbc-open-cohomology-whole-restriction-naturality"
uses = ["lem-weil-pbc-cohomology-pullback-functorial", "lem-weil-pbc-inverse-image-composition"]
+++
By the functoriality of cohomology pullback under composition [lem-weil-pbc-cohomology-pullback-functorial], for composable $a,b$ and $c=b\circ a$ one has $a^*(b^*x)=\theta_{a,b}(c^*x)$, where $\theta_{a,b}$ is induced by the composition isomorphism $c^{-1}\cong a^{-1}b^{-1}$ of [lem-weil-pbc-inverse-image-composition]. Apply this to $(a,b)=(g_W,j_W)$ and to $(a,b)=(j'_W,g)$; both composites are the same morphism $c=j_W\circ g_W=g\circ j'_W:g^{-1}W\to X$. Thus
$$g_W^*(j_W^*x)=\theta_{g_W,j_W}(c^*x),\qquad j'^*_W(g^*x)=\theta_{j'_W,g}(c^*x).$$
Since $\theta_{g_W,j_W}$ is induced by an isomorphism, applying the map induced by its inverse to the first identity gives $c^*x$, and then applying $\theta_{j'_W,g}$ gives $j'^*_W(g^*x)$. By definition of $P_W$ (and since cohomology of a composite of coefficient maps is the composite of the induced maps) this composite is $P_W(j_W^*x)$.
