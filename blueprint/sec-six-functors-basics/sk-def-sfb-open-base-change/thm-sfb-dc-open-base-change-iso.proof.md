+++
kind  = "proof"
of    = "thm-sfb-dc-open-base-change-iso"
uses = ["sk-def-sfb-module-pushforward-pullback", "sk-prop-sfb-module-derived-factorization"]
+++
All functors involved are restrictions of ambient functors and commute with the inclusions, and
on the ambient categories $Lg^*\cong D(g^*)$ and $j_!=D(j_!)$ are computed levelwise
([sk-prop-sfb-module-derived-factorization]). So it suffices to show that the underived exchange
$j'_!g'^*M\to g^*j_!M$ is an isomorphism for every $\Lambda_X$-module $M$. This exchange is the
mate of the base change morphism $j^*g_*\to g'_*j'^*$ for the pushforwards
([sk-def-sfb-module-pushforward-pullback]). For $N$ on $Z'$, adjunction gives

$$
\Hom(g^*j_!M,N)\cong\Hom(M,j^*g_*N),\qquad\Hom(j'_!g'^*M,N)\cong\Hom(M,g'_*j'^*N).
$$

So it suffices that $j^*g_*N\to g'_*j'^*N$ is an isomorphism. On an object $V$ of
$X_{\mathrm{proét}}$, both sides are the sections of $N$ over $V\times_ZZ'=V\times_XX'$. These
agree because the square is cartesian. The isomorphism is compatible with the module structures,
which are transported along the coefficient maps of the square.
