+++
kind  = "proof"
of    = "lemma-weil-pbc-finite-exchange"
uses = ["def-kun-separably-closed", "def-weil-pbc-cartesian-square", "def-weil-pbc-derived-exchange", "def-weil-pbc-geometric-fibre", "lemma-openclosed-point-ulift", "lemma-openclosed-stalk-upperstar", "lemma-weil-pbc-finite-direct-image-exact", "lemma-weil-pbc-finite-stalk-formula", "lemma-weil-pbc-geometric-stalk-conservative"]
+++
The hypotheses on $\mathcal A$ are what makes stalks computable on underlying
sets: the stalk of an $\mathcal A$-valued sheaf at a geometric point is a
filtered colimit over étale neighbourhoods, which the forgetful functor
preserves, and sheafification commutes with the forgetful functor, so the
underlying set of a stalk of a sheaf (and of a pullback or a direct image) is
the corresponding stalk of underlying sets; since the forgetful functor
reflects isomorphisms, a morphism of $\mathcal A$-valued sheaves is an
isomorphism as soon as it is an isomorphism on all geometric stalks
([lemma-weil-pbc-geometric-stalk-conservative]), and it suffices to take
geometric points with algebraically closed residue field.

Let $F$ be a sheaf on $X_{\Et}$ and $\bar y'\to Y'$ such a geometric point,
with image $\bar y=g\circ\bar y'$ in $Y$. By
[lemma-openclosed-stalk-upperstar] the stalk of $g^{-1}f_*F$ at $\bar y'$ is
the stalk of $f_*F$ at $\bar y$, which by
[lemma-weil-pbc-finite-stalk-formula] is the finite product of the stalks
of $F$ at the geometric points of the finite fibre $X\times_Y\bar y$.
Likewise the stalk of $f'_*g'^{-1}F$ at $\bar y'$ is the product of the
stalks of $g'^{-1}F$, i.e. of $F$ at the images under $g'$, over the
geometric points of $X'\times_{Y'}\bar y'$. Since the square is cartesian,
$X'\times_{Y'}\bar y'=X\times_Y\bar y$, so the two products are indexed by
the same set. Expanding the unit--$\theta_\square$--counit composite of
[def-weil-pbc-underived-exchange] shows that the induced map is the identity
on every factor; hence it is an isomorphism, and the underived exchange map
is an isomorphism at every $F$.

For the derived statement, $f$ and its base change $f'$ are finite, so $f_*$
and $f'_*$ are exact ([lemma-weil-pbc-finite-direct-image-exact]), as are
$g^{-1}$ and $g'^{-1}$. Thus $Rf_*$ and $Rf'_*$ are computed termwise on any
representative of $K\in\Dplus(X_{\Et})$, with no resolution needed, and the
derived exchange morphism of [def-weil-pbc-derived-exchange] at $K$ is the
termwise underived exchange map, an isomorphism of complexes by the first
part.
