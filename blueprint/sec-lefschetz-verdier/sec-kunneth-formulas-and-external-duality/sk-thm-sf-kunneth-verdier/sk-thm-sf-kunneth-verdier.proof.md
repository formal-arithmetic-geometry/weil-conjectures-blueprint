+++
kind = "proof"
of = "sk-thm-sf-kunneth-verdier"
uses = ["sk-lem-sf-kunneth-star", "sk-thm-pd-verdier-duality", "sk-thm-sf-ctf-stability", "sk-def-sf-kv-maps", "sk-lem-sf-flat-model", "sk-lem-sf-mate", "sk-prop-sf-closed-unit", "sk-prop-sf-dualizable-biduality", "sk-prop-sf-localization", "sk-prop-sf-open-closed-triangle", "sk-thm-regular", "sk-thm-sf-tensor-hom", "sk-thm-smooth-purity", "sk-prop-tf-exceptional-external-kunneth"]
+++
From the exceptional Künneth formula
(Proposition [sk-prop-tf-exceptional-external-kunneth]) and the ordinary one
we first deduce Künneth formulas for internal Hom and for Verdier
duals. These give the two displayed isomorphisms, and the trace
morphism is then evaluation on the diagonal.

*Internal Hom and Verdier duals.*
For $E_i,L_i\in D^b_{\mathrm{ctf}}(X_i,A)$ the external comparison
$\cHom_A(E_1,L_1)\boxtimes\cHom_A(E_2,L_2)\to \cHom_A(E_1\boxtimes E_2,L_1\boxtimes L_2)$ is an isomorphism. By
dévissage it suffices to check this on generators $E_i=Rh_{i!}F_i$, with $h_i$ the
inclusion of a stratum and $F_i$ lisse and perfect, for
which

$$
\cHom_A(Rh_{i!}F_i,L_i)
\simeq Rh_{i*}(F_i^\vee\otimes^{\mathbf L} h_i^!L_i).
$$

The ordinary Künneth formula and $\alpha$ identify the exterior product of
these expressions with internal Hom on the product. Taking
$L_i=\omega_{X_i}$ and using $\alpha$ for the structure maps, we get,
for $M_i\in D^b_{\mathrm{ctf}}(X_i,A)$,

$$
\mathbb D_{X_1\times X_2}(M_1\boxtimes M_2)
\simeq \mathbb D_{X_1}M_1\boxtimes \mathbb D_{X_2}M_2.
$$

*The two isomorphisms.*
For $M\in D^b_{\mathrm{ctf}}(U,A)$, $N\in D^b_{\mathrm{ctf}}(V,A)$ and the projections
$p_U,p_V$ of $V\times U$, Verdier exchange and biduality allow us to rewrite
$\cHom_A(p_U^*M,p_V^!N)$ as
$\mathbb D_{V\times U}(\mathbb D_VN\boxtimes M)$, and by the formula for
duals of exterior products this is
$N\boxtimes \mathbb D_UM$. Taking $M=N=K$, with the
factors of the product ordered as above, we obtain the first isomorphism.
The second follows from the canonical exchange of exceptional inverse
image with Hom, for $P,Q\in D^b_{\mathrm{ctf}}(X\times X,A)$,

$$
c^!\cHom_A(P,Q)\simeq\cHom_A(c^*P,c^!Q),
$$

applied to $P=p_2^*K$ and $Q=p_1^!K$. To prove the exchange, we
test against an object $M$ of $D^b_{\mathrm{ctf}}(C,A)$ (or of the established
localizing category $\Loc(D^b_{\mathrm{ctf}}(C,A))$), not an arbitrary ambient
object, and apply
$c_!\dashv c^!$, the projection formula for $c_!$, and the tensor–Hom
adjunction, in that order.

*The trace morphism.*
Let $e_K:P_X\to R\Delta_{X*}\omega_X$ be adjoint to the evaluation
$\Delta_X^*P_X=K\otimes^{\mathbf L} \mathbb D_XK\to\omega_X$. We apply $c^!$ and the
isomorphism of exceptional base change for the proper map $\Delta_X$:

$$
c^!P_X\xrightarrow{c^!e_K}c^!R\Delta_{X*}\omega_X
\xrightarrow{\sim}Ri_{c*}d_c^!\omega_X
\simeq Ri_{c*}\omega_{\Fix(c)}.
$$

The final isomorphism comes from the composition of exceptional inverse images.

*General coefficients.* The *General form* asserts that $\alpha$, $\beta$ and
$\kappa$ are isomorphisms for every admissible $\Lambda$; the argument above is
at finite coefficients. First, these specified maps are compatible with change
of coefficients: $\alpha$ is defined using $\mathrm{Ku}_!$ and the exceptional
counits, $\beta$ using evaluation and symmetry, and $\kappa$ is their specified
composite, so the canonical six-operation coefficient comparisons, including
those for the exceptional counits, evaluation and the dualizing object
([lem-fix-operation-reduction]), identify each of them after change of
coefficients with the corresponding map for the new ring. For
$\Lambda=\mathcal O_E$, source and target are constructible and derived
complete; reduction modulo $\pi_E$ identifies each map with its
finite-coefficient counterpart, which is invertible, so derived Nakayama
applied to its cone proves invertibility. For $\Lambda=E$, use integral models
and exactness in each variable, contravariantly where appropriate. For
$\Lambda=\Qlb$, descend the finitely many inputs to one common finite $E$.
Equality modulo $\pi_E$ alone does not identify morphisms; the argument uses
that the maps are the specified compatible ones.
