+++
kind = "proof"
of = "sk-lem-formal-closed-support-ii"
+++
The functor $R\underline\Gamma_Z$ is left $t$-exact because it is right adjoint to the exact functor $i_*$
([det-formal-closed-support-ii-left-exact]). A derived inverse limit of a sequence is the fibre of the
difference of the identity and the transition maps on a product, and hence it suffices to show that the
functors preserve products and fibres. This holds for $j^*$ and $u^*$ (restriction to an open is exact and
preserves limits), for $i^*$ ([Stacks, Tag 09AA](https://stacks.math.columbia.edu/tag/09AA)), and for
$Rj_*$ (a right adjoint), and therefore also for $R\underline\Gamma_Z=i^*\fib(\mathrm{id}\to Rj_*j^*)$.
Tensoring with a finite locally free sheaf $L$ is exact and is right adjoint to tensoring with
$L^\vee$, so it preserves products as well ([det-formal-closed-support-ii-limits]).
