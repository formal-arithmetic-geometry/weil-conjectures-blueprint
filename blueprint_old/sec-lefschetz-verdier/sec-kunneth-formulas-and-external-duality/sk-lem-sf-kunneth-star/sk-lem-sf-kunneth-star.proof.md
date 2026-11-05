+++
kind = "proof"
of = "sk-lem-sf-kunneth-star"
uses = ["sk-lem-tf-independent-base-change", "sk-thm-pe-constructible-comparison", "sk-thm-pe-direct-image-comparison", "sk-thm-sf-ctf-stability", "sk-prop-scalar-six", "sk-rem-restriction-of-injectives-to-the-closed-fibre"]
+++
For constant $Q$ the Künneth map is a base change map, and every
constructible $Q$ is built from constant sheaves on finite covers. Since the general map is a composite of two maps of the form
(12.2), it suffices to treat that case, where one
factor is an identity. For constant $Q$ it is
Lemma [sk-lem-tf-independent-base-change]. For sheaves with coefficients in a finite field, we reduce
the general $Q$ to that case by embedding $Q$ into finite direct images
of constant sheaves and by induction on the cohomological degree.
Truncation extends the result to complexes over the field, and
derived Nakayama extends it to an arbitrary finite ring $A$.

Under $h^*\dashv Rh_*$, where $h=f\times\operatorname{id}_T$, the map
(12.2) is adjoint to the counit
on the first tensor factor:

$$
h^*(Rf_*M\boxtimes Q)
=p_X^*f^*Rf_*M\otimes^{\mathbf L} p_T^*Q
\xrightarrow{\varepsilon_f\otimes^{\mathbf L}1}M\boxtimes Q.
$$

*Field coefficients and sheaves (dévissage).*
Suppose first that $A=L$ is a finite field of characteristic $\ell$,
and that $M$ and $Q$ are constructible sheaves. We may compute with
their small étale models, since Theorems [sk-thm-pe-constructible-comparison]
and [sk-thm-pe-direct-image-comparison] identify the operations and the
adjunction maps defining (12.2) on the two sites. For $Q=L_T$, the
assertion is Lemma [sk-lem-tf-independent-base-change].
It also holds for $Q=\pi_*L_{T'}$ with $\pi:T'\to T$ finite. To see
this, set

$$
v=\operatorname{id}_Y\times\pi,\qquad
w=\operatorname{id}_X\times\pi,\qquad
h'=f\times\operatorname{id}_{T'}.
$$

Direct image along a finite morphism is exact and commutes with pullback, and by the
projection formula we have

