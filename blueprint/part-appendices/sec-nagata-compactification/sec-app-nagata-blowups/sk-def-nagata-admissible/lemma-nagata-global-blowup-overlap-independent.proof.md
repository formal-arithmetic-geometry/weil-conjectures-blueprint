+++
kind  = "proof"
of    = "lemma-nagata-global-blowup-overlap-independent"
+++
The transition morphisms of [def-nagata-global-blowup-local-model] form a
functor, so $r_{V,W}=r_{V,U}\circ r_{U,W}$ for $V=V_i,V_j$ (this is
[lemma-nagata-affine-blowup-restrict-cocycle]). Hence
$\omega_{ij,U}\circ r_{V_i,W}=r_{V_j,U}\circ r_{V_i,U}^{-1}\circ
r_{V_i,U}\circ r_{U,W}=r_{V_j,W}$. Since $r_{V_i,W}$ and $r_{V_j,W}$ are
isomorphisms onto $\mathsf B_{V_i}(\mathcal I)|_W$ and
$\mathsf B_{V_j}(\mathcal I)|_W$, the morphism $\omega_{ij,U}$ maps the
first onto the second and agrees there with
$r_{V_j,W}\circ r_{V_i,W}^{-1}=\omega_{ij,W}$. Applying this to $U$ and to
$U'$ gives the last assertion.
