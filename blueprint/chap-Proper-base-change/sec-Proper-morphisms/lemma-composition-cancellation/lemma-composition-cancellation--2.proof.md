+++
kind = "proof"
of = "lemma-composition-cancellation--2"
order = 389005
uses = ["definition-torsion-pbc-property", "definition-torsion-sheaves", "definition-injective-acyclicity", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "lemma-acyclic-resolutions"]
+++
Fix a base change $g:Z'\to Z$, and write $g_Y:Y'\to Y$,
$g_X:X'\to X$, $u':X'\to Y'$ and $v':Y'\to Z'$ for the maps in the
two resulting cartesian squares. Every sheaf of $\Lambda$-modules is
torsion. Applying $\mathrm{PBC}_\Lambda(u)$ to an injective sheaf $J$
placed in degree zero gives $\mathrm{IA}_\Lambda(u)$: the source of
the derived base change map is concentrated in degree zero, so the
target has no positive cohomology. The same argument gives
$\mathrm{IA}_\Lambda(vu)$.

We also recover the underived exchange at $J$:

$$
g_Y^*u_*J\simeq u'_*g_X^*J.
$$

Indeed, the derived base change map at $J[0]$ factors through the
underived exchange and the comparison to the derived direct image.
Both comparison maps are isomorphisms by injectivity of $J$ and
$u'_*$-acyclicity of $g_X^*J$, using [lemma-acyclic-resolutions]. Taking
degree-zero cohomology gives the displayed isomorphism. This applies
to $vu$ as well.

Let $I$ be an injective sheaf on $Y$, and choose a monomorphism
$u^*I\hookrightarrow J$ with $J$ injective on $X$. Surjectivity of $u$
makes $u^*$ faithful, as can be checked on geometric stalks, so the
adjunction unit $I\to u_*u^*I$ is a monomorphism. Since $u_*$ preserves
monomorphisms, the adjoint $I\to u_*J$ is a monomorphism and splits by
injectivity of $I$.

Direct image preserves injectives, since inverse image is exact, so
the derived direct images compose. Placing the sheaves in degree zero,
the underived exchange at $J$,
acyclicity of $g_X^*J$, and composition of derived direct images give

$$
Rv'_*(g_Y^*u_*J)
\simeq Rv'_*(u'_*g_X^*J)
\simeq Rv'_*Ru'_*(g_X^*J)
\simeq R(v'u')_*(g_X^*J).
$$

The last object has no positive cohomology by
$\mathrm{IA}_\Lambda(vu)$. Pulling back the splitting makes $g_Y^*I$
a direct summand of $g_Y^*u_*J$, and taking higher direct images
preserves this splitting. Hence $\mathrm{IA}_\Lambda(v)$ holds.

It remains to prove the underived exchange for $v$. At a sheaf $u_*J$
with $J$ injective, vertical pasting of the underived base change maps
expresses the exchange for $vu$ as the exchange for $v$ followed by
$v'_*$ applied to the exchange for $u$, under the composition
isomorphisms. The latter and the exchange for $vu$ are isomorphisms by
the preceding argument, so the exchange for $v$ at $u_*J$ is an
isomorphism. For a general sheaf $G$ on $Y$, embed $u^*G$ into an
injective $J_1$. Its adjoint is a monomorphism $G\hookrightarrow u_*J_1$.
Repeat with its cokernel to obtain an exact sequence

$$
0\longrightarrow G\longrightarrow u_*J_1\longrightarrow u_*J_2
$$

with $J_2$ injective. The functors $g^*v_*$ and $v'_*g_Y^*$ are left
exact, so the exchange isomorphisms at $u_*J_1$ and $u_*J_2$ give the
exchange isomorphism at their kernel $G$.

Finally, represent any bounded below complex on $Y$ by a bounded below
complex $I^\bullet$ of injectives. The underived exchange is an
isomorphism in every degree, and $g_Y^*I^\bullet$ consists of
$v'_*$-acyclic sheaves by $\mathrm{IA}_\Lambda(v)$. By
[lemma-acyclic-resolutions], its underived direct image computes its
derived direct image. The factorization of the derived base change
map through these comparisons therefore proves
$\mathrm{PBC}_\Lambda(v)$.
