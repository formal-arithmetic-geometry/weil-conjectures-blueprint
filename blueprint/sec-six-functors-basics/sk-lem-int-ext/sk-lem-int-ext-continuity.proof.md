+++
kind = "proof"
of = "det-lem-int-ext-continuity"
+++
By the five lemma applied to the long exact Hom sequences of the filtration
of [det-lem-int-ext-formula](1), it suffices to treat $C=a_!L$. By
[det-lem-int-ext-formula](2),
$\Hom(a_!L,K[q])=H^q R\Gamma(S,L^\vee\otimes^{\mathbf L}u^*R\underline\Gamma_ZK)$.
The functor $R\underline\Gamma_Z$ is the fibre of $K\to Rj_*j^*K$ (followed by
$i^*$), and the proof of [sk-cor-pe-bounded-continuity], which works for any
sheaf of rings, shows that $Rj_*$, $R\Gamma(S,-)$ and the exact functors $j^*$,
$i^*$, $u^*$ commute with filtered colimits of complexes with a common lower
bound; hence so does the fibre $R\underline\Gamma_Z$ (as in the proof of
[sk-lem-constructible-ext-continuity]). The functor $L^\vee\otimes^{\mathbf L}-$
commutes with filtered colimits and, having finite Tor amplitude $[0,1]$,
keeps a common lower bound (its amplitude is bounded). Composing, the
displayed $H^q$ commutes with such colimits. In particular this applies to
$\Hom$ and $\Ext^1$ between constructible sheaves.
