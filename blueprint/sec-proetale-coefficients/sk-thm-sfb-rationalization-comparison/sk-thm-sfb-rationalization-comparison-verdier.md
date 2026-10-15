+++
id = "det-thm-sfb-rationalization-comparison-verdier"
kind = "proposition"
title = "Extension of scalars to $E$ is a Verdier localization"
uses = ["det-prop-sfb-qlbar-colimit-x-invert-ell", "sk-def-sfb-derived-extension-of-scalars", "sk-def-sfb-change-of-scalars"]
+++
Let $X$ be a scheme, $E/\mathbf Q_\ell$ finite, and let
$F=E_X\otimes_{\cO_{E,X}}-\colon D(X_{\mathrm{proét}},\cO_E)\to D(X_{\mathrm{proét}},E)$ be
extension of scalars and $G\colon D(X_{\mathrm{proét}},E)\to D(X_{\mathrm{proét}},\cO_E)$
restriction of scalars along $\varphi\colon\cO_{E,X}\to E_X$. Let
$\mathcal N\subseteq D(X_{\mathrm{proét}},\cO_E)$ be the full subcategory of complexes $K$
with $H^q(K)[1/\ell]=0$ for all $q$. Then:

1. $F$ is exact (needs no deriving), and $H^q(F(K))=E_X\otimes_{\cO_{E,X}}H^q(K)=H^q(K)[1/\ell]$;
   in particular $\ker F=\mathcal N$, a thick triangulated subcategory.
2. $F\dashv G$, and the counit $FG\to\mathrm{id}$ is an isomorphism; so $G$ is fully
   faithful.
3. The induced functor $\bar F\colon D(X_{\mathrm{proét}},\cO_E)/\mathcal N\to D(X_{\mathrm{proét}},E)$
   from the Verdier quotient is an equivalence of triangulated categories.
