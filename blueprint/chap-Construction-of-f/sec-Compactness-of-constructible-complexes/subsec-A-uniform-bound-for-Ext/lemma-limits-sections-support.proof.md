+++
kind = "proof"
of = "lemma-limits-sections-support"
order = 437
+++
The functor $R\underline\Gamma_Z$ is left $t$-exact because it is right
adjoint to the exact functor $i_*$. Restricting along the open
immersion $u$ is exact, so $u^*R\underline\Gamma_Z$ is left $t$-exact as
well.

For the limits, recall that the derived inverse limit of a
sequence $(K_n)$ is the fibre of the map
$\prod_nK_n\to\prod_nK_n$ given by the identity minus the transition
maps. It therefore suffices to show
that the functors preserve products and fibres. Restriction to an open
is exact and preserves limits, so this holds for $j^*$ and $u^*$. It
holds for $i^*$ by [Stacks, [09AA](https://stacks.math.columbia.edu/tag/09AA)], and for $Rj_*$ because $Rj_*$ is a right
adjoint. It follows for
$R\underline\Gamma_Z=i^*\fib(\mathrm{id}\to Rj_*j^*)$.
Finally, tensoring with a finite locally free sheaf $L$ is exact and is right
adjoint to tensoring with $L^\vee$, so it preserves products as well.
