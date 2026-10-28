+++
id = "lem-kun-0f1h"
kind = "lemma"
title = "Base change for open immersions"
order = 3154
uses = ["def-kun-torsion-invertible", "def-kun-truncations", "def-kun-unbounded-exchange", "def-weil-pbc-strict-henselization-limit", "lem-kun-0ezt", "lem-kun-0f09", "lem-kun-0f0u", "lem-kun-0f14b", "lem-kun-0f1c", "lem-kun-0f1g", "lem-kun-0f1h-sep-reduction", "lem-kun-base-change-open-closed", "lem-kun-bc-base-change", "lem-kun-bc-kunneth-compat", "lem-kun-closed-points-of-product", "lem-kun-compactification-affine", "lem-kun-descent-limit", "lem-kun-descent-limit-open", "lem-kun-dimension-extension", "lem-kun-dimension-finite-type", "lem-kun-fibre-product-limits", "lem-kun-finite-closed-subscheme", "lem-kun-invertible-orders-colimit", "lem-kun-leray-bdd", "lem-kun-projective-implies-proper", "lem-kun-proper-stability", "lem-kun-stalk-as-pullback", "lem-kun-stalk-faithful-derived", "lem-kun-tensor-unit", "lem-kun-zn-sheaf-invertible-orders", "lem-weil-pbc-exchange-identity-pasting", "lemma-weil-pbc-direct-image-filtered-colimit"]
+++
Let $K$ be a field. Let $j:U\to X$ be an open immersion of
schemes of finite type over $K$ and let $Y$ be a scheme of finite
type over $K$. Consider the diagram

$$
\begin{array}{ccc}
Y\times_{\Spec(K)}X&\xleftarrow{\;h\;}&Y\times_{\Spec(K)}U\\
\Big\downarrow{\scriptstyle q}&&\Big\downarrow{\scriptstyle p}\\
X&\xleftarrow{\;j\;}&U .
\end{array}
$$

Then the exchange morphism of
[def-kun-unbounded-exchange],
$q^{-1}Rj_*F\to Rh_*p^{-1}F$, is an isomorphism for every abelian
sheaf $F$ on $U_{\Et}$ whose stalks are torsion of orders
invertible in $K$.
