+++
kind  = "proof"
of    = "thm-pur-composition-coherence"
+++
Step 1: the dualizing-object version. By
[thm-pur-cohomological-smoothness] (the tensor
formula for the smooth morphisms $f,g,gf$) and the composition rule
of [def-weil-exceptional-inverse-image], the identity

$$
\omega_{gf}\cong\omega_f\otimes^L_{\Lambda_X}Lf^*\omega_g
$$

holds; and the identification of
[thm-pur-diagonal-dualizing-object] applied to $gf$, to $g$
and to $f$ is compatible with this identity. Indeed, both
identifications are built from the DNC invariance of the section
invariant ([thm-pur-dnc-invariance]) and the vector-bundle purity
of the relative tangent bundle ([cor-pur-vector-bundle-purity]);
the diagonal of $gf$ is the transverse composite of the diagonals of
$g$ and of $f$ through the canonical Cartesian product
identifications of the twofold fibred products, and the canonical exact
sequence of the relative tangent bundles

$$
0\longrightarrow T_{X/Y}\longrightarrow T_{X/Z}\longrightarrow
f^*T_{Y/Z}\longrightarrow0
$$

splits in the standard coordinates of the etale local normal forms
([sbc-thm-etale-local-normal-form]); the direct-sum compatibility
of [cor-pur-vector-bundle-purity] and, above all, the uniqueness
clause of [thm-pur-dnc-invariance] – one and the same
identification is forced by being the identity on the standard pairs
and compatible with etale localization and base change, and the two
assemblies have exactly these properties – make the two assemblies
agree after the canonical reassociation (the coherence of the package's
composition isomorphisms and the pentagon for the twofold diagonal).
The remaining constituents of [thm-pur-diagonal-dualizing-object]
– the smooth base change ([lem-pur-diagonal-base-change]) and the
co-projection – are compatible with composition by the definition of
the canonical maps (the base-change squares of the composite and the
associativity of the derived tensor product).
Step 2: the $K$-form. The identity of Step 1 transposes to the
statement: the tensor formula is compatible with composition by its
definition (the mate of the projection formula), the twist
isomorphisms [def-coefficient-twists-detailed] are compatible with the
pullback-composition, and composing gives the composite of the
statement, the identifications being those displayed.
