+++
kind = "proof"
of = "proposition-compactness-proper-direct-image--1"
order = 497002
+++
The rational proofs (Theorem [theorem-compactness-rational-coefficients],
Lemmas [lemma-reduction-finitely-many-degrees] and [lemma-proper-direct-image-unbounded-complexes])
go through once we supply for $\mathcal O_E$ the four inputs they use:
the abelian structure of Lemma [lemma-structure-integral-constructible-complexes](1),
continuity of $\Ext^i(C,-)$ for
bounded below systems, a bound $d_C$ with $\Ext^i(C,N)=0$ for $i>d_C$ and
$N$ constructible, and a bound on the amplitude of $Rp_*$.

For continuity, take $C=a_!L$ on a stratum. By
Lemma [lemma-sections-support-closed-subscheme](2), $R\!\operatorname{Hom}(a_!L,-)$ is
$R\Gamma(S,-)$ of the dual of $L$ tensored with
$u^*R\underline\Gamma_Z$. The proof of that formula uses only that $L$ is
dualizable, which holds by
Lemma [lemma-structure-integral-constructible-complexes](3), and so continuity follows from
Corollary [corollary-continuity-cohomology].

The bound $d_C$ comes from counting degrees as in
Lemma [lemma-uniform-ext-bound]. The reductions of $N$ lie
in $[-1,0]$, and the dual of $L$ adds one degree. The functors $R\Gamma$ and
$R\underline\Gamma_Z$ add the cohomological dimensions of
Definition [definition-cohomological-dimension]. The derived limit over the reductions adds
one more [Stacks, [08TB](https://stacks.math.columbia.edu/tag/08TB)].

*Source:* the proof of Proposition [proposition-compactness-proper-direct-image].
