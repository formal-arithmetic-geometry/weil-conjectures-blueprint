+++
kind  = "proof"
of    = "lemma-nagata-common-modification"
+++
**Construction.** The schemes $X_i$ are of finite type over the qcqs
scheme $S$, hence qcqs, and $U$ is separated and of finite type over $S$,
since $j_i$ is a quasi-compact open immersion. Identify $U$ with its images
$j_i(U)\subseteq X_i$. Construct the following objects in order.

1. Let
$$
X_{12}=\operatorname{SIm}
\bigl(U\xrightarrow{(j_1,j_2)}X_1\times_SX_2\bigr)
$$
and write $p_i\colon X_{12}\to X_i$ for the projections.
1. Apply [def-nagata-elimination-indeterminacy] to $(p_i,U)$.
Denote the resulting blow-ups by
$X_i^i= X^{\mathrm{el}}(p_i,U)$, their center ideals by
$\mathcal I_i$, and the open strict transforms by
$X_{12}^i\subseteq X_i^i$.
1. On $X_{12}$ define
$$
\mathcal K_{12}
=p_1^{-1}\mathcal I_1\mathcal O_{X_{12}}\,
p_2^{-1}\mathcal I_2\mathcal O_{X_{12}},
\qquad
X'_{12}=\operatorname{Bl}_{\mathcal K_{12}}(X_{12}).
$$
1. The product-center blow-up maps to each $X_{12}^i$. Extend
$X'_{12}\to X_{12}^i$ across the open
$X_{12}^i\subseteq X_i^i$ by
[def-nagata-extended-admissible-blowup]; call the resulting
ambient schemes $X'_i$ and the composite maps $\pi_i\colon X'_i\to X_i$.
1. Define
$$
W=X'_1\amalg_{X'_{12}}X'_2
$$
using the two constructed open immersions of $X'_{12}$, with the
gluing maps $k_i\colon X'_i\to W$ and the induced morphism
$w\colon W\to S$.

**Verification.** This is Stacks Project, Tag 0F3X (Lemma 38.33.4), with
the qcqs base $S$, the common quasi-compact open $U$, and the separated
finite-type morphisms $X_i\to S$. The inputs of step 2 are legitimate: each
$p_i$ is the composite of the closed immersion
$X_{12}\hookrightarrow X_1\times_SX_2$ with the base change of the separated
finite-type morphism $X_{3-i}\to S$, hence is separated and of finite
type; and by [lemma-nagata-scheme-image-partial-section], applied to the
quasi-compact open immersion $j_i$ and the separated morphism
$X_{3-i}\to S$, the inverse image $p_i^{-1}(U)$ maps isomorphically to $U$.
Step 2 first principalizes the two projection ideals, and step 3 takes their
product center, which gives the map $X'_{12}\to X_{12}$ of
[lemma-nagata-product-ideal-common-blowup]. Its strict-transform comparison
gives $X'_{12}\subseteq X'_i$ as an open subscheme, with both restrictions
identified with $U$; this is the extension step recorded by
[lemma-nagata-extend-admissible-blowup]. Consequently the two open
immersions glue along exactly $X'_{12}$, not merely along their underlying
topological intersection, so $k_1$ and $k_2$ are open immersions whose images
cover $W$, and $w\circ k_i=s_i\circ\pi_i$ by construction.

The copy of $U$ in $X'_{12}$ gives morphisms $u_i\colon U\to X'_i$ with
$\pi_i\circ u_i=j_i$, and $k_1\circ u_1=k_2\circ u_2$ because both factor
through the common open $X'_{12}$. By the composition statement
[lemma-nagata-admissible-blowup-comp], each $\pi_i$ is a $U$-admissible
blow-up.

The graph of the overlap $X'_{12}\to X'_1\times_SX'_2$ is an immersion
because $X'_2\to S$ is separated. The composite
$X'_{12}\to X_1\times_SX_2$ is proper, and the product map from
$X'_1\times_SX'_2$ to $X_1\times_SX_2$ is separated; hence the graph map
is proper by [lemma-nagata-proper-to-separated-target]. It is therefore
closed, so the two-open diagonal criterion
[lemma-nagata-separated-two-open-cover] proves that $W\to S$ is separated.
Finally $W$ is covered by the two opens $X'_i$, which are of finite type over
$S$ (blow-ups along finite type centres of schemes of finite type over $S$),
so $W\to S$ is of finite type. The data
$(\pi_i,W,w,k_i,u_i)$ form a common modification of $X_1$ and $X_2$ along
$U$ in the sense of [def-nagata-common-modification].
