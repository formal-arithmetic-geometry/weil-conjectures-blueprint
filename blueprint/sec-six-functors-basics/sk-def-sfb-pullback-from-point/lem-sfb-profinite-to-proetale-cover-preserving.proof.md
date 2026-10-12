+++
kind  = "proof"
of    = "lem-sfb-profinite-to-proetale-cover-preserving"
+++
The morphisms are weakly étale, because a morphism between weakly étale
$\Spec\Z$-schemes is weakly étale. They are also morphisms of affine schemes.

Write $LC(S,\Z)=\colim_j\Z^{S_j}$ over the finite quotients $S_j$ of $S$.
Then
$$
\Spec LC(S,\Z)=\lim_j\coprod_{S_j}\Spec\Z ,
$$
and its underlying set is $S\times|\Spec\Z|$. A map $g\colon S'\to S$ induces
$g\times\mathrm{id}$ on underlying sets, so joint surjectivity of the $S_i\to S$
gives joint surjectivity of the induced family of spectra. A finite jointly
surjective family of weakly étale morphisms between affine schemes is a
pro-étale covering.
