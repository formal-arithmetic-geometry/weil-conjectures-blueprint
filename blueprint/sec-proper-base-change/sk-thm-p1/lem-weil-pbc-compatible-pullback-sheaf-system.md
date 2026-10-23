+++
id = "lem-weil-pbc-compatible-pullback-sheaf-system"
kind = "lemma"
title = "Compatible pullback sheaves form a system and become constant on a cone"
uses = ["def-pc-scheme", "def-weil-pbc-inverse-image", "lem-weil-pbc-inverse-image-composition"]
lean = ["AlgebraicGeometry.Etale.compatiblePullbackSheafSystem"]
order = 1848
+++
Let $I$ be a preordered set and $D:I^{op}\to\mathrm{Sch}$ an inverse diagram of schemes [def-pc-scheme], with an arbitrary cone $(X,(p_i:X\to D_i))$. Let $T$ be a scheme, $G$ an abelian sheaf on its small etale site, and $v_i:D_i\to T$ morphisms satisfying $v_j=v_i\circ D(f^{op})$ for every $f:i\to j$. Let $v:X\to T$ satisfy $v=v_i\circ p_i$. Use inverse images [def-weil-pbc-inverse-image] and their canonical composition comparisons [lem-weil-pbc-inverse-image-composition]. Put $F_i=v_i^{-1}G$, and let $a_f:D(f^{op})^{-1}F_i\xrightarrow{\sim}F_j$ be the inverse of the composition comparison transported by the specified equation for $v_j$. Let $b_i:v^{-1}G\xrightarrow{\sim}p_i^{-1}F_i$ be the forward composition comparison transported by the specified equation for $v$. Then (1) $a_{1_i}$ equals the inverse-image identity comparison, with transport along $D(1_i)=1_{D_i}$; (2) the $a_f$ satisfy the inverse-image cocycle law for every composable pair, including the comparison between the inverse image along the composite transition and $D(g^{op})^{-1}D(f^{op})^{-1}$; (3) the transition $p_i^{-1}F_i\to p_j^{-1}F_j$ obtained from the cone equation and $p_j^{-1}(a_f)$ becomes the identity of $v^{-1}G$ under $b_i,b_j$. Equivalently these comparisons present the pulled-back sheaves as the constant diagram with value $v^{-1}G$. No limiting, directedness, compactness or separatedness hypothesis is imposed.
