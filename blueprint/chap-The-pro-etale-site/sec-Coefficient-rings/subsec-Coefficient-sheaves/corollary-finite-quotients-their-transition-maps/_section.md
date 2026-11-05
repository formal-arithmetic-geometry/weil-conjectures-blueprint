+++
id = "corollary-finite-quotients-their-transition-maps"
kind = "corollary"
title = "Finite quotients and their transition maps"
order = 181
lean = ["AlgebraicGeometry.ProEtale.PrincipalNormalization.principal_cone_tensor_normalization"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local"]
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
