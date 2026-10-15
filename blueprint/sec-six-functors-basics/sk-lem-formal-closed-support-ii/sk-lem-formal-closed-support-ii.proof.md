+++
kind = "proof"
of = "sk-lem-formal-closed-support-ii"
+++
$R\underline\Gamma_Z$ is left $t$-exact because it is right adjoint to the exact functor $i_*$
([det-formal-closed-support-ii-left-exact]). A derived inverse limit of a sequence is the fiber of
$1-\mathrm{shift}$ on a product, so it suffices that the functors preserve products and fibers. This
holds for $j^*$ and $u^*$ (open restriction is exact and preserves limits), for $i^*$ (Stacks, Tag 09AA),
for $Rj_*$ (a right adjoint), hence for $R\underline\Gamma_Z=i^*\fib(\mathrm{id}\to Rj_*j^*)$.
Tensoring with a finite locally free sheaf $L$ is exact and is right adjoint to tensoring with
$L^\vee$, so it preserves products ([det-formal-closed-support-ii-limits]). The lemma is used below
with $\Lambda=\mathcal O_E$.
