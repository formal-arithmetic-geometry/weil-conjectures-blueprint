+++
kind  = "proof"
of    = "lem-coef-finite-dualizing"
+++
The object $\omega_{X,A}$ is finite-Tor constructible by
[lem-weil-verdier-preservation-strata], applied to $A_X$.
Thus compact-support coefficient comparison
[lem-fix-compact-support-coefficient-change] constructs the
displayed adjoint map without any coefficient compatibility
assumption on an exceptional right adjoint.

By [lem-amb-etale-adjoint-locality], the assertion is local
on $X$. Choose an affine open and a closed embedding
$i:X\hookrightarrow\mathbf A^r_k$. Composition of ambient
right adjoints and [cor-amb-affine-space-adjunction] give

$$
\omega_{X,A}=Ri_A^!A(r)[2r],\qquad
\omega_{X,B}=Ri_B^!B(r)[2r].
$$

The Tate rank-one object at $A$ reduces to the one at $B$,
and shifts commute with coefficient tensor. Applying
[lem-coef-finite-closed-shriek] therefore proves the displayed
map is an isomorphism. The local map is the global map defined
above: transposing it under the composite adjunction yields the
closed-immersion counit followed by the affine-space counit,
which is the structure-morphism counit. In particular these
maps agree on overlaps. The same adjoint calculation proves
the quotient cocycle and compatibility with the counit.
The dualizing-object comparison of
[lem-weil-finite-duality-site-comparison] transports this
canonical map to the finite pro-etale realization.
