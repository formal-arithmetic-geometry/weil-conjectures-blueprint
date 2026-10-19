+++
kind = "proof"
of = "sk-lem-sf-kunneth-star"
uses = ["sk-lem-tf-independent-base-change", "sk-thm-pe-constructible-comparison", "sk-thm-pe-direct-image-comparison", "sk-thm-sf-ctf-stability", "sk-prop-scalar-six"]
+++
The main case is the identity-factor form (1). For constant $Q$ it is
Lemma [sk-lem-tf-independent-base-change], and this is where the content lies. For
sheaves over a finite field, an embedding of $Q$ into finite direct images of constant
sheaves and an induction on the cohomological degree reduce the general $Q$ to that
case. Truncation extends the result to complexes over the field, and derived Nakayama
to an arbitrary finite ring $A$. These three steps are routine dévissage. The general
map is a composite of two identity-factor maps.

The map (1) is adjoint under $h^*\dashv Rh_*$, where $h=f\times\operatorname{id}_T$, to
the counit on the first tensor factor:

$$
h^*(Rf_*M\boxtimes Q)
=p_X^*f^*Rf_*M\dt p_T^*Q
\xrightarrow{\varepsilon_f\dt1}M\boxtimes Q.
$$

This description fixes the map throughout the proof; it is called the Künneth map.

*Field coefficients and sheaves (dévissage).* Suppose first that $A=L$ is a finite
field of characteristic $\ell$, and that $M$ and $Q$ are constructible sheaves. We may
calculate on their small étale models: Theorems [sk-thm-pe-constructible-comparison]
and [sk-thm-pe-direct-image-comparison] compare the operations and the adjunction maps
defining (1), and thus transport this calculation to the small pro-étale site. For
$Q=L_T$, the assertion is Lemma [sk-lem-tf-independent-base-change]. It also holds for
$Q=\pi_*L_{T'}$ with $\pi:T'\to T$ finite. To see this, set

$$
v=\operatorname{id}_Y\times\pi,\qquad
w=\operatorname{id}_X\times\pi,\qquad
h'=f\times\operatorname{id}_{T'}.
$$

Finite direct image is exact and commutes with pullback, and its projection formula
gives

$$
Rf_*M\boxtimes\pi_*L_{T'}
\simeq v_*p_{Y,T'}^*Rf_*M,
\qquad
M\boxtimes\pi_*L_{T'}\simeq w_*p_{X,T'}^*M.
$$

Since $hw=vh'$, the comparison between these two expressions is $v_*$ of the base
change map of Lemma [sk-lem-tf-independent-base-change] for $h'$, hence an
isomorphism. This comparison is the Künneth map, because the $h^*\dashv Rh_*$ and the
finite-map adjunctions turn both into the counit $\varepsilon_f\dt1$ displayed above.
Finite sums and finite-dimensional constant $L$-modules give the same conclusion.

An arbitrary constructible $Q$ embeds into a sheaf of this form: by the embedding of
constructible sheaves into finite direct images of constant sheaves recalled in the
section on proper base change, there is a short exact sequence of constructible
$L$-sheaves

$$
0\longrightarrow Q\longrightarrow P\longrightarrow Q'\longrightarrow0,
\qquad
P=\bigoplus_a\pi_{a*}L_{T_a}^{\oplus n_a},
\quad \pi_a\text{ finite}.
$$

This is [Stacks, Tag 09Z7](https://stacks.math.columbia.edu/tag/09Z7)(3) on $T$: every
constructible sheaf on a qcqs scheme embeds into a finite sum of finite direct images
of constant sheaves with finite coefficients, written here as finite sums of $L$. For
$r\geq0$ put

$$
F^r(Q)=p_Y^*R^rf_*M\otimes_Lp_T^*Q,
\qquad
G^r(Q)=R^rh_*(p_X^*M\otimes_Lp_T^*Q).
$$

Tensoring over $L$ is exact, so each $F^r$ is exact in $Q$, whereas the $G^r$ form a
long exact sequence. On cohomology sheaves the Künneth map induces natural maps
$a_Q^r:F^r(Q)\to G^r(Q)$, and we show that they are isomorphisms.

Each $a_Q^r$ is injective, since in its naturality square for $Q\hookrightarrow P$ the
map $F^r(Q)\to F^r(P)$ is injective and $a_P^r$ is an isomorphism. Surjectivity is
proved by induction on $r$. For $r=0$, the beginning of the long exact $G$-sequence
identifies $G^0(Q)$ with the kernel of $G^0(P)\to G^0(Q')$; the isomorphism $a_P^0$ and
the injectivity of $a_{Q'}^0$ identify that kernel with $F^0(Q)$. For $r>0$, the
induction hypothesis and the surjection $F^{r-1}(P)\to F^{r-1}(Q')$ imply that
$G^{r-1}(P)\to G^{r-1}(Q')$ is surjective. By the long exact sequence,

$$
G^r(Q)=\ker\bigl(G^r(P)\to G^r(Q')\bigr).
$$

Using $a_P^r$ and the injectivity of $a_{Q'}^r$ identifies this kernel with $F^r(Q)$,
proving surjectivity and completing the induction. Hence (1) is an isomorphism for
sheaves over $L$.

*Complexes over $L$ (dévissage).* Both sides of (1) are exact functors in each
variable and the map is natural, so the finitely many truncation triangles of bounded
constructible complexes and two-out-of-three extend the sheaf case to these complexes.
All operations are bounded on the standing schemes, and over the field $L$ the
truncations stay in $\Dctf$, since constructible cohomology sheaves have Tor amplitude
zero.

*Arbitrary finite coefficient rings (dévissage).* Return to the finite commutative
ring $A$ of the statement. Let $C$ be the cone of (1). Both its source and target are
in $\Dctf(Y\times T,A)$ by Proposition [sk-thm-sf-ctf-stability], so every geometric
stalk of $C$ is a perfect $A$-complex. Let $\mathfrak m\subset A$ be a maximal ideal and
apply the field case to the residue field $L=A/\mathfrak m$. The pullback, tensor and
ordinary-direct-image coefficient comparisons of Proposition [sk-prop-scalar-six]
respect the unit and counit defining the Künneth map, so they identify
$k_{f,M,Q}\dt_A L$ with $k_{f,M\dt_A L,Q\dt_A L}$. Hence $C\dt_A L=0$ for every maximal
ideal. At a geometric point $\bar z$, derived Nakayama for the perfect complex
$C_{\bar z}$ over the Artinian ring $A$, a product of local rings, gives
$C_{\bar z}=0$. The cone is classical constructible, so geometric stalks detect its
vanishing by the finite-coefficient comparison, and $C=0$.

*Two morphisms.* Factor $f_1\times f_2$ as

$$
X_1\times X_2\xrightarrow{\operatorname{id}_{X_1}\times f_2}
X_1\times Y_2\xrightarrow{f_1\times\operatorname{id}_{Y_2}}
Y_1\times Y_2.
$$

Apply the identity-factor isomorphism to $f_1$ with second coefficient $Rf_{2*}M_2$,
which lies in $\Dctf(Y_2,A)$ by Proposition [sk-thm-sf-ctf-stability], and, after
interchanging the factors, to $f_2$ with coefficient $M_1$. Their composite is an
isomorphism from $Rf_{1*}M_1\boxtimes Rf_{2*}M_2$ to
$R(f_1\times f_2)_*(M_1\boxtimes M_2)$. Its adjoint is the tensor product of
$\varepsilon_{f_1}$ and $\varepsilon_{f_2}$, so it is the Künneth map of the
statement. In particular it is independent of the compactification and the embedding
chosen in the proof.
