+++
id = "sheaves-on-the-small-etale-site"
kind = "section"
title = "Sheaves on the small étale site"
order = 131
+++
A sheaf in the detailed chapters is a sheaf on the *small* étale site of
a scheme $X$, with values in a coefficient category $A$. In Lean this is
`Sheaf X.smallEtaleTopology A`; the small étale topology is mathlib's
`AlgebraicGeometry.Scheme.smallEtaleTopology`, and its objects are the
schemes étale over $X$. Sheaves are formed on this site and on no other:
the pro-étale site and the fpqc site do not occur in the Lean development at
all. Where an étale cover of $X$ is needed — to say that a sheaf is
locally constant, for instance — it is taken to be a cover in the big
étale precoverage `AlgebraicGeometry.Scheme.etalePrecoverage`, that
is, a jointly surjective family of étale maps $U_i\to X$; this names the
covering families, and no sheaf is ever formed on the big site.

The coefficient category $A$ is not a fixed category in Lean but a parameter,
required to be Grothendieck abelian and, following the convention of the
`SixFunctors` folder, to have $\operatorname{Hom}$-types in the universe
$u+1$, one above the universe $u$ of the base schemes. Predicates involving
finiteness require $A$ to be moreover concrete, finiteness referring to the
underlying type. This convention is stated in the module docstrings of

- `WeilConjectures/SixFunctors/UpperLowerStar/Etale.lean`, which
constructs the pushforward $g_*$ and the pullback $g^*$ between
categories of sheaves on small étale sites, together with the
adjunction $g^*\dashv g_*$, the composition isomorphisms and the
exactness statements; and
- `WeilConjectures/ConstructibleSheaf/Defs.lean`, which defines
the locally constant, finite, finite locally constant and
constructible sheaves on the small étale site.

Both files record that the Grothendieck abelian generality is what supplies
sheafification and the left Kan extensions along base change used to define
$g^*$, and that some of those existence statements are, with current mathlib,
sorried instances rather than proved ones — the small étale site is not
known to be essentially small, only the small affine étale site is. This is
a limitation of the ambient library, not a mathematical hypothesis of the
theory.
