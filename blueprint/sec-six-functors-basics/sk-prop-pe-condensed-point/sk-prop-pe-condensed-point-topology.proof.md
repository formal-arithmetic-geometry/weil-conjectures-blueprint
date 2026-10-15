+++
kind = "proof"
of = "det-pe-condensed-point-topology"
+++
*Points.* $\Spec$ turns the filtered colimit $LC(S,\Omega)=\varinjlim_i\Omega^{S_i}$
into the limit of the finite discrete spaces $\Spec\Omega^{S_i}=S_i$, so
$|\Omega[S]|=\varprojlim_iS_i=S$ as topological spaces; the point $x\in S$
corresponds to the kernel of evaluation at $x$. By
[det-pe-condensed-point-basis], part (3), the morphism induced by $s$ is
precomposition with $s$, which pulls the kernel of evaluation at $s(t)$ back to
the kernel of evaluation at $t$; so it is $s$ on points.

*Coverings.* A pro-étale covering ([def-weil-pbc-proetale-site]) of the affine
scheme $\Omega[S]$ is jointly surjective and, by quasi-compactness of affine
schemes in the definition of pro-étale coverings, is refined by a finite
subfamily which is still jointly surjective. Conversely a finite jointly
surjective family of weakly étale, hence flat, morphisms of affine schemes is an
fpqc covering by weakly étale maps, i.e. a pro-étale covering. On underlying
spaces joint surjectivity is surjectivity of $\coprod_aT_a\to S$.

*Topoi.* The affine ind-étale objects form a basis of $(\Spec\Omega)_{\Proet}$
stable under fibre products ([sk-prop-pe-affine-basis]); fibre products are
$\Omega[T]\times_{\Omega[S]}\Omega[T']=\Omega[T\times_ST']$ since the functor is an
equivalence preserving finite limits. By the comparison lemma, restriction to
this basis with the induced topology is an equivalence of topoi. Via
[det-pe-condensed-point-basis] the basis with the induced topology is the site of
profinite sets with finite jointly surjective families as covers, which is the
site $*_{\Proet}$ of [sk-def-sfb-condensed-ring]; its sheaves are condensed
sets.
