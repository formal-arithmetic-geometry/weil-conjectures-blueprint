+++
kind  = "proof"
of    = "prop-trf-compact-support-perfectness"
+++
Let $C=R\Gamma_c(X,K)$, with compact support as in
[def-compact-support-direct-image-detailed], [def-trf-coefficient-conventions].
The finite-level constructibility theorem
[prop-finite-compact-support-constructibility] gives a bounded
complex on $\operatorname{Spec}k$ with finite cohomology modules,
using the point identification of
[def-weil-finite-coefficient-point]. This assertion alone does
not give perfectness over the finite local ring $A$.

Put $\kappa=A/(\pi_E)$. The narrow coefficient-change result
[lem-fix-compact-support-coefficient-change], applied to
$A_{E,n}\to A_{E,1}=\kappa$, identifies

$$
C\otimes_A^L\kappa
\xrightarrow{\sim}R\Gamma_c(X,K\otimes_A^L\kappa).
$$

The input on the right is bounded constructible: finite Tor amplitude
gives boundedness, and its cohomology is constructible by restricting
to a finite constructible stratification and taking the derived
tensor of the finite coefficient modules, as in
[def-weil-finite-tor-amplitude], [def-weil-finite-torsion-constructibility].
Hence the right side is bounded by
[prop-finite-compact-support-constructibility] at the residue
admissible coefficient ring. The residue-field criterion of
[lem-exc-residue-tor-test], applied on the point, now proves
that $C$ has finite Tor amplitude. Together with its finite
cohomology, [lem-trf-finite-tor-amplitude-perfect] shows that
$C$ is represented by a bounded complex of finite free
$A$-modules.

For $K_{\bar x}$, the exact inverse-image property
[prop-weil-pbc-inverse-image-exact] and the finite-stalk
condition of [def-weil-finite-torsion-constructibility] give
bounded finite cohomology. The tensor-vanishing definition
[def-weil-finite-tor-amplitude] is preserved by this inverse
image, so the same module-theoretic perfectness criterion applies.
Thus both objects lie in the perfect category used for categorical
trace in [def-trf-categorical-trace].
No preservation of finite Tor amplitude by a package summary is used
in this argument.

*Recorded in advance* from chapter *The trace formula* of the source.
