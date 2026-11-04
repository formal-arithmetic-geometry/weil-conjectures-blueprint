+++
kind = "proof"
of = "lemma-kunneth-field-coefficients"
order = 709
uses = ["theorem-comparison-direct-images", "theorem-comparison-constructible-sheaves", "remark-finiteness-small-etale-topoi", "lemma-kunneth-finite-direct-image"]
+++
We first treat constructible sheaves $M$ and $Q$, by the usual argument for
comparing a $\delta$-functor with an exact functor, and then pass to
complexes by truncation. We may compute with the small étale models of
$M$ and $Q$, since Theorems [theorem-comparison-constructible-sheaves]
and [theorem-comparison-direct-images] identify the operations and the
adjunction maps defining (8.4) on the two sites.

*Sheaves.* Let $M$ and $Q$ be constructible sheaves of $L$-modules.
By (4.9), that is, [Stacks, [09Z7](https://stacks.math.columbia.edu/tag/09Z7)](3)
on $T$, there is a short exact sequence of constructible $L$-sheaves

$$
0\longrightarrow Q\longrightarrow P\longrightarrow Q'\longrightarrow0,
\qquad
P=\bigoplus_a\pi_{a*}L_{T_a}^{\oplus n_a},
\quad \pi_a\text{ finite}.
$$

Indeed, every constructible sheaf on a qcqs scheme embeds into a finite sum
of finite direct images of constant sheaves with finite coefficients, and
over $L$ these coefficients are finite sums of $L$. For $r\geq0$ put

$$
F^r(Q)=p_Y^*R^rf_*M\otimes_Lp_T^*Q,
\qquad
G^r(Q)=R^rh_*(p_X^*M\otimes_Lp_T^*Q).
$$

Since tensoring over $L$ is exact, each $F^r$ is exact in $Q$. The $G^r$
form a long exact sequence. On cohomology sheaves the Künneth map induces
natural maps $a_Q^r:F^r(Q)\to G^r(Q)$, and $a_P^r$ is an isomorphism for
every $r$ by Lemma [lemma-kunneth-finite-direct-image]. Each $a_Q^r$ is
injective. Indeed, in its naturality square for $Q\hookrightarrow P$ the
map $F^r(Q)\to F^r(P)$ is injective and $a_P^r$ is an isomorphism.
Surjectivity is proved by induction on $r$, simultaneously for all
constructible $Q$.
For $r=0$, the beginning of the long exact sequence of the $G^r$ identifies
$G^0(Q)$ with the kernel of $G^0(P)\to G^0(Q')$. Since $F^0$ is exact,
$F^0(Q)$ is the kernel of $F^0(P)\to F^0(Q')$. As $a_P^0$ is an
isomorphism and $a_{Q'}^0$ is injective, $a^0_Q$ maps the second kernel
onto the first. For $r>0$, the induction hypothesis for $Q'$ and the
surjection $F^{r-1}(P)\to F^{r-1}(Q')$ imply that
$G^{r-1}(P)\to G^{r-1}(Q')$ is surjective. By the long exact
sequence,

$$
G^r(Q)=\ker\bigl(G^r(P)\to G^r(Q')\bigr).
$$

Since $F^r(Q)=\ker(F^r(P)\to F^r(Q'))$ by exactness of $F^r$, the
isomorphism $a_P^r$ and the injectivity of $a_{Q'}^r$ identify this
kernel with $F^r(Q)$. This completes the induction, so
(8.4) is an isomorphism for sheaves.

*Complexes.* Both sides of (8.4) are exact
functors in each variable, and the map is natural. Using the finitely many
truncation triangles of $M$ and of $Q$ and two-out-of-three, we extend the
case of sheaves to $M\in D^b_{\mathrm{ctf}}(X,L)$ and $Q\in D^b_{\mathrm{ctf}}(T,L)$. Over the field $L$
the truncations stay in $D^b_{\mathrm{ctf}}$, since constructible cohomology sheaves have
Tor amplitude zero, and all operations are bounded on the schemes under
consideration.
