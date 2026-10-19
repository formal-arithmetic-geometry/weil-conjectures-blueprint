+++
kind  = "proof"
of    = "lem-chow-segre"
uses = ["def-nagata-homogeneous-localization-degree-zero", "lem-weil-pbc-closed-immersion-from-composite", "lem-weil-pbc-closed-immersion-products", "lemma-nagata-projective-space-base-change-proper", "prop-nagata-proj-standard-open"]
+++
*Reference: Stacks Project, Constructions of Schemes, Lemma 27.13.6,
[Tag 01WD](https://stacks.math.columbia.edu/tag/01WD).*

**The binary case.** Write $x=(x_k)_{k\in n}$, $y=(y_l)_{l\in m}$ for the
coordinates of the factors and $X_{(k,l)}$ for those of $\mathbf P^{n\times m}_S$,
so that $s^*X_{(k,l)}=x_ky_l$. Being a closed immersion is local on the target
and on $S$, so we may assume $S=\Spec A$ is affine and check the assertion on
the standard affine charts $D_+(X_{(a,b)})\subseteq\mathbf P^{n\times m}_S$,
$(a,b)\in n\times m$, which cover the target. One has

$$
s^{-1}\bigl(D_+(X_{(a,b)})\bigr)=D_+(x_a)\times_SD_+(y_b),
$$

which is affine, being a fibre product of affine schemes over the affine
base. On these charts $s$ is induced by the $A$-algebra homomorphism

$$
\mathcal O_{\mathbf P^{n\times m}_S}\bigl(D_+(X_{(a,b)})\bigr)
\longrightarrow
\mathcal O_{\mathbf P^{n}_S}\bigl(D_+(x_a)\bigr)\otimes_A
\mathcal O_{\mathbf P^{m}_S}\bigl(D_+(y_b)\bigr),
\qquad
\frac{X_{(k,l)}}{X_{(a,b)}}\longmapsto\frac{x_k}{x_a}\otimes\frac{y_l}{y_b}.
$$

This homomorphism is surjective: $X_{(k,b)}/X_{(a,b)}\mapsto x_k/x_a\otimes1$
and $X_{(a,l)}/X_{(a,b)}\mapsto1\otimes y_l/y_b$, and these elements generate
the target as an $A$-algebra. Hence $s$ is, locally on the target, the
morphism of affine schemes attached to a surjective ring homomorphism, i.e. a
closed immersion.

**Finite products.** The $m$-fold statement follows by induction on the
number of factors. For the empty product the fibre product is $S$ itself,
which is $\mathbf P^{N}_S$ for a one-element index set $N$; and if
$\mathbf P^{n_2}_S\times_S\dots\times_S\mathbf P^{n_m}_S\to\mathbf P^{N}_S$ is
a closed immersion with $N$ finite, then so is

$$
\mathbf P^{n_1}_S\times_S\bigl(\mathbf P^{n_2}_S\times_S\dots\times_S
\mathbf P^{n_m}_S\bigr)
\longrightarrow\mathbf P^{n_1}_S\times_S\mathbf P^{N}_S
\longrightarrow\mathbf P^{n_1\times N}_S,
$$

the first morphism because closed immersions are stable under base change and
the second by the binary case; and $n_1\times N$ is finite.

**Properness.** This does not use the Segre embedding: a finite fibre product
of proper $S$-schemes is proper over $S$, because properness is stable under
base change and under composition, and $\mathbf P^{n_i}_S\to S$ is proper for
finite $n_i$ by 01WC.

**The pullback of $\mathcal O(1)$.** The opens
$s^{-1}\bigl(D_+(X_{(k,l)})\bigr)=D_+(x_k)\times_SD_+(y_l)$, $(k,l)\in n\times m$,
cover $\mathbf P^{n}_S\times_S\mathbf P^{m}_S$, and on each of them both
$s^*\mathcal O(1)$ and $p_1^*\mathcal O(1)\otimes p_2^*\mathcal O(1)$ are free
of rank one, with generators $s^*X_{(k,l)}$ and $p_1^*x_k\otimes p_2^*y_l$
respectively. On the overlap of the charts for $(k,l)$ and $(k',l')$ the
transition functions agree, because $s$ pulls
$X_{(k,l)}/X_{(k',l')}$ back to $(x_k/x_{k'})\cdot(y_l/y_{l'})$. Hence the
local isomorphisms sending one generator to the other glue to an isomorphism
$s^*\mathcal O(1)\cong p_1^*\mathcal O(1)\otimes p_2^*\mathcal O(1)$.

**Tensor products.** Let $f,\mathcal M,\mathcal N,i,j$ be as in the statement
and let $(i,j)\colon X\to\mathbf P^{n}_S\times_S\mathbf P^{m}_S$ be the induced
morphism over $S$. The projection $p_1$ is a base change of
$\mathbf P^{m}_S\to S$, which is proper, hence separated, for finite $m$
[lemma-nagata-projective-space-base-change-proper]; so $p_1$ is separated, and
since $p_1\circ(i,j)=i$ is a closed immersion, so is $(i,j)$
[lem-weil-pbc-closed-immersion-from-composite]. By the binary case and
[lem-weil-pbc-closed-immersion-products], $s\circ(i,j)$ is a closed immersion,
and it lies over $S$ because $i$ does. Since pullback commutes with tensor
products and $p_1\circ(i,j)=i$, $p_2\circ(i,j)=j$,

$$
(s\circ(i,j))^*\mathcal O(1)\cong(i,j)^*\bigl(p_1^*\mathcal O(1)\otimes
p_2^*\mathcal O(1)\bigr)\cong i^*\mathcal O(1)\otimes j^*\mathcal O(1)
\cong\mathcal M\otimes\mathcal N .
$$
