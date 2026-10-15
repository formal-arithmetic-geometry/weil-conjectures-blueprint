+++
kind = "proof"
of = "sk-thm-chow"
uses = ["sk-thm-chow-projective"]
+++
This is [sk-thm-chow-projective], whose closed-graph argument gives both
closed immersions.

Recall the shape of that argument in the Noetherian case. Cover $X$ by
finitely many affine opens $U_1,\dots,U_m$ all of which contain the generic
points of all irreducible components, so $U=\bigcap_iU_i$ is dense; embed the
$U_i$ in projective spaces, take the closure $\widetilde X$ of $U$ in
$\prod_iZ_i$, $Z_i$ the closure of $U_i$ in a projective space over $Y$, and
glue the projections $\widetilde X\to Z_i$ into $\pi:\widetilde X\to X$ (they
agree on the dense $U$); $\pi$ is proper and surjective. The Segre composite
$i_Y:\widetilde X\hookrightarrow\prod_iZ_i\hookrightarrow\mathbf P^n_Y$ is a
closed immersion, because $\widetilde X$ is proper over $Y$ and a proper
immersion is closed. The same closed-graph reasoning shows that
$(\pi,i_Y):\widetilde X\to\mathbf P^n_X$ is an immersion which is proper over
$X$, hence a closed immersion. Over a general affine base the statement is
taken from [sk-thm-chow-projective]; the detail
[lemma-weil-pbc-chow-factorization] reaches it by descending $f$ to a model
over a Noetherian base, and [lem-weil-pbc-projective-embedding] gives the
closed immersion $i_X$.
