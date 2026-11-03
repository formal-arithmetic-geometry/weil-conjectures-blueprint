+++
kind = "proof"
of = "det-pe-topos-functoriality-site"
+++
*1.* A pro-étale covering is an fpqc covering of schemes whose members are weakly étale.
Fpqc coverings of schemes satisfy the three axioms: isomorphisms are fpqc coverings,
composites of fpqc coverings and base changes of fpqc coverings along arbitrary morphisms
are fpqc coverings (Stacks Project, Topologies, fpqc coverings). It remains to see that the members stay weakly
étale and that the fibre products stay in the site. If $U_i\to U$ and $V\to U$ are
morphisms of weakly étale $X$-schemes, then $U_i\to U$ is weakly étale
([lem-trf-weakly-etale-between-objects]); its base change $U_i\times_UV\to V$ is weakly
étale, and the composite $U_i\times_UV\to V\to X$ is weakly étale by stability under
composition ([lem-weil-pbc-ind-etale-stability]). So the scheme fibre product is an
object of $X_{\mathrm{proét}}$ and is the fibre product there. Composites of weakly étale
morphisms are weakly étale, which treats the composite coverings.

*2.* Let $\{U_i\to U\}$ be a covering. A compatible family of $X$-morphisms
$a_i\colon U_i\to T$ (agreeing on $U_i\times_UU_j$) descends to a unique morphism of schemes
$a\colon U\to T$, because representable functors are sheaves for the fpqc topology on
schemes (fpqc descent for morphisms, Stacks Project, Descent). The descended morphism is an
$X$-morphism, since its composite with $T\to X$ and the structure map $U\to X$ agree after
composition with each $U_i\to U$, and uniqueness of descent applies to $h_X$.

*3.* The objects are weakly étale morphisms from $\mathcal U$-small schemes, as in the size
convention of [def-weil-pbc-proetale-site], so the isomorphism classes form a set of the
next universe, and the morphism sets are small. Hence $X_{\mathrm{proét}}$ is equivalent to a
small category, and so is every slice of it. On a small site, sheafification exists for a
Grothendieck abelian $\mathcal A$ with morphism groups of the size of the site: it is the
transfinite iteration of the plus construction, which converges because $\mathcal A$ is
locally presentable and filtered colimits in $\mathcal A$ are exact. Transport along the
equivalence gives sheafification on $X_{\mathrm{proét}}$.
