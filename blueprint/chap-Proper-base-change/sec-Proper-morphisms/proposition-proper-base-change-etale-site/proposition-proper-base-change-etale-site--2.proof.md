+++
kind = "proof"
of = "proposition-proper-base-change-etale-site--2"
order = 398004
uses = ["definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-cohomology-modules-underlying-abelian", "prose-04-17"]
+++
For (i), restriction of scalars along $\Lambda\to\Lambda/N\Lambda$ is
exact and conservative. It preserves torsion cohomology and commutes
with inverse images, derived direct images and the base change maps;
the direct images can be computed on the underlying abelian sheaves
as in Lemma [lemma-cohomology-modules-underlying-abelian]. Thus the
base change map over $\Lambda/N\Lambda$ is an isomorphism if and only if
the one over $\Lambda$ at the restricted complex is an isomorphism.
Apply $\mathrm{PBC}_\Lambda(f)$.

For (ii), first let $F$ be a sheaf of $\Lambda$-modules killed by a prime
$p$. It comes from a sheaf of $\Lambda/p\Lambda$-modules: the counit of
restriction and coextension of scalars is an isomorphism at $F$.
The ring $\Lambda/p\Lambda$ is killed by $p$, so its module sheaves
are torsion. The assumed base change property and the same comparison
under restriction of scalars give the degreewise base change
isomorphisms for $F$.

If $nF=0$ for $n>0$, induction on the number of prime factors of $n$
reduces to this case. For $p\mid n$, use
$0\to F[p]\to F\xrightarrow{p}pF\to0$; the outer terms are killed by
$p$ and $n/p$, and the long exact cohomology sequences give the result
for $F$. An arbitrary torsion sheaf is a filtered colimit of sheaves
killed by positive integers. Since $f$ and its base changes are
quasi-compact and quasi-separated, higher direct images commute with
these colimits by (4.7) in [prose-04-17]. This proves the assertion for
all torsion sheaves.

Finally, both sides of the derived base change map do not lower
cohomological degrees. For a bounded below complex $K$, their
cohomology in degree $m$ therefore depends only on $\tau_{\leq m}K$.
This is a bounded complex built from its shifted cohomology sheaves
by truncation triangles. The sheaf case and the long exact cohomology
sequences prove that the base change map is an isomorphism at every
$K$ with torsion cohomology.
