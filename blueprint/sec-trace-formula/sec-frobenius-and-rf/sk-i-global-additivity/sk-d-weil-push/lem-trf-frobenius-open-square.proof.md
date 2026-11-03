+++
kind  = "proof"
of    = "lem-trf-frobenius-open-square"
+++
The absolute $q^m$-power map on a characteristic-$p$ ring sends
each prime ideal to itself. Hence the scheme Frobenius of $Y_0$
has inverse image $X_0$ on the underlying open subset, and its
restriction is the Frobenius of $X_0$. For open immersions,
pullback is exactly the inverse-image open with the restricted
structure sheaf ([def-weil-scheme-morphism-properties]).
Thus the open square over $k_0$ is Cartesian. Base changing gives
the scheme-Frobenius square in the statement, with the definitions
of [def-trf-scheme-frobenius].

The maps $g_Y^m=\operatorname{id}_{Y_0}\times\Spec(\gamma^m)$
preserve $X_0\times_{k_0}k$; their restrictions there are $g_X^m$.
They are isomorphisms, so the same inverse-image description of
opens gives the second Cartesian square. Finally, the structure
map of the geometric fiber of [def-weil-finite-field-fiber]
is the second projection. Composing it with the displayed product
automorphism gives $\Spec(\gamma^m)a_Y$, and the same computation
applies to $X$. This proves the two asserted equalities.
