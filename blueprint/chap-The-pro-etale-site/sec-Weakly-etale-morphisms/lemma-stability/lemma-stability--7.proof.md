+++
kind = "proof"
of = "lemma-stability--7"
order = 32015
+++
For ind-étale ring maps, base change is clear because tensor products
commute with filtered colimits. For composition, let $R\to B$ and $B\to C$
be ind-étale, with $B=\varinjlim_\alpha B_\alpha$. Each étale
$B$-algebra $C'$ occurring in a presentation of $C$ is of finite
presentation over $B$, hence is the base change of an étale algebra
$C'_\alpha$ over some $B_\alpha$. Since $B_\alpha$ is étale over $R$,
so is $C'_\alpha$, and $C'$ is the filtered colimit of the étale
$R$-algebras $C'_\alpha\otimes_{B_\alpha}B_\beta$ for $\beta\geq\alpha$.
Thus $C$ is a filtered colimit of ind-étale $R$-algebras, and such a
colimit is again ind-étale [Stacks, [097L](https://stacks.math.columbia.edu/tag/097L)].

*Source:* the proof of Lemma [lemma-stability].
