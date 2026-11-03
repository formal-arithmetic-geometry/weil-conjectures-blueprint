+++
kind  = "proof"
of    = "lem-kun-bc-kunneth-compat"
+++
By [def-kun-unbounded-exchange] the base change map is adjoint to
the counit composite
$p^{-1}j^{-1}Rj_*F\to p^{-1}F$ under
$h^{-1}\dashv Rh_*$ (using the cartesian identification
$h^{-1}q^{-1}\cong p^{-1}j^{-1}$). By [lem-kun-tensor-unit] we
have $q^{-1}Rj_*F\cong \pr_1^{-1}\underline{\kunZn}\kunotimes{\kunZn}\pr_2^{-1}Rj_*F$, and
applying $\RGamma$ to the base change map gives, through the
Kunneth maps of [def-kun-kunneth-map] (which are isomorphisms here by [lem-kun-0f14b]), the map

$$
\RGamma(Y_{\Et},\underline{\kunZn})\kunotimes{\kunZn}
\RGamma(X_{\Et},Rj_*F)
\longrightarrow
\RGamma(Y_{\Et},\underline{\kunZn})\kunotimes{\kunZn}
\RGamma(U_{\Et},F)
$$

induced by the counit $j^{-1}Rj_*F\to F$. Since
$\RGamma(X_{\Et},Rj_*F)=\RGamma(U_{\Et},F)$ through the Leray
identification of [lem-kun-leray-bdd] (the direct image
$j_*$ is the identity on $U$-sections, see
[lem-kun-open-immersion-restriction]; on the derived level the
induced map is the Leray identification by functoriality of the
adjunction and of [lem-kun-leray-bdd]), this induced map is the
identity, as asserted.
