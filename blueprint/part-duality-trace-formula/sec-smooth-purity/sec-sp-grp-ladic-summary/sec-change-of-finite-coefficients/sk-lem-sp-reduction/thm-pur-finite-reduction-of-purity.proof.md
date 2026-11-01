+++
kind  = "proof"
of    = "thm-pur-finite-reduction-of-purity"
+++
Step 1: reduction to the unit object. Agreement on geometric fibres does
not by itself give equality of morphisms (the Kummer class of $t$ on
$\mathbf G_{m,\bar k}$ is a nonzero map $A_X\to A_X[1]$ that vanishes on
every stalk), so the comparison is made through the unit object. By the
tensor formula, $\gamma_{f,K}$ is $\gamma_{f,A_Y}$ tensored with
$Lf^*K$ ([def-pur-smooth-purity-map], [pur9-cs-def-phi]), and the
reduction compatibilities of Step 2 are compatible with this tensor
decomposition. It therefore suffices to compare the two composites of the
square for $K=A_Y$, using the independently established unit-object
computation [thm-pur-diagonal-dualizing-object]. There both composites are
maps $A_X(d)[2d]\to Rf^!A_{E,m}$, that is, degree-zero sections of the
locally constant rank-one sheaf $\mathcal H^{-2d}(Rf^!A_{E,m})(-d)$. Such
sections are determined by their stalks, and on stalks the two composites
agree by the fibrewise description of the purity map: the affine-space case
[cor-pur-affine-space-zero-section-purity] together with the rank-one
computation [thm-pur-affine-line-orientation], whose reductions are
treated below. The identity then extends to every $K$ by the tensor formula.
Step 2: the reduction compatibilities of the operations. All these
constructions are built from the operations of the six-operations
package, whose finite-reduction compatibilities

$$
(Lf^*K)_m\cong Lf_m^*K_m,\qquad
(Rf^!K)_m\cong Rf_m^!K_m,\qquad
(K(d))_m\cong K_m(d)
$$

are natural in $K$ and in the morphism, by
[def-weil-derived-tensor] and
[def-weil-derived-pullback-tensor-hom] (finite reduction is the derived tensor product along
$A_{E,n}\to A_{E,m}$; this ring map need not be flat, and the
finite-Tor condition is essential for boundedness). The reduction
functor does land in $D^b_{ctf}(T,A_{E,m})$ with the same Tor interval:
if $K$ has Tor amplitude in $[a,b]$ it has a bounded flat model in
degrees $[a,b]$ by [lem-sf-flat-model], and the reduction of that model
is a bounded flat model of $K_m$ in $[a,b]$ by
[lem-sf-reduction-flat-model]. Compatibility
with pullback and the invertible twist follows from associativity
of derived tensor. For the smooth exceptional inverse image use
the previously constructed tensor formula and its coefficient
compatibility, rather than flat base change. The composition
identifications are those of
[def-weil-exceptional-inverse-image] (the functoriality of
$R^!$ and of the composition isomorphisms), and by
[def-coefficient-twists-detailed] (the coefficient twists are reduced
coefficient twists). Step 3: the glueing data reduce. The sheaf
axiom gluing used in [thm-pur-dnc-invariance] is a statement
about finite locally constant rank-one sheaves, and the reduction of a
finite locally constant rank-one sheaf is again one; the local
normalizations of [thm-pur-dnc-invariance] are the reductions of
the normalizations, the lisse-uniqueness of
[lem-pur-lisse-uniqueness] reduces, and the splitting-principle
descent of one element of an abelian group used in
[thm-pur-diagonal-dualizing-object] reduces for the same reason
(the Künneth and supported-cohomology groups of
[lem-pur-kunneth-supported] are compatible with the coefficient
reduction, the boundary of the Kummer class reducing to the boundary
of the reduced Kummer class). Hence the vertical isomorphisms of the
square identify $\operatorname{red}_{n,m}(\gamma_{f,K})$ with
$\gamma_{f,\operatorname{red}_{n,m}K}$, which is the commutativity
of the displayed square. Step 4: the remaining statements. The
affine orientations of [thm-pur-affine-line-orientation] are
constructed from the Kummer boundary, whose reduction is the boundary
of the reduced Kummer class, i.e. the reduction of the orientation;
the smooth trace of [def-pur-smooth-trace] reduces because the
counit of the adjunction reduces (the adjunction itself is compatible
with the finite reduction of the coefficient ring); the composition
and base-change coherence statements are the compatible systems
obtained from Steps 1–3 applied to the constituents of the two
squares.
