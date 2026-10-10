+++
kind  = "proof"
of    = "thm-weil-pbc-amplification-proper"
+++
*step (a), AMP.* In the quotient datum of the adic coefficient datum, the
condition $N(A/I)=0$ means $N\in I$. Hence $N^nP_n=0$, and $N^n$ is
invertible on the four schemes for every $n\geq1$. The geometric fibers of
$f'$ are base changes of those of $f$, hence of dimension at most $e$, so
[thm-weil-pbc-direct-image-finiteness-proper] gives
$\mathrm{FIN}(f,P_n;2e)$ and $\mathrm{FIN}(f',P_n;2e)$ for every $n\geq1$,
i.e. clause (i) of [def-weil-pbc-finite-level-amplification]; clause (ii) is
[lem-weil-pbc-pullback-preserves-bounded-constructible] for the two
pullbacks.

*step (b), WIT.* The finite-level functors commute with the normalization
isomorphisms for $P_{n+1}\to P_n$: for the direct images this is the
projection-formula compatibility of the reduction maps (the tensor with the
perfect $P_n$ commuting with $Rf_{*,n+1}$), and for the pullbacks it is the
tensor compatibility of inverse image with the quotient maps. A compatible
etale-origin witness [def-weil-pbc-etale-origin-witness]
$K_n\cong\nu_X^*L_n$ is transported: for the direct images by
$$
 Rf_{*,n}K_n\cong Rf_{*,n}\nu_X^*L_n\cong\nu_Y^*Rf_{\Et,*}L_n
$$
of [prop-weil-pbc-comparison-direct-image] (the quotient tower being built
from the same $L_n$), and for the pullbacks by
[lem-weil-pbc-comparison-pullback]; the compatibility of the transported
witnesses is the above commutation with the normalizations. Hence
$\mathrm{WIT}(\square)$.

*step (c), TOW.* A uniformly bounded constructible tower is compatibly
witnessed on the local models $L_{\alpha j}$ supported in $[d_0,d_1]$ with
finite lisse cohomology reductions, and step (b) transports the witnesses.
The levelwise direct images are therefore etale-origin; their reduction
cohomology is bounded constructible by
[thm-weil-pbc-direct-image-finiteness-proper] with the amplitude containment
of [prop-weil-pbc-amplification-consequences], and the local models are
obtained from the etale-origin descriptions: a finite lisse module is finite
locally constant, which is exactly what the tower condition requires, while
no freeness is needed or available, a finite module over a finite local ring
being possibly non-free (for instance $\mathbf Z/2$ over $\mathbf Z/4$). The
pullback side is [lem-weil-pbc-pullback-preserves-bounded-constructible].
The output tower is hence uniformly bounded constructible, i.e.
$\mathrm{TOW}(\square)$.

The source text records that audit item BC-07 was resolved by correcting the
definition rather than the proof: the bounded constructible tower and the
tower-preservation condition formerly required the local models to have
finite locally *free* terms, which a general constructible complex does not
have. The requirement is now finite local constancy, which is exactly what
finite lissity gives.
