+++
kind = "proof"
of = "proposition-extension-zero-restriction-closed-subscheme"
order = 202
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "proposition-pro-etale-coverings", "proposition-pro-etale-affines-form-basis"]
+++
The special feature of the pro-étale site is that $i^*$ preserves
limits; we prove this first, deduce exactness of $j_!$ from the
localization sequence, obtain the statement about products and derived
limits from a triangle expressing $j_!$ through $Rj_*$, $i^*$ and $i_*$,
and check base change by adjunction.

*Step 1: the functors $i^*$ and $i_*$.* The functor $i^*$ preserves
limits, because evaluating $i^*M$ on a weakly contractible affine over $Z$
is the same as evaluating $M$ on an affine object of $X_{\mathrm{pro}\acute{e}t}$, and
evaluation commutes with limits. The assertion is local on $X$. Let $V$
be a weakly contractible object of the affine ind-étale basis of $Z$. It
determines an affine object $v(V)$ in the corresponding basis of $X$,
henselian along its inverse image of $Z$: the functor $v$ is the fully
faithful left adjoint to base change of these affine bases, and
$v(V)\times_XZ\simeq V$ [Stacks, [09A9](https://stacks.math.columbia.edu/tag/09A9)]. The pullback of a sheaf, evaluated
on $V$, is its evaluation on $v(V)$, because every covering of a weakly
contractible object splits, so that sheafification does not change values
there. Since evaluation commutes with limits and these objects detect
isomorphisms, $i^*$ preserves limits. Being a left adjoint, it also
preserves colimits. Since it preserves both limits and colimits, it is exact. Lifting covers
along $v$ shows that $i_*$ is exact and that $i^*i_*=\mathrm{id}$ and
$j^*i_*=0$. Finally, the localization sequence is exact on the
pro-étale site [Stacks, [09AH](https://stacks.math.columbia.edu/tag/09AH)], that is, the adjunction map
$M\to i_*i^*M$ is surjective with kernel $j_!j^*M$.

*Step 2: exactness of $j^*$ and $j_!$.* The functor $j^*$ is
restriction to $U_{\mathrm{pro}\acute{e}t}$, hence exact. The functor $j_!$ is exact
because its composites $j^*j_!$ and $i^*j_!$ are exact and the pair
$(j^*,i^*)$ detects exactness. Here the first composite is $j^*j_!=\mathrm{id}$,
and the second is $i^*j_!=0$. Indeed, in the localization sequence of $j_!N$
the first map $j_!j^*j_!N\to j_!N$ is an isomorphism since $j^*j_!N=N$.
Hence $i_*i^*j_!N=0$, and $i^*j_!N=0$ because $i_*$ is fully faithful. The pair
$(j^*,i^*)$ detects exactness, because both functors are exact, hence
commute with taking homology of a complex of sheaves, while a sheaf $M$
with $j^*M=0$ and $i^*M=0$ is zero by the localization sequence.

*Step 3: products and derived inverse limits.* For
$K\in D(U_{\mathrm{pro}\acute{e}t},j^*\mathcal R)$, applying the localization sequence to a
complex representing $Rj_*K$ and using $j^*Rj_*K\simeq K$, we obtain the
triangle

$$
j_!K\longrightarrow Rj_*K\longrightarrow i_*i^*Rj_*K
\longrightarrow j_!K[1].
$$

The last two terms preserve products and derived inverse limits, because
$Rj_*$ and $i_*$ are right adjoints and $i^*$ is exact and preserves
limits by Step 1; hence so does their fibre $j_!$. As $j_!$ is exact and
products are exact, the corresponding statements about limits of sheaves
of modules follow.

*Step 4: base change.* The map $j'_!g'^*\to g^*j_!$ is an isomorphism
because its right adjoint is. Indeed, $j'_!g'^*$ is left adjoint to
$g'_*j'^*$ and $g^*j_!$ is left adjoint to $j^*g_*$, and the right adjoint
of the map is the base change map $j^*g_*\to g'_*j'^*$, which is an
isomorphism since both sides send a sheaf on $X'_{\mathrm{pro}\acute{e}t}$ to its
restriction to the objects lying over $U'$. The same holds on derived
categories, since the coefficient rings are inverse images, so that
$g^*$, $g'^*$ and $j'_!$ are exact.
The argument with the functor $v$ is [bhatt-scholze15, §6.1]; see also
[Stacks, [09AA](https://stacks.math.columbia.edu/tag/09AA), [09AH](https://stacks.math.columbia.edu/tag/09AH), [09BM](https://stacks.math.columbia.edu/tag/09BM)] and [Stacks, [09BP](https://stacks.math.columbia.edu/tag/09BP)].
