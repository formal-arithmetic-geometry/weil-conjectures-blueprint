+++
kind = "proof"
of = "lemma-composition-cancellation--1"
order = 389004
uses = ["definition-torsion-sheaves", "definition-torsion-pbc-property", "lemma-identity-pasting"]
+++
Since $\Lambda$ is torsion as an abelian group, every sheaf of
$\Lambda$-modules is torsion. Thus $\mathrm{PBC}_\Lambda(u)$ and
$\mathrm{PBC}_\Lambda(v)$ assert that their derived base change maps are
isomorphisms on every bounded below complex.

Fix a base change $g:Z'\to Z$. Form $Y'=Y\times_ZZ'$ and
$X'=X\times_YY'$, with projections $g_Y:Y'\to Y$, $g_X:X'\to X$ and
induced maps $u':X'\to Y'$, $v':Y'\to Z'$. Under the canonical
composition isomorphisms, the vertical pasting law of
[lemma-identity-pasting] identifies the base change map of $vu$ at $K$
with

$$
g^*Rv_*Ru_*K
\longrightarrow Rv'_*g_Y^*Ru_*K
\longrightarrow Rv'_*Ru'_*g_X^*K.
$$

The first arrow is an isomorphism by $\mathrm{PBC}_\Lambda(v)$ applied to
$Ru_*K$, and the second by $\mathrm{PBC}_\Lambda(u)$ and functoriality of
$Rv'_*$. Every cartesian square for $vu$ has this factorization, up to
the canonical pullback isomorphism. Hence the base change map for $vu$
is an isomorphism on every bounded below complex, giving
$\mathrm{PBC}_\Lambda(vu)$.
