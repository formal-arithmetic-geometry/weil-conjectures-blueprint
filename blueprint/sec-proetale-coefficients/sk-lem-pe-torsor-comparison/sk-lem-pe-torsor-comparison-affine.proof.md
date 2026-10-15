+++
kind = "proof"
of = "det-pe-torsor-comparison-affine"
+++
*Step 1: one affine trivializing cover.* Since $T\to *$ is an epimorphism there
is a pro-étale covering of $X$ on whose members $T$ has a section. By
[sk-thm-pe-indetale-refinement] and [sk-prop-pe-affine-basis] each member is
covered by affine ind-étale objects, and since $X$ is affine, hence
quasi-compact, finitely many of these, $W_1,\dots,W_r$, are jointly surjective
onto $X$ and each carries a section of $T$. Put $U=W_1\sqcup\dots\sqcup W_r$. It
is affine, ind-étale over $X$ (a finite product of ind-étale algebras is
ind-étale) and surjective onto $X$, and $T(U)=\prod_bT(W_b)\neq\emptyset$. Write
$U=\varprojlim_iU_i$ with $U_i$ affine étale over $X$. Since $U\to X$ is
surjective and factors through each $U_i$, every $U_i\to X$ is an étale
surjection.

*Step 2: the cocycle.* Choose $s\in T(U)$ and let $p_1,p_2\colon U\times_XU\to U$
and $p_{ab}\colon U\times_XU\times_XU\to U\times_XU$ be the projections. As the
action is simply transitive there is a unique $g\in G(U\times_XU)$ with
$p_1^*s=g\cdot p_2^*s$. Pulling back to the triple product and comparing the two
expressions of $p_1^*s$ in terms of $p_3^*s$ gives, by freeness of the action,
the cocycle identity $p_{13}^*g=p_{12}^*g\cdot p_{23}^*g$.

*Step 3: descent to a finite stage.* The fibre products
$U\times_XU=\varprojlim_iU_i\times_XU_i$ and
$U\times_XU\times_XU=\varprojlim_iU_i\times_XU_i\times_XU_i$ are pro-étale affine
presentations (the diagonal indices are cofinal). By the affine evaluation
formula of [sk-prop-pe-comparison-morphism],

$$
G(U\times_XU)=\varinjlim_iG_0(U_i\times_XU_i),\qquad
G(U\times_XU\times_XU)=\varinjlim_iG_0(U_i\times_XU_i\times_XU_i),
$$

compatibly with the projections and the group laws. So $g$ is the image of some
$g_i\in G_0(U_i\times_XU_i)$. The two sides of the cocycle identity for $g_i$ have
the same image in the colimit, hence agree at some later stage $j\geq i$; replacing
$i$ by $j$ and $g_i$ by its pullback, $g_i$ is a Čech $1$-cocycle of $G_0$ for the
étale covering $\{U_i\to X\}$.

*Step 4: the étale torsor.* Étale sheaves satisfy descent along étale coverings,
so gluing the trivial torsor $G_0|_{U_i}$ along the cocycle $g_i$ gives a
$G_0$-torsor $T_0$ on $X_{\Et}$ together with a section $s_0\in T_0(U_i)$
satisfying $p_1^*s_0=g_i\cdot p_2^*s_0$ on $U_i\times_XU_i$ (the standard
correspondence between torsors trivialized on a covering and Čech cocycles).

*Step 5: comparison.* The functor $\nu_X^*$ preserves finite limits and
epimorphisms, so $\nu_X^*T_0$ is a $G$-torsor. Let $s'\in(\nu_X^*T_0)(U)$ be the
pullback of $s_0$; then $p_1^*s'=g\cdot p_2^*s'$, since $g$ is the image of $g_i$.
The $G|_U$-equivariant map $\nu_X^*T_0|_U\to T|_U$ of trivial torsors sending $s'$
to $s$ is an isomorphism, and its two pullbacks to $U\times_XU$ agree because
both $s'$ and $s$ satisfy the same relation with the same $g$. As $U\to X$ is a
pro-étale covering, the isomorphism descends to an isomorphism of $G$-torsors
$\nu_X^*T_0\cong T$. Finally $\nu_X^*T_0$ is classical by
[det-pe-classical-sheaves-image], and $T_0$, hence $T$, has a section over the
étale covering $U_i\to X$.
