+++
kind  = "proof"
of    = "lem-exc-open-closed-detection"
+++
Take a section $s\in F(W)$ on an affine basis object, using
[lem-weil-pbc-ind-etale-basis]. By [lem-exc-closed-localization], its closed
restriction is computed by the local closed immersion $Z_W\subset W$. The
presheaf map in [lem-exc-closed-inverse-image-formula] sends it to the
restriction of $s$ in $F(v_W(Z_W))$. Since $i^*F=0$, this element is locally
zero before sheafification: the kernel of the map from a presheaf to its
associated sheaf consists of locally zero sections. Select a finite basis
covering $\{V_a\to Z_W\}$ on which it is zero. Restriction along
$v_W(V_a)\to v_W(Z_W)\to W$, with the counit of
[lem-exc-closed-site-adjunction], shows that $s$ is zero on each $v_W(V_a)$.

Extend this to a covering of $W$ by [lem-exc-closed-cover-extension]. On its
open members the section is zero because $j^*F=0$. The sheaf axiom now gives
$s=0$, proving the assertion.
