+++
id = "corollary-finite-quotients-their-transition-maps"
kind = "corollary"
title = "Finite quotients and their transition maps"
order = 181
lean = ["AlgebraicGeometry.ProEtale.DerivedNakayama.derived_nakayama_resolution", "AlgebraicGeometry.ProEtale.PrincipalNormalization.principal_cone_tensor_normalization"]
uses = ["definition-small-pro-etale-site", "prose-02-50", "prose-02-51", "proposition-topos-functoriality"]
+++
For every $n\geq1$ there is a canonical exact sequence on $X_{\mathrm{pro}\acute{e}t}$

$$
0\longrightarrow\mathcal O_{E,X}
\xrightarrow{\pi_E^n}\mathcal O_{E,X}
\longrightarrow(\mathcal O_E/\pi_E^n)_X\longrightarrow0.
$$

Thus the quotient is represented by the two-term complex
$[\mathcal O_{E,X}\xrightarrow{\pi_E^n}\mathcal O_{E,X}]$ in degrees
$-1,0$. Under this representation, reduction from level $n+1$ to level
$n$ is the chain map $(\pi_E,\mathrm{id})$. These resolutions and maps
commute with inverse image along every morphism of schemes.