$$
Rf_*M\boxtimes\pi_*L_{T'}
\simeq v_*p_{Y,T'}^*Rf_*M,
\qquad
M\boxtimes\pi_*L_{T'}\simeq w_*p_{X,T'}^*M.
$$

Since $hw=vh'$, the comparison between these two expressions is
$v_*$ of the base change map of
Lemma [sk-lem-tf-independent-base-change] for $h'$, and hence an isomorphism.
This comparison is the Künneth map, because under the adjunction
$h^*\dashv Rh_*$ and the adjunctions for the finite maps, both correspond to the counit
$\varepsilon_f\otimes^{\mathbf L}1$ displayed above. The same conclusion holds for finite sums and
for finite-dimensional constant $L$-modules.

An arbitrary constructible $Q$ embeds into a sheaf of this form: by
(4.8) there is a short exact
sequence of constructible $L$-sheaves

$$
0\longrightarrow Q\longrightarrow P\longrightarrow Q'\longrightarrow0,
\qquad
P=\bigoplus_a\pi_{a*}L_{T_a}^{\oplus n_a},
\quad \pi_a\text{ finite}.
$$

This is [Stacks, Tag 09Z7](https://stacks.math.columbia.edu/tag/09Z7)(3) on $T$, which says that every constructible sheaf on a qcqs
scheme embeds into a finite sum of finite direct images of constant
sheaves with finite coefficients. Over $L$ these coefficients are finite
sums of $L$, which gives the displayed form of $P$.
For $r\geq0$ put

$$
F^r(Q)=p_Y^*R^rf_*M\otimes_Lp_T^*Q,
\qquad
G^r(Q)=R^rh_*(p_X^*M\otimes_Lp_T^*Q).
$$

Since tensoring over $L$ is exact, each $F^r$ is exact in $Q$, whereas
the $G^r$ form a long exact sequence. On cohomology sheaves the
Künneth map induces natural maps $a_Q^r:F^r(Q)\to G^r(Q)$, and we
show that they are isomorphisms.

Each $a_Q^r$ is injective, since in its naturality square for
$Q\hookrightarrow P$ the map $F^r(Q)\to F^r(P)$ is injective and
$a_P^r$ is an isomorphism. Surjectivity is proved by induction on
$r$.
For $r=0$, the beginning of the long exact sequence of the $G^r$ identifies
$G^0(Q)$ with the kernel of $G^0(P)\to G^0(Q')$. Since $F^0$ is exact,
$F^0(Q)$ is the kernel of $F^0(P)\to F^0(Q')$, and since $a_P^0$ is
an isomorphism and $a_{Q'}^0$ is injective, $a^0_Q$ maps the second
kernel onto the first. For $r>0$, the induction hypothesis and the surjection
$F^{r-1}(P)\to F^{r-1}(Q')$ imply that
$G^{r-1}(P)\to G^{r-1}(Q')$ is surjective. By the long exact
sequence,

$$
G^r(Q)=\ker\bigl(G^r(P)\to G^r(Q')\bigr).
$$

Since $F^r(Q)=\ker(F^r(P)\to F^r(Q'))$ by exactness of $F^r$, the
isomorphism $a_P^r$ and the injectivity of $a_{Q'}^r$ identify this
kernel with $F^r(Q)$. This proves surjectivity and completes the induction,
so (12.2) is an isomorphism for sheaves over $L$.

*Complexes over $L$ (dévissage).*
Both sides of (12.2) are exact functors in each
variable, and the map is natural. Hence, using the finitely many truncation
triangles of a bounded constructible complex and two-out-of-three, we
extend the case of sheaves to these complexes. Here all operations are bounded
on the schemes under consideration, and over the field $L$ the truncations stay
in $D^b_{\mathrm{ctf}}$, since constructible cohomology sheaves have Tor amplitude
zero.

*Arbitrary finite coefficient rings (dévissage).*
Return to the finite commutative ring $A$ of the statement, and let $N$ be
the cone of the Künneth map (12.2). Both its source and target are in
$D^b_{\mathrm{ctf}}(Y\times T,A)$ by Proposition [sk-thm-sf-ctf-stability], so every
geometric stalk of $N$ is a perfect $A$-complex. Let
$\mathfrak m\subset A$ be a maximal ideal and apply the field case to
the residue field $L=A/\mathfrak m$. The change-of-coefficients maps of
Proposition [sk-prop-scalar-six] for pullback, tensor product and
ordinary direct image respect the unit and counit defining the
Künneth map, so they identify the reduction
$(12.2)\otimes^{\mathbf L}_A L$ with the map
(12.2) for $M\otimes^{\mathbf L}_A L$ and
$Q\otimes^{\mathbf L}_A L$. It follows that $N\otimes^{\mathbf L}_A L=0$ for every maximal
ideal. The Artinian ring $A$ is a product of local rings, so at a
geometric point $\bar z$, derived Nakayama for the perfect complex
$N_{\bar z}$ shows that $N_{\bar z}=0$. Since $N$ lies in
$D^b_{\mathrm{ctf}}(Y\times T,A)$, it comes from a complex on the small étale site
by Theorem [sk-thm-pe-constructible-comparison], and there vanishing is
detected on geometric stalks. Hence $N=0$.

*Two morphisms.*
Factor $f_1\times f_2$ as

$$
X_1\times X_2\xrightarrow{\operatorname{id}_{X_1}\times f_2}
X_1\times Y_2\xrightarrow{f_1\times\operatorname{id}_{Y_2}}
Y_1\times Y_2.
$$

Apply the isomorphism (12.2) to $f_1$ with second
coefficient $Rf_{2*}M_2$, which lies in $D^b_{\mathrm{ctf}}(Y_2,A)$ by
Proposition [sk-thm-sf-ctf-stability], and, after interchanging the factors,
to $f_2$ with coefficient $M_1$. Their composite is an isomorphism
from $Rf_{1*}M_1\boxtimes Rf_{2*}M_2$ to
$R(f_1\times f_2)_*(M_1\boxtimes M_2)$. Since its adjoint is the tensor
product of $\varepsilon_{f_1}$ and $\varepsilon_{f_2}$, it is the
Künneth map of the statement.
