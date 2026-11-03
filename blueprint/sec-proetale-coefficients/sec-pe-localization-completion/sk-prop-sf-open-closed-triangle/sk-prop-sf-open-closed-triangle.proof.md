+++
kind = "proof"
of = "sk-prop-sf-open-closed-triangle"
+++
The assertion about limits is local on $X$. It holds because a weakly
contractible affine over $Z$ is the base change to $Z$ of an affine object
of $X_{\mathrm{pro}\acute{e}t}$ that is henselian along its inverse image of $Z$, and evaluating $i^*M$ on the former is the same as
evaluating $M$ on the latter, an operation that commutes with limits. Let $V$
be a weakly contractible object of the affine ind-étale basis of $Z$. It
determines an affine object $v(V)$ in the corresponding basis of $X$:
the functor $v$ is the fully faithful left adjoint to base change of
these affine bases, and $v(V)\times_XZ\simeq V$ [Stacks, Tag 09A9](https://stacks.math.columbia.edu/tag/09A9). The pullback of a sheaf, evaluated on $V$,
is its evaluation on $v(V)$, because every covering of a weakly
contractible object splits and therefore sheafification does not change values
there. Since evaluation commutes with limits and these objects detect
isomorphisms, it follows that $i^*$ preserves limits. As a left
adjoint it preserves colimits, and it is exact. Lifting covers along
$v$, we obtain exactness of $i_*$ and the identities
$i^*i_*=\mathrm{id}$ and $j^*i_*=0$. The localization sequence says that the adjunction map
$M\to i_*i^*M$ is surjective with kernel $j_!j^*M$. Its exactness on the
pro-étale site is [Stacks, Tag 09AH](https://stacks.math.columbia.edu/tag/09AH).

The functor $j^*$ is restriction to $U_{\mathrm{pro}\acute{e}t}$, hence exact. To see
that $j_!$ is exact, note first that $j^*j_!=\mathrm{id}$ and
$i^*j_!=0$. For the second identity, note that in the localization
sequence of $j_!N$ the first map $j_!j^*j_!N\to j_!N$ is an isomorphism
because $j^*j_!N=N$, so $i_*i^*j_!N=0$, and hence $i^*j_!N=0$ since $i_*$
is fully faithful. Moreover the pair $(j^*,i^*)$ detects exactness: both
functors are exact, so they commute with taking homology of a complex of
sheaves, and by the localization sequence a sheaf $M$ with $j^*M=0$ and
$i^*M=0$ is zero. Since $j^*j_!$ and
$i^*j_!$ are exact, so is $j_!$. That $j_!$ also preserves products and
derived inverse limits is shown next.

For $K\in D(U_{\mathrm{pro}\acute{e}t},j^*\mathcal R)$ we apply the localization sequence to a
complex representing $Rj_*K$. Since $j^*Rj_*K\simeq K$, we obtain the
triangle

$$
j_!K\longrightarrow Rj_*K\longrightarrow i_*i^*Rj_*K
\longrightarrow j_!K[1].
$$

Its last two terms preserve products and derived inverse limits, and hence
so does their fibre $j_!$. Since $j_!$ is exact and products are exact, we get the
corresponding statements about limits of sheaves of modules.
The argument with the functor $v$ is [bhatt-scholze15, §6.1]; see also
[Stacks, Tag 09AA](https://stacks.math.columbia.edu/tag/09AA), [Stacks, Tag 09AH](https://stacks.math.columbia.edu/tag/09AH), [Stacks, Tag 09BM](https://stacks.math.columbia.edu/tag/09BM) and [Stacks, Tag 09BP](https://stacks.math.columbia.edu/tag/09BP).
