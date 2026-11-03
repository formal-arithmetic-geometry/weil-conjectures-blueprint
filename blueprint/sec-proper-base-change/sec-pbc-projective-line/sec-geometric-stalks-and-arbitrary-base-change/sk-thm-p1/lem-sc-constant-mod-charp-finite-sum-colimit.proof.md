+++
kind = "proof"
of = "lem-sc-constant-mod-charp-finite-sum-colimit"
uses = ["lem-weil-pbc-zmod-module-structure-killed-by-n", "lem-weil-pbc-constant-sheaf-maps-global-sections", "lem-weil-pbc-constant-module-sheaf-underlying"]
+++
Put $M=\Lambda/(p)$. The image of $p$ in $M$ is zero, so $p\cdot m=0$ for every $m\in M$, and $M$ carries its canonical $\mathbf Z/p$-module structure [lem-weil-pbc-zmod-module-structure-killed-by-n]; regard it as a vector space over the field $\mathbf F_p=\mathbf Z/p$.

Choose a basis $B$ of $M$ over $\mathbf F_p$. The coordinate map identifies $M$ with the space of finitely supported functions $B\to\mathbf F_p$, i.e. with the direct sum $\bigoplus_{b\in B}\mathbf F_p$, which is the coproduct of copies of $\mathbf F_p$ in the category of $\mathbf F_p$-modules.

An arbitrary coproduct is the filtered colimit of its finite subcoproducts: the finite subsets $S\subseteq B$, ordered by inclusion, form a filtered category (the empty set is an object and unions give upper bounds), the diagram $S\mapsto\bigoplus_{b\in S}\mathbf F_p$ has the inclusions as transition maps, and $\bigoplus_{b\in B}\mathbf F_p$ with the canonical inclusions is its colimit.

Apply the functor "forget the scalars, then take the constant abelian sheaf" to this colimit cocone. Forgetting scalars preserves colimits of modules, and the constant-sheaf functor is a left adjoint (of global sections, [lem-weil-pbc-constant-sheaf-maps-global-sections]), so the image is again a colimit cocone. Its vertex is the constant abelian sheaf with value $M$, which is the underlying abelian sheaf $F$ of the constant sheaf of $\Lambda$-modules with value $M$ [lem-weil-pbc-constant-module-sheaf-underlying]; transport the cocone along this isomorphism so that its vertex is exactly $F$.

For each finite $S$, the constant-sheaf functor preserves finite coproducts, so the stage is the finite coproduct of $|S|$ copies of $\underline{\mathbf Z/p}$, i.e. the finite direct sum $(\underline{\mathbf Z/p})^{\oplus n}$ with $n=|S|$ after enumerating $S$. If $M=0$ the basis is empty, the index category has one object and the stage is the zero sheaf. No geometric assumption enters.
