+++
kind = "proof"
of = "proposition-extension-zero-restriction-closed-subscheme--3"
order = 201007
+++
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

*Source:* the proof of Proposition [proposition-extension-zero-restriction-closed-subscheme].
