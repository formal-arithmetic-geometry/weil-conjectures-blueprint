+++
kind = "proof"
of = "lemma-stability"
order = 33
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability--1", "lemma-stability--2", "lemma-stability--3", "lemma-stability--4", "lemma-stability--5", "lemma-stability--6", "lemma-stability--7"]
+++
Since weakly étale means that a morphism and its diagonal are flat,
each assertion about weakly étale morphisms comes down to writing the
relevant diagonal in terms of diagonals and base changes that we already
know to be flat.

Base change preserves flatness of a morphism and its diagonal. For a
composite $V\to U\to X$, the morphism $V\to X$ is flat as a composite of
flat morphisms. Its diagonal $\Delta_{V/X}$ is $\Delta_{V/U}$ followed by
$V\times_UV\to V\times_XV$, and the second map is a base change of
$\Delta_{U/X}$. Both maps are flat, and hence so is $\Delta_{V/X}$.

Let $h:U\to V$ be an $X$-morphism between weakly étale $X$-schemes. We
factor $h$ as the graph $U\to U\times_XV$ followed by the projection
$U\times_XV\to V$. The graph is a base change of the diagonal of $V/X$,
which is flat, and the projection is a base change of $U\to X$, which is also
flat. Their composite $h$ is therefore flat. Similarly, the diagonal $\Delta_h:U\to
U\times_VU$ is the base change of $\Delta_{U/X}$ along the monomorphism
$U\times_VU\to U\times_XU$, so it is flat as well. Finally, Zariski locality
follows from the fact that flatness is Zariski local.

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
