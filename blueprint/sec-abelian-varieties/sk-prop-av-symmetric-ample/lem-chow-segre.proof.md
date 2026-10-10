+++
kind  = "proof"
of    = "lem-chow-segre"
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

**The consequences.** A composite of closed immersions is a closed
immersion. On $\mathbf P^{n}_S\times_S\mathbf P^{m}_S$ one has
$s^*\mathcal O(1)=\mathcal O(1)\boxtimes\mathcal O(1)$, since
$s^*X_{(k,l)}=x_ky_l$ is a section of bidegree $(1,1)$; as $s$ is a closed
immersion, $\mathcal O(1)\boxtimes\mathcal O(1)$ is very ample.
