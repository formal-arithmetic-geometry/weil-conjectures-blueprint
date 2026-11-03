+++
kind  = "proof"
of    = "det-lem-coefficient-finite-descent-objects"
+++
*Models persist.* $((K_E)_F)_{\Qlb}=(K_E)_{\Qlb}$ since extension of scalars is transitive; and
$(K_E)_F$ has constructible cohomology $F_X\otimes H^q(K_E)$ (flatness, and extension of scalars
preserves local freeness on strata). So we may always enlarge $E$.

*Cones.* Suppose $K'\to K\to K''\xrightarrow{\delta}K'[1]$ is distinguished in $\Dbc(X,\Qlb)$ and
$K'$, $K''$ have models $K'_E$, $K''_E$ over a common $E$ (enlarge to a common one). By
[det-lem-coefficient-finite-descent-hom] (3), with $C=K''_E$, $D=K'_E$, $r=1$, the class
$\delta$, transported along the isomorphisms $(K''_E)_{\Qlb}\cong K''$, $(K'_E)_{\Qlb}\cong K'$,
is the image of some $\delta_F\colon(K''_E)_F\to(K'_E)_F[1]$ for a finite $F\supseteq E$. Let
$K_F$ be the shifted cone of $\delta_F$, i.e. a fibre: $K_F\to(K''_E)_F\xrightarrow{\delta_F}(K'_E)_F[1]$.
Extension of scalars to $\Qlb$ is exact, so it carries this triangle to one isomorphic to the
given one (by the axiom TR3 a morphism of triangles with two isomorphisms gives an
isomorphism on the third vertex), whence $(K_F)_{\Qlb}\cong K$. Also $K_F\in\Dbc(X,F)$ since
$\Dbc(X,F)$ is triangulated ([det-cor-coefficient-heart-ii-triangulated]).

*Sheaves.* For constructible $K$, take the filtration of [det-lem-coefficient-heart-filtration];
each $F_k/F_{k-1}=a_{k!}L_k$ with $L_k$ lisse descends by [det-lem-coefficient-finite-descent-lisse]
(1), because $a_{k!}$ commutes with extension of scalars ($a_{k!}=i_*u_!$, and both $u_!$ and
$i_*$ commute with the exact functor $\QbarX\otimes_{E_X}-$, as one checks on the open and closed
pieces). Induction on $k$ with the cone step gives a model of $F_m=K$.

*Complexes.* Induct on the number of nonzero cohomology sheaves using
$\tau_{<q}K\to K\to\mathcal H^q(K)[-q]\to$ and the cone step. Each step enlarges $E$ by a
finite extension, and there are finitely many steps.
