+++
kind  = "proof"
of    = "lem-finrepair-constant-finite-comparison"
+++
The unit $\underline M_X\to\nu_*\underline M_Y$ is injective
by the diagonal description of
[lemma-weil-pbc-finite-stalk-formula]; the fibre of the
surjective finite $\nu$ is nonempty at every geometric point.
Let $Q$ be its cokernel. Both sheaves in this monomorphism are
constructible by [lem-fin-finite-morphism], so $Q$ is
constructible by [thm-constructible-serre].
Outside $Z$ the unit is an isomorphism; hence $Q$ restricts to
zero there, and its canonical map $Q\to i_*i^*Q$ is an
isomorphism on all geometric stalks. Use
[lemma-weil-pbc-geometric-stalk-conservative] to identify them.

Closed-immersion exactness in [lem-fin-closed-immersion] and
the composition spectral sequence
[lem-weil-pbc-grothendieck-spectral-sequence] give
$R^qf_*Q=R^q(f|_Z)_*i^*Q$.
Since $f|_Z$ is finite,
[lem-fin-finite-morphism] makes $H=f_*Q$ constructible
and makes these higher direct images zero for $q>0$.
The same finite exactness and composition spectral sequence
identify $R^qf_*\nu_*\underline M_Y$ with
$R^qv_*\underline M_Y$.
The long exact sequence of

$$
0\to\underline M_X\to\nu_*\underline M_Y\to Q\to0
$$

therefore gives

$$
f_*\underline M_X
=\ker\bigl(v_*\underline M_Y\to H\bigr)
$$

and

$$
0\to\operatorname{coker}\bigl(v_*\underline M_Y\to H\bigr)
\to R^1f_*\underline M_X
\to R^1v_*\underline M_Y\to0.
$$

All sheaves used to take the indicated kernel and cokernel are
constructible, and the rightmost term in the short exact sequence
is constructible by hypothesis. The weak-Serre property of
[thm-constructible-serre] proves constructibility
in degrees zero and one. In every degree $q\geq2$, the adjacent
terms $R^{q-1}f_*Q$ and $R^qf_*Q$ are zero, so the same long
exact sequence gives the claimed isomorphism. This proves the
remaining constructibility assertions as well.
