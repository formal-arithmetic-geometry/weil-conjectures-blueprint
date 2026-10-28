+++
id = "sk-prop-sf-pf-coherence"
kind = "proposition"
title = "Coherence of the projection formula"
order = 3463
uses = ["sk-lem-sf-mate", "sk-prop-sf-comp-proper", "sk-thm-sf-pf-adic", "sk-thm-sf-pf-field", "sk-thm-sf-pf-proetale", "sk-thm-sbc-coefficients"]
lean = ["AlgebraicGeometry.Etale.hasProjectionFormula_id", "AlgebraicGeometry.Etale.nonempty_iso_rightDerivedLowerShriek_comp", "AlgebraicGeometry.Etale.hasProjectionFormula_comp", "AlgebraicGeometry.Etale.hasProjectionFormulaOfCompactification_iff"]
tags = ["sketch"]
+++
The projection transformations are natural in $K$, $L$, $f$ and the
coefficient ring; the transformation for $f=\mathrm{id}$ is the identity; the
associativity pentagon for composable $f,g$ commutes and is compatible with
the composition law of def:compact-support-direct-image; the
transformation is independent of the chosen compactification; for proper $f$
it agrees with the direct-image projection formula through $Rf_!\cong Rf_*$;
it is *compatible with base change*: for a Cartesian square
$(f',g',f,g)$ as in [det-def-sf-exchanges], $K\in\Dbc(X,\Lambda)$ and
$L\in\Dctf(Y,\Lambda)$ (pullback preserves both classes) the square

$$
\begin{array}{ccc}
Lg^*\bigl(Rf_!K\otimes^L_\Lambda L\bigr)&\xrightarrow{\ Lg^*\operatorname{PF}_{f,K,L}\ }&
Lg^*Rf_!\bigl(K\otimes^L_\Lambda Lf^*L\bigr)\\
{\scriptstyle \operatorname{Ex}_!\otimes1}\downarrow&&\downarrow{\scriptstyle \operatorname{Ex}_!}\\
Rf'_!Lg'^*K\otimes^L_\Lambda Lg^*L&\xrightarrow{\ \operatorname{PF}_{f',Lg'^*K,Lg^*L}\ }&
Rf'_!\bigl(Lg'^*K\otimes^L_\Lambda Lf'^*Lg^*L\bigr)
\end{array}
$$

commutes, the vertical arrows being read through the monoidality
isomorphisms $Lg^*(M\otimes^LN)\cong Lg^*M\otimes^LLg^*N$ and
$Lg'^*Lf^*\cong Lf'^*Lg^*$ (the projection formula commutes with base
change; SGA 4, XVII, §5.2);
and it is compatible with finite reduction, scalar extension and the
pro-étale realization. Every one of these assertions is an identity between
natural transformations of the functors typed in [det-def-sf-operations] and
[det-def-sf-exchanges], at the categories written there.
