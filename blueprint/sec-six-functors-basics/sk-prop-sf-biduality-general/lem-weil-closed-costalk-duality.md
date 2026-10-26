+++
id = "lem-weil-closed-costalk-duality"
kind = "lemma"
title = "Exceptional restriction of a Verdier dual"
lean = ["AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_verdierDual"]
order = 2828
uses = ["def-weil-derived-pullback-tensor-hom", "def-weil-exceptional-inverse-image", "def-weil-open-closed-recollement"]
+++
Let $i:Z\hookrightarrow T$ be a closed immersion and suppose the
ambient exceptional adjoints are defined, with
$\omega_Z=Ri^!\omega_T$. Put
$D_T=R\mathcal Hom_T(-,\omega_T)$ and
$D_Z=R\mathcal Hom_Z(-,\omega_Z)$. Then there is a natural
isomorphism

$$
\alpha_K:Ri^!D_TK\xrightarrow{\sim}D_Zi^*K.
$$
