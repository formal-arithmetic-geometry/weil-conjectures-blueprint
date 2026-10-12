+++
kind  = "proof"
of    = "lem-weil-pbc-derived-exchange-termwise"
+++
*The comparison with $J$ is canonical.* Given two K-injective resolutions
$g'^{-1}I\to J$ and $g'^{-1}I\to J'$, the identity of $g'^{-1}I$ lifts to maps
$J\to J'$ and $J'\to J$ under $g'^{-1}I$, because K-injective complexes are
homotopically injective [def-weil-pbc-kinjective-resolutions]; their
composites are homotopic to the identities by the same lifting property.
Applying $f'_*$ preserves chain homotopies, so the two resulting maps out of
$g^{-1}f_*I$ define the same morphism of the derived category.

*Case of a bounded below complex of injectives.* Suppose first that $I$ is a
bounded below complex of injective sheaves. Then $f_*I$ computes $Rf_*I$, i.e.
the canonical map $\eta_I:f_*I\to Rf_*I$ is an isomorphism, and since $J$ is
K-injective the canonical map $f'_*g'^{-1}I\to Rf'_*g'^{-1}I$ is the class of
$f'_*(g'^{-1}I\to J)$. Hence the morphism produced by the termwise
construction is

$$
 g^{-1}Rf_*I\xrightarrow{(g^{-1}\eta_I)^{-1}}g^{-1}f_*I
 \xrightarrow{\Ex^0_{\square,I}}f'_*g'^{-1}I\longrightarrow Rf'_*g'^{-1}I,
$$

which is $\Ex_{\square,I}$ by the defining identity of
[def-weil-pbc-derived-exchange] applied to the complex $I$. Transporting along
the isomorphism $K\cong I$ in $\Dplus(X_{\Et})$ by naturality of $\Ex_\square$
gives $\Ex_{\square,K}$.

*General case.* Let $K\to I$ be an arbitrary K-injective resolution. Choose a
resolution $K\to I_0$ by a bounded below complex of injective sheaves (it
exists because the category of etale sheaves is Grothendieck abelian; it is a
K-injective resolution, cf. [prop-weil-pbc-kinjective-resolutions-exist]).
Since $I$ is K-injective, $K\to I$ extends along $K\to I_0$ to a map
$u:I_0\to I$, unique up to homotopy; $u$ is a quasi-isomorphism between
K-injective complexes, hence a homotopy equivalence, and so $f_*u$ and
$g^{-1}f_*u$ are homotopy equivalences. Choose K-injective resolutions
$g'^{-1}I_0\to J_0$ and $g'^{-1}I\to J$; since $J$ is K-injective, the map
$g'^{-1}u$ extends to $v:J_0\to J$, a quasi-isomorphism between K-injective
complexes, hence a homotopy equivalence. Because $\Ex^0_\square$ is a natural
transformation applied degreewise, the diagram

$$
 \begin{array}{ccccc}
 g^{-1}f_*I_0&\xrightarrow{\Ex^0_{\square,I_0}}&f'_*g'^{-1}I_0&\longrightarrow&f'_*J_0\\
 \downarrow g^{-1}f_*u&&\downarrow f'_*g'^{-1}u&&\downarrow f'_*v\\
 g^{-1}f_*I&\xrightarrow{\Ex^0_{\square,I}}&f'_*g'^{-1}I&\longrightarrow&f'_*J
 \end{array}
$$

commutes up to homotopy (the right square commutes up to homotopy because
both composites $g'^{-1}I_0\to J$ are lifts of the same map into a K-injective
complex). The vertical outer maps are homotopy equivalences compatible with
the identifications of their sources with $g^{-1}Rf_*K$ and of their targets
with $Rf'_*g'^{-1}K$, so the termwise constructions for $I$ and for $I_0$ give
the same morphism $g^{-1}Rf_*K\to Rf'_*g'^{-1}K$, which is $\Ex_{\square,K}$
by the previous case.
