+++
id = "det-prop-diagonal-tower-system"
kind = "lemma"
title = "The torsion diagonal classes as one morphism of inverse systems"
lean = ["AlgebraicGeometry.ProEtale.exists_diagonalTowerSystem"]
order = 2749
uses = ["lem-amb-cartier-kummer-map", "sk-lem-geo-cartier"]
+++
Put $W=\mathbf P^1_Y\times_Y\mathbf P^1_Y$ and let
$\Delta:\mathbf P^1_Y\hookrightarrow W$ be the diagonal. Write
$D(W^{\mathbf N}_{\mathrm{proét}})$ for the derived category of inverse systems
$(K_n)_{n\geq1}$ of sheaves of $\underline{\mathbf Z_\ell}$-modules on
$W_{\mathrm{proét}}$. Then:

1. The pro-étale pullback of the Cartier extension
   $0\to\mathbf G_m\to\mathcal M_\Delta\to\Delta_*\mathbf Z\to0$ of the diagonal
   (with $t^{-1}\mapsto+1$ for a local equation $t$ of $\Delta$) defines a
   morphism $\partial:\Delta_*\mathbf Z\to\mathbf G_m[1]$ in
   $D(W_{\mathrm{proét}},\mathbf Z)$, represented by the roof
   $\Delta_*\mathbf Z\xleftarrow{\sim}[\mathbf G_m\to\mathcal M_\Delta]\to\mathbf G_m[1]$
   with the two-term complex in degrees $-1,0$.
2. The functor
   $T:K\mapsto K\otimes^{\mathbf L}_{\mathbf Z}(\underline{\mathbf Z/\ell^n})_{n\geq1}$
   is a well-defined exact functor
   $D(W_{\mathrm{proét}},\mathbf Z)\to D(W^{\mathbf N}_{\mathrm{proét}})$, and
   $R\varprojlim\circ T$ is derived $\ell$-completion.
3. There are isomorphisms of systems
   $T(\Delta_*\mathbf Z)\simeq\Delta_*\mathbf Z/\ell^\bullet$ and
   $T(\mathbf G_m[1])\simeq\mathbf Z/\ell^\bullet(1)[2]$, where the transition
   maps of $\mathbf Z/\ell^\bullet(1)=(\mu_{\ell^n})_n$ are
   $\zeta\mapsto\zeta^\ell$.
4. Under these identifications $c_\bullet=T(\partial)$ is a morphism
   $\Delta_*\mathbf Z/\ell^\bullet\to\mathbf Z/\ell^\bullet(1)[2]$ in
   $D(W^{\mathbf N}_{\mathrm{proét}})$ whose $n$-th level is the torsion cycle
   class of $\Delta$ with coefficients $\mathbf Z/\ell^n$ of
   [sk-lem-geo-cartier].
