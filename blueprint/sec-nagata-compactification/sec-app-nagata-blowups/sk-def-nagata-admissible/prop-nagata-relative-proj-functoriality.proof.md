+++
kind  = "proof"
of    = "prop-nagata-relative-proj-functoriality"
+++
For (1), use the restriction isomorphism in
[lemma-nagata-relative-proj-exists]; transitivity of coefficientwise
localization gives the iterated-restriction equality. For (2), on an affine
chart the graded equivalence carries each homogeneous denominator to a
homogeneous denominator and induces an isomorphism of the corresponding
degree-zero localizations, hence an isomorphism of standard affine opens.
These maps agree on overlaps by the localization cocycle and glue uniquely.
For (3), a surjection has surjective maps on every homogeneous localization;
the induced maps on degree-zero rings give closed immersions of all standard
affine opens, which glue to the asserted closed immersion. Finally, for
(4), put $A=\Gamma(X,\mathcal O_X)$ and $C=\mathcal A(X)$. The rings
$\Gamma(V',\mathcal O_{X'})\otimes_AC$ with the base-changed grading and the
induced restriction maps form a quasi-coherent graded algebra on $X'$,
because base change is transitive. On an affine open
$V'=\operatorname{Spec}(B)\subseteq X'$, the chart at a
homogeneous $f$ is identified on both sides using

$$
(C_{(f),0})\otimes_A B
\xrightarrow{\sim}(B\otimes_A C)_{(f\otimes1),0},
\qquad (x/f^m)\otimes b\longmapsto (x\otimes b)/(f\otimes1)^m .
$$

To justify this without a hidden cancellation argument, identify the
degree-zero homogeneous localization with the filtered colimit
$\varinjlim_m C_{md}$ whose transition map is multiplication by $f$.
Tensor product commutes with this filtered colimit, giving the displayed
isomorphism; no flatness is needed. On pure fractions its inverse
sends $(x\otimes b)/(f\otimes1)^m$ to $(x/f^m)\otimes b$. It is compatible
with further localization, so the chart isomorphisms glue, and their
structural maps identify the glued schemes over $X$. This proves all four
assertions.
