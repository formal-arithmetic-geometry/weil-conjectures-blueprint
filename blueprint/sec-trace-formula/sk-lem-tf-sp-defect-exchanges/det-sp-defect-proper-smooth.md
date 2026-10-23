+++
id = "det-sp-defect-proper-smooth"
kind = "lemma"
title = "Proper and smooth exchange for the defect"
order = 3576
uses = ["det-sp-defect-definition"]
+++
Let $f\colon X'\to X$ be a morphism of separated finite-type $k$-schemes, let $Z\subset X$ be a
closed subscheme, let $Z'=f^{-1}Z$ schematically, and let $f_Z\colon Z'\to Z$ be the restriction
of $f$. With the defect $C$ of [det-sp-defect-definition], there are natural isomorphisms

$$
\begin{aligned}
C_{X,Z}(Rf_*L')&\simeq Rf_{Z*}C_{X',Z'}(L') &&(f\text{ proper},\ L'\in D^b_c(X'_{\mathrm{\acute et}},A)),\\
C_{X',Z'}(f^*L)&\simeq f_Z^*C_{X,Z}(L) &&(f\text{ smooth},\ L\in D^b_c(X_{\mathrm{\acute et}},A)).
\end{aligned}
$$
