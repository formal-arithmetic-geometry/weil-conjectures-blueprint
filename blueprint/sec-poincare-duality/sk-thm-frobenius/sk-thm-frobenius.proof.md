+++
kind  = "proof"
of    = "sk-thm-frobenius"
+++
*Step 1 (each ingredient is equivariant).* The mixed-support cup
product is induced by the tensor product of complexes and its
$\Gamma_c$-realization, both of which are lifted to Weil complexes by the
functoriality built into [sk-def-weil]; the evaluation is a morphism of
Weil objects; and the orientation of [sk-def-sf-orientation] is
Frobenius-equivariant, by the Weil equivariance of purity and trace
(whose target datum on the coefficient ring is the canonical one).
*Step 2 (the pairing is a morphism of Weil objects).* Composing, the
triple $\bigl(\RGammac(X,K),\RGamma(X,K^\vee(d))[2d],\Lambda\bigr)$ carries
the Weil data $\varphi_{c,K}$, $\varphi_{K^\vee(d)}$ and the canonical
data, and $\beta_K$ is a morphism of Weil objects from the tensor of the
first two to the last. Evaluated on the tensor of two vectors this reads
$\langle F_{c,K}x,F_{K^\vee(d)}y\rangle_i=F(\langle x,y\rangle_i)$; the
target datum is the canonical one, so $F$ acts on $\Lambda$ as the
identity by [sk-def-weil], which is the equivariance clause. Nothing
here depends on the coefficient stage: the identity holds for the
$\Lambda$-bilinear map induced by $\beta_K$ on cohomology at every
$\Lambda\in\{\AEn,\Oe,E,\Qlb\}$.
*Step 3 (eliminating the twist).* The second factor is
$H^{2d-i}(X,K^\vee)\otimes\Lambda(d)$, and
$\varphi_{K^\vee(d)}=\varphi_{K^\vee}\otimes\tau_d$, where $\tau_d$ is
the scalar $q^{-d}$ on the twist line; writing $y=y_0\otimes\xi_d$ under
that identification turns the identity of Step 2 into

$$
\langle F_{c,K}x,F_{K^\vee}y_0\rangle_i^{\mathrm{untw}}
=q^d\,\langle x,y_0\rangle_i^{\mathrm{untw}},
$$

because the untwisted pairing is a morphism into the value line
$\Lambda(-d)$ and $F$ acts on $\Lambda(-d)$ by $q^d$ by the
normalization of [sk-def-weil].
*Step 4 (reciprocity, field stages only).* This is the one step that
needs a field stage. Over a field coefficient stage the degreewise pairing is
perfect by [sk-thm-derived-duality], so the adjoint
$\Phi:H^{2d-i}(X,K^\vee)\to H^i_c(X,K)^\vee$, $\Phi(y)(x)=\langle
x,y\rangle_i^{\mathrm{untw}}$, is an isomorphism of finite-dimensional
vector spaces, and the similitude of Step 3 reads
$\Phi\circ F_{K^\vee}=q^d(F_{c,K}^{-1})^{\mathsf t}\circ\Phi$; hence
$F_{K^\vee}$ is conjugate to $q^d(F_{c,K}^{-1})^{\mathsf t}$. The
characteristic polynomial is invariant under transposition, so the
eigenvalues of $F$ on $H^{2d-i}(X,K^\vee)$ are the $q^d/\alpha$, with the
multiplicities of the eigenvalues $\alpha$ of $F$ on $H^i_c(X,K)$.
Over $\Oe$ the adjoint $\Phi$ is not an isomorphism in general (only the
derived duality holds, [sk-thm-sf-identification]), and the example in the
statement shows that (b) genuinely fails there; the derived equivariance of
Step 2 is all that survives at that stage. (The conjugacy alone holds
whenever the degreewise pairing is perfect, e.g. over $\AEn$ for proper
$X$ by [sk-thm-sf-identification], since $\Phi$ is then an
isomorphism of $\Lambda$-modules.) No step uses properness.
