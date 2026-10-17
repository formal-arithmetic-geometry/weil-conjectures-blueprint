+++
kind  = "proof"
of    = "cor-coef-verdier-weil-equivariance"
+++
The underlying operations preserve $\Dbc(X,\Lambda)$ and biduality holds
there for every admissible $\Lambda$ ([sk-thm-sf-ctf-stability],
[sk-thm-existence], [sk-thm-pd-verdier-duality]). Consequently the equivariance construction of
[lem-fix-weil-operations] applies, including to the
dualizing object supplied by the exceptional adjoint. Write
$g$ for geometric Frobenius and
$\theta_K:g^*K\xrightarrow{\sim}K$ for a Weil structure as in
[def-weil-weil-sheaf-complex]. The dual Weil structure is
the composite

$$
g^*\mathbb DK\xrightarrow{\sim}\mathbb D(g^*K)
\xrightarrow{\mathbb D(\theta_K^{-1})}\mathbb DK.
$$

The first map is the internal-Hom comparison for the equivalence
$g^*$ of $D(X_{\mathrm{pro\acute et}},\Lambda)$, using the dualizing Weil
structure. Naturality of evaluation proves its equivariance, and
transposition gives the same conclusion for $\delta$. All of this takes
place in $D(X_{\mathrm{pro\acute et}},\Lambda)$ with $\theta_K$ itself; no
integral lattice and no finite coefficient field is needed. (If one wishes
to work over a finite field of coefficients when $\Lambda=\Qlb$,
[sk-thm-sfb-qlbar-two-colimit] descends $K$, $\theta_K$ and its inverse to
one finite $E'$, as a consequence.)

The comparisons of [lem-coef-integral-finite-extension] and
[sk-prop-scalar-six] for extension of scalars are built from scalar tensor,
the dualizing counit, and evaluation, and $g^*$ commutes with extension of
scalars, so they commute with the displayed dual Weil structures. The same
units and counits as in [lem-fix-weil-operations] give the
exceptional-adjunction assertion.
