+++
kind  = "proof"
of    = "lem-weil-pbc-module-sheaves-enough-injectives"
uses  = ["lem-weil-pbc-module-sheaves-grothendieck-abelian", "def-sp-grothendieck-abelian", "lem-sp-grothendieck-enough-injectives", "def-sp-injective-resolutions"]
+++
**Step 1.** *$\Mod(T_{\Et},R)$ and $\Ab(T_{\Et})$ are Grothendieck abelian.* By [lem-weil-pbc-module-sheaves-grothendieck-abelian] with $\Lambda=R$, the category $\Mod(T_{\Et},R)$ of sheaves of $R_T$-modules is a Grothendieck abelian category [def-sp-grothendieck-abelian]: it is abelian, has all small colimits, filtered colimits in it are exact, and it has a generator ($\bigoplus_U j_{U!}R_U$ over a set of representatives $U$ of an essentially small dense subcategory of $T_{\Et}$). The same lemma (its case $\Lambda=\mathbf Z$) says that $\Ab(T_{\Et})$ is Grothendieck abelian.

**Step 2.** *Enough injectives.* A Grothendieck abelian category has enough injectives [lem-sp-grothendieck-enough-injectives] (Stacks 079H: it even has a functorial injective embedding, i.e. a functor $M\mapsto I(M)$ with $I(M)$ injective and a natural monomorphism $i_M:M\to I(M)$; taking $J=I(F)$ and $F\hookrightarrow J$ the map $i_F$ gives the statement for each $F$). Applied to the two Grothendieck abelian categories of step 1, $\Mod(T_{\Et},R)$ and $\Ab(T_{\Et})$ have enough injectives, with injectivity in the sense of [def-sp-injective-resolutions] taken inside the respective category.

*Source: Stacks project, injectives.tex, Theorem 079H (theorem-injective-embedding-grothendieck), applied to Mod(O) as in Cohomology on Sites, proof of Lemma 07AC.*
