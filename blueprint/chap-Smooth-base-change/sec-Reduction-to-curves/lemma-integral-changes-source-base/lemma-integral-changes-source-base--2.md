+++
id = "lemma-integral-changes-source-base--2"
kind = "lemma"
title = "Integral changes of source and base (2)"
name_showing = false
order = 678002
aliases = ["bp-r204-2"]
lean = ["AlgebraicGeometry.Etale.isIso_baseChangeHomologyMap_iff_of_isIntegralHom"]
uses = ["definition-derived-base-change-map"]
+++
Let $\Lambda$ be a commutative ring, let $g:T'\to T$ and $f_1:Z\to T_1$
be morphisms of schemes, and let $\pi:T_1\to T$ be integral. Put
$f=\pi\circ f_1$, $T'_1=T'\times_TT_1$, and
$Z'=T'_1\times_{T_1}Z\simeq T'\times_TZ$. Write $g_1:T'_1\to T_1$,
$\pi':T'_1\to T'$, $g_Z:Z'\to Z$, and $f'_1:Z'\to T'_1$ for the
projections, and put $f'=\pi'\circ f'_1$.

For every integer $q$ and every sheaf $M$ of $\Lambda$-modules on
$Z_{\acute{e}t}$, the base change maps

$$
b^q_{f,M}:g^{-1}R^qf_*M\longrightarrow R^qf'_*g_Z^{-1}M,
\qquad
b^q_{f_1,M}:g_1^{-1}R^qf_{1*}M\longrightarrow R^qf'_{1*}g_Z^{-1}M
$$

satisfy

$$
b^q_{f,M}\text{ is an isomorphism}
\quad\Longleftrightarrow\quad
b^q_{f_1,M}\text{ is an isomorphism}.
$$

Thus a failure persists in either direction. No lower-degree base change
hypothesis or qcqs hypothesis on $f_1$ is required.
