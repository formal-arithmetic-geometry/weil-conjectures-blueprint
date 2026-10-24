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
suffices that constructible $\Lambda_X$-modules [def-sfb-constructible-module] on $X$
are closed under cokernels, kernels and extensions.

*Common stratification.* Given finitely many constructible modules and morphisms between
them, intersect the strata of their stratifications. Since $X$ is topologically
Noetherian, the pairwise intersections of strata are locally closed, hence constructible,
and finite in number, and choosing immersions onto them gives a common refinement
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

*Kernels.* Let $f\colon N'\to N$ be a morphism of locally finitely presented
$\Lambda_Z$-modules on a stratum $Z$; the restriction of $\Lambda_X$ to $Z$ is $\Lambda_Z$,
since inverse images compose. It suffices that $\ker f$ is locally finitely presented on
the strata of some stratification of $Z$: as $X$ is topologically Noetherian, these strata
are locally closed and constructible in $X$, and together with the other strata of $X$
they refine the given stratification. This is the step that uses the hypothesis on
$\Lambda$; for a general ring object it fails, since kernels of maps of finitely presented
modules over a non-coherent ring need not be finitely generated. For instance, on
$X=\operatorname{Spec}\bar k$ with $\mathcal R$ the constant sheaf of
$B=k[x,y_1,y_2,\dots]/(xy_1,xy_2,\dots)$, the cone of $x\colon\mathcal R\to\mathcal R$ has
$H^{-1}$ the constant sheaf of the ideal $(y_1,y_2,\dots)$, which is not locally finitely
generated, because this ideal is not a finitely generated $B$-module.

If $\Lambda=\underline T$ with $T$ finite and discrete, $\Lambda_Z$ is the constant sheaf
$T$, whose sections are locally constant. After refining the cover, the finitely many
entries of presentation matrices of $N'$ and $N$, and of a lift of $f$ to the free
modules presenting them (which exists after refining, as in the previous step), are
constant. Then $N'$, $N$ and $f$ are the constant sheaves of finite $T$-modules $P'$, $P$
and of a $T$-linear map $\varphi\colon P'\to P$. The constant sheaf functor is exact, so
$\ker f$ is the constant sheaf of $\ker\varphi$, which is finitely presented over the
Noetherian ring $T$; hence $\ker f$ is locally finitely presented, already on $Z$.

If $\Lambda$ is $\underline E$, $\underline{\cO}_E$ or $\underline{\Qlb}$, the scalar ring
$\Lambda(*)$ is a field or a discrete valuation ring, in particular Noetherian. By the
structure theory of constructible $\ell$-adic sheaves (Bhatt–Scholze, §6.8), the locally
finitely presented $\Lambda_Z$-modules are, on the strata of a stratification of $Z$, the
lisse sheaves, pro-étale locally of the form $\Lambda_U\otimes_{\Lambda(*)}P$ with $P$ a
finitely generated $\Lambda(*)$-module, and they form an abelian subcategory of the
$\Lambda$-modules on each stratum, closed under kernels; this rests on the Noetherianity
of $\Lambda(*)$ and on $\Lambda_U$ being flat over $\Lambda(*)$. Hence $\ker f$ is locally
finitely presented on the strata of a stratification of $Z$, as required.
