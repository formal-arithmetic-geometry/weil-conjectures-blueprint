+++
id = "def-weil-pbc-finite-section-pullback"
kind = "definition"
title = "Pullback of a section along a finite morphism"
order = 1110
lean = ["AlgebraicGeometry.Etale.globalSectionsUpperStarMap"]
uses = ["def-weil-pbc-inverse-image", "def-weil-pbc-scheme-conventions"]
+++
Let $\mathcal A$ be a Grothendieck abelian category for which $\mathcal A$-valued
sheaves on small etale sites admit sheafification, let $u:T'\to T$ be a
morphism of schemes [def-weil-pbc-scheme-conventions] (in the applications
$u$ is finite), and let $F$ be an $\mathcal A$-valued etale sheaf on $T$. The
*pullback of global sections* along $u$ is the map

$$
u^\sharp:\Gamma(T,F)\longrightarrow\Gamma(T',u^{-1}F)
$$

obtained by evaluating on $T$ the unit $F\to u_*u^{-1}F$ of the inverse-image
adjunction [def-weil-pbc-inverse-image] and identifying
$(u_*u^{-1}F)(T)=(u^{-1}F)(T\times_TT')$ with $(u^{-1}F)(T')$.

More generally, for an etale $V\to T$ and $s\in F(V)$ write

$$
u_V^\sharp(s)\in(u^{-1}F)(V\times_TT')
$$

for the image of $s$ under the unit, i.e. under the map from the presheaf
inverse image to its sheafification; this is the pullback of the global section
$s$ of $F|_V$ along the base change $V\times_TT'\to V$ of $u$.
