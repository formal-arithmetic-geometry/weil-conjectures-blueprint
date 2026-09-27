+++
id = "sk-prop-sf-cbc"
kind = "section"
title = "Compact-support base change"
order = 1517
uses = ["sk-def-av-jacobian"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_upperStar_comp_rightDerivedLowerShriek"]
+++
*Proposition (sketch).*

For $f:X\to Y$ separated of finite type, $g:Y'\to Y$ arbitrary and a
Cartesian square, the exchange transformation
$\operatorname{Ex}_!:Lg^*Rf_!\to Rf'_!Lg'^*$ of [sk-def-sf-exchanges] is an
isomorphism at every coefficient stage — in the ambient category in which the
two sides live, and in $\Dbc(Y',\Lambda)$ whenever the two sides are bounded
constructible — natural in the coefficient complex and coherent for identity
and pasted squares.
Chapter 17 (compact-support base change): the five stages are
thm:cbc-finite-torsion (finite coefficients on the étale site),
cor:cbc-degreewise-constructible,
thm:cbc-finite-level-proetale (pro-étale, for objects with an
étale-origin witness), thm:cbc-complete-proetale (completed
coefficients), thm:cbc-finite-extension and thm:cbc-qbar.

Uses: `cor:cbc-degreewise-constructible`, `thm:cbc-complete-proetale`, `thm:cbc-finite-extension`, `thm:cbc-finite-level-proetale`, `thm:cbc-finite-torsion`, `thm:cbc-qbar`
