+++
kind  = "proof"
of    = "det-thm-sfb-proper-base-change-finite"
+++
*Transport.* Objects of $\Dctf(X,A)$ are bounded with constructible cohomology, hence classical:
they are pulled back from $D^b(X_{\mathrm{ét}},A)$ along $\nu^*$, fully faithfully, and $R\nu_*$,
$\nu^*$ commute with direct images, inverse images and tensor products on bounded below
classical complexes ([sk-thm-pe-constructible-comparison]). So (1)–(3) may be checked on the
étale sites, for the étale counterparts of $K$ and $M$.

(1) is [sk-prop-ctf-finite-proper]. Proper direct image of a constructible complex is
constructible (\stacks{0GL0}) and bounded, since $p$ has finite cohomological dimension $c$
(\stacks{0F10}). For the Tor bound: for classical complexes Tor amplitude can be tested
stalkwise, i.e. against constant sheaves $N_Y$ of $A$-modules $N$. The constant-module
projection formula $Rp_*K\otimes^{\mathbf L}_AN_Y\cong Rp_*(K\otimes^{\mathbf L}_AN_X)$ (resolve $N$
by free $A$-modules; $Rp_*$ commutes with the resulting direct sums on bounded below torsion
complexes) shows: if $K$ has Tor amplitude in $[a,b]$, then $K\otimes^{\mathbf L}_AN_X$ has
cohomology in $[a,b]$, so $Rp_*K\otimes^{\mathbf L}_AN_Y$ has cohomology in $[a,b+c]$; hence
$Rp_*K$ has Tor amplitude in $[a,b+c]$.

(2) The exchange map for bounded below torsion complexes on the étale site is an isomorphism by
the proper base change theorem [sk-thm-properbasechange]; [sk-cor-pbc-proet-finite] transports
it to the pro-étale sites.

(3) For bounded below $K$ and $M$ of finite Tor amplitude with torsion coefficients, the
projection formula map on the étale site is an isomorphism (\stacks{0F0G}); pulling back by
$\nu^*$, which is exact and monoidal and commutes with $Rp_*$ on these classical complexes,
gives the pro-étale statement.
