+++
id = "prose-11-04"
kind = "hidden"
title = "Verdier biduality"
order = 507
+++
On a smooth curve $C$ over an algebraically closed field, with
$\omega_C=\Lambda_C(1)[2]$, biduality is easy to see for the two basic
kinds of sheaves. For a locally constant sheaf $L$ of free
$\Lambda$-modules the dual is $L^\vee(1)[2]$, and dualizing twice gives
back $L$. For a skyscraper $i_*M$ at a closed point $i:x\to C$, the dual is
$i_*\mathbb D_xM$, by the exchange $\mathbb D_Ci_*\simeq i_*\mathbb D_x$
for the proper map $i$, and biduality is biduality on the point. A
general constructible sheaf is an extension of such pieces, through
$j_!L$ and $i_*M$, and the trouble is the open piece: $\mathbb D_C(j_!L)\simeq Rj_*\mathbb D_UL$, and to dualize $Rj_*$ we would need
the second exchange formula, which depends on biduality. In dimension
one this can still be checked by hand, using the cohomology of the
henselian punctured disc, but in higher dimension the direct images
$Rj_*$ along the boundary of a stratum have no such description.

The proof of Theorem [sk-thm-pd-verdier-duality] never dualizes $Rj_*$.
It shows that the cone $Q$ of $\delta_K$ vanishes at nonclosed points by
induction on dimension, restricting to the geometric generic fibre of a
function $X\to\mathbf A^1_k$. On the remaining finitely many closed
points, $Q$ is detected by its global sections, and these vanish because
$R\Gamma(X,\delta_K)$ is the double-dual map of the perfect complex
$R\Gamma(X,K)$ when $X$ is proper. Two preliminary facts are
needed. The first is that $\mathbb D_X$ preserves $D^b_{\mathrm{ctf}}(X,\Lambda)$
(Lemma [sk-lem-pd-preservation]), which was already used in
Definition [sk-def-ops]. The second is that $\mathbb D_X$ and
$\delta$ commute with restriction to a geometric generic fibre up to the
twist $(1)[2]$ (Lemma [sk-lem-pd-generic-restriction]), which cancels in
the double dual. The result is that $\mathbb D_X$ is an anti-equivalence
of $D^b_{\mathrm{ctf}}(X,\Lambda)$, and with it come the two remaining exchange
formulas (Corollary [sk-thm-sf-verdier-exchange]).
