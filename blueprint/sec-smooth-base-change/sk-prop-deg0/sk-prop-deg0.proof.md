+++
kind = "proof"
of = "sk-prop-deg0"
+++
By [Stacks, Tag 0EY5](https://stacks.math.columbia.edu/tag/0EY5), locally on an étale object
$U\to Y'$ there is a
factorization $U\to V\to Y$ in which $V\to Y$ is étale and $U\to V$
is flat and qcqs with geometrically connected fibres. Pullback along
such a map does not change the sections of a pulled-back étale sheaf
([Stacks, Tag 0A3H](https://stacks.math.columbia.edu/tag/0A3H), as used in
[Stacks, Tag 0EZX](https://stacks.math.columbia.edu/tag/0EZX)), and the connected-fibre
property survives base change to $X$. Hence on these objects

$$
 (g^{-1}f_*F_{\mathrm{\acute et}})(U)
   =F_{\mathrm{\acute et}}(V\times_Y X)
   =(f'_*u^{-1}F_{\mathrm{\acute et}})(U).
$$

These equalities are given by the exchange map, so descent proves the
lemma. This is the degree-zero argument of
[Stacks, Tag 0EYS](https://stacks.math.columbia.edu/tag/0EYS).

*Complement.* In the notation of [sk-def-bc] the smooth (or flat) morphism is $f$ and the
qcqs one is $g$. A sheaf of $\Lambda$-modules is in particular a sheaf of sets, and the
base-change map is the exchange map of underlying sheaves; the argument in detail is as follows.

*Step 1 (an étale-local normal form with connected fibres).*
Because $f$ is flat, locally of finite presentation and has
geometrically reduced fibres, there is an étale covering
$\{X_i\to X\}$ such that each $X_i\to S$ factors as
$X_i\to S_i\to S$ with $S_i\to S$ étale and $X_i\to S_i$ flat of
finite presentation with geometrically connected (and geometrically
reduced) fibres. Geometric reducedness is what allows a geometric
fibre to be cut into quasi-compact geometrically connected opens which
then spread out over an étale neighbourhood of the base point.

*Step 2 (sections agree on such a chart).* Let $U\to X$ be étale
and factor as $U\to V\to S$ with $V\to S$ étale and $U\to V$
quasi-compact flat with geometrically connected fibres. Since $V\to S$
is étale, the inverse image of a sheaf on $S_{\Et}$ restricted to $V$
is its restriction, so

$$
(f^{-1}g_*\mathcal F)(U)=(g_*\mathcal F)(V)
=\mathcal F(V\times_ST)=(e^{-1}\mathcal F)(U\times_XY)
=(h_*e^{-1}\mathcal F)(U).
$$

The outer two equalities are the definitions of $g_*$ and $h_*$ together
with $U\times_XY=U\times_ST$. The first and third use the same input:
for a flat quasi-compact morphism with geometrically connected fibres,
global sections of an inverse image agree with global sections
downstairs ([Stacks `0A3H`](https://stacks.math.columbia.edu/tag/0A3H)) — applied to $U\to V$,
and then to its base change $U\times_ST\to V\times_ST$, whose fibres are
base changes of those of $U\to V$ and hence still geometrically
connected. That lemma is itself the statement that a section of the
pullback is constant on each connected geometric fibre, so descends
along the fpqc covering $U\to V$.

*Step 3 (glue).* Both sides are sheaves on $X_{\Et}$, and by
Step 1 every object of $X_{\Et}$ has a covering by objects of the shape
used in Step 2, so the two sheaves agree.

*Step 4 ($\mathrm{BC}(f,\Lambda,0)$ for smooth $f$).* A smooth morphism
is flat and locally of finite presentation and its geometric fibres are
smooth varieties, hence reduced; so Steps 1–3 apply and give the
degree-zero case of [sk-def-bc] for every quasi-compact
quasi-separated $g:T\to S$ and every sheaf $\mathcal F$ of $\Lambda$-modules.

This is Stacks, Étale Cohomology, Lemma 59.87.2
([`0EYS`](https://stacks.math.columbia.edu/tag/0EYS)), combining Lemma 59.87.1
([`0EZX`](https://stacks.math.columbia.edu/tag/0EZX)) for Steps 2–3 with More on Morphisms,
Lemma 37.46.3 ([`0EY5`](https://stacks.math.columbia.edu/tag/0EY5)) for Step 1.
