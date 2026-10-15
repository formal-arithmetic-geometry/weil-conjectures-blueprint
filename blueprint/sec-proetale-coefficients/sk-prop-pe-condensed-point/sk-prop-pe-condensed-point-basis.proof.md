+++
kind = "proof"
of = "det-pe-condensed-point-basis"
+++
*(1).* An étale algebra over a field is a finite product of finite separable
field extensions; as $\Omega$ is separably closed, each factor is $\Omega$.

*Idempotents.* Since $\Omega$ is a field, its only idempotents are $0,1$. Hence
an $\Omega$-algebra map $\Omega^S\to B$ from a finite product is the same as a
family $(b_x)_{x\in S}$ of orthogonal idempotents of $B$ with sum $1$. If
$B=LC(T,\Omega)$ with $T$ profinite, the idempotents are the characteristic
functions of clopen subsets, so such families are the clopen partitions of $T$
indexed by $S$, i.e. the continuous maps $T\to S$.

*(3).* Write $S=\varprojlim_iS_i$ over its finite discrete quotients. Every
locally constant function on $S$ factors through some $S_i$, so
$LC(S,\Omega)=\varinjlim_i\Omega^{S_i}$. Therefore
$\Hom(LC(S,\Omega),LC(T,\Omega))=\varprojlim_i\Hom(\Omega^{S_i},LC(T,\Omega))
=\varprojlim_i\operatorname{Cont}(T,S_i)=\operatorname{Cont}(T,S)$, and tracing the
identifications shows that this is the map $s\mapsto(f\mapsto f\circ s)$.

*(2).* By definition an ind-étale algebra is a filtered colimit of étale algebras
of finite presentation ([def-weil-pbc-ind-etale-algebra]); by (1) and the
idempotent description, it is a filtered colimit $\varinjlim_i\Omega^{S_i}$
along maps induced by maps of finite sets $S_j\to S_i$. With
$S=\varprojlim_iS_i$, a profinite set, the colimit is $LC(S,\Omega)$, because a
locally constant function on the compact space $S$ factors through some $S_i$,
and two functions on $S_i$ agreeing on $S$ agree on the image of $S$ in some
$S_j$. Conversely $LC(S,\Omega)=\varinjlim_i\Omega^{S_i}$ is ind-étale.

By (2) the functor is essentially surjective onto affine ind-étale
$\Omega$-schemes, and by (3), using that $\Spec$ is an anti-equivalence between
algebras and affine schemes, it is fully faithful. Finally
$X[S]=\Spec(LC(S,\mathbf Z)\otimes_{\mathbf Z}\Omega)$ and
$LC(S,\mathbf Z)\otimes\Omega=\varinjlim_i\mathbf Z^{S_i}\otimes\Omega=
\varinjlim_i\Omega^{S_i}=LC(S,\Omega)$, compatibly with the maps.
