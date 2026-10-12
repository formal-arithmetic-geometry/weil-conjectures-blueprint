+++
kind  = "proof"
of    = "prop-weil-pbc-finite-morphism"
uses = ["def-weil-pbc-derived-exchange", "def-weil-pbc-underived-exchange", "lemma-weil-pbc-finite-direct-image-exact", "lemma-weil-pbc-finite-exchange"]
+++
Every base change $f':X'\to Y'$ of the finite morphism $f$ is finite. For a
cartesian square with $f$ on the right and $g$ arbitrary,
[lemma-weil-pbc-finite-exchange] shows that the underived exchange morphism
[def-weil-pbc-underived-exchange] $g^{-1}f_*F\to f'_*g'^{-1}F$ is an
isomorphism for every sheaf $F$ on $X_{\Et}$: at a geometric point of $Y'$
both sides are the same finite direct sum of stalks of $F$, indexed by the
geometric points of the finite fibre, and the map is the identity on each
summand. No torsion hypothesis on $F$ enters. By
[lemma-weil-pbc-finite-direct-image-exact] the direct images $f_*$ and
$f'_*$ are exact, so for $K\in\Dplus(X_{\Et})$ the derived direct images
$Rf_*K$ and $Rf'_*g'^{-1}K$ are computed termwise by $f_*$ and $f'_*$, and
the derived exchange morphism [def-weil-pbc-derived-exchange] on $K$ is the
termwise underived exchange morphism; it is an isomorphism in every degree,
hence an isomorphism in $\Dplus(Y'_{\Et})$. Since $g$ was arbitrary, this is
$\mathrm{PBC}(f)$ in the sense of [def-weil-pbc-property], which in
particular contains the case of torsion sheaves.
