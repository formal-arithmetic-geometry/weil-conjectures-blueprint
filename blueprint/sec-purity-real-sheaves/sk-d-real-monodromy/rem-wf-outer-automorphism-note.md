+++
id = "rem-wf-outer-automorphism-note"
kind = "remark"
title = "On the source's outer-automorphism claim"
order = 2804
uses = ["lem-wf-torus-central-power-trivial", "lem-wf-weight-lattice-generates"]
+++
The classical proof (loc. cit.) says that ``there are only finitely
many outer automorphisms of the reductive $G_{\mathrm{geom}}$
preserving $T$''. As a general assertion about reductive groups this
is not correct: for $H=\mathbf G_m^2$ one has
$\operatorname{Aut}(H)=\operatorname{Aut}(X^*(H))=GL_2(\mathbf Z)$,
so $\operatorname{Out}(H)$ is infinite. The mechanism that is
actually available is the one used above: the weights of the faithful
module $V$ under the central torus generate the character lattice
([lem-wf-weight-lattice-generates]), the Frobenius conjugation
permutes the finitely many weights ([lem-wf-torus-central-power-trivial]),
and only for the semisimple derived group is the finiteness of the
outer classes needed, where it is proved elementarily by
[lem-wf-finite-outer-power] (via inner derivations of semisimple
Lie algebras). This is the elementary route of the workspace note
*prop21\_elementary\_proof.md* (Z. Rosengarten, ``Purity of Real
Sheaves'', Prop. 2.1), which this chapter follows.
