+++
kind  = "proof"
of    = "lemma-weil-pbc-derived-exchange-replacement"
+++
Write $Q$ for the passage from bounded below complexes (up to homotopy) to
$\Dplus$, and $c_M:f'_*M\to Rf'_*M$ for the canonical map. The termwise
underived exchange morphisms $\Ex^0_{\square,K}$, followed by
$c_{g'^{-1}K}$, form a natural transformation
$\beta:g^{-1}f_*\to Rf'_*g'^{-1}Q$ of functors on bounded below complexes up to
homotopy: $\Ex^0_\square$ is natural [lemma-weil-pbc-underived-exchange-naturality],
so applied degreewise it commutes with chain maps and carries chain homotopies
to chain homotopies.

Because $g^{-1}$ is exact, the pair $(g^{-1}Rf_*,\,g^{-1}\eta)$ is a right
derived functor of $g^{-1}f_*$: for every functor $G$ on $\Dplus(X_{\Et},\mathcal A)$
and every natural transformation $\beta:g^{-1}f_*\to GQ$ there is a unique
natural transformation $\alpha:g^{-1}Rf_*\to G$ with
$\alpha_K\circ g^{-1}(\eta_K)=\beta_K$ for all $K$. (Uniqueness: every object of
$\Dplus$ is isomorphic to a bounded below complex of injectives $I$
[def-weil-pbc-kinjective-resolutions], and for such $I$ the map $\eta_I$ is an
isomorphism, so $\alpha_I=\beta_I\circ(g^{-1}\eta_I)^{-1}$ is forced.
Existence: define $\alpha$ by this formula on a chosen injective resolution of
each object; naturality of $\beta$ and the homotopy uniqueness of maps into
complexes of injectives make it well defined and natural, and naturality of
$\beta$ along $K\to I$ gives $\alpha_K\circ g^{-1}(\eta_K)=\beta_K$ for every $K$.)

By [def-weil-pbc-derived-exchange], $\Ex_\square$ is the transformation
$\alpha$ attached to $\beta$ above. The first assertion is the identity
$\alpha\circ g^{-1}\eta=\beta$, and the converse assertion is the uniqueness
part of the universal property. Finally, if $K$ is a bounded below complex of
injectives, then $\eta_K$ is an isomorphism, so

$$
 \Ex_{\square,K}=c_{g'^{-1}K}\circ\Ex^0_{\square,K}\circ(g^{-1}\eta_K)^{-1},
$$

an expression involving no choices.
