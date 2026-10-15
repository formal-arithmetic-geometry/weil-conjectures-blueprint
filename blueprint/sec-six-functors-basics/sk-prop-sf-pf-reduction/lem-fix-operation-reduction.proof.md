+++
kind  = "proof"
of    = "lem-fix-operation-reduction"
+++
Pullback and tensor are computed with K-flat resolutions in
[def-weil-derived-pullback-tensor-hom]; reassociation of the same
threefold tensor product proves their reduction comparisons and
the corresponding associativity identities. If the first argument
of internal Hom is site-perfect in [def-weil-site-perfect-complex],
choose a bounded finite-projective representative locally. Its
termwise Hom commutes with coefficient change. This identifies the
actual evaluation maps, since evaluation of a finite-projective
module is compatible with tensoring the coefficients.

The two-term free resolution
$[\mathcal O_E\xrightarrow{\varpi_E^n}\mathcal O_E]$
shows that $A_{E,n}$ is perfect over $\mathcal O_E$ ([lem-weil-pbc-standard-quotients-perfect]).
For internal Hom this gives, without a perfectness assumption on $K$,

$$
\begin{aligned}
R\mathcal Hom_{\mathcal O_E}(K,L)\otimes^L_{\mathcal O_E}A_{E,n}
&\cong R\mathcal Hom_{\mathcal O_E}
(K,L\otimes^L_{\mathcal O_E}A_{E,n})\\
&\cong R\mathcal Hom_{A_{E,n}}(K_n,L_n).
\end{aligned}
$$

The first map commutes Hom in its second variable with the finite
two-term cone. The second is extension–restriction of scalars
adjunction. Both are the maps adjoint to tensoring evaluation, so this
is the specified coefficient comparison, compatible with evaluation.
Consequently [lemma-weil-pbc-perfect-projection-formula] gives
$(Rf_*K)_n\simeq Rf_*K_n$; the compatibility with completed
realization is [prop-weil-pbc-direct-image-limits] and
[def-weil-derived-complete-integral-detailed]. Applying this to the
proper factor and using extension by zero gives the compact-support
comparison of [def-weil-integral-rational-qbar-compact-support].
Between finite levels use
[lem-fix-compact-support-coefficient-change]. The corresponding
comparison for an exceptional right adjoint is precisely the
coefficient compatibility in
[def-weil-exceptional-adjoint-admissibility]; it is invoked only
under that explicit hypothesis.

The constructions in [def-weil-rationalization-karoubi] and
[def-weil-algebraically-closed-coefficients], together with
[lem-weil-scalar-extension-exact-triangulated], transport these
maps to the field stages. Units and counits there are the transported
adjunction maps. Each asserted identity is an identity between
composites of the tensor associativity map, the evaluation or the
adjunction maps already described, so transporting those maps
transports the identity itself. This proves compatibility of the
specified maps, beyond the existence of comparison isomorphisms.
