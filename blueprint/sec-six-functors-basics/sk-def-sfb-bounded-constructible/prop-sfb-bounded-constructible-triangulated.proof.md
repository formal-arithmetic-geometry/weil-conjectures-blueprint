+++
kind  = "proof"
of    = "prop-sfb-bounded-constructible-triangulated"
uses = ["lem-sfb-bounded-constructible-iff", "def-sfb-constructible-module", "def-constructible-stratification"]
+++
Stability under $0$, shifts and isomorphisms is clear from
[lem-sfb-bounded-constructible-iff]. Let $K\to L\to M\to K[1]$ be distinguished with two
of the vertices bounded constructible; by rotation we may assume these are $K$ and $M$.
The long exact cohomology sequence
$$
H^{n-1}(M)\xrightarrow{\delta}H^n(K)\to H^n(L)\to H^n(M)\xrightarrow{\delta}H^{n+1}(K)
$$
shows that $L$ is bounded and that $H^n(L)$ is an extension of
$\ker(H^n(M)\to H^{n+1}(K))$ by $\operatorname{coker}(H^{n-1}(M)\to H^n(K))$. So it
suffices that constructible $\mathcal R$-modules [def-sfb-constructible-module] on $X$
are closed under cokernels, kernels and extensions.

*Common stratification.* Given finitely many constructible modules and morphisms between
them, intersect the strata of their stratifications. Since $X$ is topologically
Noetherian, the pairwise intersections of strata are locally closed and finite in number,
and choosing immersions onto them gives a common refinement
[def-constructible-stratification]. Restriction to a smaller stratum preserves local
finite presentation, because pullback is strong monoidal and right exact and so preserves
free modules and their cokernels. So we may work over a single stratum $Z$, where all
the modules involved are locally finitely presented. Passing to a common refinement of
the covers, we may also work on a single member $U$ of a pro-étale cover, where they are
finitely presented.

*Cokernels and extensions.* Let $N'\to N$ be a morphism of finitely presented modules
over $\mathcal R|_U$. After refining $U$, each image of a basis vector of the free module
presenting $N'$ lifts to the free module presenting $N$, since $\mathcal R^n\to N$ is an
epimorphism of sheaves. So the cokernel is presented by the combined relations, and it is
finitely presented. If $0\to N'\to N\to N''\to0$ is exact with $N',N''$ finitely
presented, then, after refining $U$, the generators of $N''$ lift to $N$. Together with
the generators of $N'$ they give an epimorphism from a free module of finite rank onto
$N$. Its kernel is an extension of the relation modules of $N'$ and $N''$, which are
locally finitely generated. So $N$ is locally finitely presented.

*Kernels.* For kernels one needs that the kernel of a morphism of locally finitely
presented $\mathcal R$-modules over a stratum is again locally finitely presented, after
refining the stratification. This is a coherence property of $\mathcal R$ on the strata.
For the $\ell$-adic coefficient rings it is where the Noetherianity of $\cO_E$ enters, as
for the constructible $\ell$-adic sheaves of Bhatt–Scholze, §6.8, which are locally
constant with finitely generated values on the strata.
