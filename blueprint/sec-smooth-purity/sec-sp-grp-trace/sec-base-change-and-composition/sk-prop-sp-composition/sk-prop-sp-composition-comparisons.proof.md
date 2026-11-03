+++
kind = "proof"
of = "det-sp-composition-comparisons"
+++
(1) Composites of adjunctions are adjunctions: $Rg_!Rf_!\dashv f^!g^!$ with
counit $\varepsilon_g\circ Rg_!\varepsilon_fg^!$. Transporting along the
composition isomorphism $R(g\circ f)_!\simeq Rg_!Rf_!$ and using uniqueness of
right adjoints with their counits identifies $(g\circ f)^!$ with $f^!g^!$, the
counit becoming the composite of the two counits.

(2) For $b$: choose compactifications compatibly; on each finite free term
$A^r$ of a resolution of $B$ over $A$, both sides are the identity of the
$r$-fold sum, by naturality of the composition isomorphism
$R(g\circ f)_!\simeq Rg_!Rf_!$; the totalization argument of
[det-sp-reduction-direct-image] (finite windows in each degree) then gives the
identity for arbitrary $A\to B$. For $c$: transpose both sides under the
composite adjunction of (1). Using the defining counit identity of
[det-sp-reduction-exceptional] for $f$ and for $g$ and naturality, the transpose
of the right-hand side is $(\varepsilon_{g\circ f,A}(K))_B$ composed with the
inverse of $Rg_{!,B}(b^f)\circ b^g$, which by the identity for $b$ is
$(\varepsilon_{g\circ f,A}(K))_B\circ b^{g\circ f}(-)^{-1}$, the transpose of
$c^{g\circ f}_{A,B}(K)$.

(3) The tower composition isomorphisms are built in the tower categories by the
same recipe (composition of tower adjunctions, [det-sp-tower-gluing]), so their
levels are the finite ones. By (2) for $\mathcal O_E/\ell^n\to\mathcal O_E/\ell^m$ they
commute with the reduction maps, hence preserve normalized towers; under the
equivalence of normalized towers with integral complexes
([det-sp-integral-adjunction-bijection]), $R\varprojlim$ gives the integral
composition isomorphisms.
