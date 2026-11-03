+++
id = "prop-sf-pf-coherence"
kind = "theorem"
title = "Coherence of the projection formula"
order = 3466
tags = ["latex:proposition"]
uses = ["def-sf-datum", "def-sf-pf", "fix-prop-adjunctions", "prop-sf-pf-reduction", "thm-sf-comp-composition"]
+++
In the setting of [def-sf-datum], the projection transformations
satisfy: naturality in $K$, $L$ and $f$; the identity
for $f=\operatorname{id}$; the associativity pentagon for composable
$f,g$, compatible with the composition law (A4), i.e. the isomorphism
$\alpha_{g,f}:Rg_!Rf_!\cong R(gf)_!$ of [thm-sf-comp-composition]; independence of the chosen
compactification; the identification with the direct-image projection
formula through $Rf_!\cong Rf_*$ for proper $f$; compatibility with base
change, i.e. for a Cartesian square $(f',g',f,g)$ the square

$$
\begin{array}{ccc}
Lg^*\bigl(Rf_!K\otimes^L_\Lambda L\bigr)&\xrightarrow{\ Lg^*\operatorname{PF}_{f,K,L}\ }&
Lg^*Rf_!\bigl(K\otimes^L_\Lambda Lf^*L\bigr)\\
{\scriptstyle \operatorname{Ex}_!\otimes1}\downarrow&&\downarrow{\scriptstyle \operatorname{Ex}_!}\\
Rf'_!Lg'^*K\otimes^L_\Lambda Lg^*L&\xrightarrow{\ \operatorname{PF}_{f',Lg'^*K,Lg^*L}\ }&
Rf'_!\bigl(Lg'^*K\otimes^L_\Lambda Lf'^*Lg^*L\bigr)
\end{array}
$$

commutes, with $\operatorname{Ex}_!$ the exchange of axiom (A2) and the
vertical arrows read through the monoidality isomorphisms
$Lg^*(M\otimes^LN)\cong Lg^*M\otimes^LLg^*N$ and $Lg'^*Lf^*\cong Lf'^*Lg^*$
(the projection formula commutes with base change; SGA 4, XVII, §5.2); and
compatibility with finite reduction: for every ideal $J\subseteq\Lambda$ the
square of [prop-sf-pf-reduction] comparing the reduction modulo $J$ of
$\operatorname{PF}_{f,K,L}$ with $\operatorname{PF}_{f,K,\rho_YL}$ commutes.
