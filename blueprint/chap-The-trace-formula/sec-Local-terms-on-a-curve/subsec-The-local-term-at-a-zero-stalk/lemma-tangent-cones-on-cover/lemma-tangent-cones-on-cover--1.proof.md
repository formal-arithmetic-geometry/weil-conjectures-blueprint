+++
kind = "proof"
of = "lemma-tangent-cones-on-cover--1"
order = 984003
uses = ["lemma-covers-degree-prime-to-ell"]
+++
The product $C\times_k C$ is smooth of dimension two. Regularity and
dimension are preserved by strict henselization, so $R'$ is a regular
local ring of dimension two. To prove finiteness of $\pi$, factor
$p\times p$ through the finite map $C\times_k C\to U\times_k U$, where
$U$ is a neighbourhood of $y$ over which $p$ is finite. Strict localization
along this finite map selects an open and closed part of its finite base
change; the open immersion $U\times_k U\to X\times_k X$ induces an
isomorphism on the strict localizations.

Choose parameters $\xi,\eta$ of $R'$ from the two curve factors. A point
over $H$ has second coordinate over $y$ specializing to $c$. The fibre of
$p$ is discrete, so this coordinate is $c$, equivalently $\eta=0$.
Consequently the ideal of $H'_{\mathrm{red}}$ is $(\eta)$. The quotient
$R'/(\eta)$ is regular local of dimension one, hence a discrete valuation
ring.

Let $C_c$ and $X_y$ be the strict localizations at $c$ and $y$, and let
$\rho:C_c\to X_y$ be induced by $p$. Its finite fibre over $y$ has one
point. The product over $T$ of the two pullbacks of $\rho$ is therefore
strictly local, and the universal property of strict localization
identifies it with $T'$. Since $\rho$ is étale off $y$, this proves
étaleness of $\pi$ away from the axes. The uniformizer identity
$p^\#u=w\xi^e$, with $w$ a unit, gives rank $e$ for the finite extension
of discrete valuation rings. Thus each geometric fibre of $\rho$ off $y$
has $e$ points, and the corresponding fibre of $\pi$ has $e^2$ points.
Over $\Delta-y$ the finite étale pullback is reduced and identifies with
$\Delta'_{\mathrm{red}}-D'$. This gives the asserted map and its
compatibility with the inclusions.
