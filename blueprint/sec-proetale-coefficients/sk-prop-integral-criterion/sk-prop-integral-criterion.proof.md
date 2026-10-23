+++
kind  = "proof"
of    = "sk-prop-integral-criterion"
uses = ["sk-def-sfb-constructible", "sk-def-pe-derived-completion", "sk-prop-sf-open-closed-triangle", "sk-lem-pe-derived-nakayama", "sk-prop-pe-milnor", "sk-prop-pe-replete", "sk-thm-pe-constructible-comparison", "sk-cor-pe-finite-tor-comparison"]
+++
We prove (1)$\Rightarrow$(2)$\Rightarrow$(3)$\Rightarrow$(1) and (3)$\Leftrightarrow$(4).

*(1) implies (2).* A finitely generated $\cO_E$-module is a finite sum of copies of $\cO_E$
and of modules $\cO_E/\pi_E^r$, so its sheaf has a two-term finite free resolution. The
coefficient sheaf $\cO_{E,U}$ is derived complete by its profinite description and the
surjectivity of the transition maps between its finite quotients. Completeness is preserved
by finite sums and cones, so the finite constant local models of [sk-def-sfb-constructible]
are complete, and their reductions are bounded locally constant finite complexes; this can be
checked on a pro-étale cover. For a constructible sheaf, choose a finite stratification as in
the definition and write a locally closed immersion as $a=i\circ u$ with $u$ a quasi-compact
open and $i$ a closed immersion. Then $a_!=i_*u_!$ is exact, commutes with the cones defining
the reductions and preserves limits ([sk-prop-sf-open-closed-triangle]), so extension by zero
preserves completeness. The finite filtration by open and closed pieces shows that the sheaf
is complete with constructible finite reductions, and (2) follows by applying this to the
finitely many cohomology sheaves of $K$ and the bounded Postnikov triangles.

*(2) implies (3).* First, the finite levels. The filtration of $\cO_E/\pi_E^n$ by the powers
of $\pi_E$ has graded pieces $\mathbf F_E$; tensoring its short exact sequences with $K$ gives
triangles showing that every $K_n$ lies in $\Dbc(X,\cO_E/\pi_E^n)$, with cohomology in an
interval $[a,b]$ containing that of $K_1$, and with locally constant cohomology on any stratum
on which the cohomology of $K_1$ is locally constant. These complexes are classical
([sk-thm-pe-constructible-comparison]). Minimal finite free resolutions of the stalks over the
Artinian local rings $\cO_E/\pi_E^n$ have rank $\dim_{\mathbf F_E}H^q(K_1)$ in degree $q$, so
each $K_n$ has Tor amplitude in $[a,b]$ ([sk-cor-pe-finite-tor-comparison]); and
$K=R\varprojlim_nK_n$ has cohomology in $[a,b]$ by the Milnor sequence
([sk-prop-pe-milnor]) and repleteness ([sk-prop-pe-replete]).

Next, the local models. Choose a finite stratification on which the cohomology sheaves of
$K_1$ are locally constant and refine it by connected components; restriction to a stratum
preserves completeness and the reductions ([sk-prop-sf-open-closed-triangle]). On a connected
stratum $S$ each $K_n|_S$ is locally isomorphic to a constant complex $(M_n)_S$, with $M_n$ a
minimal finite free complex over $\cO_E/\pi_E^n$, and the reduction maps induce
$M_{n+1}\otimes^{\mathbf L}\cO_E/\pi_E^n\simeq M_n$. Such a compatible system of perfect
complexes comes from one bounded complex $P^\bullet$ of finite free $\cO_E$-modules, by lifting
the minimal complexes and their transition isomorphisms level by level. On an affine weakly
contractible cover $W\to S$ the local isomorphisms $(P^\bullet/\pi_E^n)_W\simeq K_n|_W$ exist
for each $n$, but are chosen separately. The Hom groups between them form a tower whose images
stabilise at a uniform rate: if $\pi_E^e$ kills the torsion of $H^1$ of
$(P^\bullet)^\vee\otimes P^\bullet$, the images from levels $m$ and $N\ge m\ge k+e$ at level $k$
agree. This Mittag-Leffler property gives a compatible family of isomorphisms, which by the
Milnor sequence ([sk-prop-pe-milnor]) and completeness lifts to a morphism
$\cO_{E,W}\otimes_{\cO_E}P^\bullet\to K|_W$ whose first reduction is an isomorphism. Both sides
are complete, so it is an isomorphism by derived Nakayama ([sk-lem-pe-derived-nakayama]).

*(3) implies (1).* The strata are quasi-compact, so their local models are checked on finite
covers and have a common cohomological interval. The map from the constant sheaf $\cO_E$ to
$\cO_{E,S}$ is flat (\stacks{099L}; alternatively apply Smith normal form to each
differential), so the cohomology of a local model is
$\cO_{E,S}\otimes_{\cO_E}H^q(P^\bullet)$ with $H^q(P^\bullet)$ finitely generated. These are
finite constant local models ([sk-def-sfb-constructible]), which proves (1).

*(3) is equivalent to (4).* Bounded finite free local models have finite Tor amplitude. Since
the stratification is finite there is a common interval, and the restrictions to the strata
are exact and jointly conservative, so they detect the vanishing after tensoring with any sheaf
of modules; so (3) implies (4). Conversely, (4) implies (1) by definition of $\Dctf$
([sk-def-sfb-constructible]).
