+++
kind = "proof"
of = "lem-weil-pbc-compatible-pullback-sheaf-system"
uses = ["lem-weil-pbc-inverse-image-composition"]
+++
*(1) Identities.* For $f=1_i$ the composition comparison for $D(1_i)$ and $v_i$, transported along $D(1_i)=1_{D_i}$ and $v_i=v_i\circ1_{D_i}$, is the left unit law of [lem-weil-pbc-inverse-image-composition]; its inverse at $G$ is the identity comparison of inverse images. By induction on the equality $D(1_i)=1_{D_i}$ this gives exactly the transported identity comparison claimed for $a_{1_i}$.

*(2) Cocycle law.* For $f:i\to j$ and $g:j\to k$, apply the associativity coherence of the composition comparisons [lem-weil-pbc-inverse-image-composition] to the three morphisms $D(g^{op})$, $D(f^{op})$, $v_i$, with $D(f^{op})\circ D(g^{op})=D((g\circ f)^{op})$, $v_j=v_i\circ D(f^{op})$ and $v_k=v_i\circ D((g\circ f)^{op})$. Evaluated at $G$ and rearranged (cancelling one comparison isomorphism) it gives $a_{g\circ f}=a_g\circ D(g^{op})^{-1}(a_f)\circ\gamma$, where $\gamma$ is the comparison from the inverse image along the composite transition to $D(g^{op})^{-1}D(f^{op})^{-1}$; this is the cocycle law.

*(3) The cone.* Apply the same associativity coherence to $p_j$, $D(f^{op})$ and $v_i$, with the composites $p_i=D(f^{op})\circ p_j$ (the cone equation), $v_j$ and $v$. Composing the resulting equality on the left with $b_i$ and on the right with $b_j^{-1}$, the comparisons cancel and the transition $p_i^{-1}F_i\to p_j^{-1}F_j$ becomes the identity of $v^{-1}G$, which is the transition of the constant diagram.
