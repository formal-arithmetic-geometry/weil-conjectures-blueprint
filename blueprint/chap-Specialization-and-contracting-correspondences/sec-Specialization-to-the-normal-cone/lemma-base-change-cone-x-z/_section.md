+++
id = "lemma-base-change-cone-x-z"
kind = "lemma"
title = "Base change for the cone of $\\tau_{X,Z}$"
order = 1633
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.nonempty_specializationDefect_lowerStar_iso", "AlgebraicGeometry.ProEtale.CondensedRing.nonempty_specializationDefect_upperStar_iso", "AlgebraicGeometry.ProEtale.CondensedRing.isZero_specializationDefect_lowerStar_centreι", "AlgebraicGeometry.ProEtale.CondensedRing.nonempty_specializationDefect_lowerShriek_upperStar_iso"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "lemma-inverse-image-coefficient-sheaves", "definition-constructible-sheaves", "definition-lisse-sheaves", "definition-deformation-normal-bundle", "proposition-sp-unique-adjoint", "lemma-functoriality-deformation"]
+++
Let $f:X'\to X$ be a morphism of separated $k$-schemes of finite type,
let $Z'=f^{-1}Z$ schematically, and let $f_Z:Z'\to Z$ be the
restriction of $f$.  There are isomorphisms

$$
\begin{aligned}
C_{X,Z}(Rf_*L')&\simeq Rf_{Z*}C_{X',Z'}(L')
&&(f\text{ proper}),\\
C_{X',Z'}(f^*L)&\simeq f_Z^*C_{X,Z}(L)
&&(f\text{ smooth}).
\end{aligned}
$$

Moreover, $C_{X,Z}(i_*M)=0$ for every $M\in D^b_c(Z_{\acute et},A)$.
Consequently, writing $j:X\setminus Z\hookrightarrow X$, we have

$$
C_{X,Z}(j_!j^*L)\xrightarrow{\sim}C_{X,Z}(L).
$$
