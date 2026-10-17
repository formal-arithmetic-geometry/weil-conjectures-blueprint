+++
kind = "proof"
of = "det-sp-defect-closed-vanishing"
uses = ["det-sp-defect-definition", "det-sp-defect-proper-smooth", "det-sp-constant-family-vanishing"]
+++
For the pair $(Z,Z)$ the ideal is zero, so $\mathcal D_ZZ=Z\times S$, with special fibre $Z$ and
zero section the identity. The pullback exchange along the identity is the identity, so
$\epsilon_{Z,Z}(M)$ is the specialization unit $\sigma_Z(M)$ followed by its inverse; by
[det-sp-constant-family-vanishing] this is the identity, and $C_{Z,Z}=0$.

The closed immersion $i$ is proper and $i^{-1}Z=Z$ schematically, so the proper case of
[det-sp-defect-proper-smooth] gives $C_{X,Z}(i_*M)\simeq C_{Z,Z}(M)=0$ (here $f_Z$ is the identity
of $Z$).

Finally apply the exact functor $C_{X,Z}$ to the triangle $j_!j^*L\to L\to i_*i^*L$. The third term
goes to zero, so the first map becomes an isomorphism.
